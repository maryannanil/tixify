# 🐍 Use official Python image
FROM python:3.11-slim

# 🏠 Set working directory
WORKDIR /app

# 📦 Copy your project files into the container
COPY . .

# 🔥 Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 🚀 Run the FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
