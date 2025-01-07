import os
from vosk import Model

# Get the current script directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Define the relative path to the model
model_path = os.path.join(current_dir, "../models/vosk-model-en-us-0.22-lgraph")

# Initialize the model
vosk_model = Model(model_path)
