from django.urls import path
from . import views

#app_name
app_name="welcome"

urlpatterns=[
    path("login/",views.login,name="login"),
    path("register/",views.register,name="register"),
    path('check_username/', views.check_username, name='check_username'),
    path('check_email/', views.check_email, name='check_email'),
    path('logout/', views.logout, name='logout'),#注销
    path('protected/', views.protected_view, name='protected'),#保护
]
