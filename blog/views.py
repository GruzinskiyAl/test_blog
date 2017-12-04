from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from django.contrib import auth
from .forms import PostForm
from django.shortcuts import redirect
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer


def post_list(request):
    username = auth.get_user(request).username
    posts = Post.objects.order_by('pk').reverse()
    return render(request, 'index.html', {'posts': posts, 'username': username})


def post_detail(request, pk):
    username = auth.get_user(request).username
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post, 'username': username})


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'create_new_post.html', {'form': form})


# @api_view(['GET'])
# def PostViewSet(request):
#     if request.method == 'GET':
#         username = auth.get_user(request).username
#         posts = Post.objects.order_by('published_date').reverse()
#         serializer = PostSerializer(posts, many=True)
#         return Response(serializer.data)
