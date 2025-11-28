import redis
from rq import Queue

# Conexão Redis
redis_conn = redis.Redis(host="redis", port=6379, db=0)

# Fila de scraping (alta prioridade)
scraping_queue = Queue("scraping_queue", connection=redis_conn)