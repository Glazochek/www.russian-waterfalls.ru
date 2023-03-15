"""waterfalls URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import mainapp.views as mainapp
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainapp.main),
    path('texts/', mainapp.texts, name='texts'),
    path('text/<int:id>/', mainapp.text, name='text'),
    path('waterfalls/regs/srt/<str:id_district>', mainapp.srt, name='srt'),
    path('waterfalls/search/regs', mainapp.search_regions, name='search_regions'),
    path('waterfalls/search/<str:reg>/', mainapp.search, name='search'),
    path('waterfalls/regs/', mainapp.regions, name='regions'),
    path('waterfalls/<int:id>/info/', mainapp.info_waterfall, name='info_waterfall'),
    path('district/<int:id>/info/', mainapp.info_district, name='info_district'),
    path('waterfall_administrative_district/<int:id>/info/',
         mainapp.info_administrative_district, name='info_administrative_district'),
    path('waterfalls/<str:name>/district/<str:id_district>/type/<str:id_type>/sorted/<str:srt_id>/',
         mainapp.sorted, name='sorted'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)