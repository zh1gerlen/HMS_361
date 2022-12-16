from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# Patient Models
class Patient(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    pid=models.AutoField(primary_key=True)
    phone=models.CharField(max_length=10)
    age=models.CharField(max_length=3)
    gender=models.CharField(max_length=10)
    address=models.CharField(max_length=100)
    casepaper=models.CharField(max_length=10)
    government_id=models.CharField("1",max_length=10)
    caregiver=models.CharField("88005553535",max_length=10)
    otp=models.CharField(max_length=6)
    image=models.ImageField(default='default.jpg',upload_to='med_report')
    
    def __str__(self):
        return f'{self.user.first_name}'
    
    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        img=Image.open(self.image.path)
        if img.height > 400 or img.width > 400:
            output_size=(400,400)
            img.thumbnail(output_size)
            img.save(self.image.path)

            
# Doctor Models            
class Doctor(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    did=models.AutoField(primary_key=True)
    phone=models.CharField(max_length=10)
    age=models.CharField(max_length=3)
    gender=models.CharField(max_length=10)
    Department=models.CharField(max_length=20)
    attendance=models.CharField(max_length=10)
    status=models.CharField(max_length=15)
    salary=models.CharField(max_length=10)
    otp=models.CharField(max_length=6)
    
    def __str__(self):
        return f'{self.user.first_name}'

class HR(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    mid=models.AutoField(primary_key=True)
