import React, { useState } from 'react';

const API_URL = '/api/search';

export default function SearchForm() {
    const [projectTitle, setProjectTitle] = useState('');
    const [adherenceMatrix, setAdherenceMatrix] = useState([
        { keyword: '', weight: 0.5, id: Date.now() }
    ]);

    const [results, setResults] = useState(null);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);

    // ------------------------------
    // Adicionar linha da matriz
    // ------------------------------
    const handleAddAdherence = () => {
        setAdherenceMatrix([
            ...adherenceMatrix,
            { keyword: '', weight: 0.5, id: Date.now() }
        ]);
    };

    // ------------------------------
    // Editar valores da matriz
    // ------------------------------
    const handleMatrixChange = (id, field, value) => {
        setAdherenceMatrix(
            adherenceMatrix.map(item =>
                item.id === id
                    ? { ...item, [field]: field === 'weight' ? parseFloat(value) : value }
                    : item
            )
        );
    };

    // ------------------------------
    // Remover linha da matriz
    // ------------------------------
    const handleRemoveAdherence = (id) => {
        setAdherenceMatrix(adherenceMatrix.filter(item => item.id !== id));
    };

    // ------------------------------
    // SUBMIT DO FORM
    // ------------------------------
    const handleSubmit = async (e) => {
        e.preventDefault();
        setLoading(true);
        setError(null);
        setResults(null);

        // Filtrar itens válidos
        const validMatrix = adherenceMatrix
            .filter(item => item.keyword.trim() !== '' && item.weight > 0 && item.weight <= 1)
            .map(({ id, ...rest }) => rest);

        if (projectTitle.trim() === '' || validMatrix.length === 0) {
            setError("Por favor, preencha o Título do Projeto e adicione pelo menos uma aderência válida.");
            setLoading(false);
            return;
        }

        const requestBody = {
            title: projectTitle,
            adherence_matrix: validMatrix
        };

        try {
            const response = await fetch(API_URL, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(requestBody),
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.detail ?? "Erro desconhecido no servidor.");
            }

            const data = await response.json();
            setResults(data.data);

        } catch (err) {
            setError(`Falha na busca: ${err.message}`);

        } finally {
            setLoading(false);
        }
    };

    // ======================================================
    // RENDER
    // ======================================================
    return (
        <div style={{ maxWidth: '800px', margin: 'auto', fontFamily: 'Arial' }}>
            <h1>Sistema de Classificação de Software</h1>

            <form onSubmit={handleSubmit}>
                <h2>Título do Projeto/Sistema 📝</h2>

                <input
                    type="text"
                    placeholder="Ex: Sistema de CRM"
                    value={projectTitle}
                    onChange={(e) => setProjectTitle(e.target.value)}
                    style={{ width: '100%', padding: '10px', marginBottom: '20px' }}
                />

                <h2>Matriz de Aderência (Keywords e Pesos) ⚖️</h2>

                {adherenceMatrix.map((item) => (
                    <div key={item.id} style={{ display: 'flex', gap: '10px', marginBottom: '10px' }}>
                        <input
                            type="text"
                            placeholder="Palavra-chave (Ex: API REST)"
                            value={item.keyword}
                            onChange={(e) => handleMatrixChange(item.id, 'keyword', e.target.value)}
                            style={{ flex: 3, padding: '8px' }}
                        />

                        <input
                            type="number"
                            step="0.05"
                            min="0.05"
                            max="1.0"
                            value={item.weight}
                            onChange={(e) => handleMatrixChange(item.id, 'weight', e.target.value)}
                            style={{ flex: 1, padding: '8px', textAlign: 'center' }}
                        />

                        <button
                            type="button"
                            onClick={() => handleRemoveAdherence(item.id)}
                            style={{
                                background: '#f44336',
                                color: 'white',
                                border: 'none',
                                padding: '0 10px',
                                cursor: 'pointer'
                            }}
                        >
                            x
                        </button>
                    </div>
                ))}

                <button
                    type="button"
                    onClick={handleAddAdherence}
                    style={{
                        padding: '10px 15px',
                        marginRight: '10px',
                        background: '#4CAF50',
                        color: 'white',
                        border: 'none',
                        cursor: 'pointer'
                    }}
                >
                    + Adicionar Aderência
                </button>

                <button
                    type="submit"
                    disabled={loading}
                    style={{
                        padding: '10px 15px',
                        background: '#2196F3',
                        color: 'white',
                        border: 'none',
                        cursor: 'pointer'
                    }}
                >
                    {loading ? 'Buscando...' : 'Buscar e Pontuar Sistemas'}
                </button>
            </form>

            {error && <p style={{ color: 'red', marginTop: '20px' }}>Erro: {error}</p>}

            {results && <ResultsTable data={results} />}
        </div>
    );
}


// ======================================================
// TABELA DE RESULTADOS
// ======================================================
function ResultsTable({ data }) {
    if (!data || data.length === 0)
        return <p style={{ marginTop: '20px' }}>Nenhum sistema correspondente foi encontrado.</p>;

    return (
        <div style={{ marginTop: '30px' }}>
            <h3>Resultados Classificados por Aderência:</h3>

            <table style={{ width: '100%', borderCollapse: 'collapse', border: '1px solid #ccc' }}>
                <thead>
                    <tr style={{ background: '#f2f2f2' }}>
                        <th style={tableHeaderStyle}>Rank</th>
                        <th style={tableHeaderStyle}>Software / Empresa</th>
                        <th style={tableHeaderStyle}>Pontuação</th>
                        <th style={tableHeaderStyle}>Aderências Encontradas</th>
                    </tr>
                </thead>

                <tbody>
                    {data.map(item => (
                        <tr key={item.rank}>
                            <td style={tableCellStyle}>{item.rank}</td>

                            <td style={tableCellStyle}>
                                <strong>{item.name}</strong><br />
                                <small>({item.company})</small>
                            </td>

                            <td style={{ ...tableCellStyle, fontWeight: 'bold' }}>
                                {item.score}
                            </td>

                            <td style={tableCellStyle}>
                                {item.adherences_found.join(', ')}
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}


const tableHeaderStyle = {
    padding: '10px',
    border: '1px solid #ccc',
    textAlign: 'left'
};

const tableCellStyle = {
    padding: '10px',
    border: '1px solid #ccc',
    verticalAlign: 'top'
};