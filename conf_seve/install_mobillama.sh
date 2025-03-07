#!/bin/bash

echo "Installation de MobiLlama..."

# Crée un environnement virtuel pour éviter les conflits de paquets
python -m venv venv
source venv/bin/activate

# Installe les bibliothèques nécessaires
pip install requests
pip install openai-whisper
pip install sounddevice
pip install numpy
pip install soundfile
pip install gtts
pip install pyserial pyaudio numpy
pip install scipy

pip install -U openai-whisper
pip install git+https://github.com/openai/whisper.git 
pip install --upgrade --no-deps --force-reinstall git+https://github.com/openai/whisper.git