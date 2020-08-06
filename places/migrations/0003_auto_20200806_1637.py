# Generated by Django 3.1 on 2020-08-06 16:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_auto_20200804_0751'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['image_number'], 'verbose_name': 'Фотография', 'verbose_name_plural': 'Фотографии'},
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(null=True, upload_to='image', verbose_name='Картинка'),
        ),
        migrations.AlterField(
            model_name='image',
            name='image_number',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Позиция'),
        ),
        migrations.AlterField(
            model_name='image',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image', to='places.place', verbose_name='Название экскурсии'),
        ),
    ]