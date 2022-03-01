#HI THERe
from django.contrib import admin
from django.urls import path,include

from django.conf.urls.static import static
from django.conf import settings 
from . import views

urlpatterns=[
	#base url
    re_path(r'^images/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),

	path('',views.home,name="Home"),
	path('single-work/<str:workTitle>/',views.single_work,name='single-work')
	# path('order/',views.orderPage,name="Order"),
	]


urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)