from django.shortcuts import render
from django.http import HttpResponse
from vid.models import Video
# Create your views here.

def index(request):
    context = {
        'videos': Video.objects.all()
    }
    return render(request, 'vid/index.html', context=context)

def video(request, video_id):
    context = {
        'video': Video.objects.get(id=video_id)
    }
    return render(request, 'vid/video.html', context=context)
