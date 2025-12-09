# Use a lightweight Python base image
FROM python:3.10-slim


WORKDIR /app


RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*


COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 3. Copy the rest of your application code
COPY . .

# 4. Create the folder for generated PDFs and set permissions
RUN mkdir -p generated


RUN adduser --disabled-password --gecos '' appuser
RUN chown -R appuser:appuser /app
USER appuser


EXPOSE 5000

CMD ["gunicorn", "--workers=4", "--bind", "0.0.0.0:5000", "--timeout", "120", "app:app"]