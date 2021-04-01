from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from main.forms import PostForm
from main.models import Post


def index(request):
    return render(request, "main/index.html",{'title' :'homepage' })

def about(request):
    return render(request, "main/about.html",{'title' :'about' })

def posts(request):
    _posts = Post.objects.all()
    return render(request, "main/posts.html", {'title': "Posts", "posts": _posts})


def post_create(request):
    errors = ''
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            errors = "Cannot save the post"
    else:
        form = PostForm()
    context = {
        "form": form,
        "errors": errors
    }
    return render(request, "main/post_create.html", context=context)

def post_api(request):
    posts = Post.objects.all()
    data = [dict(title=post.title,description=post.description,content = post.content) for post in posts]       
    return JsonResponse(data, safe = False)