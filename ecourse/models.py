from django.db import models
from django.db import models

# Create your models here.
class Accounts(models.Model):  
    name=models.CharField(max_length=17)
    password=models.CharField(max_length=10)
    email = models.EmailField(primary_key=True, blank=False, null=False)
class Courses(models.Model):
    cname=models.CharField(primary_key=True,max_length=10)
    description=models.CharField(max_length=200)
    url=models.URLField(max_length=200,null=True)

class Videos(models.Model):
    vno=models.IntegerField(default=1)
    course=models.ForeignKey('Courses',on_delete=models.CASCADE)
    vname=models.CharField(max_length=200)
    vurl=models.URLField(max_length=200,null=True)

class Comments(models.Model):
    nameofcmt=models.CharField(max_length=20,default='Ajith')
    cmt=models.CharField(max_length=200)
    vid=models.ForeignKey('Videos',on_delete=models.CASCADE)

       
