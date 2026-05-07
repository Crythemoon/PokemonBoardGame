import asyncio
import websockets

clients = set()

async def handler(websocket):
    print("Client connected")
    clients.add(websocket)

    try:
        async for message in websocket:
            print(f"Received message: {message}")
            
            for client in clients:
                await client.send(message)

    except:
        print("Client disconnected")

    finally:
        clients.remove(websocket)


async def main():
    async with websockets.serve(handler, "localhost", 8765):
        print("Server running...")
        await asyncio.Future()  # run forever

asyncio.run(main())
                  