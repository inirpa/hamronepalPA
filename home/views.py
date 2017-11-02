from django.shortcuts import render
from django.views import generic
from django.views.generic import View
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from . models import BlogOption, Memo

# Create your views here.

class HomeView(generic.ListView):
	template_name = 'home/index.html'
	context_object_name = 'memos'
	queryset = Memo.objects.all().order_by('-id')
	paginate_by = 1

	# def get_queryset(self):
	# 	return BlogOption.objects.all()

	def get_context_data(self, **kwargs):
		context = super(HomeView,self).get_context_data(**kwargs)
		context['blog_options'] = BlogOption.objects.all()
		# context['memos'] = Memo.objects.order_by('-id')[:1]

		# context['memos'] = Memo.objects.all()
		# paginator = Paginator(context['memos'],1)
		# page = request.GET.get('page')

		# memos = paginator.page(page)
		return context