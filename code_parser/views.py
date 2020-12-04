from rest_framework import viewsets
from django_filters import rest_framework as filters

from .models import LocodeCode
from .serializers import LocodeSerializer
from .filters import LocodeFilter


class LocodeViewSet(viewsets.ModelViewSet):
    serializer_class = LocodeSerializer
    queryset = LocodeCode.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = LocodeFilter
