from django.urls.resolvers import URLPattern
from django.urls import path
from . import views

urlpatterns = [
     path('',views.IndexMenu,name='indexmenu'),
     path('create/curriculum/',views.CuriculumCreate,name='curriculumcreate'),
     path('',views.IndexMenu,name='indexmenu'),
     path('',views.IndexMenu,name='indexmenu'),
     path('',views.IndexMenu,name='indexmenu'),
     path('',views.IndexMenu,name='indexmenu'),
     path('',views.IndexMenu,name='indexmenu'),
]
