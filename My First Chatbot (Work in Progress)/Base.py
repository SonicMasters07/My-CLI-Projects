import pandas as pd
import numpy as np
import json
from sentence_transformers import SentenceTransformer


with open("Database.json", "r") as d:
    database = check = json.load(d)

model = SentenceTransformer("all-MiniLM-L6-v2")

with open("Database.json", "r") as d:
    check = json.load(d)

for item in check:
    question = item["question"] + "" + item["answer"]
    embedding = model.encode(question).tolist()  # convert numpy array to list
    item["embedding"] = embedding  # save embedding inside the JSON structure

with open("knowledge_with_embeddings.json", "w", encoding="utf-8") as f:
    json.dump(check, f, indent=4, ensure_ascii=False)

indexed = np.array(["Q1", "Q2", "Q3"])
refine = pd.DataFrame(check, index = indexed).to_string()

print(refine)


print("✅ Embeddings generated and saved to knowledge_with_embeddings.json")
