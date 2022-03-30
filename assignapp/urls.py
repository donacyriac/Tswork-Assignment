from django.urls import re_path
from . import views

urlpatterns=[
    re_path(r'^getallrecordbydate/(?P<date>\d{4}-\d{2}-\d{2})$',views.GetAllRecordbyDateApi),

]