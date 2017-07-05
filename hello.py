#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Python从3.5版本开始为asyncio提供了async和await的新语法；
#把@asyncio.coroutine替换为async；
#把yield from替换为await。


import threading
import asyncio

async def hello():
    print('Hello world! (%s)' % threading.currentThread())
    await asyncio.sleep(1)
    print('Hello again! (%s)' % threading.currentThread())

loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()