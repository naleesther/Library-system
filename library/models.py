from django.db import models

# Create your models here.
class StudentReport(models.Model):
    Firstname = models.CharField(max_length=15)
    Lastname = models.CharField(max_length=15)
    EnrollmentNo = models.CharField(max_length=15)
    Branch = models.CharField(max_length=5)
    


