from django.shortcuts import render, get_object_or_404, redirect
from .models import Music
from .forms import MusicUploadForm

# View to list all music
def MusicListView(request):
    music = Music.objects.all()
    return render(request, 'music/music_list.html', {'music': music})

# View to display details of a specific music
def MusicDetailView(request, pk):
    music = get_object_or_404(Music, pk=pk)

    # Retrieve user-specific rating information from session
    user_rated = request.session.get(f'user_rated_{pk}', False)
    user_rating = request.session.get(f'user_rating_{pk}', None)
     
    return render(request, 'music/music_detail.html', 
                  {'music': music,
                   'user_rated': user_rated,
                   'user_rating': user_rating
                   })

# View to handle music uploads
def MusicUploadView(request):
    if request.method == 'POST':
        form = MusicUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('music:musicList')  # Redirect to the music list view
    else:
        form = MusicUploadForm()
    return render(request, 'music/music_upload.html', {'form': form})

# Rate music
def rate_music(request, music_id):
    music = get_object_or_404(Music, id=music_id)
    
    if request.method == 'POST':
        rating = request.POST.get('rating')
        if rating is not None:
            rating = int(rating)
            # Store user-specific rating information in session
            request.session[f'user_rated_{music_id}'] = True
            request.session[f'user_rating_{music_id}'] = rating
            music.total_ratings += 1
            music.total_rating_value += rating
            music.save()
        return redirect('music:musicDetail', pk=music_id)
    return render(request, 'music/rate_music.html', {'music': music})