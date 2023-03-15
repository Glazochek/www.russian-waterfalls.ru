# -*- coding: UTF-8 -*-
import os
from pathlib import Path
from django.shortcuts import render
from mainapp.models import Waterfall, Waterfall_District, Administrative_District, Text
from urllib.parse import unquote

fl = str(os.getcwd()).replace('\\', '/') + '/static/waterfalls/'
tx = str(os.getcwd()).replace('\\', '/') + '/static/texts/'


def main(request):

    waterfall = []
    wf = list(Waterfall.objects.all().order_by('id'))
    files = [str(img.name) for img in Path(fl).glob('*.jpg')]
    blocks = []

    for f in list(Waterfall.objects.all())[:10]:
        for ff in files:
            if str(f.id) in ff:
                blocks.append(f)

    for f in list(set(blocks)):
        img = [i for i in files if str(f.id) in i][0]
        waterfall.append([img, f.name, f.place])

    context = {
        'title': 'главная',
        'cord': Waterfall.objects.all().order_by('cordinats').exclude(cordinats="-").exclude(cordinats=''),
        'texts_slide': list(set(blocks)),
        'texts_info': reversed(wf),
        'sgf': 'q',
        'txt': Text.objects.all()[:3],
        'wtrf': Waterfall_District.objects.all(),
        'wt_slider': waterfall,
       }
    return render(request, 'mainapp/index.html', context)


def sorted(request, name="all", id_district='all', id_type='all', srt_id='0'):

    srt_id = list(set(srt_id.split('&')))

    sorted_list = []
    type_dict = {}
    distric_dict = {}

    slwt = list(set([i[list(i)[0]] for i in Waterfall.objects.values('type')]))
    slwd = list(Waterfall_District.objects.all())
    wf = Waterfall.objects.all()

    for i in range(len(slwt)):
        type_dict[i] = slwt[i]

    for i in slwd:
        distric_dict[i.id] = i.District_name

    if name != 'all':
        wf = wf.filter(name__contains=f'{unquote(name)}')

    if id_district != 'all':
        wf = wf.filter(District_id=int(id_district))

    if id_type != 'all':
        wf = wf.filter(type=type_dict[int(id_type)])

    context = {
        'title': 'список водопадов',
        'wf': list(wf),
        'name': name,
        'district': 'Россия' if id_district == 'all' else distric_dict[int(id_district)],
        'district_id': id_district,
        'btns': [
            {'text': 'по высоте', 'urls': 1},
            {'text': 'по ширине', 'urls': 2},
            # {'text': 'по названию', 'urls': 3},
            # {'text': 'по месту', 'urls': 4},
            {'text': 'по выосте над у. м.', 'urls': 5},
            {'text': 'по площади водосбора', 'urls': 6},
            {'text': 'по площади зеркала', 'urls': 7},
            {'text': 'по тратам енергии', 'urls': 8},
            {'text': 'по расходу воды', 'urls': 9},
        ],
        'btns_disrict': [{'text': distric_dict[i], 'urls': i} for i in distric_dict.keys()],
    }

    sort_dict = {
        1: '-height',
        2: '-weight',
        3: '-name',
        4: '-place',
        5: '-Altitude_above_sea_level',
        6: '-S_catchment',
        7: '-S_mirror',
        8: '-Energy_joules',
        9: '-water_consumption',
    }

    if min(map(int, srt_id)) == 0 or max(map(int, srt_id)) == 13:
        context['sl'] = list(wf)
    else:
        sort = [sort_dict[int(s)] for s in srt_id]
        context['sl'] = list(wf.order_by(*sort))

    return render(request, 'mainapp/waterfalls.html', context)


def srt(request, id_district='all'):
    type_dict = {}
    slwt = list(set([i[list(i)[0]] for i in Waterfall.objects.values('type')]))
    for i in range(len(slwt)):
        type_dict[i] = slwt[i]
    cntx = {'id_district': id_district,
            'reg_text': Waterfall_District.objects.get(id=id_district) if id_district != 'all' else None,
            'btns_type': [{'text': type_dict[i], 'urls': i} for i in type_dict.keys()],
            }
    return render(request, 'mainapp/sorted.html', cntx)


def regions(request):
    distric_dict = {}
    slwd = list(Waterfall_District.objects.all())
    for i in slwd:
        if i.District_name != '-':
            distric_dict[i.id] = i.District_name
    cntx = {'reg': [{'text': distric_dict[i], 'urls': i} for i in distric_dict.keys()]}
    return render(request, 'mainapp/regions.html', cntx)


def search_regions(request):
    distric_dict = {}
    slwd = list(Waterfall_District.objects.all())
    for i in slwd:
        if i.District_name != '-':
            distric_dict[i.id] = i.District_name
    cntx = {'reg': [{'text': distric_dict[i], 'urls': i} for i in distric_dict.keys()]}
    return render(request, 'mainapp/search_reg.html', cntx)


def search(request, reg):
    cntx = {'reg': reg,
            'reg_text': Waterfall_District.objects.get(id=reg) if reg != 'all' else None}
    return render(request, 'mainapp/search.html', cntx)


def info_waterfall(request, id=None):
    waterfall = Waterfall.objects.get(id=id)
    d_id = waterfall.District_id
    ad_id = waterfall.Administrative_District_id

    files = [str(img.name) for img in Path(fl).glob('*.jpg')]

    img = []

    for f in files:
        if str(id)+' ' in f:
            img.append('waterfalls/' + f)

    context = {
        'title': 'подробная информация',
        'waterfall': waterfall,
        'waterfall_district': Waterfall_District.objects.get(id=d_id),
        # 'waterfall_administrative_district': Administrative_District.objects.get(id=ad_id),
        'img': img
        }

    return render(request, 'mainapp/waterfall_info.html', context)


def info_district(request, id=None):

    waterfall_district = Waterfall_District.objects.get(id=id)
    waterfalls = Waterfall.objects.filter(District_id=id)

    context = {
        'title': 'подробная информация',
        'waterfall_district': waterfall_district,
        'waterfalls': waterfalls,
        }
    return render(request, 'mainapp/waterfall_district.html', context)


def info_administrative_district(request, id=None):

    waterfall_administrative_district = Administrative_District.objects.get(id=id)

    context = {
        'title': 'подробная информация',
        'waterfall_administrative_district': waterfall_administrative_district,
        }

    return render(request, 'mainapp/waterfall_administrative_district.html', context)


def texts(request):
    text = Text.objects.all()
    context = {"text": text, 'res':1}
    return render(request, 'mainapp/texts.html', context)


def text(request, id):
    text = Text.objects.all().get(id=id)
    mx_len = len(Text.objects.all())
    img = ['/static/texts/'+str(img.name) for img in Path(tx).glob('*.j*') if f'{id}' == str(img.name).split('.')[0]]
    imgs = [[i+1, img[i]] for i in range(len(img))]
    context = {"text": [text], 'res': 0, 'img': imgs,
               'next':id+1 if id != mx_len else 1,
               'bfr':id-1 if id != 1 else mx_len}
    return render(request, 'mainapp/texts.html', context)
