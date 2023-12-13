from django_filters.rest_framework import FilterSet
from . models import History


class HistoryFilter(FilterSet):
    class Meta:
        model = History
        fields = {
            'date':['lt','gt',],
        }