import base64
from django.db import models
from django.http import HttpResponse


class Waterfall(models.Model):

    name = models.CharField(verbose_name="Имя", max_length=128, default='-')
    image = models.ImageField(blank=True, verbose_name="фото", upload_to='waterfalls_images', default='-')
    description = models.TextField(verbose_name='описание', max_length=1024, default='-')
    place = models.TextField(verbose_name='место', max_length=60, default='-')

    height = models.PositiveIntegerField(verbose_name='высота', default=0)
    weight = models.PositiveIntegerField(verbose_name='ширина', default=0)
    S_catchment = models.PositiveIntegerField(verbose_name='Площадь водосбора', default=0)
    S_mirror = models.PositiveIntegerField(verbose_name='Площадь зеркала в кв. м', default=0)
    water_consumption = models.PositiveIntegerField(verbose_name='Расход воды в куб. м', default=0)
    Altitude_above_sea_level = models.PositiveIntegerField(verbose_name='Высота над ур. моря', default=0)
    Energy_joules = models.PositiveIntegerField(verbose_name='Энергия в джоулях', default=0)
    type = models.TextField(verbose_name='тип', max_length=60, default='-')

    cordinats = models.TextField(verbose_name='кординаты', default='-')
    District_id = models.PositiveIntegerField(verbose_name='айди района', default=1)
    Administrative_District_id = models.PositiveIntegerField(verbose_name='айди административного района', default=1)

    def __str__(self):
        return f"{self.name}"


class Waterfall_District(models.Model):
    District_name = models.CharField(verbose_name="Имя", max_length=128, default='не указанно')
    District_description = models.TextField(verbose_name='описание', max_length=60, default='не указанно')

    def __str__(self):
        return f"{self.District_name}"


class Administrative_District(models.Model):
    Administrative_District_name = models.CharField(verbose_name="Имя", max_length=128, default='не указанно')
    Administrative_District_description = models.TextField(verbose_name='описание', max_length=60, default='не указанно')

    def __str__(self):
        return f"{self.Administrative_District_name}"


class Text(models.Model):
    text_name = models.CharField(verbose_name="название", max_length=128, default=' ')
    text = models.TextField(verbose_name='текст', max_length=8192, default=' ')

    def __str__(self):
        return f"{self.text_name}"
