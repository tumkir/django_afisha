# Generated by Django 3.0.8 on 2020-07-02 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('excursion_image', models.ImageField(null=True, upload_to='excursion_image', verbose_name='Фотографии экскурсии')),
                ('image_number', models.IntegerField(verbose_name='Номер картинки')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='excursion_image', to='places.Place', verbose_name='название экскурсии')),
            ],
        ),
    ]