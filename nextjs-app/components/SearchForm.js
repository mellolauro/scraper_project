"use client";
import { useState } from "react";

export default function SearchForm() {
    const [projectTitle, setProjectTitle] = useState("");
    const [adherenceMatrix, setAdherenceMatrix] = useState("");

    return (
        <form>
            <input
                type="text"
                value={projectTitle}
                onChange={(e) => setProjectTitle(e.target.value)}
                placeholder="Título do projeto"
            />
        </form>
    );
}
