from django.db import models

# Create your models here.
class EmployeeClass(models.Model):
    Employee_ID = models.CharField(primary_key=True,max_length=10)
    Name = models.CharField(max_length=100)
    Age = models.IntegerField()
    Phone = models.IntegerField()
    City = models.CharField(max_length=100)

    def __str__(self):
        return self.Name

class CompanyClass(models.Model):
    Job_Profile_ID = models.CharField(max_length=100)
    JobProfile = models.CharField(max_length=100)
    Salary = models.IntegerField()
    Employee_ID = models.CharField(primary_key=True,max_length=10)

    def __str__(self):
        return self.JobProfile