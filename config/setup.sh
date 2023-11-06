#!/bin/bash

echo "Running setup script"
OS=$(uname -s)

if [ $OS = "Darwin" ]; then
    echo "Detected macOS"
    if python3.10 -c "import sys; sys.exit(sys.version_info < (3, 10))"; then
        python3.10 -m venv ../aihao_venv
        source ../aihao_venv/bin/activate
        pip install -r ../requirements.txt
    else
        echo "AIHAO requires Python >=3.10, but yours is $(python3.10 --version)"
        exit 1
    fi
elif [ $OS = "Linux" ]; then
    echo "Detected Ubuntu"
    if python3.10 -c "import sys; sys.exit(sys.version_info < (3, 10))"; then
        cd /home/ubuntu/aihao-prod
        sudo apt update -y
        sudo apt-get install python3.10-venv
        python3.10 -m venv aihao_venv
        source ./aihao_venv/bin/activate
        pip install -r requirements.txt
    else
        echo "AIHAO requires Python >=3.10, but yours is $(python3.10 --version)"
        exit 1
    fi
else
    echo "Unsupported operating system"
    exit 1
fi