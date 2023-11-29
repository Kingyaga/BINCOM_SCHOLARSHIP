from django.urls import path
from . import views

app_name = "videos" 
urlpatterns = [
    path("", views.index, name = "index"),
    path("Video_List_View", views.VideoListView, name = "videoList"),
    path("Video_Detail_View", views.VideoDetailView, name = "videoDetail"),
    path("Video_Upload_View", views.VideoUploadView, name = "videoUpload")
]