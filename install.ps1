# install.ps1
# This script automates the setup of your Python project on Windows.

Write-Host "Starting project setup on Windows..."

# Step 1: Create a virtual environment
Write-Host "Creating virtual environment 'venv'..."
try {
    python -m venv venv
    Write-Host "Virtual environment created successfully."
} catch {
    Write-Error "Failed to create virtual environment. Ensure Python is installed and in your PATH."
    exit 1
}

# Step 2: Activate the virtual environment
Write-Host "Activating virtual environment..."
# Check if the activation script exists
if (Test-Path ".\venv\Scripts\Activate.ps1") {
    # Source the activation script to activate the venv in the current session
    . ".\venv\Scripts\Activate.ps1"
    Write-Host "Virtual environment activated."
} else {
    Write-Error "Activation script not found. Make sure 'venv' was created correctly."
    exit 1
}

# Step 3: Install requirements
Write-Host "Installing requirements from requirements.txt..."
try {
    pip install -r requirements.txt
    Write-Host "Requirements installed successfully."
} catch {
    Write-Error "Failed to install requirements. Check requirements.txt and your internet connection."
    exit 1
}

# Step 4: Delete installation scripts
Write-Host "Deleting install.ps1 and install.sh..."
try {
    Remove-Item "install.ps1" -ErrorAction SilentlyContinue
    Remove-Item "install.sh" -ErrorAction SilentlyContinue
    Write-Host "Installation scripts deleted."
} catch {
    Write-Error "Could not delete installation scripts. Please remove them manually."
}

Write-Host "Project setup complete! You can now run 'python -m app'."

# Keep the virtual environment active in the current PowerShell session