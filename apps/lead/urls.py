from django.urls import path

from apps.lead.views import LeadViewSet

urlpatterns = [
    path('leads/', LeadViewSet.as_view({'post': 'create'}), name='leads')
]
