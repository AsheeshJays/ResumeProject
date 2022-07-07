from django.urls import path
from Resume import views

urlpatterns = [
    path('',views.Index,name='index'),
    path('skill/',views.skill,name='skill'),
    path('services/', views.services,name="services"),
    path('education/', views.education,name="education"),
    path('contact/', views.contact,name='contact'),
]
