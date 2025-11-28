from fastapi import FastAPI
from pydantic import BaseModel
from queue.queue_connection import scraping_queue
from scraper.run_scraper import run_scraper
from rq.job import Job
from redis import Redis

redis_conn = Redis(host="redis", port=6379, db=0)

app = FastAPI()

class SearchRequest(BaseModel):
    title: str
    adherence_matrix: list

@app.post("/api/search")
def enqueue_scraper(request: SearchRequest):
    job = scraping_queue.enqueue(run_scraper, request.title, request.adherence_matrix)
    return {"job_id": job.get_id(), "status": "queued"}

@app.get("/api/result/{job_id}")
def get_result(job_id: str):
    job = Job.fetch(job_id, connection=redis_conn)

    return {
        "job_id": job_id,
        "status": job.get_status(),
        "result": job.result
    }