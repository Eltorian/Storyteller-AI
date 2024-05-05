@echo off

:: Check if Gradio is installed
echo Checking if Gradio is installed
pip show gradio > nul 2>&1
if %errorlevel% neq 0 (
    echo Gradio is not installed, installing it now...
    pip install gradio
)

:: Run app.py
echo Running app.py, Running...
python app.py

pause
