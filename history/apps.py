import os
from django.apps import AppConfig
from django.db import IntegrityError
from django.db.utils import OperationalError
from distutils.util import strtobool


class HistoryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'history'

    def ready(self):
        if strtobool(os.environ.get('HISTORY_APP_READY_TO_CRAWL')):
            from .serializers import HistorySerializer
            from .crawler import TSETMCCrawler
            crawler = TSETMCCrawler()
            for data in crawler.crawl():
                try:
                    serializer = HistorySerializer(data=data)
                    if serializer.is_valid():
                        serializer.save()
                except IntegrityError:
                    continue
                except OperationalError as e:
                    raise Exception(
                        "\nIf you didn't run python manage.py makemigrations or migrate before runserver \n"
                        "Please first set HISTORY_APP_READY_TO_CRAWL=False then run again your command !!! "
                    ) from e
            with open('.env', 'w') as env_file:
                env_file.write('HISTORY_APP_READY_TO_CRAWL=False')
