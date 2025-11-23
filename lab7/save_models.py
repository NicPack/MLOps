from pathlib import Path

import onnxruntime as ort
import torch
import torch.onnx
from transformers import AutoModel, AutoTokenizer

model_name = "sentence-transformers/multi-qa-mpnet-base-cos-v1"

Path("models").mkdir(exist_ok=True)

print("Loading model and tokenizer...")
model = AutoModel.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

print("Saving tokenizer...")
tokenizer.save_pretrained("models/tokenizer")

print("Saving PyTorch model...")
torch.save(model.state_dict(), "models/model.pt")

print("Exporting to ONNX...")
model_cpu = model.eval().cpu()
sample_input = tokenizer(
    "Sample text for ONNX export",
    padding=True,
    truncation=True,
    return_tensors="pt",
)

torch.onnx.export(
    model_cpu,
    (sample_input["input_ids"], sample_input["attention_mask"]),
    "models/model.onnx",
    opset_version=14,
    input_names=["input_ids", "attention_mask"],
    output_names=["output"],
    dynamic_axes={
        "input_ids": {0: "batch_size", 1: "sequence_length"},
        "attention_mask": {0: "batch_size", 1: "sequence_length"},
        "output": {0: "batch_size"},
    },
    export_params=True,
    do_constant_folding=True,
    dynamo=False,
)

print("Optimizing ONNX model...")
sess_options = ort.SessionOptions()
sess_options.graph_optimization_level = ort.GraphOptimizationLevel.ORT_ENABLE_EXTENDED
sess_options.optimized_model_filepath = "models/model_optimized.onnx"
ort.InferenceSession("models/model.onnx", sess_options)

print("Models saved successfully!")
print("- PyTorch model: models/model.pt")
print("- ONNX model: models/model_optimized.onnx")
print("- Tokenizer: models/tokenizer/")
