#!/usr/bin/env python3
import argparse, sqlite3, pandas as pd
from pathlib import Path

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default="data/engines.db")
    ap.add_argument("--battles", required=True, help="Path to WarChest/data/battles.csv")
    args = ap.parse_args()

    con = sqlite3.connect(args.db)
    df = pd.read_csv(args.battles)

    # populate battles table
    for _, r in df.iterrows():
        con.execute("""
            INSERT OR IGNORE INTO battles(name, year, war, location)
            VALUES (?, ?, ?, ?)
        """, (r["Name"], r["Year"], r["War/Campaign"], r["Location"]))

    con.commit()
    con.close()
    print("✔ Imported battles into engines.db")

if __name__ == "__main__":
    main()
