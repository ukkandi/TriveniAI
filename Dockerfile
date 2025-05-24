# 1. Start from Python 3.11 slim
FROM python:3.11-slim

# 2. Install Tesseract for OCR
RUN apt-get update && apt-get install -y tesseract-ocr

# 3. Create and set /app as our working directory
WORKDIR /app

# 4. Copy only the requirements for the OCR module and install them
COPY ocr/requirements.txt ./ocr/requirements.txt
RUN pip install --no-cache-dir -r ocr/requirements.txt

# 5. Copy the rest of your project into /app
COPY . .

# 6. Default command: run the OCR script from inside the ocr folder
CMD ["python", "ocr/ocr.py"]

