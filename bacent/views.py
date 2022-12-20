from django.shortcuts import render
from bacent.views import *
from .models import Post
from .models import TopPost
from django.views.generic import TemplateView

def home(request):
    posts = Post.objects.all()
    top = TopPost.objects.all()
    context = {
        'posts':posts,
        'top':top
    }
    return render(request ,  'index.html', context)

class AboutView(TemplateView):
    template_name = 'about.html'
 
