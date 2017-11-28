from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from django.contrib import auth


# Create your views here.
def post_list(request):
    username = auth.get_user(request).username
    posts = Post.objects.order_by('id').reverse()
    return render(request, 'index.html', {'posts': posts, 'username': username})


def post_detail(request, pk):
    username = auth.get_user(request).username
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post, 'username': username})




