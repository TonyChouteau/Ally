#!/usr/bin/env python

import asyncio
import websockets
import json

from process.ally import Ally
from utils.logger import Logger

logger = Logger("WebSocket")
ally = Ally()


async def handler(websocket):

    def message_is_valid(message):
        return isinstance(message, dict) and message.get("route") and message.get("data")

    while True:
        try:
            str_messaage = await websocket.recv()
            message = json.loads(str_messaage)
            logger.log(message)
            if message_is_valid(message):
                ally.handle(message["route"], message["data"])
        except websockets.ConnectionClosedOK:
            break


async def main():
    async with websockets.serve(handler, "", 8001):
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())
