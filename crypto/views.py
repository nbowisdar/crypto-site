from django.shortcuts import render
from crypto.models import Post

def post(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'crypto/post_page.html', {'post':post})

def main(request):
    posts = Post.objects.filter(visible=True).order_by('-created')
    return render(request, "crypto/main_page.html", context={'posts':posts})

def page404(request, exception):
    return render(request, 'crypto/page404.html', status=404)

