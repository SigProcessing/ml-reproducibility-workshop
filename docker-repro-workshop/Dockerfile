# Use an official Python base image
FROM python:3.7

# Set working directory
WORKDIR /app

# Install specific NumPy version
RUN pip install numpy==1.15

# Copy script into container
COPY docker_script.py .

# Command to run script
CMD ["python", "docker_script.py"]