from django.http import HttpResponse
from TestModel.models import Test
from django.shortcuts import render


def testdb(request):
    # Test.objects.all().delete()
    # test1 = Test(name="dongbo", age="18")
    # test1.save()
    # test2 = Test(name="bobo", age="20")
    # test2.save()
    list = Test.objects.all()
    return render(request, 'manage.html', {'list': list})