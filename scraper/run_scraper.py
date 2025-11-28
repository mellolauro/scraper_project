import asyncio
from typing import List, Dict, Any
from ai.insights import calculate_adherence_score_embeddings


async def fetch_software_data(title: str, adherence_matrix: List[Dict[str, Any]]):
        # Mock provisório
        await asyncio.sleep(0.5)
        return [
            {
                "name": "Sistema CRM Plus",
                "company": "TechCorp",
                "description": "Plataforma de CRM com dashboard, automações e app mobile."
            },
            {
                "name": "SalesFlow Cloud",
                "company": "CloudSoft",
                "description": "CRM completo com API REST, relatórios e pagamento online integrado."
            },
            {
                "name": "ClientMaster",
                "company": "MasterSoft",
                "description": "Ferramenta de gestão de clientes com check-in QR Code e app mobile."
            }
        ]

import time

def run_scraper(title: str, adherence_matrix: list):
    """
    Simula processamento pesado (chamadas HTTP, IA, scraping...).
    Depois você ajusta com sua lógica real.
    """
    print("⏳ Executando scraper...")
    time.sleep(3)  # simula processo longo

    # Exemplo simples de resposta
    return {
        "title": title,
        "keywords_used": [item["keyword"] for item in adherence_matrix],
        "result": "Scraping finalizado com sucesso."
    }