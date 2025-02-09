import sys
import os
import nibabel as nib  

# Add the project root directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))



import os
from src.extract import extract_dicom_data
from src.transform import convert_to_nifti, resample_image
from src.normalize import normalize_image
from src.load import save_processed_data

def run_pipeline(input_folder, output_folder):
    """
    Run the ETL pipeline.
    """
    try:
        # Extract
        dicom_data = extract_dicom_data(input_folder)

        for filename, image in dicom_data:
            # Transform
            resampled_image = resample_image(image)
            normalized_image = normalize_image(resampled_image)

            # Load
            output_filename = filename.replace(".mhd", ".nii.gz")
            save_processed_data(normalized_image, output_folder, output_filename)

    except Exception as e:
        print(f"Pipeline failed: {e}")

if __name__ == "__main__":
    input_folder = "dicom_data"
    output_folder = "processed_data"
    run_pipeline(input_folder, output_folder)