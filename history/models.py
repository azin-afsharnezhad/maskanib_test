from django.db import models


class History(models.Model):
    date = models.CharField(max_length=8)
    count = models.CharField(max_length=20)
    volume = models.CharField(max_length=30)
    value = models.CharField(max_length=30)
    yesterday_price = models.CharField(max_length=30)
    first_price = models.CharField(max_length=30)
    last_trade = models.CharField(max_length=30)
    close = models.CharField(max_length=30)
    low = models.CharField(max_length=30)
    high = models.CharField(max_length=30)

    class Meta:
        unique_together = ['date', 'close']
