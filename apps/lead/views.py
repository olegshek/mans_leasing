from rest_framework import viewsets

from apps.core.parsers import MultipartFormEncodeParser
from apps.lead.models import Lead
from apps.lead.serialzers import LeadSerializer


class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
