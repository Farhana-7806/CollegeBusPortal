import json
from channels.generic.websocket import AsyncWebsocketConsumer

class BusLocationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.bus_id = self.scope['url_route']['kwargs']['bus_id']
        self.group_name = f'bus_{self.bus_id}'
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'send_location',
                'latitude': data['lat'],
                'longitude': data['lng'],
                'speed': data['speed']
            }
        )

    async def send_location(self, event):
        await self.send(text_data=json.dumps({
            'lat': event['latitude'],
            'lng': event['longitude'],
            'speed': event['speed']
        }))
