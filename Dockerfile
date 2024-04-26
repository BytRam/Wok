FROM python:3.8-slim
LABEL authors="22011557"

WORKDIR /app

COPY req.txt .
COPY WoReader.py .
COPY random_paragraphs.txt .


RUN pip install --no-cache-dir -r req.text
RUN python -m spacy download en_core_web_sm

CMD ["python", "WoReader.py"]
