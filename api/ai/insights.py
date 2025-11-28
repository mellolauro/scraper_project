from sentence_transformers import util
from ai.model_selector import select_optimal_model


async def calculate_adherence_score_embeddings(project_title, matrix, scraped_data):
    # seleciona modelo
    model = select_optimal_model(project_title, matrix, scraped_data)


    print("
--- INICIANDO PIPELINE: NLP PRO AUTO-MODEL ---")


# embedding do título
    title_embedding = model.encode(project_title, convert_to_tensor=True)


# embeddings da matriz
    matrix_embeddings = []
    for item in matrix:
    # item é dict com 'keyword' e 'weight'
    kw = item['keyword'] if isinstance(item, dict) else getattr(item, 'keyword')
    weight = item['weight'] if isinstance(item, dict) else getattr(item, 'weight')
    emb = model.encode(kw, convert_to_tensor=True)
    matrix_embeddings.append({
        'keyword': kw,
        'weight': weight,
        'embedding': emb
    })


    results = []
    for sw in scraped_data:
        text = f"{sw.get('name','')} - {sw.get('description','')}"
        sw_embedding = model.encode(text, convert_to_tensor=True)


        sim_title = float(util.cos_sim(title_embedding, sw_embedding))


        sim_matrix = 0.0
        adherences_found = []
        for m in matrix_embeddings:
            sim = float(util.cos_sim(m['embedding'], sw_embedding))
            if sim > 0.45:
                adherences_found.append(m['keyword'])
            sim_matrix += sim * m['weight']


        max_possible = sum(m['weight'] for m in matrix_embeddings) or 1.0
        normalized = (sim_matrix / max_possible)


        final_score = (0.6 * sim_title) + (0.4 * normalized)


        results.append({
            'rank': None,
            'name': sw.get('name'),
            'company': sw.get('company'),
            'score': round(float(final_score), 6),
            'adherences_found': adherences_found
        })


# ordena e adiciona rank
        results = sorted(results, key=lambda x: x['score'], reverse=True)
        for i, r in enumerate(results, start=1):
            r['rank'] = i

        return results