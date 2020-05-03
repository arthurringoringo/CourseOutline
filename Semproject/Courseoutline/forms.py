from django import forms
from .models import *
from django.forms import ModelForm


class CreateCurriculumForm(forms.ModelForm):
    CurriculumID = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    CurriculumName = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    FacultyName = forms.ChoiceField(label='Faculty Name?',widget=forms.Select())
    class Meta:
        model = CourseOutline
        fields = 'CurriculumID', 'CurriculumName', 'FacultyName'

class CreateCourseOutlineForm(forms.ModelForm):
    CourseOutlineID = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    CourseName = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    CourseCode = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = CourseOutline
        fields = 'CourseOutlineID', 'CourseName', 'CourseCode'

class CreateCourseOutlineForm1(forms.ModelForm):
    SectionID = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    SectionName = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    NumberOfCredit = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    CategoryOfCourse = forms.CharField(label='Course Category?', widget=forms.Select(choices=CourseCategory))
    Prerequisite = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    Corequisite = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    Place = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    DateofCourseDevelopmentorRevision = forms.DateField()
    class Meta:
        model = CourseOutline
        fields = 'SectionID', 'SectionName', 'NumberOfCredit', 'CategoryOfCourse', 'Prerequisite', 'Corequisite', 'Place', 'DateofCourseDevelopmentorRevision'

class CreateCourseOutlineForm2(forms.ModelForm):
    CourseAims = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','rows':'4'}))
    ObjofCourse = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','rows':'4'}))
    class Meta:
        model = CourseOutline
        fields = 'CourseAims', 'ObjofCourse'

class CreateCourseOutlineForm3(forms.ModelForm):
    CourseDesc = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','rows':'4'}))
    NumofLectureHrs = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    NumofAddLectureHrs = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    NumofLabHrs = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    NumofSSHrs = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    NumofAdvHrs = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = CourseOutline
        fields = 'CourseDesc', 'NumofLectureHrs', 'NumofAddLectureHrs', 'NumofLabHrs', 'NumofSSHrs', 'NumofAdvHrs'

class CreateCourseOutlineForm4(forms.ModelForm):
    CourseTopic = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    CourseTopicDesc = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','rows':'4'}))
    class Meta:
        model = CourseOutline
        fields = 'CourseTopic', 'CourseTopicDesc'

class CreateCourseOutlineForm5(forms.ModelForm):
    EvaluationType = forms.CharField(label='Evaluation Type?', widget=forms.Select(choices=EvaluationTypes))
    EvaluationPercentage = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = CourseOutline
        fields = 'EvaluationType', 'EvaluationPercentage'


class CreateCourseOutlineForm6(forms.ModelForm):
    ResourcesTypes = forms.CharField(label='Resources Type?', widget=forms.Select(choices=ResourcesTypes))
    ResourcesDescription = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','rows':'4'}))
    class Meta:
        model = CourseOutline
        fields = 'ResourcesTypes', 'ResourcesDescription'

 
