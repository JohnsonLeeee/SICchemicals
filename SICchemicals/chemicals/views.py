from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse('欢迎登陆碳化物课题组药品管理系统')

