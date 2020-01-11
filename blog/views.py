from django.shortcuts import render
from django.http import HttpResponse
from . models import Post
from django.utils import timezone
from django.shortcuts import render, get_object_or_404

from django.template.utils import get_app_template_dirs


# Create your views here.
# def home(request):
#     return HttpResponse("<h1>Hello World!</h1>")

# def about(request):
#     return HttpResponse("<h2>Boli mnie brzuszek</h2>")

def post_list(request):
    posts = Post.objects.filter(published_date__lte = timezone.now()).order_by("published_date")
    return render(request, "blog/post_list.html", {"posts": posts})
    # return HttpResponse(get_app_template_dirs('templates'))

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
