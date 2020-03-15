from django.urls import path, include
from rest_framework import routers


router = routers.DefaultRouter()
# router.register('books', views.BookViewSet)

app_name = 'apiv1'
urlpatterns = [
    path('', include(router.urls)),
]
