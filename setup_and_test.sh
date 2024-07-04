#!/bin/bash

# Set up and activate the virtual environment
python -m venv venv       # Create a new virtual environment named 'venv'
source venv/bin/activate  # Activate the virtual environment

# Install dependencies
pip install -r requirements1.txt  # Install Python dependencies listed in 'requirements.txt'

# Run tests
pytest  # Run tests using pytest

# Deactivate the virtual environment
deactivate  # Deactivate the virtual environment to return to the system Python
