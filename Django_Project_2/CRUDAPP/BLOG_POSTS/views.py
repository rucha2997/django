from django.shortcuts import get_object_or_404, redirect, render
from .form import BlogForm
from .models import Blog

def post_list(request):
    blog_post = Blog.objects.all()
    return render(request,"BLOG_POSTS/Post_List.html",{'object_list':blog_post})
    
def post_view(request,pk):
    blog_post= get_object_or_404(Blog,pk=pk)
    return render(request,"BLOG_POSTS/Post_Details.html",{'object':blog_post})

def post_update(request,pk):
    blog_post=get_object_or_404(Blog,pk=pk)
    form = BlogForm(request.POST or None,instance=blog_post)
    if form.is_valid():
        form.save()
        return redirect(post_list)
    return render(request, 'BLOG_POSTS/Post_Form.html',{'form':form})

def post_delete(request,pk):
    blog_post = get_object_or_404(Blog,pk=pk)
    if request.method =='POST':
        blog_post.delete()
        return redirect(post_list)

    return render(request,"BLOG_POSTS/Post_delete.html",{'object':blog_post})

def post_create(request):
    form = BlogForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(post_list)
    return render(request, 'BLOG_POSTS/Post_Form.html',{'form':form})