# import os
import json
import redis
import logging
from flask import Flask, request
from rq import Queue
import time


# app = Flask(__name__)

r = redis.Redis(host='localhost', port=6379, db=0)

p = r.pubsub(ignore_subscribe_messages=True)
p.subscribe('producer')
for message in p.listen():
    print(f"Сообщение: {message['data']}")
    time.sleep(0.001)
p.close()