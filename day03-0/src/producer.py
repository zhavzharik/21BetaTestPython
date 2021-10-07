# import os
import random
import json
import redis
import logging
from rq import Queue
import time


# q = Queue(connection=r)

def data_publish():
    r = redis.Redis(host='localhost', port=6379, db=0)
    keyslist = ['from', 'to']
    accounts = [4815162342, 3133780085, 5625162372, 7833780089]
    for i in range(10):
        valuelist = random.sample(accounts, k=2)
        metadata = dict(zip(keyslist, valuelist))
        message = dict(metadata=metadata, amount=random.randint(-10000, 10000))
        S = json.dumps(message)
        print(S)
        r.publish('producer', S)
        time.sleep(0.01)
    r.close()


# logging.debug('This is a debug message')
# logging.info('This is an info message')
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')


if __name__ == "__main__":
    data_publish()



