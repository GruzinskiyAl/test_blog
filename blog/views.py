from django.shortcuts import render
from .models import Post

# Create your views here.
def post_list(request):
    posts = Post.objects.order_by('id').reverse()
    return render(request, 'index.html', {'posts': posts})