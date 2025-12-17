from sentence_transformers import SentenceTransformer

# Download complete model (including weights)
model = SentenceTransformer("all-MiniLM-L6-v2")

# Save it properly
model.save("model/sentence_transformer.model")