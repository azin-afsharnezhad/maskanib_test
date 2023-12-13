
from rest_framework import status
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from .models import History
from .serializers import HistorySerializer
from . filters import HistoryFilter
from . paginations import DefaultPagination


class HistoryViewSet(ReadOnlyModelViewSet):
    serializer_class = HistorySerializer
    queryset = History.objects.all()
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['value', 'volume', 'last_trade', 'date', ]
    search_fields = ['date', ]
    pagination_class = DefaultPagination
    filterset_class = HistoryFilter
    lookup_field = 'date'

    def get_serializer_context(self):
        return {'request': self.request}
