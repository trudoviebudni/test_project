#from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.views.generic import TemplateView

"""
представления через функции
def mainView(request):
    return render(request, 'index.html')


def departureView(request, departure='novosib'):
    return render(request, 'departure.html')


def tourView(request, id=0):
    return render(request, 'tour.html')
"""


def custom_handler404(request, exception):
    return HttpResponseNotFound('Ой, что то сломалось... Простите извините!')


class MainView(TemplateView):
    template_name = 'index.html'


class DepartureView(TemplateView):
    template_name = 'tours/departure.html'


class TourView(TemplateView):
    template_name = 'tours/tour.html'

