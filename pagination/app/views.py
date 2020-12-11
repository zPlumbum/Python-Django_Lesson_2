import csv
import urllib
from urllib import parse

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from app.settings import BUS_STATION_CSV, ITEMS_PER_PAGE


with open(BUS_STATION_CSV, 'r', encoding='cp1251') as csvfile:
    reader = csv.DictReader(csvfile)
    content = []
    for row in reader:
        content.append({'Name': row['Name'], 'Street': row['Street'], 'District': row['District']})


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    current_page = int(request.GET.get('page', 1))
    paginator = Paginator(content, ITEMS_PER_PAGE)

    page_object = paginator.get_page(current_page)
    base_url = reverse('bus_stations')

    next_page_url = None
    prev_page_url = None

    if page_object.has_next():
        params = urllib.parse.urlencode({'page': page_object.next_page_number()})
        next_page_url = f'{base_url}?{params}'

    if page_object.has_previous():
        params = urllib.parse.urlencode({'page': page_object.previous_page_number()})
        prev_page_url = f'{base_url}?{params}'

    return render(request, 'index.html', context={
        'bus_stations': page_object,
        'current_page': current_page,
        'prev_page_url': prev_page_url,
        'next_page_url': next_page_url,
    })
