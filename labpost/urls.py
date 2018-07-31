from django.urls import path
from . import views

urlpatterns = [
    path('', views.labReportInput, name = 'labReportInput'),
    path('report/', views.labReportGenerate, name = 'labReportGenerate'),

]
