from django.conf.urls import url
from . import views

urlpatterns = [
	url('^$',views.MemoView.as_view(),name = 'memo'),
]