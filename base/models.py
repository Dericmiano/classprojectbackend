from django.db import models
from django.contrib.auth.models import User

class School(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    cutoff = models.DecimalField(max_digits=7,decimal_places=2,null=True, blank=True)
    numberOfChoice = models.IntegerField(null=True,blank=True)
    numberOfstudents = models.IntegerField(null=True,blank=True)
    image = models.ImageField(null=True,blank=True,default='/placeholder.png')
    motto = models.CharField(max_length=200, null=True, blank=True)
    level =models.CharField(max_length=200, null=True, blank=True)
    location =models.CharField(max_length=200, null=True, blank=True)
    status =models.CharField(max_length=200, null=True, blank=True)
    _id = models.AutoField(primary_key=True,editable=False)

    def __str__(self):
        return str(self.name)
class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    studentScoreAverage = models.DecimalField(max_digits=7,decimal_places=2)
    # applicationItems = models.ForeignKey('ApplicationItem',on_delete=models.CASCADE,blank=True, null=True)
    # cutoff = models.DecimalField(max_digits=7,decimal_places=2)
    _id = models.AutoField(primary_key=True,editable=False)

    def __str__(self):
        return str(self.user)

class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    application = models.OneToOneField(Application, on_delete=models.CASCADE, null=True, blank=True)
    username = models.CharField(blank=True, null=True, max_length=200)
    index_number = models.CharField(blank=True, null=True, max_length=200)
    sex = models.CharField(blank=True, null=True,max_length=200)
    DOB = models.CharField(blank=True, null=True, max_length=200)
    school = models.CharField(blank=True, null=True, max_length=200)
    _id = models.AutoField(primary_key=True,editable=False)

    def __str__(self):
        return str(self.user)





class StudentScores(models.Model):
    application = models.OneToOneField(Application, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    student = models.ForeignKey(Student, on_delete=models.SET_NULL,null=True),
    # averageScore =  models.DecimalField(max_digits=7,decimal_places=2)
    mathes = models.IntegerField(default=0)
    english = models.IntegerField(default=0)
    kiswahili = models.IntegerField(default=0)
    science =models.IntegerField(default=0)
    socialStudies = models.IntegerField(default=0)
    _id = models.AutoField(primary_key=True,editable=False)

    def __str__(self):
        return str(self.application)




class ApplicationItem(models.Model):
    student = models.CharField(max_length=200, null=True, blank=True)
    studentScoreAverage = models.IntegerField(null=True, blank=True, default=0)
    numberOfChoice = models.IntegerField(null=True, blank=True, default=0)
    numberOfstudents = models.IntegerField(null=True, blank=True)
    cutoff = models.IntegerField(null=True, blank=True, default=0)
    _id = models.AutoField(primary_key=True, editable=False)
    application = models.ForeignKey(Application, on_delete=models.SET_NULL, null=True)
    school = models.ForeignKey(School, on_delete=models.SET_NULL, null=True)
    username = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)

    image = models.ImageField(null=True,blank=True)

    def __str__(self):
        return str(self.name)








