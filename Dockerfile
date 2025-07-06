FROM python:3.11
WORKDIR /app
COPY pyproject.toml .
RUN pip install --no-cache-dir poetry && poetry install --no-dev
COPY vectormatch vectormatch
COPY main.py .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]