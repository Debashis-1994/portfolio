from django.shortcuts import render
from .models import Blog

# Create your views here.
def all_blogs(request):
    #blogs=Blog.objects.all()
    #if we want to order by date:
    blogs=Blog.objects.order_by('-Date')[:5]
    return render(request,'blog/all_blogs.html',{'BLOGS':blogs})
