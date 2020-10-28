from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from places.models import Place


def index_page(request):
    places_geojson = {
        'type': 'FeatureCollection',
        'features': [{
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [place.longitude, place.latitude]
            },
            'properties': {
                'title': place.title,
                'placeId': place.id,
                'detailsUrl': reverse(place_data, args=[place.id])
            }
        } for place in Place.objects.all()]
    }

    data = {'places_geojson': places_geojson}
    return render(request, 'index.html', context=data)


def place_data(request, place_id):
    place = get_object_or_404(Place, id=place_id)

    place_data = {
        'title': place.title,
        'imgs': [image.image.url for image in place.images.all()],
        'description_short': place.short_description,
        'description_long': place.long_description,
        'coordinates': {
            'lng': place.longitude,
            'lat': place.latitude
        }
    }

    return JsonResponse(place_data, json_dumps_params={'ensure_ascii': False, 'indent': 4})
