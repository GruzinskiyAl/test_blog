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


def post_change(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            post.title = data['title']
            post.text = data['text']
            post.author = request.user.username
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'change_post.html', {'form': form})


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


@api_view(['GET', 'POST'])
def post_list_set(request):
    if request.method == 'GET':
        posts = Post.objects.order_by('pk').reverse()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def post_detail_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def message(request):
    if request.method == 'GET':
        mes = 'Hello world!'
        # serializer = PostSerializer(mes)
        return Response(mes)