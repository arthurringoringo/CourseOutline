from django import forms
from .models import *
from django.forms import ModelForm
from .choices import *


class CreateCurriculumForm(forms.ModelForm):
    
    CurriculumName = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),label='Curriculum Name:')
    FacultyName = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),label='Faculty Name:',choices = FacultyNameChoices)
    class Meta:
        model = Curriculum
        fields = 'CurriculumName', 'FacultyName'

class CreateCourseOutlineForm(forms.ModelForm):
    CourseName = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),label='Course Name')
    CourseCode = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),label='Course Code:')
    FacultyName = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),label='Faculty Name:',choices = FacultyNameChoices)
    CourseCurriculumID = forms.ModelChoiceField(widget=forms.Select(attrs={'class':'form-control'}),label='Curriculum Name:',queryset=Curriculum.objects.all())
    class Meta:
        model = CourseOutline
        fields = 'CourseName', 'CourseCode','FacultyName','CourseCurriculumID'

class CreateCourseOutlineForm1(forms.ModelForm):

    NumberOfCredit = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),label='Number of Credit:',choices = Credits)
    CategoryOfCourse = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),label='Category of course:',choices = CourseCategory)
    Prerequisite = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),label='Pre-Requisite:')
    Corequisite = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),label='Co-Requisite:')
    Place = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),label='Place:')
    DateofCourseDevelopmentorRevision = forms.DateTimeField(widget = forms.DateTimeInput(attrs={'class':'form-control'}),label='Date of course Development or Revision:',initial =timezone.now)
    class Meta:
        model = CourseOutlineSection1
        fields = 'NumberOfCredit', 'CategoryOfCourse', 'Prerequisite', 'Corequisite', 'Place', 'DateofCourseDevelopmentorRevision'

class CreateCourseOutlineForm2(forms.ModelForm):
    CourseAims = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','rows':'4'}),label='Course Aims')
    ObjofCourse = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','rows':'4'}),label='Objective of Course')
    class Meta:
        model = CourseOutlineSection2
        fields = 'CourseAims', 'ObjofCourse'

class CreateCourseOutlineForm3(forms.ModelForm):
    CourseDesc = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','rows':'4'}),label='Course Description')
    NumofLectureHrs = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),label='Number of Lecture Hours',choices=HoursChoices)
    NumofAddLectureHrs = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),label='Number of Additional Lecture Hours',choices=HoursChoices)
    NumofLabHrs = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),label='Number of Lab Hours',choices=HoursChoices)
    NumofSSHrs = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),label='Number of Self Study Hours',choices=HoursChoices)
    NumofAdvHrs = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),label='Number of Advising Hours',choices=HoursChoices)
    class Meta:
        model = CourseOutlineSection3
        fields = 'CourseDesc', 'NumofLectureHrs', 'NumofAddLectureHrs', 'NumofLabHrs', 'NumofSSHrs', 'NumofAdvHrs'

class CreateCourseOutlineForm4(forms.ModelForm):
    CourseTopic = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),label='Course Topics')
    CourseTopicDesc = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','rows':'4'}),label='Course Topics Description')
    class Meta:
        model = CourseOutlineSection4
        fields = 'CourseTopic', 'CourseTopicDesc'

class CreateCourseOutlineForm5(forms.ModelForm):
    EvaluationType = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),label='Evaluation type',choices=EvaluationTypes)
    EvaluationPercentage = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = CourseOutlineSection5
        fields = 'EvaluationType', 'EvaluationPercentage'


class CreateCourseOutlineForm6(forms.ModelForm):
    ResourcesTypes = forms.CharField(label='Resources Type?', widget=forms.Select(choices=ResourcesTypes))
    ResourcesDescription = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','rows':'4'}))
    class Meta:
        model = CourseOutlineSection6
        fields = 'ResourcesTypes', 'ResourcesDescription'

 
