from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100,unique=True)
    email = models.EmailField(max_length=100,unique=True)
    phone = models.CharField(max_length=100,default="")#手机号,后续修改密码要提供正确的手机号
    password = models.CharField(max_length=100)
    id = models.IntegerField(primary_key=True,unique=True,auto_created=True)