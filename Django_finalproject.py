from channels.generic.websocket import AsyncWebsocketConsumer
import json

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        await self.send(text_data=json.dumps({
            'message': message
        }))
<script>
    const chatSocket = new WebSocket(
        'ws://' + window.location.host + '/ws/notifications/'
    );

    chatSocket.onmessage = function(e) {
        const data = JSON.parse(e.data);
        document.querySelector('#notifications').innerHTML += '<p>' + data.message + '</p>';
    };

    chatSocket.onclose = function(e) {
        console.error('Chat socket closed unexpectedly');
    };

    document.querySelector('#send-button').onclick = function(e) {
        const messageInput = document.querySelector('#message-input');
        chatSocket.send(JSON.stringify({
            'message': messageInput.value
        }));
        messageInput.value = '';
    };
</script>
