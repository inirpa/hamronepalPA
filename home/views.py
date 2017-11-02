from django.shortcuts import render
from django.views import generic
from django.views.generic import View
from django.http import HttpResponse

from . models import BlogOption, Memo

# Create your views here.

class HomeView(generic.ListView):
	template_name = 'home/index.html'
	context_object_name = 'blog_options'
	queryset = BlogOption.objects.all()

	# def get_queryset(self):
	# 	return BlogOption.objects.all()

	def get_context_data(self, **kwargs):
		context = super(HomeView,self).get_context_data(**kwargs)
		context['blog'] = BlogOption.objects.all()
		context['memos'] = Memo.objects.order_by('-id')[:1]
		return context