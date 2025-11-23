import onnxruntime as ort
import numpy as np
import time
from transformers import AutoTokenizer
import statistics

print("="*60)
print("ONNX RUNTIME MODEL BENCHMARK")
print("="*60)

print("\nLoading tokenizer...")
tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/multi-qa-mpnet-base-cos-v1")

print("Loading ONNX model...")
sess_options = ort.SessionOptions()
sess_options.graph_optimization_level = ort.GraphOptimizationLevel.ORT_DISABLE_ALL
sess_options.intra_op_num_threads = 4
sess_options.inter_op_num_threads = 4

ort_session = ort.InferenceSession(
    "model_optimized.onnx",
    sess_options=sess_options,
    providers=["CPUExecutionProvider"]
)

test_texts = [
    "Short text for testing.",
    "This is a medium length text that we will use to test the inference speed of our model.",
    "This is a longer text that contains significantly more words and should take more time to process through the transformer model architecture for generating high-quality embeddings."
]

print("\nWarming up model...")
for text in test_texts:
    inputs = tokenizer(text, padding=True, truncation=True, return_tensors="pt")
    ort_inputs = {
        "input_ids": inputs["input_ids"].numpy(),
        "attention_mask": inputs["attention_mask"].numpy()
    }
    for _ in range(10):
        _ = ort_session.run(None, ort_inputs)

print("\nRunning benchmark (100 iterations)...")
times = []
num_runs = 100

for i in range(num_runs):
    text = test_texts[i % len(test_texts)]
    inputs = tokenizer(text, padding=True, truncation=True, return_tensors="pt")
    
    ort_inputs = {
        "input_ids": inputs["input_ids"].numpy(),
        "attention_mask": inputs["attention_mask"].numpy()
    }
    
    start = time.time()
    outputs = ort_session.run(None, ort_inputs)
    embeddings = np.mean(outputs[0], axis=1)
    elapsed = time.time() - start
    times.append(elapsed)
    
    if (i + 1) % 25 == 0:
        print(f"  Progress: {i + 1}/{num_runs}")

print("\n" + "="*60)
print("RESULTS")
print("="*60)
print(f"Total runs:        {len(times)}")
print(f"Mean time:         {statistics.mean(times)*1000:.4f} ms")
print(f"Median time:       {statistics.median(times)*1000:.4f} ms")
print(f"Min time:          {min(times)*1000:.4f} ms")
print(f"Max time:          {max(times)*1000:.4f} ms")
print(f"Std deviation:     {statistics.stdev(times)*1000:.4f} ms")
print(f"Total time:        {sum(times):.4f} s")
print("="*60)