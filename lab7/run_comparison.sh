#!/bin/bash

echo "=========================================="
echo "DOCKER IMAGE COMPARISON"
echo "=========================================="

echo -e "\nBuilding PyTorch image..."
docker build -f dockerfile.pytorch -t inference-pytorch:latest . --quiet

echo "Building ONNX image..."
docker build -f dockerfile.onnx -t inference-onnx:latest . --quiet

echo -e "\n=========================================="
echo "IMAGE SIZES"
echo "=========================================="

pytorch_size=$(docker images inference-pytorch:latest --format "{{.Size}}")
onnx_size=$(docker images inference-onnx:latest --format "{{.Size}}")

echo "PyTorch image:  $pytorch_size"
echo "ONNX image:     $onnx_size"

echo -e "\nDetailed breakdown:"
docker images | head -1
docker images | grep -E "inference-pytorch|inference-onnx"

echo -e "\n=========================================="
echo "RUNNING PYTORCH BENCHMARK"
echo "=========================================="
docker run --rm inference-pytorch:latest

echo -e "\n=========================================="
echo "RUNNING ONNX BENCHMARK"
echo "=========================================="
docker run --rm inference-onnx:latest

echo -e "\n=========================================="
echo "COMPARISON COMPLETE"
echo "=========================================="