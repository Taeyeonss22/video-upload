from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .forms import VideoForm
from .models import Video
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def index(request):
    files = Video.objects.all().order_by('-id')
    return render(request, 'index.html', {'files':files})

def subir_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            video.subido_por = request.user
            form.save()
            return redirect('index')
    else:
        form = VideoForm()
    return render(request, 'upload_video.html', {'form':form})
