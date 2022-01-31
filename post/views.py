from django.shortcuts import render,get_object_or_404,redirect
from .models import Post
from .forms import PostForm
from django.contrib import messages
# Create your views here.
def all_posts(request):
    all_posts = Post.objects.filter(active=True)
    context = { "all_posts": all_posts}
    return render(request, 'all_posts.html', context)

def post(request, pk):
    #post = Post.objects.get(pk=pk)
    post = get_object_or_404(Post, pk=pk)
    context ={ "post": post}
    return render(request, "detail.html", context)
def createPost(request):
    if (request.method == 'POST'):
        form = PostForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            messages.success(request, 'Post created successfully')
            return redirect('/')
    else:
        form = PostForm()
    context={
        "form": form
    }
    return render(request, 'create.html', context)
def editPost(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if (request.method == 'POST'):
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            new_form = form.save(commit=False)
            #new_form.user = request.user
            new_form.save()
            return redirect('/')
    else:
        form = PostForm(instance=post)
    context={
        "form": form
    }
    return render(request, 'edit.html', context)
