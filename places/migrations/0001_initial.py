# Generated by Django 3.0.7 on 2020-06-09 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=200, verbose_name='Название экскурсии')),
                ('description_short', models.CharField(max_length=500, verbose_name='Короткое описание')),
                ('description_long', models.TextField(verbose_name='Длинное описание')),
                ('longitude', models.DecimalField(decimal_places=14, max_digits=16, verbose_name='Долгота')),
                ('latitude', models.DecimalField(decimal_places=14, max_digits=16, verbose_name='Широта')),
            ],
        ),
    ]
