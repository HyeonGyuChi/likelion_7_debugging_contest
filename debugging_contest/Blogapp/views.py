from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .form import PostForm
from .models import Post

def index(request):
    posts = Post.objects.all().order_by('-pub_date')
    return render(request, 'index.html', {'posts':posts})

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'detail.html', {'post':post})

def delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return redirect('index')

def newpost(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('detail', post.id)
    else:
        form = PostForm()
        return render(request, 'new.html', {'forms':form})

def edit(request,post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)    
        post = form.save(commit=False)
        post.pub_date = timezone.now()
        post.save()
        return redirect('detail', post.id)

    else :
        form = PostForm(instance=post)
        return render(request, 'edit.html', {'form':form})
