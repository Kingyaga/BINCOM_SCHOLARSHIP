from django.urls import path
from . import views

app_name = "images"
urlpatterns = [
    path("", views.index, name = "index"),
    path("Image_List_View", views.ImageListView, name = "imageList"),
    path("Image_Detail_View", views.ImageDetailView, name = "imageDetail"),
    path("Image_Upload_View", views.ImageUploadView, name = "imageUpload")
]