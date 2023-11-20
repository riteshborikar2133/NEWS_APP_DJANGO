from django.shortcuts import render
from .models import News, Category

# Create your views here.
def home(request):
    fnews=News.objects.last()
    nnews=News.objects.all()[0:3]
    three_cat = Category.objects.all()[0:3]
    return render(request,'index.html',{'firstn':fnews,'threenews':nnews,'threecat':three_cat})