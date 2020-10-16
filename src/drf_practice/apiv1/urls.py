from django.urls import path, include
from rest_framework import routers

from . import views

# DefaultRouterを使いModelViewSetのURLをまとめて登録する
router = routers.DefaultRouter()
router.register('books', views.BookViewSet)

app_name = 'apiv1'
urlpatterns = [
    path('', include(router.urls))
]
