from django.conf.urls import url
from django.views.generic import ListView
from .views import index, ArtikelListView
from .models import Artikel


urlpatterns = [
	url(r'^(?P<penulis>\w+)/(?P<page>\d+)$', ArtikelListView.as_view(), name='list'),
	# url(r'^$', ListView.as_view(model=Artikel), name = 'list'),
]