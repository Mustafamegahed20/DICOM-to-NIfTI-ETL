import os
import SimpleITK as sitk
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def extract_dicom_data(input_folder):
    """
    Extract DICOM data from .mhd and .raw files.
    """
    try:
        logging.info("Extracting DICOM data...")
        mhd_files = [f for f in os.listdir(input_folder) if f.endswith(".mhd")]
        extracted_data = []

        for mhd_file in mhd_files:
            mhd_path = os.path.join(input_folder, mhd_file)
            raw_file = get_raw_file_from_mhd(mhd_path)
            raw_path = os.path.join(input_folder, raw_file)

            # Read the image using SimpleITK
            image = sitk.ReadImage(mhd_path)
            extracted_data.append((mhd_file, image))

        logging.info(f"Extracted {len(extracted_data)} DICOM files.")
        return extracted_data

    except Exception as e:
        logging.error(f"Error extracting DICOM data: {e}")
        raise

def get_raw_file_from_mhd(mhd_path):
    """
    Extract the name of the .raw file from the .mhd file.
    """
    try:
        with open(mhd_path, "r") as f:
            for line in f:
                if line.startswith("ElementDataFile"):
                    return line.split("=")[1].strip()
        raise ValueError(f"No .raw file associated with {mhd_path}")
    except Exception as e:
        logging.error(f"Error reading .mhd file: {e}")
        raise