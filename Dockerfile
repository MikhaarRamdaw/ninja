# Use full Python base image (more stable, fewer vulnerabilities)
FROM python:3.11

# Set the working directory
WORKDIR /app

# Copy the requirements file first
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . .

# Expose port for FastAPI
EXPOSE 8000

# Run the FastAPI app using Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
