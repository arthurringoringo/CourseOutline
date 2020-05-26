from django.urls.resolvers import URLPattern
from django.urls import path
from . import views

urlpatterns = [
     
     #CURRICULUM URLS
     path('',views.IndexMenu,name='indexmenu'),
     path('create/curriculum/',views.CurriculumCreate,name='curriculumcreate'),
     path('curriculum/<int:curriculum_id>/delete/',views.CurriculumDelete,name='curriculumdelete'),
     path('curriculum/<int:id>/update/',views.CurriculumUpdate.as_view(),name='update'),
     path('curriculum/view/all/',views.CurriculumList.as_view(),name='curriculumlistview'),
     #COURSEOUTLINE URLS
     path('create/courseoutline/',views.CourseoutlineCreate,name='courseoutlinecreate'),
     path('view/courseoutline/<int:courseoutline_id>/',views.CourseoutlineView,name='courseoutlineview'),
     path('<int:courseoutline_id>/delete/',views.CourseoutlineDelete,name='courseoutlinedelete'),
     path('<int:id>/update/',views.CourseoutlineUpdate.as_view(),name='courseoutlineupdate'),
     #COURSEOUTLINE SECTIONS URLS
     path('<int:courseoutline_id>/create/sections/',views.Courseoutlinesectionscreate,name='courseoutlinesectioncreate'),
     path('view/sections/<int:courseoutline_id>/',views.Courseoutlinesectionslist,name='courseoutlinesectionlist'),
     path('update/sections1/<int:id>/',views.CourseoutlineSection1Update.as_view(),name='courseoutlinesectionupdate'),
     path('update/sections2/<int:id>/',views.CourseoutlineSection2Update.as_view(),name='courseoutlinesectionupdate2'),
     path('update/sections3/<int:id>/',views.CourseoutlineSection3Update.as_view(),name='courseoutlinesectionupdate3'),
     path('create/sections4/<int:courseoutline_id>/',views.CourseoutlineSection4Create,name='courseoutlinesection4create'),
     path('update/sections4/<int:id>/',views.CourseoutlineSection4Update.as_view(),name='courseoutlinesectionupdate4'),
     path('delete/sections4/<int:courseoutlinesection_id>/',views.CourseoutlineSection4Delete,name='courseoutlinesectiondelete4'),
     path('create/sections5/<int:courseoutline_id>/',views.CourseoutlineSection5Create,name='courseoutlinesection5create'),
     path('update/sections5/<int:id>/',views.CourseoutlineSection5Update.as_view(),name='courseoutlinesectionupdate5'),
     path('delete/sections5/<int:courseoutlinesection_id>/',views.CourseoutlineSection5Delete,name='courseoutlinesectiondelete5'),
     path('create/sections6/<int:courseoutline_id>/',views.CourseoutlineSection6Create,name='courseoutlinesection6create'),
     path('update/sections6/<int:id>/',views.CourseoutlineSection6Update.as_view(),name='courseoutlinesectionupdate6'),
     path('delete/sections6/<int:courseoutlinesection_id>/',views.CourseoutlineSection6Delete,name='courseoutlinesectiondelete6'),
]

