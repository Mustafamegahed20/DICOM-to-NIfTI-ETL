# ETL Pipeline for DICOM to NIfTI Conversion: Summary Report

## Tools and Libraries Used
- **Python Libraries**:
  - `pydicom`: Reading DICOM metadata.
  - `SimpleITK`: Handling medical images, resampling, and saving NIfTI files.
  - `nibabel`: Converting and saving images in NIfTI format.
  - `numpy`: Numerical operations and intensity normalization.
  - `scikit-image`: Advanced image processing (if needed).
  - `logging`: Logging pipeline progress and errors.
  - `os`: File and folder operations.
- **Data Versioning**: DVC (Data Version Control) for tracking dataset versions.
- **Containerization**: Docker for portability and reproducibility.
- **Dataset**: LUNA16 Dataset (lung CT scans in `.mhd` and `.raw` formats).


## Future Improvements

1. **Parallel Processing**:
   - Implement parallel processing to handle large datasets more efficiently.

3. **Cloud Storage Integration**:
   - Configure DVC to use cloud storage (e.g., AWS S3, Google Cloud Storage).

4. **Automated Testing**:
   - Add unit tests and integration tests for pipeline reliability.

5. **integrate with airflow and pyspark**
