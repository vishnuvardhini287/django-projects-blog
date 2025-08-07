from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm, CommentForm, AttachmentFormSet
from .models import Post

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        formset = AttachmentFormSet(request.POST, request.FILES)
        if form.is_valid() and formset.is_valid():
            post = form.save()
            formset.instance = post
            formset.save()
            return redirect('post_detail', post.id)
    else:
        form = PostForm()
        formset = AttachmentFormSet()
    return render(request, 'blog/create_post.html', {
        'form': form,
        'formset': formset,
    })

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    attachments = post.attachments.all()
    comments = post.comments.all()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', post.id)
    else:
        comment_form = CommentForm()

    return render(request, 'blog/post_detail.html', {
        'post': post,
        'attachments': attachments,
        'comments': comments,
        'comment_form': comment_form,
    })

# blog/views.py

from django.shortcuts import render

def home(request):
    return render(request, 'blog/home.html')


