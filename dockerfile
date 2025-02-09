# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . .



# Create the input and output directories
RUN mkdir -p ${INPUT_FOLDER} ${OUTPUT_FOLDER}

# Run the pipeline when the container starts
CMD ["python", "scripts/run_pipeline.py"]