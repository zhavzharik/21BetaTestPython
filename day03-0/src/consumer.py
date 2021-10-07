# import os
import json
import sys
import redis
import logging
from rq import Queue
import time


bad_guys = []


def read_bad_guys():
    # flag = 0
    # for argument in text:
    #     if str(argument) == '-e':
    #         flag = 1
    #     argument = argument.rstrip(',')
    #     if flag == 1 and str(argument) != '-e' and len(argument) == 10:
    #         bad_guys.append(int(argument))
    #     if not argument:
    #         break
    if sys.argv[1] == '-e':
        for guy in sys.argv[2].split(','):
            bad_guys.append(int(guy))
    return bad_guys


def read_queue(accounts):
    r = redis.Redis(host='localhost', port=6379, db=0)
    p = r.pubsub(ignore_subscribe_messages=True)
    p.subscribe('producer')
    flag = 0
    keyslist = ['from', 'to']
    for message in p.listen():
        message = json.loads(message['data'])
        metadata = message['metadata']
        from_account = metadata['from']
        to_account = metadata['to']
        amount = message['amount']
        check = 0
        for account in accounts:
            if account == to_account and amount > 0:
                check = 1
        if check == 1:
            valuelist = [to_account, from_account]
            metadata = dict(zip(keyslist, valuelist))
            message = dict(metadata=metadata, amount=amount)
            message = json.dumps(message)
            print(message)
        else:
            print(message)
        flag += 1
        time.sleep(0.001)
        if flag == 10:
            p.close()


if __name__ == "__main__":
    bad_guys = read_bad_guys()
    print(f'bad guys: {bad_guys}')
    read_queue(bad_guys)


# python consumer.py -e 4815162342,3133780085
