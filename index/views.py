from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import Task
import json
from datetime import datetime, timedelta
from . import mathimage as mi


# ---------- 工具 ----------
def _parse_body(request):
    """
    统一解析 POST JSON 与日期字段。
    成功返回 (data, date_obj, None)
    失败返回 (None, None, JsonResponse(...))
    """
    try:
        data = json.loads(request.body)
        date_str = data.get('date')
        date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()
        return data, date_obj, None
    except (ValueError, TypeError):
        return None, None, JsonResponse({'error': '日期格式应为 YYYY-MM-DD'}, status=400)


# ---------- 页面 ----------
def no_login(request):
    return render(request, 'home.html')

def index(request):
    return render(request, 'index.html')


# ---------- 用户信息 ----------
@require_http_methods(['GET'])
def get_user_info(request):
    username = request.session.get('username')
    return JsonResponse({'username': username})


# ---------- 任务 ----------
@require_http_methods(['POST'])
def get_task(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return JsonResponse([], safe=False)

    data, date_obj, err_resp = _parse_body(request)
    if err_resp:
        return err_resp

    tasks = Task.objects.filter(user_id=user_id, date=date_obj).order_by('date')
    result = [
        {
            'id': t.id,
            'title': t.title,
            'completed': t.completed,
            'date': t.date.strftime('%Y-%m-%d'),
        }
        for t in tasks
    ]
    return JsonResponse(result, safe=False, json_dumps_params={'ensure_ascii': False})


@require_http_methods(['POST'])
def add_task(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return JsonResponse({'error': '未登录'}, status=401)

    data, date_obj, err_resp = _parse_body(request)
    if err_resp:
        return err_resp

    title = data.get('title')
    task = Task.objects.create(user_id=user_id, title=title, date=date_obj, completed=False)
    return JsonResponse({'message': '10220101', 'id': task.id}, status=200)


@require_http_methods(['POST'])
def delete_task(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return JsonResponse({'error': '未登录'}, status=401)

    try:
        data = json.loads(request.body)
        task_id = data.get('id')
        
        if not task_id:
            return JsonResponse({'error': '缺少任务ID'}, status=400)
            
        task = Task.objects.get(id=task_id, user_id=user_id)
        task.delete()
        return JsonResponse({'message': '10220201'}, status=200)
    except Task.DoesNotExist:
        return JsonResponse({'error': '任务不存在'}, status=404)
    except (ValueError, TypeError):
        return JsonResponse({'error': '无效的任务ID'}, status=400)


@require_http_methods(['POST'])
def update_task(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return JsonResponse({'error': '未登录'}, status=401)

    try:
        data = json.loads(request.body)
        title = data.get('title')
        task_id = data.get('id')
        completed = data.get('completed')
        
        if not task_id:
            return JsonResponse({'error': '缺少任务ID'}, status=400)
            
        task = Task.objects.get(id=task_id, user_id=user_id)
        task.title = title
        task.completed = completed
        task.save()
        return JsonResponse({'message': '10220301'}, status=200)
    except Task.DoesNotExist:
        return JsonResponse({'error': '任务不存在'}, status=404)
    except (ValueError, TypeError):
        return JsonResponse({'error': '无效的任务ID'}, status=400)


@require_http_methods(['POST'])
def complete_task(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return JsonResponse({'error': '未登录'}, status=401)

    try:
        data = json.loads(request.body)
        task_id = data.get('id')
        completed = data.get('completed')
        
        if not task_id:
            return JsonResponse({'error': '缺少任务ID'}, status=400)
            
        task = Task.objects.get(id=task_id, user_id=user_id)
        task.completed = completed
        task.save()
        return JsonResponse({'message': '10220301'}, status=200)
    except Task.DoesNotExist:
        return JsonResponse({'error': '任务不存在'}, status=404)
    except (ValueError, TypeError):
        return JsonResponse({'error': '无效的任务ID'}, status=400)
    

@require_http_methods(['POST'])
def get_total_image(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return JsonResponse({'error': '未登录'}, status=401)
    
    date = datetime.now().date()
    date_7_bef = date - timedelta(days=7)
    data_30_bef = date - timedelta(days=30)
    
    # 获取7天内的任务,完成与未完成
    tasks = Task.objects.filter(user_id=user_id, date__gte=date_7_bef, date__lte=date).order_by('date')
    
    # 构建data字典，键为日期，值为元组(完成,未完成) {日期: (完成,未完成)}
    data7 = {}
    for task in tasks:
        date_str = task.date.strftime('%Y-%m-%d')
        if date_str not in data7:
            data7[date_str] = [0, 0]  # [完成, 未完成]
        if task.completed:
            data7[date_str][0] += 1
        else:
            data7[date_str][1] += 1
    
    # 获取30天内的任务,完成与未完成数 [完成,未完成]
    data30_y = Task.objects.filter(user_id=user_id, date__gte=data_30_bef, date__lte=date, completed=True).count()
    data30_n = Task.objects.filter(user_id=user_id, date__gte=data_30_bef, date__lte=date, completed=False).count()
    
    try:
        d7 = mi.status(data7)
        d30 = mi.status2([data30_y, data30_n])
        return JsonResponse({
            'message': '图表生成成功',
            'd7_image': d7,
            'd30_image': d30
        }, status=200)
    except Exception as e:
        return JsonResponse({'error': f'图表生成失败: {str(e)}'}, status=500)


@require_http_methods(['POST'])
def export_tasks_excel(request):
    """导出任务列表到 Excel 文件"""
    user_id = request.session.get('user_id')
    if not user_id:
        return JsonResponse({'error': '未登录'}, status=401)

    try:
        data = json.loads(request.body)
        date_str = data.get('date')
        
        if not date_str:
            return JsonResponse({'error': '缺少日期参数'}, status=400)
            
        date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()
        
        # 获取指定日期的任务
        tasks = Task.objects.filter(user_id=user_id, date=date_obj).order_by('date')
        
        if not tasks.exists():
            return JsonResponse({'error': '该日期没有任务'}, status=404)
        
        # 准备任务数据
        task_data = []
        for task in tasks:
            task_data.append({
                "description": task.title,
                "status": "已完成" if task.completed else "未完成"
            })
        
        # 生成 Excel 文件到内存
        excel_data = mi.create_task_excel(task_data, save_to_memory=True)
        
        # 将字节数据转换为 base64 字符串
        import base64
        excel_base64 = base64.b64encode(excel_data).decode('utf-8')
        
        return JsonResponse({
            'message': 'Excel 文件生成成功',
            'filename': f'tasks_{date_str}.xlsx',
            'data': excel_base64
        }, status=200)
        
    except ValueError:
        return JsonResponse({'error': '日期格式错误，应为 YYYY-MM-DD'}, status=400)
    except Exception as e:
        return JsonResponse({'error': f'Excel 生成失败: {str(e)}'}, status=500)