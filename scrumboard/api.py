from rest_framework.generics import ListAPIView

from .models import List, Card

from .serializers import ListSerializer, CardSerializer

class ListAPI(ListAPIView):
    queryset = List.objects.all()
    serializer_class = ListSerializer

class CardAPI(ListAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer