from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
	# Author.objects.order_by('-score')
	headers=Header.objects.all()
	sliders=Slider.objects.all()
	ourWorks=OurWork.objects.all()
	workItems=WorkItem.objects.all()
	clientCompanies=ClientCompany.objects.all()
	ourServices=OurService.objects.all()

	return render(request,'home.html',{'headers':headers,'sliders':sliders,
		'ourWorks':ourWorks,'workItems':workItems,'clientCompanies':clientCompanies,
		'ourServices':ourServices})

def single_work(request,workId):
	workItem=WorkItem.objects.get(id=workId)
	context={'workItem':workItem}

	return render(request,'single-work.html',context)