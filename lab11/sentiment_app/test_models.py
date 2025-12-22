import onnxruntime as ort
from tokenizers import Tokenizer

OONX_CLASSIFIER_PATH = "model/onnx/classifier.onnx"
OONX_EMBEDDING_MODEL_PATH = "model/onnx/sentence_transformer/embedding.onnx"
OONX_TOKENIZER_PATH = "model/onnx/sentence_transformer/tokenizer/tokenizer.json"

print("Testing model loading...")

try:
    embedding_session = ort.InferenceSession(OONX_EMBEDDING_MODEL_PATH)
    print("✓ Embedding model loaded")
    print(
        f"  Inputs: {[(i.name, i.shape, i.type) for i in embedding_session.get_inputs()]}"
    )
    print(
        f"  Outputs: {[(o.name, o.shape, o.type) for o in embedding_session.get_outputs()]}"
    )
except Exception as e:
    print(f"✗ Failed to load embedding model: {e}")

try:
    classifier_session = ort.InferenceSession(OONX_CLASSIFIER_PATH)
    print("✓ Classifier model loaded")
    print(
        f"  Inputs: {[(i.name, i.shape, i.type) for i in classifier_session.get_inputs()]}"
    )
    print(
        f"  Outputs: {[(o.name, o.shape, o.type) for o in classifier_session.get_outputs()]}"
    )
except Exception as e:
    print(f"✗ Failed to load classifier model: {e}")

try:
    tokenizer = Tokenizer.from_file(OONX_TOKENIZER_PATH)
    print("✓ Tokenizer loaded")
except Exception as e:
    print(f"✗ Failed to load tokenizer: {e}")
