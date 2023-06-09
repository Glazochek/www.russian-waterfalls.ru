# Generated by Django 4.0.3 on 2022-09-11 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0011_waterfall_district_waterfall_district_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Administrative_District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Administrative_District_name', models.CharField(default='не указанно', max_length=128, verbose_name='Имя')),
                ('Administrative_District_description', models.TextField(default='не указанно', max_length=60, verbose_name='описание')),
            ],
        ),
        migrations.AddField(
            model_name='waterfall',
            name='Administrative_District_id',
            field=models.PositiveIntegerField(default=0, verbose_name='айди административного района'),
        ),
    ]
