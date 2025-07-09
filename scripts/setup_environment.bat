@echo off
REM Set up Python virtual environment and install requirements
python -m venv venv
call venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
