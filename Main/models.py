from django.db import models
from taggit.managers import TaggableManager
from django_jalali.db import models as jmodels

# Create your models here.

class Header(models.Model):
	name=models.CharField(max_length=200)

	def __str__(self):
		return str(self.name)



class Slider(models.Model):
	title=models.CharField(max_length=200)
	image=models.ImageField()
	subtitle=models.CharField(max_length=200)
	buttonName=models.CharField(max_length=200)
	buttonLink=models.URLField(max_length=200)
	
	def imageURL(self):
		try:
			url=self.image.url
		except:
			url=''
		return url

	def __str__(self):
		return str(self.title)



class OurWork(models.Model):
	title=models.CharField(max_length=200)
	headerImage=models.ImageField(null=True,blank=True)

	def headerImageURL(self):
		try:
			url=self.headerImage.url
		except:
			url=''
		return url

	def __str__(self):
		return str(self.title)



class Tag(models.Model):
	word=models.CharField(max_length=200)

	def __str__(self):
		return str(self.word)



class WorkItem(models.Model):
	ourWork=models.ForeignKey(OurWork,on_delete=models.CASCADE)
	title=models.CharField(max_length=200)
	headerImage=models.ImageField()
	sliderImage1=models.ImageField()
	sliderImage2=models.ImageField(blank=True,null=True)
	sliderImage3=models.ImageField(blank=True,null=True)
	sliderImage4=models.ImageField(blank=True,null=True)
	videoURL=models.URLField(max_length=1000,blank=True,null=True)
	youTubeLink=models.URLField(max_length=1000,blank=True,null=True)
	workDescription=models.TextField(max_length=2000)
	tags = models.ManyToManyField(Tag,related_name='tags')
	created_at=jmodels.jDateTimeField(auto_now_add=True)
	subtitle=models.CharField(max_length=200)

	def imageURL(self):
		try:
			url=self.headerImage.url
		except:
			url=''
		return url

	def slider1URL(self):
		try:
			url=self.sliderImage1.url
		except:
			url=''
		return url

	def slider2URL(self):
		try:
			url=self.sliderImage1.url
		except:
			url=''
		return url

	def slider3URL(self):
		try:
			url=self.sliderImage1.url
		except:
			url=''
		return url

	def slider4URL(self):
		try:
			url=self.sliderImage1.url
		except:
			url=''
		return url


	def __str__(self):
		return str(self.title)


class ClientCompany(models.Model):
	name=models.CharField(max_length=200)
	logo=models.ImageField()
	url=models.URLField(null=True,blank=True)

	def imageURL(self):
		try:
			url=self.logo.url
		except:
			url=''
		return url

	def __str__(self):
		return str(self.name)


class OurService(models.Model):
	title=models.CharField(max_length=200)
	image=models.ImageField()
	text=models.CharField(max_length=2000)

	def imageURL(self):
		try:
			url=self.image.url
		except:
			url=''
		return url

	def __str__(self):
		return str(self.title)		










