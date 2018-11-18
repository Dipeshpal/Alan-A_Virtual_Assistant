from django.conf.urls import url
from search.views import HomeView

urlpatterns = [
	url(r'^$', HomeView.as_view(), name='search'),
]
