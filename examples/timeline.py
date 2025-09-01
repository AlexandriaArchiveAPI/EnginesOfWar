import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

con = sqlite3.connect("data/engines.db")
df = pd.read_sql_query("SELECT name, first_use FROM technologies", con)
con.close()

# crude numeric ordering: extract earliest year-ish number in string
def to_num(s):
    if s is None: return None
    import re
    m = re.search(r"-?\d+", str(s))
    return int(m.group()) if m else None

df["year_hint"] = df["first_use"].map(to_num)
df = df.dropna(subset=["year_hint"]).sort_values("year_hint")

plt.figure()
plt.scatter(df["year_hint"], [1]*len(df))
for _, r in df.iterrows():
    plt.text(r["year_hint"], 1.02, r["name"], rotation=45, ha="left", va="bottom", fontsize=8)
plt.yticks([])
plt.xlabel("Year (approx.)")
plt.title("Timeline of Wartime Technologies")
plt.tight_layout()
plt.savefig("tech_timeline.png")
print("Wrote tech_timeline.png")
