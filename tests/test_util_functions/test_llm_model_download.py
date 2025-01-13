import os
import pytest
from unittest.mock import patch, MagicMock
from aihao.util_funtions import llm_model_download
import torch

from aihao.util_funtions.llm_model_download import download_model, load_model_and_generate

# Mock environment variables
os.environ["HUGGING_FACE_API_KEY"] = "fake_api_key"

# Mocked input
MOCK_INPUT_TEXT = "Write me a poem about Machine Learning."
MOCK_GENERATED_TEXT = "This is a generated poem about Machine Learning."
FILE_NAMES = [
    "config.json", "gemma-2b-it.gguf", "generation_config.json", "model-00001-of-00002.safetensors",
    "model-00002-of-00002.safetensors",
    "model.safetensors.index.json", "special_tokens_map.json", "tokenizer.json", "tokenizer.model",
    "tokenizer_config.json"
]

@pytest.fixture
def mock_hf_hub_download():
    """
    Mock hf_hub_download function from huggingface_hub.
    """
    with patch("aihao.util_funtions.llm_model_download.hf_hub_download") as mock_download:
        # Simulate returning a different file path for each call
        mock_download.side_effect = [f"/mock/path/{filename}" for filename in FILE_NAMES]
        yield mock_download


@pytest.fixture
def mock_auto_tokenizer():
    """
    Mock AutoTokenizer from transformers.
    """
    with patch.object(llm_model_download.AutoTokenizer, "from_pretrained") as mock_tokenizer:
        yield mock_tokenizer


@pytest.fixture
def mock_auto_model():
    """
    Mock AutoModelForCausalLM from transformers.
    """
    with patch.object(llm_model_download.AutoModelForCausalLM, "from_pretrained") as mock_model:
        yield mock_model


def test_download_model(mock_hf_hub_download):
    """
    Test the download_model function to ensure it handles file downloads correctly.
    """
    # Call the function
    download_model()

    # Assert hf_hub_download is called for each file that doesn't exist
    mock_hf_hub_download.assert_called()
    assert mock_hf_hub_download.call_count == len(FILE_NAMES)


