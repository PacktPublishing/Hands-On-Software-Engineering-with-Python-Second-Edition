# Start with an image that provides a bare-bones
# Python installation.
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy the source code and related resources
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Expose port for FastAPI
EXPOSE 5000

# Run FastAPI app with uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "5000"]
