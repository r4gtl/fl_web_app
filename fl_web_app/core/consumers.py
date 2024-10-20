# your_app_name/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import SchedaLavorazione
from django.core.serializers import serialize
import logging

logger = logging.getLogger(__name__)

class SchedeConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        logger.info("Connecting to WebSocket...")
        await self.channel_layer.group_add("schede", self.channel_name)
        await self.accept()
        logger.info("WebSocket connected.")

    async def disconnect(self, close_code):
        logger.info(f"Disconnecting WebSocket: {close_code}")
        await self.channel_layer.group_discard("schede", self.channel_name)

    async def receive(self, text_data):
        logger.info("Receiving update to WebSocket...")
        data = json.loads(text_data)
        # Puoi gestire i messaggi in arrivo qui se necessario
        # Invia un messaggio di esempio al client
        await self.send(text_data=json.dumps({
            'message': 'Hello from WebSocket!',
        }))

    async def send_update(self, event):
        logger.info("Receiving update to WebSocket...")
        # Invia un aggiornamento ai client connessi
        await self.send(text_data=json.dumps(event))
