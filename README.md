<p align="center">
  <img src="https://github.com/user-attachments/assets/cf64ffbf-8055-43ab-80c5-79ef5859c387" alt="EnginesOfWar Banner" width="800"/>
</p>

<h1 align="center">EnginesOfWar</h1>

<p align="center">
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.10+-blue.svg?logo=python&logoColor=white" alt="Python"></a>
  <a href="https://fastapi.tiangolo.com/"><img src="https://img.shields.io/badge/FastAPI-0.111+-009485?logo=fastapi&logoColor=white" alt="FastAPI"></a>
  <a href="https://www.sqlite.org/"><img src="https://img.shields.io/badge/SQLite-DB-003B57?logo=sqlite&logoColor=white" alt="SQLite"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License: MIT"></a>
</p>

<p align="center">
  A code-first catalogue of wartime technological advances from antiquity to the present:  
  weapons, armor, siege engines, logistics, and doctrinal innovations.  
  Includes data, a SQLite schema, an API, and example analyses.
</p>

---

## What's here
- `data/tech.csv` — human-editable dataset of technologies  
- `data/tech.sql` — SQLite schema (tech + categories + links to battles)  
- `scripts/ingest_tech.py` — build `data/engines.db` from CSV  
- `scripts/import_from_warchest.py` — optional: ingest `battles.csv` from WarChest for cross-linking  
- `api/main.py` — FastAPI for `/tech`, `/tech/{slug}`, `/timeline`  
- `examples/timeline.py` — generate a simple timeline chart (PNG)  

---

## Quickstart
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python scripts/ingest_tech.py
uvicorn api.main:app --reload
# visit http://127.0.0.1:8000/docs

```

---

<p align="center">
  <img src="https://github.com/user-attachments/assets/4e7c668a-e831-423e-b791-0f436d29fc06" alt="EnginesOfWar Banner" width="500"/>
</p>



