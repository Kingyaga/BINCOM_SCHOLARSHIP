from django.shortcuts import render, get_object_or_404, redirect
from .models import Video
from .forms import VideoUploadForm

# View to list all videos
def VideoListView(request):
    videos = Video.objects.all()
    return render(request, 'videos/video_list.html', {'videos': videos})

# View to display details of a specific video
def VideoDetailView(request, pk):
    video = get_object_or_404(Video, pk=pk)
    return render(request, 'videos/video_detail.html', {'video': video})

# View to handle video uploads
def VideoUploadView(request):
    if request.method == 'POST':
        form = VideoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('videos:videoList')  # Redirect to the video list view
    else:
        form = VideoUploadForm()
    return render(request, 'videos/video_upload.html', {'form': form})