from django.shortcuts import render
from django.views import generic
from django.views.generic import View
from django.http import HttpResponse


# Create your views here.

class HomeView(generic.ListView):
	template_name = 'home/index.html'

	def get_queryset(self):
		return HttpResponse("this")