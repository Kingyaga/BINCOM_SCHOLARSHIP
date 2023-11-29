from django.shortcuts import render, get_object_or_404, redirect
from .models import Images
from .forms import ImageUploadForm

# View to list all images
def ImageListView(request):
    images = Images.objects.all()
    return render(request, 'images/image_list.html', {'images': images})

# View to display details of a specific image
def ImageDetailView(request, pk):
    image = get_object_or_404(Images, pk=pk)
    return render(request, 'images/image_detail.html', {'image': image})

# View to handle image uploads
def ImageUploadView(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('images:imageList')  # Redirect to the image list view
    else:
        form = ImageUploadForm()
    return render(request, 'images/image_upload.html', {'form': form})