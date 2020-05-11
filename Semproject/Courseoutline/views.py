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

def IndexMenu(request,tempalate_name='Courseoutline/index.html'):
    return render(request,'Courseoutline/index.html')

#### CURICULUM


def CurriculumCreate(request,template_name='Courseoutline/curriculum_Detail.html'):
    curriculumForm = CreateCurriculumForm()

    if request.method == 'POST':
        curriculumForm = CreateCurriculumForm(request.POST)
        if curriculumForm.is_valid():
            curriculumForm.save()
        return redirect('indexmenu')
    context = {'curriculumForm': curriculumForm,'title':'Curriculum'}
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
            courseoutlineForm.save()
        return redirect('indexmenu')
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

