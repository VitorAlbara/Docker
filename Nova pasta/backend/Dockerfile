FROM python:3.9
WORKDIR /APP
COPY main.py .
RUN python -m pip install "fastapi[standard]"
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]