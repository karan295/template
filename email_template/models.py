from django.db import models

# Create your models here.
class employee(models.Model):
    employee_name=models.CharField(max_length=100)
    employee_id=models.CharField(max_length=100,unique=True)
    employee_email=models.EmailField(null=True,blank=True)
    employee_birthday_date=models.CharField(max_length=100)
    employee_birthday_year=models.CharField(max_length=100,null=True,blank=True)
    employee_birthday_month=models.CharField(max_length=100,null=True,blank=True)
    employee_age=models.IntegerField()
    employee_gender=models.IntegerField()
    employee_joining_date=models.DateTimeField()