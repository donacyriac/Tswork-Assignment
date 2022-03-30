from django.shortcuts import render
from django.http.response import JsonResponse

from assignapp.models import Industry
from assignapp.serializer import IndustrySerializer

# Create your views here.

def GetAllRecordbyDateApi(request,date=""):
    if request.method=='GET':
        industry=Industry.objects.filter(date=date)
        industry_serializer=IndustrySerializer(industry,many=True)
        return JsonResponse(industry_serializer.data,safe=False)
