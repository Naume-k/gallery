from django.http  import HttpResponse, Http404
from django.shortcuts import render,redirect
from .models import Image,Category, Location, Image

# views here.

def image_list(request):
    images = Image.image_list()
    return render(request, 'index.html',{"images":images})


def search_results(request):

    if 'image_category' in request.GET and request.GET["image_category"]:
        searched_category = request.GET.get("image_category")
        images = Image.search_by_category(searched_category)
        message = f"{searched_category}"

        return render(request, 'search.html',{"message":message,"images":images})

    else:
        message = "Enter a category"
        return render(request, 'search.html',{"message":message})

def image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,{"image":image, id: image_id})

def location_filter(request,image_location_id):
    images = Image.filter_by_location(id=image_location_id)
    return render(request,'location.html',{"images":images,"image_location_id":image_location_id})

