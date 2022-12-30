from django.urls import path
from app1.views import *
app_name='first'

urlpatterns=[ 
    path('html1/',html1,name='html1'),
]