from django.urls.resolvers import URLPattern
from django.urls import path
from . import views

urlpatterns = [
     path('',views.IndexMenu,name='indexmenu'),
     path('create/curriculum/',views.CurriculumCreate,name='curriculumcreate'),
     path('<int:pk>/view/',views.CurriculumView.as_view(),name='curriculumview'),
     path('<int:curriculum_id>/delete/',views.CurriculumDelete,name='curriculumdelete'),
   #  path('<int:pk>/update',views.Update,name='update'),

]
