from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import User
import json
import re
from django.contrib.auth.hashers import check_password

@require_http_methods(['GET', 'POST'])
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        try:
            data = json.loads(request.body)
            identifier = data.get('username')  # 接收用户输入，可能是用户名或邮箱
            password = data.get('password')
            print(f"用户: {identifier} 登入")
            # print(password)

            if not identifier or not password:
                return JsonResponse({'error': '用户名/邮箱和密码不能为空'}, status=400)

            def is_email(value):
                """判断输入是否为邮箱格式"""
                email_regex = re.compile(r'^[^\s@]+@[^\s@]+\.[^\s@]+$')
                return email_regex.match(value)

            try:
                if is_email(identifier):
                    user = User.objects.get(email=identifier)
                else:
                    user = User.objects.get(name=identifier)

                if password == user.password:
                    # 登录成功，设置 session
                    request.session['user_id'] = user.id
                    request.session['username'] = user.name
                    return JsonResponse({'message': '登录成功'}, status=200)
                else:
                    return JsonResponse({'error': '用户名/邮箱或密码错误'}, status=401)
            except User.DoesNotExist:
                return JsonResponse({'error': '用户不存在'}, status=401)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': '无效的请求方法'}, status=405)



@require_http_methods(['GET','POST'])
def register(request):
    if request.method == 'GET':
        return render(request,'register.html')
    elif request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data.get('username')
            email = data.get('email')
            password = data.get('password')

            if not name or not email or not password:
                return JsonResponse({'error': '用户名、邮箱和密码不能为空'}, status=400)

            if User.objects.filter(name=name).exists():
                return JsonResponse({'error': '用户名已存在'}, status=400)

            if User.objects.filter(email=email).exists():
                return JsonResponse({'error': '邮箱已存在'}, status=400)

            user = User.objects.create(name=name, email=email, password=password)
            # user.save()
            return JsonResponse({'message': '注册成功'}, status=201)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': '无效的请求方法'}, status=405)


def check_username(request):
    name = request.GET.get('username')
    exists = User.objects.filter(name=name).exists()
    return JsonResponse({'exists': exists})

def check_email(request):
    email = request.GET.get('email')
    exists = User.objects.filter(email=email).exists()
    return JsonResponse({'exists': exists})

def protected_view(request):
    user_id = request.session.get('user_id')
    if user_id:
        # 可以根据 user_id 获取用户信息
        try:
            user = User.objects.get(id=user_id)
            return JsonResponse({'message': f'欢迎，{user.name}'})
        except User.DoesNotExist:
            pass
    return JsonResponse({'error': '请先登录'}, status=401)

def logout(request):
    request.session.flush()
    return render(request, 'login.html')

@require_http_methods(['GET'])
def get_user_id(request):
    username = request.session.get('username')
    try:
        find_id = User.objects.get(name=username).id
        return JsonResponse({'id': find_id})
    except User.DoesNotExist:
        return JsonResponse({'error': '用户不存在'}, status=404)
