FROM python:3.10-slim

# basic env
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# install dependencies dulu (cache friendly)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy source code
COPY . .

# healthcheck
HEALTHCHECK --interval=30s --timeout=5s --retries=3 \
  CMD python healthcheck.py || exit 1

CMD ["python", "main.py"]
