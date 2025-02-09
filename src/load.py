import os
import logging
import SimpleITK as sitk

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def save_processed_data(image, output_folder, filename):
    """
    Save processed image to the output folder.
    """
    try:
        logging.info("Saving processed data...")
        os.makedirs(output_folder, exist_ok=True)
        output_path = os.path.join(output_folder, filename)
        sitk.WriteImage(image, output_path)
        logging.info(f"Processed data saved to {output_path}")

    except Exception as e:
        logging.error(f"Error saving processed data: {e}")
        raise