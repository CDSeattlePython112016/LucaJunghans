from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^$', views.books, name = "home"),
	url(r'^new_book/$', views.new_book, name="new_book"),
	url(r'^display/$', views.display, name="display"),
	url(r'^abook/(?P<book_id>\d+)', views.abook, name="abook"),

]