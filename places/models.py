from django.db import models


class Place(models.Model):
    title = models.CharField('Название экскурсии', max_length=200, db_index=True)
    description_short = models.CharField('Короткое описание', max_length=500)
    description_long = models.TextField('Длинное описание')
    longitude = models.DecimalField('Долгота', max_digits=17, decimal_places=14)
    latitude = models.DecimalField('Широта', max_digits=17, decimal_places=14)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Экскурсия'
        verbose_name_plural = 'Экскурсии'


class Image(models.Model):
    place = models.ForeignKey(Place, verbose_name='название экскурсии', on_delete=models.CASCADE, related_name='image')
    image = models.ImageField(verbose_name='Фотографии экскурсии', upload_to='image', null=True)
    image_number = models.PositiveSmallIntegerField(verbose_name='Номер картинки')

    def __str__(self):
        return self.place

    class Meta:
        verbose_name = 'Изображение экскурсии'
        verbose_name_plural = 'Изображения экскурсии'
        ordering = ['place', 'image_number']
