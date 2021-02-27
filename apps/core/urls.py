from django.urls import path

from apps.core.views import homepage

urlpatterns = [
    path('', homepage, name='homepage')
]