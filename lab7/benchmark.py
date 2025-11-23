import statistics
import time

import torch
from transformers import AutoModel, AutoTokenizer

print("=" * 60)
print("PYTORCH COMPILED MODEL BENCHMARK")
print("=" * 60)

print("\nLoading tokenizer...")
tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/multi-qa-mpnet-base-cos-v1")

print("Loading model...")
model = AutoModel.from_pretrained("sentence-transformers/multi-qa-mpnet-base-cos-v1")
model.load_state_dict(torch.load("model.pt", weights_only=True))
model.eval()

print("Compiling model (this may take a while)...")
model_compiled = torch.compile(model, mode="max-autotune")

test_texts = [
    "Short text for testing.",
    "This is a medium length text that we will use to test the inference speed of our model.",
    "This is a longer text that contains significantly more words and should take more time to process through the transformer model architecture for generating high-quality embeddings.",
]

print("\nWarming up model...")
for text in test_texts:
    inputs = tokenizer(text, padding=True, truncation=True, return_tensors="pt")
    with torch.inference_mode():
        for _ in range(10):
            _ = model_compiled(**inputs)

print("\nRunning benchmark (100 iterations)...")
times = []
num_runs = 100

for i in range(num_runs):
    text = test_texts[i % len(test_texts)]
    inputs = tokenizer(text, padding=True, truncation=True, return_tensors="pt")

    start = time.time()
    with torch.inference_mode():
        outputs = model_compiled(**inputs)
        embeddings = outputs.last_hidden_state.mean(dim=1)
    elapsed = time.time() - start
    times.append(elapsed)

    if (i + 1) % 25 == 0:
        print(f"  Progress: {i + 1}/{num_runs}")

print("\n" + "=" * 60)
print("RESULTS")
print("=" * 60)
print(f"Total runs:        {len(times)}")
print(f"Mean time:         {statistics.mean(times) * 1000:.4f} ms")
print(f"Median time:       {statistics.median(times) * 1000:.4f} ms")
print(f"Min time:          {min(times) * 1000:.4f} ms")
print(f"Max time:          {max(times) * 1000:.4f} ms")
print(f"Std deviation:     {statistics.stdev(times) * 1000:.4f} ms")
print(f"Total time:        {sum(times):.4f} s")
print("=" * 60)
