# your_app_name/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import SchedaLavorazione
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

@receiver(post_save, sender=SchedaLavorazione)
def notify_schede_update(sender, instance, **kwargs):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        'schede_group',  # Nome del gruppo a cui inviare il messaggio
        {
            'type': 'send_schede',
        }
    )
