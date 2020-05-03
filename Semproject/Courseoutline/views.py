from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render
from django.http.response import HttpResponse, HttpResponseRedirect
from .models import *
from django.urls import reverse
from django.views import generic
from .forms import *
from datetime import datetime

# Create your views here.

def IndexMenu(request,tempalate_name='courseoutline/index.html'):
    return render(request,'courseoutline/index.html')


def CourseoutlineCreate(request,template_name='courseoutline/test.html'):
    form1 = CreateCourseOutlineForm(request.POST)
    
    context = {'form':form1}
    return render(request,'courseoutline/test.html',context)

def CuriculumCreate(request,template_name='Courseoutline/curriculumSection.html'):
    curriculumForm = CreateCurriculumForm(request.POST)
    
    context = {'curriculumForm': curriculumForm}
    return render(request,'Courseoutline/curriculumSection.html',context)