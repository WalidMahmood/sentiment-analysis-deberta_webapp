# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container
COPY backend/requirements.txt /app/backend/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r backend/requirements.txt

# Copy the rest of the application code
COPY backend /app/backend
COPY frontend /app/frontend
COPY models /app/models

# Set environment variable for model path
ENV MODEL_PATH=/app/models/deberta_base_config3

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run app.py when the container launches
WORKDIR /app/backend
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
