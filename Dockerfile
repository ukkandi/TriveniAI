FROM python:3.11-slim

# Install Tesseract OCR engine
RUN apt-get update && apt-get install -y tesseract-ocr

# Set working directory
WORKDIR /app

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code
COPY . .

# Default command (we’ll run this manually for now)
CMD ["python", "ocr.py"]

