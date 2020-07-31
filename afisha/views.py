from django.shortcuts import render
from places.models import Place


def index_page(request):
    places_geojson = {
        'type':
        'FeatureCollection',
        'features': [{
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [place.longitude, place.latitude]
            },
            'properties': {
                'title': place.title,
                'placeId': place.id,
                'detailsUrl': ''
            }
        } for place in Place.objects.all()]
    }

    data = {'places_geojson': places_geojson}
    return render(request, 'index.html', context=data)
