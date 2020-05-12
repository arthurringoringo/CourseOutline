from django.urls.resolvers import URLPattern
from django.urls import path
from . import views

urlpatterns = [
     
     #CURRICULUM URLS
     path('',views.IndexMenu,name='indexmenu'),
     path('create/curriculum/',views.CurriculumCreate,name='curriculumcreate'),
     #path('<int:pk>/view/',views.CurriculumView.as_view(),name='curriculumview'),
     path('curriculum/<int:curriculum_id>/delete/',views.CurriculumDelete,name='curriculumdelete'),
     path('curriculum/<int:id>/update/',views.CurriculumUpdate.as_view(),name='update'),
     #COURSEOUTLINE URLS
     path('create/courseoutline/',views.CourseoutlineCreate,name='courseoutlinecreate'),
     path('<int:courseoutline_id>/delete/',views.CourseoutlineDelete,name='courseoutlinedelete'),
     path('<int:id>/update/',views.CourseoutlineUpdate.as_view(),name='courseoutlineupdate'),
     path('<int:courseoutline_id>/create/sections/',views.Courseoutlinesectionscreate,name='courseoutlinesectioncreate')

]
