from django.db import models

# Create your models here.
class Task(models.Model):
    id = models.IntegerField(primary_key=True, unique=True,auto_created=True)
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    date=models.DateField()
    user =models.ForeignKey('welcome.User',on_delete=models.CASCADE)
    class Meta:
        db_table = 'tasks'
        ordering = ['date']

