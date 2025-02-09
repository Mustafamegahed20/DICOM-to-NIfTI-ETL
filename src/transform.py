import SimpleITK as sitk
import nibabel as nib
import numpy as np
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def convert_to_nifti(image, output_path):
    """
    Convert SimpleITK image to NIfTI format and save.
    """
    try:
        logging.info("Converting to NIfTI...")
        array = sitk.GetArrayFromImage(image)
        affine = np.eye(4)
        nifti_image = nib.Nifti1Image(array, affine)
        nib.save(nifti_image, output_path)
        logging.info(f"NIfTI file saved to {output_path}")

    except Exception as e:
        logging.error(f"Error converting to NIfTI: {e}")
        raise

def resample_image(image, new_spacing=[0.5, 0.5, 0.5]):
    """
    Resample image to isotropic spacing.
    """
    try:
        logging.info("Resampling image...")
        original_spacing = image.GetSpacing()
        original_size = image.GetSize()

        new_size = [
            int(round(osz * ospc / nspc))
            for osz, ospc, nspc in zip(original_size, original_spacing, new_spacing)
        ]

        resampled_image = sitk.Resample(
            image,
            new_size,
            sitk.Transform(),
            sitk.sitkLinear,
            image.GetOrigin(),
            new_spacing,
            image.GetDirection(),
            0,
            image.GetPixelID(),
        )

        logging.info("Resampling completed.")
        return resampled_image

    except Exception as e:
        logging.error(f"Error resampling image: {e}")
        raise