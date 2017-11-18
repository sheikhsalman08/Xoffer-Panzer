from rest_framework import mixins
from .serializers import OfferSerializer,OfferSerializer2
from .models import Offers
from offer.models import Offer
from rest_framework_mongoengine.viewsets import ModelViewSet as MongoModelViewSet
from rest_framework.response import Response

class OffersViewSet2(MongoModelViewSet):
	lookup_field = 'brand_name'
	serializer_class = OfferSerializer2

	# def __init__(self,*args,**kwargs):
	# if request.method == 'GET' and 'item' in request.GET:
	# 	print('item')
	# else:
	# 	print('nai')

	def get_queryset(self):
		# if self.request.method == 'GET':
		# 	if 'brand_name' in self.request.GET:
		# 			filt = self.request.GET['brand_name']
		# 			return Offer.objects.filter(brand_name__iexact=filt)
		# 	else:
		# 		return Offer.objects.all()

		# 	if 'shopping_mall' in self.request.GET:
		# 			filt = self.request.GET['shopping_mall']
		# 			return Offer.objects.filter(shopping_mall__iexact=filt)
		# 			print(filt)
		# 	else:
		# 		return Offer.objects.all()
				

		# 	if 'created_date' in self.request.GET:
		# 			filt = self.request.GET['created_date']
		# 			return Offer.objects.filter(created_date__iexact=filt)
		# 	else:
		# 		return Offer.objects.all()
			
		# 	if 'category' in self.request.GET:
		# 			filt = self.request.GET['category']
		# 			return Offer.objects.filter(category__iexact=filt)
		# 	else:
		# 		return Offer.objects.all()
			
		# else:
		# 	return Offer.objects.all()

		if 'brand_name' in self.request.GET:
				filt = self.request.GET['brand_name']
				return Offer.objects.filter(brand_name__iexact=filt)
		elif 'shopping_mall' in self.request.GET:
				filt = self.request.GET['shopping_mall']
				return Offer.objects.filter(shopping_mall__iexact=filt)
				print(filt)
		elif 'created_date' in self.request.GET:
				filt = self.request.GET['created_date']
				return Offer.objects.filter(created_date__iexact=filt)
		elif 'category' in self.request.GET:
				filt = self.request.GET['category']
				return Offer.objects.filter(category__iexact=filt)
		else:
			return Offer.objects.all()
			

