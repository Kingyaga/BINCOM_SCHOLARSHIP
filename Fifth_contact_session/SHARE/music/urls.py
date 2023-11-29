from django.urls import path
from . import views

app_name = "music"
urlpatterns = [
    path("", views.index, name = "index"),
    path("Music_List_View", views.MusicListView, name = "musicList"),
    path("Music_Detail_View/<int:pk>", views.MusicDetailView, name = "musicDetails"),
    path("Music_Upload_View", views.MusicUploadView, name = "musicUpload"),
    path("rate_music/<int:music_id>", views.rate_music, name = "rateMusic")
]