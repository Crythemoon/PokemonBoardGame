import asyncio
from pyclbr import Class
import websockets
import json

class NetworkClient:
    def __init__(self, url):
        self.url = url
        self.ws = None
    
    async def connect(self):
        self.ws = await websockets.connect(self.url)
        print("Connected to server")

    async def send(self, data):
        if self.ws is None:
            raise Exception("Not connected to server")
        
        await self.ws.send(json.dumps(data))
    
    async def start_round(self,data):
        await self.send(data)
    
    async def send_move(self,)
    

asyncio.run(main())