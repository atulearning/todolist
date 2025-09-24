from django.urls import path
from . import views

#app_name
app_name="index"

urlpatterns=[
    path('nologin',views.no_login,name='home'),
    path('get_user_info/', views.get_user_info, name='get_user_info'),
    path('',view=views.index,name='index'),
    path('get_task/',views.get_task,name='get_task'),
    path('add_task/',views.add_task,name='add_task'),
    path('delete_task/',views.delete_task,name='delete_task'),
    path('update_task/',views.update_task,name='update_task'),
    path('complete_task/',views.complete_task,name='complete_task'),
    path('total_image/',views.get_total_image,name='total_image'),
    path('export_tasks_excel/',views.export_tasks_excel,name='export_tasks_excel')
]