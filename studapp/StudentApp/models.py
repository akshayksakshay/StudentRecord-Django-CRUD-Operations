from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class studentdetails(models.Model):
    DEPARTMENT_CHOICES = [
        ('CS', 'Computer Science'),
        ('BM', 'Bio Maths'),
        ('CM', 'Commerce'),
        ('HM', 'Humanities'),
    ]
    #FEES_CHOICES = [
    #    ('Paid','Paid'),
    #    ('Unpaid','Unpaid')
    #]
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    sregno = models.IntegerField(unique = True, null = False)
    sname = models.CharField(max_length = 100)
    sgender = models.CharField(choices= GENDER_CHOICES,max_length = 10, default='M')
    sage = models.IntegerField()
    sdept = models.CharField(choices = DEPARTMENT_CHOICES, max_length=50)
    #sfees = models.CharField(choices = FEES_CHOICES, max_length = 20, default = 'Unpaid')
    simage = models.ImageField(upload_to='studphoto/', blank=True, null=True)

    def __str__(self):
        return str(self.id)
    
class MarkList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sname = models.ForeignKey(studentdetails, on_delete=models.CASCADE)
    date = models.DateField() 
    sub1 = models.CharField(max_length=50, null = True)
    mark1 = models.IntegerField()
    sub2 = models.CharField(max_length=50, null = True)
    mark2 = models.IntegerField()
    sub3 = models.CharField(max_length=50, null = True)
    mark3 = models.IntegerField()
    sub4 = models.CharField(max_length=50, null = True)
    mark4 = models.IntegerField()
    sub5 = models.CharField(max_length=50, null = True)
    mark5 = models.IntegerField()
    total = models.IntegerField()

    #def __str__(self):
    #    return str(self.id)
