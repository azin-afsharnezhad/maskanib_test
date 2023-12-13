from django.test import TestCase
from .models import History
from django.urls import reverse


class HistoryTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.row = History.objects.create(
            date='20231112',
            count='1390',
            volume='1390',
            value='120146408570',
            yesterday_price='12520',
            first_price='12250',
            last_trade='12540',
            close='12440',
            low='12250',
            high='12600',
        )

    def test_history_list_url(self):
        response = self.client.get(reverse('history:history-list'))
        self.assertEqual(response.status_code, 200)

    def test_history_detail_url(self):
        response = self.client.get(
            reverse('history:history-detail', kwargs={'date': self.row.date}))
        self.assertEqual(response.status_code, 200)
