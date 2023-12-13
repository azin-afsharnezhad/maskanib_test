from django.urls import path, include
from rest_framework.routers import SimpleRouter, DefaultRouter
from . import views


app_name = 'history'


router = DefaultRouter()
router.register(r'histories', views.HistoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
