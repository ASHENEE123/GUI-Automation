# How to Run

## Step 1: Clone the Repo
Using the command `git clone <repository-url>`, you make a local copy of the repository. This is crucial for making your own changes or contributing to the project safely.

## Step 2: Create a Virtual Environment
Run the command `python -m venv create` to create a virtual environment. This isolates your Python dependencies from your system Python installation, reducing the risk of conflicting packages and ensuring a secure execution environment.

## Step 3: Activate the Virtual Environment
For Windows users, use the command `create/Scripts/activate` to activate the virtual environment. This means your terminal will use the installed packages in that specific virtual environment instead of globally installed packages, which is key for security and project dependency management.

## Step 4: Install Dependencies
Run `pip install -r requirements.txt` to install the necessary libraries specified in the `requirements.txt` file. This command ensures that you have the exact versions of packages needed, minimizing vulnerabilities that arise from using outdated or incompatible libraries.

## Step 5: Run the Application
Execute the file using `python gui.py`. This launches the application, allowing you to use it as intended. Running through a virtual environment ensures that only allowed dependencies and scripts run, enhancing your security posture.

Keep the rest of the README content the same.