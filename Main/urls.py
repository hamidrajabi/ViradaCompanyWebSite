#HI THERe
from django.contrib import admin
from django.urls import path,include

from django.conf.urls.static import static
from django.conf import settings 
from . import views

urlpatterns=[
	#base url
	path('',views.home,name="Home"),
	path('single-work/<int:workId>/',views.single_work,name='single-work')
	# path('order/',views.orderPage,name="Order"),
	]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)