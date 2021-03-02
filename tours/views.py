from django.http import HttpResponseNotFound
from tours.data import *
from django.views import View
from django.shortcuts import render




def custom_handler404(request, exception):
    return HttpResponseNotFound('Ой, что то сломалось... Простите извините!')


class MainView(View):

    def get(self, request, *args, **kwargs):
        context = {}
        context['tours_list'] = tours_list
        context['title'] = title
        context['subtitle'] = subtitle
        context['description'] = description
        context['departures'] = departures
        return render(request, 'index.html', context=context)


class TourView(View):

    def get(self, request, *args, **kwargs):
        x = kwargs['id']
        context = {}
        context['tour'] = tours[x]
        context['departure'] = departures[tours[x]['departure']]
        context['tours_list'] = tours_list
        context['title'] = title
        context['subtitle'] = subtitle
        context['description'] = description
        context['departures'] = departures
        return render(request, 'tour.html', context=context)


class DepartureView(View):

    def get(self, request, *args, **kwargs):
        context = {}
        context['departure'] = departures[kwargs['departure']]
        context['tours_list'] = tours_list
        context['title'] = title
        context['subtitle'] = subtitle
        context['description'] = description
        context['departures'] = departures
        context['tours'] = [tours[key] for key in tours if tours[key]['departure'] == kwargs['departure']]
        context['size'] = len(context['tours'])
        context['price_min'] = min(elem['price'] for elem in context['tours'])
        context['price_max'] = max(elem['price'] for elem in context['tours'])
        context['nights_min'] = min(elem['nights'] for elem in context['tours'])
        context['nights_max'] = max(elem['nights'] for elem in context['tours'])
        return render(request, 'departure.html', context=context)


