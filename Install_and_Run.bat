@echo off

:: Create a new environment named "gradio-env"
conda create --name gradio-env python=3.9

:: Activate the environment
conda activate gradio-env

:: Install Gradio
pip install gradio

:: Run the app.py file
python app.py

:: Deactivate the environment (optional, but a good practice)
conda deactivate