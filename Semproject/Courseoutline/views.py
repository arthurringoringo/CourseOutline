from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render
from django.http.response import HttpResponse, HttpResponseRedirect
from .models import *
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import *
from .forms import *
from datetime import datetime
from django.urls import reverse_lazy

# Create your views here.

def IndexMenu(request,template_name='Courseoutline/index.html'):
    return render(request,'Courseoutline/index.html')

#### CURICULUM


def CurriculumCreate(request,template_name='Courseoutline/curriculum_Detail.html'):
    curriculumForm = CreateCurriculumForm()
    currentcurriculum = Curriculum.objects.all()
    if request.method == 'POST':
        curriculumForm = CreateCurriculumForm(request.POST)
        if curriculumForm.is_valid():
            curriculumForm.save()
        return redirect('indexmenu')
    context = {'curriculumForm': curriculumForm,'title':'Curriculum','currentcurriculum':currentcurriculum}
    return render(request,'Courseoutline/curriculum_Detail.html',context)

#Waiting for template
#class CurriculumView(generic.DetailView):
#        template_name: 'Courseoutline/curriculum_Detail.html'
#        model = Curriculum


def CurriculumDelete(request,curriculum_id):
    obj = get_object_or_404(Curriculum,pk=curriculum_id)
    if request.method == "POST":
        obj.delete()
        return redirect('indexmenu')
    return render(request,'curriculum_Detail.html')

class CurriculumUpdate(UpdateView):
    model = Curriculum
    form_class = CreateCurriculumForm
    template_name = 'Courseoutline/curriculum_Detail.html'

    def get_object(self):
        CurriculumID = self.kwargs.get("id")
        return get_object_or_404(Curriculum, pk=CurriculumID)
    def get_success_url(self):
        return reverse_lazy('indexmenu')


#### COURSEOUTLINE
def CourseoutlineCreate(request,template_name='courseoutline/courseOutlineSection.html'):
    courseoutlineForm = CreateCourseOutlineForm()

    if request.method == 'POST':
        courseoutlineForm = CreateCourseOutlineForm(request.POST)
        if courseoutlineForm.is_valid():
            new_courseoutline=courseoutlineForm.save()
        return HttpResponseRedirect(reverse(Courseoutlinesectionscreate, args=(new_courseoutline.pk,)))
    context = {'courseoutlineForm': courseoutlineForm,'title':'Course Outline'}
    return render(request,'Courseoutline/courseOutlineSection.html',context)

def CourseoutlineDelete(request,courseoutline_id):
    obj = get_object_or_404(CourseOutline,pk=courseoutline_id)
    if request.method == "POST":
        obj.delete()
        return redirect('indexmenu')
    return render(request,'courseOutlineSection.html')

class CourseoutlineUpdate(UpdateView):
    model = CourseOutline
    form_class = CreateCourseOutlineForm
    template_name = 'Courseoutline/courseOutlineSection.html'

    def get_object(self):
        CourseOutlineID = self.kwargs.get("id")
        return get_object_or_404(CourseOutline, pk=CourseOutlineID)
    def get_success_url(self):
        return reverse_lazy('indexmenu')


# Section Forms within 1 html page
def Courseoutlinesectionscreate(request,courseoutline_id,template_name='Courseoutline/courseOutlineSection1.html'):
    currentcourseoutlineobj = get_object_or_404(CourseOutline,pk = courseoutline_id)
    courseoutlineForm1 = CreateCourseOutlineForm1()
    courseoutlineForm2 = CreateCourseOutlineForm2()
    courseoutlineForm3 = CreateCourseOutlineForm3()
    courseoutlineForm4 = CreateCourseOutlineForm4()
    
    if request.method == 'POST':
        courseoutlineForm1 = CreateCourseOutlineForm1(request.POST)
        if courseoutlineForm1.is_valid():
            tempcourseoutline = courseoutlineForm1.save(commit=False)
            tempcourseoutline.CourseOutlineID =currentcourseoutlineobj
            tempcourseoutline.save()
        return redirect('indexmenu')
    context = {'courseoutlineForm1': courseoutlineForm1,'courseoutlineForm2': courseoutlineForm2,
    'courseoutlineForm3': courseoutlineForm3,'courseoutlineForm4': courseoutlineForm4,
    'title':'Course Outline','Course':currentcourseoutlineobj.CourseName,'CourseID':currentcourseoutlineobj.CourseCode}
    return render(request,'Courseoutline/courseOutlineSection1.html',context)

def CourseoutlineCreateSection2(request,template_name='courseoutline/courseOutlineSection1.html'):
    courseoutlineForm2 = CreateCourseOutlineForm2()

    if request.method == 'POST':
        courseoutlineForm2 = CreateCourseOutlineForm2(request.POST)
        if courseoutlineForm2.is_valid():
            courseoutlineForm2.save()
        return redirect('indexmenu')
    context = {'courseoutlineForm2': courseoutlineForm2,'title':'Course Outline'}
    return render(request,'Courseoutline/courseOutlineSection1.html',context)

def CourseoutlineCreateSection3(request,template_name='courseoutline/courseOutlineSection1.html'):
    courseoutlineForm2 = CreateCourseOutlineForm2()

    if request.method == 'POST':
        courseoutlineForm3 = CreateCourseOutlineForm3(request.POST)
        if courseoutlineForm3.is_valid():
            courseoutlineForm3.save()
        return redirect('indexmenu')
    context = {'courseoutlineForm3': courseoutlineForm3,'title':'Course Outline'}
    return render(request,'Courseoutline/courseOutlineSection1.html',context)

def CourseoutlineCreateSection4(request,template_name='courseoutline/courseOutlineSection1.html'):
    courseoutlineForm4 = CreateCourseOutlineForm4()

    if request.method == 'POST':
        courseoutlineForm4 = CreateCourseOutlineForm4(request.POST)
        if courseoutlineForm4.is_valid():
            courseoutlineForm4.save()
        return redirect('indexmenu')
    context = {'courseoutlineForm4': courseoutlineForm4,'title':'Course Outline'}
    return render(request,'Courseoutline/courseOutlineSection1.html',context)

def CourseoutlineCreateSection5(request,template_name='courseoutline/courseOutlineSection1.html'):
    courseoutlineForm5 = CreateCourseOutlineForm1()

    if request.method == 'POST':
        courseoutlineForm5 = CreateCourseOutlineForm5(request.POST)
        if courseoutlineForm5.is_valid():
            courseoutlineForm5.save()
        return redirect('indexmenu')
    context = {'courseoutlineForm5': courseoutlineForm5,'title':'Course Outline'}
    return render(request,'Courseoutline/courseOutlineSection1.html',context)

def CourseoutlineCreateSection6(request,template_name='courseoutline/courseOutlineSection1.html'):
    courseoutlineForm6 = CreateCourseOutlineForm6()

    if request.method == 'POST':
        courseoutlineForm6 = CreateCourseOutlineForm6(request.POST)
        if courseoutlineForm6.is_valid():
            courseoutlineForm6.save()
        return redirect('indexmenu')
    context = {'courseoutlineForm6': courseoutlineForm6,'title':'Course Outline'}
    return render(request,'Courseoutline/courseOutlineSection1.html',context)


