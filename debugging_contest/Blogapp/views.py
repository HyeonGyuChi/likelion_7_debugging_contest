from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .form import PostForm
from .models import Blog

def index(request, post.id):
    posts = Post.objects.all()
    #order_by('-id') 없애고 난 후에 최근에 쓴 글이 맨 위로 올라오게 해달라고 md 파일에 정리해 놓으면 좋을 듯

    return render(request, 'index.html', {'posts':posts})

def detail(request, post.id):
    post = get_object_or_404(Post, pk=post_id)

    return render(request, 'detail.html', {'post':post})

def delete(request, post.id):
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
        return redirect('/post/'+post.id)
    form = PostForm()
    return render(request, 'new.html', {'forms':form})

def edit(request,post.id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
    if form.is_valid():
        post = form.save(commit=False)
        post.pub_date = timezone.now()
        post.save()
        return redirect('post/'+str(post.id)
    form = PostForm(instance=post)
    return render(request, 'edit.html', {'form':form})