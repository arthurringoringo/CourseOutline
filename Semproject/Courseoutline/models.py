from django.db import models
from django.utils import timezone
import datetime



# Create your models here.
FacultyNameChoices = [
    ('FAH','Arts And Humanities'),('FBA','Business Admin'),
    ('FEd','Education'),('FRS','Religous Studies'),('FOS','Science'),
    ('FIT','Information Technology'),('FON','Nursing')]
CourseCategory = [
    ('Core Course','Core Course'),('General Education Course','General Education Course'),
    ('Major Required Course','Major Required Course'),('Major Elective Course','Major Elective Course')
]
HoursChoices = [
    ('1','1'),('2','2'),('3','3'),('4','4')
]
ResourcesTypes = [
    ('Text Book','Text Book'),('Internet Resources','Internet Resources'),
    ('Research Paper','Reserach Paper')
]
EvaluationTypes = [
    ('Assignments','Assignments'),('Quizzes','Quizzes'),('Attendance','Attendance'),
    ('Midterm Exam','Midterm Exam'),('Final Exam','Final Exam'),('Projects','Projects')
]
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

class CourseOutlineSection1(models.Model):
    SectionID = models.AutoField(primary_key = True)
    CourseOutlineID = models.ForeignKey(CourseOutline,on_delete=models.CASCADE)
    SectionName = models.CharField(max_length=55,default='Course Identification and General Information')
    DateCreated = models.DateTimeField(default=timezone.now)
    NumberOfCredit = models.CharField(max_length=10)
    CategoryofCourse = models.CharField(max_length=55,choices=CourseCategory)
    Prerequisite = models.CharField(max_length=100)
    Corequisite = models.CharField(max_length=100)
    Place = models.CharField(max_length=100)
    DateofCourseDevelopmentorRevision = models.DateField()

class CourseOutlineSection2(models.Model):
    SectionID = models.AutoField(primary_key = True)
    CourseOutlineID = models.ForeignKey(CourseOutline,on_delete=models.CASCADE)
    SectionName = models.CharField(max_length=55,default='Aims and Objectives')
    DateCreated = models.DateTimeField(default = timezone.now)
    CourseAims = models.TextField(max_length=555)
    ObjofCourse = models.TextField(max_length=555)

class CourseOutlineSection3(models.Model):
    SectionID = models.AutoField(primary_key = True)
    CourseOutlineID = models.ForeignKey(CourseOutline,on_delete=models.CASCADE)
    SectionName = models.CharField(max_length=55,default='Course Composition')
    DateCreated = models.DateTimeField(default = timezone.now)
    CourseDesc =  models.TextField(max_length=555)
    NumofLectureHrs = models.IntegerField(max_length=2,choices=HoursChoices)
    NumofAddLectureHrs = models.IntegerField(max_length=2,choices=HoursChoices)
    NumofLabHrs = models.IntegerField(max_length=2,choices=HoursChoices)
    NumofSSHrs = models.IntegerField(max_length=2,choices=HoursChoices)
    NumofAdvHrs = models.IntegerField(max_length=2,choices=HoursChoices)

class CourseOutlineSection4(models.Model):
    SectionID = models.AutoField(primary_key = True)
    CourseOutlineID = models.ForeignKey(CourseOutline,on_delete=models.CASCADE)
    SectionName = models.CharField(max_length=55,default='Course Topics')
    DateCreated = models.DateTimeField(default = timezone.now)
    CourseTopic = models.TextField(max_length=555)    
    CourseTopicDesc = models.TextField(max_length=555) 

class CourseOutlineSection5(models.Model):
    SectionID = models.AutoField(primary_key = True)
    CourseOutlineID = models.ForeignKey(CourseOutline,on_delete=models.CASCADE)
    SectionName = models.CharField(max_length=55,default='Evaluation Plans')
    DateCreated = models.DateTimeField(default = timezone.now)
    EvaluationType = models.CharField(max_length=20,choices=EvaluationTypes)    
    EvaluationPercentage = models.CharField(max_length=3)    

class CourseOutlineSection6(models.Model):
    SectionID = models.AutoField(primary_key = True)
    CourseOutlineID = models.ForeignKey(CourseOutline,on_delete=models.CASCADE)
    SectionName = models.CharField(max_length=55,default='Resources')
    DateCreated = models.DateTimeField(default = timezone.now)
    ResourcesTypes = models.CharField(max_length=20, choices = ResourcesTypes)    
    ResourcesDescription = models.TextField(max_length=3)    