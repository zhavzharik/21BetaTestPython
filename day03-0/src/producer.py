# import os
import json
import redis
import logging
from flask import Flask, request
from rq import Queue
import time

# this_path = os.getcwd()
# full_path_file = os.path.join(os.path.dirname(this_path), 'message.json')
#
data = {"metadata": {"from": 1023461745, "to": 5738456434}, "amount": 10000}
json_dump = json.dumps(data, indent=4)
# print(json_dump)

# with open(full_path_file, "w") as file:
#     file.write(json_dump)

# app = Flask(__name__)

r = redis.Redis(host='localhost', port=6379, db=0)

# p = r.pubsub()
# p.subscribe('producer')
# answer = p.get_message()

r.publish('producer', str(data))
time.sleep(10)
r.close()

# q = Queue(connection=r)

# logging.debug('This is a debug message')
# logging.info('This is an info message')
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')
