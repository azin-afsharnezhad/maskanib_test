from rest_framework import serializers
from .models import History


class HistorySerializer(serializers.ModelSerializer):

    class Meta:
        model = History
        fields = ['date', 'count', 'volume', 'value', 'yesterday_price',
                  'first_price', 'last_trade', 'close', 'low', 'high']
