from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from fetching import *
import json




def index(request, *args, **kwargs):
    return render(request, 'personal/charts.html', {})
def contact(request):
    return render(request, 'personal/basic.html',{'content':['If you would like to contact me, please email me.','hskinsley@gmail.com']})


def ajax(request):
    defaultdata= query_with_fetchall() # for y axis
    labels = query_with_fetchall1() # for x axis
    data = {'defaultdata': defaultdata, 'labels': labels}
    return JsonResponse(data)
