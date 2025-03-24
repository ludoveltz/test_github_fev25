# test_deps.py
import numpy as np
import torch
from transformers import pipeline
import streamlit as st

def test_dependencies():
    print(f"NumPy version: {np.__version__}")
    print(f"PyTorch version: {torch.__version__}")
    print("Transformers pipeline test...")
    classifier = pipeline("zero-shot-classification")
    print("All dependencies working correctly!")

if __name__ == "__main__":
    test_dependencies()