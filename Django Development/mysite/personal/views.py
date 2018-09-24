from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from fetching import * 

var = query_with_fetchall()     #for y axis
var_label = query_with_fetchall1()   #for x axis


def index(request, *args, **kwargs):
    return render(request, 'personal/charts.html', {})
def contact(request):
    return render(request, 'personal/basic.html',{'content':['If you would like to contact me, please email me.','hskinsley@gmail.com']})


def get_data(request, *args, **kwargs):
    data = {'sales':100,
            'customers': 10,}
    return JsonResponse(data)

class ChartData(APIView):

    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        labels = var_label
        defaultitems = var
        data = { 'labels': labels,   
                'defaultdata': defaultitems,}
        return Response(data)   
