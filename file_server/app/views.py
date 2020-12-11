import datetime
import os
from django.shortcuts import render
from django.conf import settings


def file_list(request, date=None):
    template_name = 'index.html'

    context = {
        'files': []
    }

    files = os.listdir(settings.FILES_PATH)

    for file in files:
        ctime = datetime.datetime.fromtimestamp(os.path.getctime(f'{settings.FILES_PATH}/{file}'))
        mtime = datetime.datetime.fromtimestamp(os.path.getmtime(f'{settings.FILES_PATH}/{file}'))
        print(ctime, mtime)

        file_info = {
            'name': file,
            'ctime': ctime,
            'mtime': mtime
        }
        context['files'].append(file_info)

    if date:
        context.setdefault('date', date.date())

    return render(request, template_name, context)


def file_content(request, name):
    files = os.listdir(settings.FILES_PATH)
    if name in files:
        with open(f'{settings.FILES_PATH}/{name}', 'r', encoding='utf-8') as file:
            file_content = ''.join(file.readlines())

    return render(
        request,
        'file_content.html',
        context={
            'file_name': name,
            'file_content': file_content
        }
    )
