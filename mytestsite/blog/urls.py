from django.urls import path
from . import views

from django.conf.urls import url,include

from .views import *

urlpatterns = [
	path('',views.index,name='index'),
	# url(r'^(?P<id>[0-9]+)/detail/$',views.detail,name="detail"),
	path('<int:id>/detail/',views.detail,name="detail"),
	url('hello', HelloView.as_view()),

	# url(r'^test/$',views.GetMessageView.as_view()),
	path('test/',views.GetMessageView.as_view()),
]