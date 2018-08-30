from rest_framework import serializers

from .models import List, Card


class ListSerializers(serializers.ModelSerializer):
    class Meta:
        model = List 



class CardSerializers(serializers.ModelSerializer):
    class Meta:
        model = Card


