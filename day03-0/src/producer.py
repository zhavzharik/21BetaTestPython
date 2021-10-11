import random
import json
import redis
import logging
import time
# from rq import Queue

logger = logging.getLogger('example_logger')


def data_publish(number):
    r = redis.Redis(host='localhost', port=6379, db=0)
    keyslist = ['from', 'to']
    accounts = [1111111111, 5625162372, 7833780089, 4815162342]
    time.sleep(10)
    for i in range(number):
        valuelist = random.sample(accounts, k=2)
        metadata = dict(zip(keyslist, valuelist))
        message = dict(metadata=metadata, amount=random.randint(-10000, 10000))
        S = json.dumps(message)
        logger.warning(S)
        r.publish('producer', S)
        time.sleep(0.001)
    accounts = [2222222222, 3133780085, 5625162372, 7833780089]
    for i in range(number):
        valuelist = random.sample(accounts, k=2)
        metadata = dict(zip(keyslist, valuelist))
        message = dict(metadata=metadata, amount=random.randint(-10000, 10000))
        S = json.dumps(message)
        logger.warning(S)
        r.publish('producer', S)
        time.sleep(0.001)
    r.close()


# def redis_queue():
#     r = redis.Redis(host='localhost', port=6379, db=0)
#     q = Queue(connection=r)
#     job = q.enqueue(data_publish, 10)


if __name__ == "__main__":
    data_publish(10)
    # redis_queue()
    # print(job.result)



