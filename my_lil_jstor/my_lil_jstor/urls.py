"""my_lil_jstor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^coloringbook/(?P<book_id>[0-9]+)', views.coloring_books, name='coloring_books'),
    url(r'^purchase/(?P<book_id>[0-9]+)', views.purchase, name='purchase'),
    url(r'^browse', views.browse, name='browse'),
    url(r'^coloringbook/like', views.like, name="like"),
    url(r'^coloringbook/comment', views.comment, name="comment"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', views.home, name='home'),
]
