# Use the official python image as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy requirements.txt in same directory as the Dockerfile on the host to /app/requirements.txt inside the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt inside the container
RUN pip install -r requirements.txt

# Copy files from the same directory as the Dockerfile on the host to the /app directory inside the container (/app/api.py)
COPY api.py .
# Copy directories from the same directory as the Dockerfile on the host to the directory in the working directory (/app/models/ and /app/static/) 
# Note: Using 'COPY static .' instead would copy the contents of the static directory to the /app directory!
COPY static static
COPY models models

ENV ROOT_PATH ""

# Run the command to start uvicorn
CMD ["uvicorn", "api:model_api", "--host", "0.0.0.0"]

# Document which port is used for an application in the container 
EXPOSE 8000
