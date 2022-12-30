from django.urls import path
from app2.views import *
app_name='second'

urlpatterns=[ 
    path('html2/',html2,name='html2'),
]