# Generated by Django 3.1.2 on 2020-10-27 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0006_auto_20201022_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='image', verbose_name='Картинка'),
        ),
    ]