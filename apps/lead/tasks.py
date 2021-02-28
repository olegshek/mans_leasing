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
        'driverAddress': lead.driverAddress,
        'driverEmail': lead.driverEmail,
        'driverFullName': lead.driverFullName,
        'driverPersonalCode': lead.driverPersonalCode,
        'driverPhone': lead.driverPhone,
        'driverRelation': lead.driverRelation,
        'driversLicence': lead.driverLicense if lead.driverLicense else False,
        'education': 'HIGHEST',
        'email': lead.email,
        'familyType': 'NON_MARRIED',
        'income': int(lead.income),
        'incomeFamily': 1000000,
        'incomeType': lead.incomeType,
        'kidsNum': int(lead.kidsNum),
        'ktpFirstName': lead.ktpFirstName,
        'ktpPhone': lead.ktpPhone,
        'ktpRelation': lead.ktpRelation,
        'livingPlaceType': 'OWN_PROPERTY',
        'lvCitizen': True if lead.lvCitizen == 'on' else False,
        'name': lead.fio,
        'origin': 'TEST',
        'otherLeasingPayments': int(lead.otherLeasingPayments),
        'personalCode': lead.personalCode,
        'phone': lead.phone,
        'politicalPerson': True if lead.politicalPerson == 'on' else False,
        'sex': 'MALE',
        'workMonths': int(lead.workMonths),
        'workplace': lead.workplace,
        'workType': lead.workType
    }

    try:
        send_request_to_mans_crm(data)
    except MansCRMError:
        logger = logging.getLogger('django')
        logger.error(
            'Internal Server Error: PCMiler Route State Report Service Error',
            exc_info=sys.exc_info(),
            extra={'status_code': 500, 'request': None},
        )
