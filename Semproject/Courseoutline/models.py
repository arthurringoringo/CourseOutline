from django.db import models
from django.utils import timezone
import datetime



# Create your models here.
FacultyNameChoices = [
    ('FAH','Arts And Humanities'),('FBA','Business Admin'),
    ('FEd','Education'),('FRS','Religous Studies'),('FOS','Science'),
    ('FIT','Information Technology'),('FON','Nursing')]

class Curriculum(models.Model):

    CurriculumID = models.AutoField(primary_key=True,max_length=10)
    CurriculumName = models.CharField(max_length=50)
    FacultyName = models.CharField(max_length=50,choices=FacultyNameChoices)
    CreateDate = models.DateTimeField('Created on',default=timezone.now)
    def __str__(self):
        return self.CurriculumName

class CourseOutline(models.Model):
    CourseOutlineID =  models.AutoField(primary_key = True, max_length = 10)
    CourseCurriculumID = models.ForeignKey(Curriculum,on_delete=models.CASCADE)
    CourseName =  models.CharField(max_length=99)
    CourseCode = models.CharField(max_length=8)
    FacultyName = models.CharField(max_length=50,choices=FacultyNameChoices)
    CreateDate = models.DateTimeField('Created on',default=timezone.now)
    def __str__(self):
        return self.CourseName

