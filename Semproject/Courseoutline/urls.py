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
     #COURSEOUTLINE SECTIONS URLS
     path('<int:courseoutline_id>/create/sections/',views.Courseoutlinesectionscreate,name='courseoutlinesectioncreate'),
     path('view/sections/<int:courseoutline_id>/',views.Courseoutlinesectionslist,name='courseoutlinesectionlist'),
     path('update/sections1/<int:id>/',views.CourseoutlineSection1Update.as_view(),name='courseoutlinesectionupdate'),
     path('update/sections2/<int:id>/',views.CourseoutlineSection2Update.as_view(),name='courseoutlinesectionupdate2'),
     path('update/sections3/<int:id>/',views.CourseoutlineSection3Update.as_view(),name='courseoutlinesectionupdate3'),
]

