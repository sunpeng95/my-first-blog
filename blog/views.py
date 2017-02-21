from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    posts = Post.objects.filter(publishded_date__lte=timezone.now()).order_by('publishded_date')
    return render(request, 'blog/post_list.html',{'posts': posts})