from django.db import models

# Create your models here.
class Student(models.Model):
    id_num=models.IntegerField(default=0)
    name=models.CharField(max_length=30)
    class Meta:
        db_table="student"
