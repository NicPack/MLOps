from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    s3_bucket_name: str = "mlops-lab11-nicolas"
    s3_artifacts_path: str = "model"
    sentence_transformer_path: str = "model/sentence_transformer.model"
    classifier_joblib_path: str = "model/classifier.joblib"
    sentence_transformer_dir: str = "model/sentence_transformer.model"
    onnx_classifier_path: str = "model/onnx/classifier.onnx"
    onnx_embedding_model_path: str = "model/onnx/sentence_transformer/embedding.onnx"
    onnx_tokenizer_path: str = "model/onnx/sentence_transformer/tokenizer/"
    local_artifacts_path: str = "artifacts"
    batch_size: int = 32
    embedding_dim: int = 384


settings = Settings()
