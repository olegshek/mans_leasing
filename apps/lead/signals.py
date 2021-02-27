from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.lead.models import Lead
from apps.lead.tasks import send_lead_to_crm


@receiver(post_save, sender=Lead)
def lead_created(sender, instance, *args, **kwargs):
    if kwargs['created']:
        send_lead_to_crm.delay(instance.id)
