#!/bin/bash



# Install DVC 
pip install dvc

# Initialize DVC
git init

# Initialize DVC
dvc init --no-scm  # Use --no-scm if you don't want DVC to use Git

# Track DVC metadata with Git
git add .dvc .gitignore
git commit -m "Initialize DVC"


# Add remote storage 
dvc remote add -d myremote /dvc_storage

# Add data to DVC
dvc add /dicom_data/
dvc add /processed_data/

# Track DVC data metadata in Git
git add /dicom_data.dvc /processed_data.dvc .gitignore
git commit -m "Track dataset with DVC"


# Commit changes to DVC
dvc commit

# Push data to remote storage
dvc push

git push origin main  

echo "DVC and Git setup completed successfully."

