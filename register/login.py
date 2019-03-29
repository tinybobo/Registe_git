from django.shortcuts import render
from django.views.decorators import csrf
from TestModel.models import Test
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# 接收POST请求数据
# @csrf_exempt #增加装饰器，作用是跳过 csrf 中间件的保护
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        if(request.POST['name']!="" and request.POST['age']!=""):
            new_person = Test(name=request.POST.get('name'), age=request.POST.get('age'))
            new_person.save()
            return JsonResponse({'msg': "success"})
        else:
            return JsonResponse({'msg': "false"})