from rest_framework import serializers
from rest_framework_mongoengine.serializers import DocumentSerializer
from .models import Offers
from offer.models import Offer

class OfferSerializer(DocumentSerializer):
	class Meta:
		model = Offers
		fields = '__all__'

class OfferSerializer2(DocumentSerializer):
    class Meta:
        model = Offer
        fields = '__all__'
