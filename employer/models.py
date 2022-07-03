from django.db import models
from Users.models import User

# Create your models here.

class EmployeeProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="employers")
    company_name=models.CharField(max_length=120,unique=True)
    logo=models.ImageField(upload_to="images")
    bio=models.CharField(max_length=120)
    location=models.CharField(max_length=120)
    services=models.CharField(max_length=120)


class Jobs(models.Model):
    posted_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name="company")
    job_title=models.CharField(max_length=120)
    job_discription=models.TextField(max_length=120)
    role=models.CharField(max_length=120)
    experience=models.PositiveIntegerField(default=0)
    location=models.CharField(max_length=120)
    salary=models.PositiveIntegerField()
    created_date=models.DateField(auto_now_add=True)
    last_date=models.DateField(null=True)
    qualification=models.CharField(max_length=120,null=True)

    def __str__(self):
        return self.job_title