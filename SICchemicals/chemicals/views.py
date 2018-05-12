from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse('欢迎登陆碳化物课题组药品管理系统')


def hello(request):  # 功能选择
    # t = loader.get_template("hello.html")
    # c = RequestContext(request)
    return render_to_response("hello.html", context_instance=RequestContext(request))
    return render(request, "hello.html", )

def addstu(request):# 添加学生信息
  name = request.POST.get("name")
  age = request.POST.get("age")
  learn = request.POST.get("learn")
  newstu = Student(name=name,age=age,learn=learn)
  newstu.save()
  # c = RequestContext(request)
  # t = loader.get_template("check.html")
  return render_to_response("done.html",context_instance=RequestContext(request,{"age":age,"learn":learn,"name":name}))
