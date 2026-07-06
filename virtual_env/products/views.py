from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def test(request):
    return HttpResponse("this is index page")

def index(request):
    data = {
        "name": "Adam",
        "age": 25
    }
    return render(request, 'products/index.html',context = data)