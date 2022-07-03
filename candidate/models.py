from django.db import models
from Users.models import User
# Create your models here.


class CandidateProfileModel(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="candidate")
    profile_pic=models.ImageField(upload_to="profile")
    qualification=models.CharField(max_length=120)
    age=models.PositiveIntegerField(default=18)
    skills=models.CharField(max_length=120,null=True)
    cv=models.FileField(upload_to="cvs",null=True)




