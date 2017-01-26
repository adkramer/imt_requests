# -*- coding: utf-8 -*-
#from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.RequestList.as_view(), name='requests'),
    url(r'^(?P<pk>\d+)$', views.RequestDetail.as_view(), name='request-detail'),
    url(r'^new_request$', views.RequestFormView.as_view(), name='request-new'),
    url(r'^update/(?P<pk>\d+)$', views.RequestUpdateView.as_view(), name='request-update'),
    url(r'^delete/(?P<pk>\d+)$', views.RequestDeleteView.as_view(), name='request-delete'),
]