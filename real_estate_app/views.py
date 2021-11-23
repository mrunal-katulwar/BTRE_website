from django.shortcuts import render
from django.http import HttpResponse
from listings.choices import price_choices, bedroom_choices, state_choices

from listings.models import Listing
from realtors.models import Realtor

# Create your views here.
def index(requests):
	listings = Listing.objects.order_by('-list_date').filter(is_publisted=True)[:3]
	context = {
		'listings': listings,
		'state_choices': state_choices,
		'bedroom_choices': bedroom_choices,
		'price_choices': price_choices
	}
	return render(requests,'real_estate_app/index.html', context)

def about(requests):
	# get all realtors
	realtors = Realtor.objects.order_by('-hire_date')
	# get mvp
	mvp_realtors = Realtor.objects.all().filter(is_mvp = True )
	context = {
		'realtors': realtors,
		'mvp_realtors': mvp_realtors
	}
	return render(requests,'real_estate_app/about.html', context)
