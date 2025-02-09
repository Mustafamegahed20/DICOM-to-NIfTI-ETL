
#  DICOM to NIfTI ETL Pipeline with DVC

![Python](https://img.shields.io/badge/Python-3.9-blue)
![DVC](https://img.shields.io/badge/DVC-2.0-green)
![Docker](https://img.shields.io/badge/Docker-20.10-orange)


## Overview
This project implements an **ETL (Extract, Transform, Load) pipeline** to process DICOM images from the **LUNA16 dataset**, convert them into NIfTI format, apply isotropic resampling (0.5 mm/px spacing), normalize the image intensities, and store the processed data in a structured folder system. The pipeline is containerized using **Docker** and uses **DVC (Data Version Control)** for dataset versioning.

### Pipeline Steps:
1. **Extract**:
   
    1-List .mhd Files: The script lists all .mhd files in the dicom_data/ folder.
   
    2-Read .mhd and .raw Files: For each .mhd file, it reads the associated .raw file using SimpleITK.ReadImage().
   
    3-Store Extracted Data: The extracted image data is stored as a list of tuples (filename, image)
   
3. **Transform**:
   
      1-Resampling:
      
      - The resample_image() function adjusts the image spacing to [0.5, 0.5, 0.5] mm/px.
          
      - It calculates the new image size based on the original spacing and size.
          
      - Uses SimpleITK.Resample() to perform the resampling.
      
      2-NIfTI Conversion:
  
      - The convert_to_nifti() function converts the SimpleITK image to a NIfTI format using nibabel

3. **Normalize**: Intensity Scaling:

   - The pixel values are scaled using the formula:
     
      normalized_array= array−min(array)\max(array)−min(array)
     
   - This ensures all pixel values are in the range [0, 1].

   Copy Metadata:
   
   - The metadata (e.g., spacing, origin, direction) from the original image is copied to the normalized image.

4. **Load**: The processed image is saved as a NIfTI file using SimpleITK.WriteImage().

---

## Setup Instructions

### 1. Install Dependencies
Install the required Python libraries:
```bash
pip install -r requirements.txt
```

### 2. Set Up DVC
1- Initialize DVC
```bash
dvc init
```

2-Configure remote storage
```bash
dvc remote add -d local_storage dvc_storage
```


## Usage Instructions
1. Run the Pipeline
Note >> Download sample from the datasets before running and add it on dicom data folder >> i don't add it bec i was very large to push it 
To run the ETL pipeline:
``` bash
python scripts/run_pipeline.py
```

2. Using Docker
   
Build the Docker image:
``` bash
docker build -t dicom-pipeline .
```

Run the Docker container:
``` bash
docker run -v $(pwd)/dicom_data:/app/dicom_data \
           -v $(pwd)/processed_data:/app/processed_data \
          dicom-pipeline
```
3. Using Docker Compose
 
Run the pipeline with Docker Compose:
``` bash
docker-compose up
```
## Dataset Versioning with DVC
1. Track Data with DVC
Add data to DVC tracking:
```bash
dvc add dicom_data/ processed_data/
```

Commit changes to Git:
```bash
git add dicom_data.dvc processed_data.dvc 
git commit -m "updated data"
```

Push data to remote storage:
```bash
dvc push
```

2. Retrieve a Specific Version
   
List all Git commits:
```bash
git log --oneline
```

Checkout a specific version:

```bash
git checkout <commit_hash>
dvc checkout
```
This will revert the data to the state it was in when it committed at <commit_hash>
