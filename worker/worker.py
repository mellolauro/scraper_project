import sys
import os
from rq import Worker, Queue, Connection
from queue_connection import redis_conn

listen = ["scraping_queue"]

if __name__ == "__main__":
    with Connection(redis_conn):
        worker = Worker(map(Queue, listen))
        worker.work()