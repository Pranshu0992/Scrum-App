from rest_framework.generics import ListAPIView

from .serializers import ListSerializers, CardSerializers
from .models import List, Card


class ListAPI(ListAPIView):
    queryset = List.objects.all()
    serializer_class = ListSerializers

class CardAPI(ListAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializers