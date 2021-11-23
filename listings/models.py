from django.db import models
from datetime import datetime # for getting current date in listing_date
from realtors.models import Realtor # to get realtor id from realtor model

class Listing(models.Model):
	# creating fields required for listing
	realtor = models.ForeignKey(Realtor, on_delete = models.DO_NOTHING) #deciding what to do with the listing is if realtor is deleted
	title = models.CharField(max_length=200)
	address = models.CharField(max_length=200)
	city = models.CharField(max_length=100)
	state = models.CharField(max_length=100)
	zipcode = models.CharField(max_length=20)
	description = models.TextField(blank=True)
	price = models.IntegerField()
	bedrooms = models.IntegerField()
	# bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
	garage = models.IntegerField(default=0)
	sqft = models.IntegerField()
	lot_size = models.DecimalField(max_digits=5, decimal_places=1)
	# photos, in db it will be stored in string format as in location of the photo, in django we have different field for images
	photo_main = models.ImageField(upload_to='photos/%d/%m/%Y/') # for every photo to go into folder structure of date
	#there's going to be media folder in django and anything we upload through admin area like photos or documents will be stored there
	#here we will be defining a folder we want inside of that media folder .
	photo_1=models.ImageField(upload_to='photos/%d/%m/%Y/', blank=True)
	photo_2=models.ImageField(upload_to='photos/%d/%m/%Y/', blank=True)
	photo_3=models.ImageField(upload_to='photos/%d/%m/%Y/', blank=True)
	photo_4=models.ImageField(upload_to='photos/%d/%m/%Y/', blank=True)
	photo_5=models.ImageField(upload_to='photos/%d/%m/%Y/', blank=True)
	photo_6=models.ImageField(upload_to='photos/%d/%m/%Y/', blank=True)
	is_publisted = models.BooleanField(default=True)
	list_date = models.DateTimeField(default=datetime.now, blank=True)

	#there's going to be a table that will display each listing, we need to pick a  main field to be displayed 
	# we are going to choose it to be 'title' 
	def __str__(self):
		return self.title 
