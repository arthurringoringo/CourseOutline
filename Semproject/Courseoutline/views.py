from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render
from django.http.response import HttpResponse, HttpResponseRedirect
from .models import *
from django.urls import reverse
from django.views import generic
from .forms import *
from datetime import datetime

# Create your views here.

def CourseoutlineCreate(request,template_name='courseoutline/test.html'):
    form1 = CreateForm(request.POST)
    
    context = {'form':form}
    return render(request,'courseoutline/test.html',context)