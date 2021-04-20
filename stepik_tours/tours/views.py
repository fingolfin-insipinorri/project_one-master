from django.shortcuts import render
from django.views import View
from stepik_tours.data import tours
from stepik_tours.data import departures


class MainView(View):
    def get(self, request):
        return render(request, 'main.html')


class DepartureView(View):
    def get(self, request, departure,):
        return render(request, 'departure.html', context={"departures": departures[departure], "tours": tours})


class TourView(View):
    def get(self, request, id_tour):
        return render(request, 'tour.html', context={"tour": tours[id_tour], "departure": departures[tours[id_tour]["departure"]]})

