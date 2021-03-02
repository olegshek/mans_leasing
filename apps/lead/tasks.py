import logging
import sys

from apps.core.utils.exceptions import MansCRMError
from apps.lead.models import Lead
from apps.lead.services.mans_crm import send_request_to_mans_crm
from config.celery import app


@app.task
def send_lead_to_crm(lead_id):
    lead = Lead.objects.get(id=lead_id)

    data = {
        'clientAddress': lead.address,
        'education': lead.education,
        'email': lead.email,
        'familyType': lead.familyType,
        'income': float(lead.income),
        'incomeType': lead.incomeType,
        'kidsNum': int(lead.dependents),
        'livingPlaceType': lead.accommodation_type,
        'lvCitizen': True if lead.citizenship == 'on' else False,
        'name': lead.fio,
        'origin': 'TEST',
        'personalCode': lead.personalCode,
        'phone': lead.phone,
        'sex': lead.sex,
        'workType': lead.workType
    }

    try:
        send_request_to_mans_crm(data)
    except MansCRMError:
        logger = logging.getLogger('django')
        logger.error(
            'Mans CRM Error',
            exc_info=sys.exc_info(),
            extra={'status_code': 500, 'request': None},
        )
