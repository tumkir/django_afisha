import os

import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from places.models import Image, Place


class Command(BaseCommand):
    help = 'Upload new place and image to database from json file'

    def add_arguments(self, parser):
        parser.add_argument('url', type=str, help='Вставьте url на json файл с данными')

    def handle(self, *args, **options):
        response = requests.get(options['url'])
        response.raise_for_status()
        place_data = response.json()

        place, created = Place.objects.update_or_create(
            title=place_data['title'],
            longitude=place_data['coordinates']['lng'],
            latitude=place_data['coordinates']['lat'],
            defaults={
                'short_description': place_data['description_short'],
                'long_description': place_data['description_long'],
            }
        )

        for image_number, image_url in enumerate(place_data['imgs'], 1):
            response = requests.get(image_url)
            response.raise_for_status()

            image_content = ContentFile(response.content)

            place_image, created_image = Image.objects.get_or_create(
                place=place,
                image_number=image_number,
            )

            image_filename = os.path.split(image_url)[-1]

            place_image.image.save(image_filename, image_content, save=True)

        if created:
            self.stdout.write(self.style.SUCCESS(f'Successfully loaded place "{place}"'))
        else:
            self.stdout.write(self.style.SUCCESS(f'Place "{place}" already exists'))
