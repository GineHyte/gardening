#!/bin/bash
# install.sh
# This script automates the setup of your Python project on Linux/macOS.

echo "Starting project setup on Linux/macOS..."

# Ensure python3 is available. If not, exit with an error.
if ! command -v python3 &> /dev/null
then
    echo "Error: python3 is not found. Please install python3 to proceed."
    exit 1
fi

# Step 1: Create a virtual environment using python3
echo "Creating virtual environment 'venv' with python3..."
python3 -m venv venv
if [ $? -ne 0 ]; then
    echo "Error: Failed to create virtual environment. Check python3 installation."
    exit 1
fi
echo "Virtual environment created successfully."

# Step 2: Activate the virtual environment (specifically for fish shell as requested)
echo "Activating virtual environment for fish shell (source ./venv/bin/activate.fish)..."
# Check if activate.fish exists
if [ -f "./venv/bin/activate.fish" ]; then
    # Note: 'source' command activates the venv only in the current shell.
    # To have it active in the current interactive terminal, you'd run this script
    # with `source ./install.sh` or `.` ./install.sh`.
    # For a non-interactive script, simply running the script will not keep the venv active.
    # We include it here for completeness as requested.
    source "./venv/bin/activate.fish"
    echo "Virtual environment activated (for current script execution)."
else
    echo "Warning: activate.fish not found. If you are not using fish shell, you might need to adjust the activation command (e.g., source ./venv/bin/activate for bash/zsh)."
    # We won't exit here, but warn the user.
fi

# Step 3: Install requirements
echo "Installing requirements from requirements.txt..."
pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "Error: Failed to install requirements. Check requirements.txt and your internet connection."
    exit 1
fi
echo "Requirements installed successfully."

# Step 4: Delete installation scripts
echo "Deleting install.sh and install.ps1..."
rm -f "install.sh" "install.ps1"
echo "Installation scripts deleted."

echo "Project setup complete! You can now run 'python -m app'."
