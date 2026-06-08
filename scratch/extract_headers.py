import os
import json

notebooks = [
    ("preprocessing/00_data_analysis.ipynb", "NB0 - Data Analysis"),
    ("preprocessing/01_eda_preprocessing.ipynb", "NB1 - EDA & Preprocessing"),
    ("preprocessing/02_eda_geographic.ipynb", "NB2 - Geographic Analysis"),
    ("clustering/03_clustering.ipynb", "NB3 - Clustering"),
    ("clustering/04_cluster_characterization.ipynb", "NB4 - Cluster Characterisation"),
    ("clustering/05_association_rules.ipynb", "NB5 - Association Rules")
]

out_lines = []

for path, name in notebooks:
    out_lines.append("=" * 80)
    out_lines.append(f"Notebook: {name} ({path})")
    out_lines.append("=" * 80)
    if not os.path.exists(path):
        out_lines.append(f"File {path} not found.")
        continue
    try:
        with open(path, "r", encoding="utf-8") as f:
            nb = json.load(f)
        idx = 0
        for cell in nb.get("cells", []):
            if cell.get("cell_type") == "markdown":
                source = cell.get("source", [])
                if isinstance(source, list):
                    source = "".join(source)
                
                # Check for headings or specific div boxes with headers
                lines = source.splitlines()
                for line in lines:
                    line_s = line.strip()
                    if line_s.startswith("#") or "h1" in line_s or "h2" in line_s or "h3" in line_s or "h4" in line_s or "<b>" in line_s:
                        out_lines.append(f"[{idx}] {line_s[:120]}")
            idx += 1
    except Exception as e:
        out_lines.append(f"Error reading {path}: {e}")
    out_lines.append("\n\n")

with open("scratch/notebook_headers.txt", "w", encoding="utf-8") as out_f:
    out_f.write("\n".join(out_lines))
