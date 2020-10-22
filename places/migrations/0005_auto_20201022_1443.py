# Generated by Django 3.1.2 on 2020-10-22 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_auto_20200817_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image', to='places.place', verbose_name='Экскурсия'),
        ),
        migrations.AlterField(
            model_name='place',
            name='description_short',
            field=models.TextField(verbose_name='Короткое описание'),
        ),
    ]
