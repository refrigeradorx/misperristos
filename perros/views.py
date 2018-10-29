from .models import Post
from django.shortcuts import render,redirect
from .forms import PostForm
# Create your views here.

def lista_rescate(request):
    rescata = Post.objects.all()
    return render(request, "perros/rescatados.html",{'rescata':rescata})

def formularioperro(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('servicios')
    else:
        form = PostForm()
    return render(request,'perros/rescatados.html',{'form': form})

