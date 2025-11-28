from fastapi import FastAPI, Request
from models import SearchRequest
from scraper.run_scraper import run_search


app = FastAPI(title="Scraper Adherence API")


@app.middleware("http")
async def log_raw_body(request: Request, call_next):
    raw_body = await request.body()
    print("
    === RAW HTTP BODY RECEBIDO ===")
try:
    print(raw_body.decode("utf-8"))
except Exception:
    print("Erro ao decodificar corpo bruto.")
    print("================================
    ")
response = await call_next(request)
return response


@app.post("/api/search")
async def handle_search(request: SearchRequest):
    print("
=== JSON VALIDADO (MODEL_DUMP) ===")
    print(request.model_dump())
    print("==================================
")


project_title = request.title
adherence_data = request.adherence_matrix


print(f"Iniciando busca para o projeto: {project_title}")


results = await run_search(project_title, adherence_data)


return {"status": "success", "data": results}