from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator 
from .choices import price_choices, bedroom_choices, state_choices

from .models import Listing


def index(requests):
	listings = Listing.objects.order_by('-list_date').filter(is_publisted=True)
	paginator = Paginator(listings, 6)
	page = requests.GET.get('page')
	paged_listings = paginator.get_page('page')


	context = {
		'listings':paged_listings
	}
	return render (requests, 'listings/listings.html', context)

def listing(requests, listing_id):
	
	listing = get_object_or_404(Listing, pk=listing_id)

	context = {
		'listing': listing
	}
	return render (requests, 'listings/listing.html', context)
def search(requests):
	queryset_list = Listing.objects.order_by('-list_date')
	#keywords
	if 'keywords' in requests.GET:
		keywords = requests.GET['keywords']
		if keywords:
			queryset_list = queryset_list.filter(description__icontains = keywords)

	#city
	if 'city' in requests.GET:
		city = requests.GET['city']
		if city:
			queryset_list = queryset_list.filter(city__iexact = city) # we want exatct city 

	#state
	if 'state' in requests.GET:
		state = requests.GET['state']
		if state:
			queryset_list = queryset_list.filter(state__iexact = state)

	#bedroom
	if 'bedrooms' in requests.GET:
		bedrooms = requests.GET['bedrooms']
		if bedrooms:
			queryset_list = queryset_list.filter(bedrooms__lte = bedrooms) # can do exact or upto that number less than or ewual to 

	#price
	if 'price' in requests.GET:
		price = requests.GET['price']
		if price:
			queryset_list = queryset_list.filter(price__lte = price) 
	
	context={
		'state_choices': state_choices,
		'bedroom_choices': bedroom_choices,
		'price_choices': price_choices,
		'listings' : queryset_list,
		'values' : requests.GET 
	}
	return render (requests, 'listings/search.html', context)