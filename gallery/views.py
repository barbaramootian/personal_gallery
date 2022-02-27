from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Image, Location, Category


# Create your views here.
# index.html view
def index(request):
    all_image = Image.objects.all()
    all_location = Location.objects.all()
    context = {'all_image': all_image, 'all_location': all_location}
    return render(request, 'gallery/index.html', context)


# def search_results(request):
#     if 'location' in request.GET and request.GET["location"]:
#         search_term = request.GET.get("location")
#         searched_images = Image.search_by_category(search_term)
#         message = f"{search_term}"
#         return render(request, 'gallery/search.html', {"message": message, "locations": searched_images})
#     else:
#         message = "You haven't searched for any term"
#         return render(request, 'gallery/search.html', {"message": message})


# def area_results(request, id):
#     area = Image.filter_by_location(id)
#     all_image = Image.objects.all()
#     all_location = Location.objects.all()
#     context = {'all_image': all_image, 'all_location': all_location, "image": area}
#     return render(request, "gallery/location.html", context)
