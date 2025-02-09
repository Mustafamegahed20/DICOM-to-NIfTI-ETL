import numpy as np
import logging
import SimpleITK as sitk
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def normalize_image(image):
    """
    Normalize image intensities to [0, 1].
    """
    try:
        logging.info("Normalizing image...")
        array = sitk.GetArrayFromImage(image)
        normalized_array = (array - np.min(array)) / (np.max(array) - np.min(array))
        normalized_image = sitk.GetImageFromArray(normalized_array)
        normalized_image.CopyInformation(image)
        logging.info("Normalization completed.")
        return normalized_image

    except Exception as e:
        logging.error(f"Error normalizing image: {e}")
        raise