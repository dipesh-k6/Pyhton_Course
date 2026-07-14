from django.shortcuts import render
from django.http import HttpResponse
from .models import Category

# Create your views here.
def test(request):
    return HttpResponse("this is index page")

def index(request):
    data = {
        "name": "Adam",
        "age": 25
    }
    return render(request, 'products/index.html',context = data)

def get_all_categories(request):
    categories = Category.objects.all()
    return render(request,"products/category_list.html", {
        "categories":categories
    } )