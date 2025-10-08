from sentence_transformers import SentenceTransformer, util
import json

# Step 1: Load the same model used before
model = SentenceTransformer("all-MiniLM-L6-v2")

# Step 2: Load the knowledge base with embeddings
with open("knowledge_with_embeddings.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print("🤖 Chatbot ready! Ask me anything about Islam.\n(Type 'exit' to quit.)")

# Step 3: Continuous chat loop
while True:
    user_q = input("You: ")

    if user_q.lower() == "exit":
        print("Bot: Goodbye! 👋")
        break

    # Step 4: Convert user question into embedding
    user_emb = model.encode(user_q)

    # Step 5: Compare it to all stored embeddings
    best_match = None
    best_score = -1

    for item in data:
        stored_emb = item["embedding"]
        score = util.cos_sim(user_emb, stored_emb)[0][0]
        if score > best_score:
            best_score = score
            best_match = item

    # Step 6: Show the answer
    if best_score > 0.25:  # threshold to make sure it’s a decent match
        print(f"Bot: {best_match['answer']}")
    else:
        print("Bot: Sorry, I don’t know that yet.")
