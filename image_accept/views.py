from django.shortcuts import render
from .models import image_model

# Create your views here.
def homepage(request):
    if request.method == 'POST' and request.FILES.get('image'):
        image_upload = request.FILES['image']

        new_image = image_model(image = image_upload)

        new_image.save()

    image_list = image_model.objects.all()

    context = {
        'image_list': image_list
    }
    return render(request, 'base/index.html', context)