import time

import requests
from django.conf import settings

from apps.core.utils.exceptions import MansCRMError


def send_request_to_mans_crm(data):
    for i in range(5):
        try:
            response = requests.post(settings.MANS_CRM_URL, data=data)
        except IOError:
            raise MansCRMError('No connection')

        if response.status_code == 400:
            raise MansCRMError(response.content)
        elif response.status_code == 403:
            raise MansCRMError('Permission denied')
        else:
            time.sleep(1.5)

    raise MansCRMError('No response')