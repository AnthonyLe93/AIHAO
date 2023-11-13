#!/bin/bash

echo "Running setup script"
OS=$(uname -s)

if [ $OS = "Darwin" ]; then
    echo "Detected macOS"
    if python3.10 -c "import sys; sys.exit(sys.version_info < (3, 10))"; then
        python3.10 -m venv ../aihao_venv
        source ../aihao_venv/bin/activate
        brew install portaudio
        pip install -r ../requirements.txt
    else
        echo "AIHAO requires Python >=3.10, but yours is $(python3.10 --version)"
        exit 1
    fi
else
    echo "Unsupported operating system"
    exit 1
fi