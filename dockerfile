FROM python:3.9-slim

WORKDIR /app


# Install system dependencies (git, curl, etc.)
RUN apt-get update && apt-get install -y git curl \
    && rm -rf /var/lib/apt/lists/*


# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy scripts and data
COPY . .

ENV PYTHONPATH="/app:${PYTHONPATH}"

# Make dvc_setup.sh executable
RUN chmod +x scripts/dvc_setup.sh
RUN chmod +x scripts/run_pipeline.py

# Run the DVC setup script
CMD ["python", "scripts/run_pipeline.py"]

