from django.shortcuts import render
from django.contrib import messages
from .models import News, Category, Comment

# Create your views here.
def home(request):
    fnews=News.objects.last()
    nnews=News.objects.all()[0:3]
    three_cat = Category.objects.all()[0:3]
    return render(request,'index.html',{'firstn':fnews,'threenews':nnews,'threecat':three_cat})

def allnews(request):
    fnews = News.objects.all()
    return render(request,'news.html',{'fnews':fnews})

def onenews(request,id):
    fnews = News.objects.get(id=id)
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        Comment.objects.create(
            news=fnews,
            name=name,
            email=email,
            comment=message
        )
        messages.success(request,'Comment submitted')
    comments = Comment.objects.filter(news=fnews,status=True).order_by('-id')
    return render(request,'onenews.html',{'fnews':fnews,'comments':comments })