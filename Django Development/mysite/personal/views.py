from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from fetching import *




def index(request, *args, **kwargs):
    defaultdata= query_with_fetchall() # for y axis
    labels = query_with_fetchall1() # for x axis


    return render(request, 'personal/charts.html', {"my_data":defaultdata,"my_data2":labels})
def contact(request):
    return render(request, 'personal/basic.html',{'content':['If you would like to contact me, please email me.','hskinsley@gmail.com']})



