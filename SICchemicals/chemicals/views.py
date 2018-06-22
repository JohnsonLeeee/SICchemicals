from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect

# Create your views here.


def index(request):
    username = "visitor"
    password = "123456"
    user = authenticate(username=username, password=password)
    if user is not None and user.is_active:
        login(request, user)
        return HttpResponseRedirect("admin/chemicals/chemical/")
    else:
        return HttpResponse(u"登录失败，请联系李帅13122386386")





