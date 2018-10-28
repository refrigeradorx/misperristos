from .models import Post
from django.shortcuts import render,redirect
from .forms import PostForm
# Create your views here.

def formulario(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contactanos')
    else:
        form = PostForm()
    return render(request,'blog/contactanos.html',{'form': form})