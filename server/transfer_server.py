#!/usr/bin/env python

import asyncio
import websockets

ally = None


async def handler(websocket):
    global ally
    while True:
        try:
            message = await websocket.recv()
            if message == "ally":
                print("ally")
                ally = websocket
            else:
                print(message)
                await ally.send(message)
        except websockets.ConnectionClosedOK:
            break


async def main():
    async with websockets.serve(handler, "", 8001):
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())
