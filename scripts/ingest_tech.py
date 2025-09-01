#!/usr/bin/env python3
import sqlite3, pandas as pd
from pathlib import Path
from slugify import slugify

DB = Path("data/engines.db")
CSV = Path("data/tech.csv")
SQL = Path("data/tech.sql")

def main():
    DB.parent.mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect(DB)
    con.executescript(SQL.read_text(encoding="utf-8"))

    # categories
    categories = set()
    df = pd.read_csv(CSV)
    for cat in df["Category"].fillna("Uncategorized"):
        categories.add(cat.strip())

    for cat in sorted(categories):
        con.execute("INSERT OR IGNORE INTO categories(name) VALUES (?)", (cat,))

    # tech rows
    for _, r in df.iterrows():
        name = r["Name"].strip()
        slug = slugify(name)
        cat = r.get("Category", "Uncategorized") or "Uncategorized"
        cat_id = con.execute("SELECT id FROM categories WHERE name=?", (cat,)).fetchone()[0]
        con.execute("""
            INSERT OR IGNORE INTO technologies(slug, name, first_use, region, category_id, description, notes)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            slug, name, r.get("First Use (approx.)"), r.get("Region"),
            cat_id, r.get("Description"),
            r.get("Primary Sources/Notes"),
        ))

        # Notable battle links are optional and free-form; we store as notes for now.
        # If you import WarChest battles, use import_from_warchest.py to build tech_battles.

    con.commit()
    con.close()
    print(f"✔ Built {DB}")

if __name__ == "__main__":
    main()
