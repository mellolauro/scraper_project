
from fastapi import FastAPI
from .models import SearchRequest
from scraper.run_scraper import run_search 

app = FastAPI(title="Scraper Adherence API")

@app.post("/api/search")
async def handle_search(request: SearchRequest):
    """
    Recebe a matriz de aderência do frontend (Next.js) e inicia o pipeline.
    """
    
    # 💡 Ação: Defina as variáveis antes de usá-las, acessando o objeto 'request'
    project_title = request.title
    adherence_data = request.adherence_matrix
    
    print(f"Iniciando busca para: {project_title}")
    
    # 💡 Usamos as variáveis locais definidas acima
    results = await run_search(project_title, adherence_data) 
    
    return {"status": "success", "data": results}