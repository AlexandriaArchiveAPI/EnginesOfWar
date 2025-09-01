from fastapi import FastAPI, HTTPException
import sqlite3

app = FastAPI(title="EnginesOfWar API")

def db():
    con = sqlite3.connect("data/engines.db")
    con.row_factory = sqlite3.Row
    return con

@app.get("/tech")
def list_tech(category: str | None = None):
    con = db()
    q = """
    SELECT t.slug, t.name, t.first_use, t.region, COALESCE(c.name,'Uncategorized') AS category
    FROM technologies t LEFT JOIN categories c ON c.id = t.category_id
    """
    params = ()
    if category:
        q += " WHERE c.name = ?"
        params = (category,)
    rows = [dict(r) for r in con.execute(q, params)]
    con.close()
    return rows

@app.get("/tech/{slug}")
def get_tech(slug: str):
    con = db()
    t = con.execute("""
        SELECT t.slug, t.name, t.first_use, t.region, COALESCE(c.name,'Uncategorized') AS category,
               t.description, t.notes
        FROM technologies t LEFT JOIN categories c ON c.id = t.category_id
        WHERE t.slug = ?
    """, (slug,)).fetchone()
    if not t:
        con.close()
        raise HTTPException(status_code=404, detail="not found")
    # linked battles if imported
    battles = [dict(r) for r in con.execute("""
        SELECT b.name, b.year, b.war, b.location
        FROM tech_battles tb
        JOIN battles b ON b.id = tb.battle_id
        JOIN technologies t2 ON t2.id = tb.tech_id
        WHERE t2.slug = ?
    """, (slug,))]
    con.close()
    return {"tech": dict(t), "battles": battles}

@app.get("/timeline")
def timeline():
    con = db()
    rows = [dict(r) for r in con.execute("""
        SELECT t.name, t.first_use, COALESCE(c.name,'Uncategorized') AS category
        FROM technologies t LEFT JOIN categories c ON c.id = t.category_id
        ORDER BY t.first_use
    """)]
    con.close()
    return rows
