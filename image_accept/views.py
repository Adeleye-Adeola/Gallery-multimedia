from django.shortcuts import render, redirect
from .models import image_model
from django.http import JsonResponse

# Create your views here.
def homepage(request):
    if request.method == 'POST' and request.FILES.get('image'):
        image_upload = request.FILES['image']

        new_image = image_model(image = image_upload)

        new_image.save()
        return JsonResponse({"message": "Image uploaded successfully"}, status=200)

    image_list = image_model.objects.all()

    

    context = {
        'image_list': image_list
    }
    return render(request, 'base/index.html', context)


def delete_image(request, pk):
    if request.method == 'POST':
        item = image_model.objects.get(id = pk)

        item.delete()

        return JsonResponse({"message": "Image deleted successfully"}, status=200)
        return redirect('home')