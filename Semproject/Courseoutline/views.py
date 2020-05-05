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

def IndexMenu(request,tempalate_name='courseoutline/index.html'):
    return render(request,'courseoutline/index.html')


def CourseoutlineCreate(request,template_name='courseoutline/test.html'):
    form1 = CreateCourseOutlineForm(request.POST)
    
    context = {'form':form1}
    return render(request,'courseoutline/test.html',context)

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

class CurriculumView(generic.DetailView):
        template_name: 'Courseoutline/curriculum_Detail.html'
        model = Curriculum


def CurriculumDelete(request,curriculum_id):
    obj = get_object_or_404(Curriculum,pk=curriculum_id)
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect('indexmenu')
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