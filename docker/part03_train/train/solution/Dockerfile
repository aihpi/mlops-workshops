# Use the official python image as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy requirements.txt in same directory as the Dockerfile on the host to /app/requirements.txt inside the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt inside the container
RUN pip install --no-cache -r requirements.txt

# Copy files from the same directory as the Dockerfile on the host to the /app directory inside the container (/app/train.py and /app/language_detection.csv)
COPY language_detection.csv .
COPY train.py .

CMD ["python3", "train.py"]
