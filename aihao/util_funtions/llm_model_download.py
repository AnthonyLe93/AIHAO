import os

import torch
from dotenv import load_dotenv
from huggingface_hub import hf_hub_download
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

# Load environment variables from the .env file
load_dotenv()

# Get the Hugging Face API key from environment variables
HUGGING_FACE_API_KEY = os.environ.get("HUGGING_FACE_API_KEY")

# Model ID on Hugging Face
model_id = "google/gemma-2b-it"

# Filenames to download
filenames = [
    "config.json", "gemma-2b-it.gguf", "generation_config.json", "model-00001-of-00002.safetensors", "model-00002-of-00002.safetensors",
    "model.safetensors.index.json", "special_tokens_map.json", "tokenizer.json", "tokenizer.model", "tokenizer_config.json"
]

# Specify the directory where you want to save the model files
models_repo_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'models')

# Create the directory if it doesn't exist
os.makedirs(models_repo_dir, exist_ok=True)


def download_model():
    """
    Download model files from the Hugging Face hub if they do not already exist.
    """
    for filename in filenames:
        file_path = os.path.join(models_repo_dir, filename)

        if not os.path.exists(file_path):
            downloaded_model_path = hf_hub_download(
                repo_id=model_id,
                filename=filename,
                token=HUGGING_FACE_API_KEY,
                cache_dir=models_repo_dir  # Specify the cache directory
            )
            print(f"Downloaded {filename} to {downloaded_model_path}")
        else:
            print(f"{filename} already exists. Skipping download.")


def load_model_and_generate(input_text: str):
    """
    Load the model and tokenizer and generate text based on the input.
    """
    tokenizer = AutoTokenizer.from_pretrained(model_id, token=HUGGING_FACE_API_KEY)
    model = AutoModelForCausalLM.from_pretrained(
        model_id,
        torch_dtype=torch.bfloat16,
        token=HUGGING_FACE_API_KEY
    )

    input_ids = tokenizer(input_text, return_tensors="pt")

    outputs = model.generate(**input_ids)
    generated_text = tokenizer.decode(outputs[0])
    return generated_text


def main():
    # Call the download and model loading function
    download_model()
    input_text = "Write me a poem about Machine Learning."
    generated_text = load_model_and_generate(input_text)
    print("Generated Text:\n", generated_text)


if __name__ == "__main__":
    main()