from django.conf.urls import url
from reminder.views import HomeView

urlpatterns = [
	url(r'^$', HomeView.as_view(), name='reminder'),
]
