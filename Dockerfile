FROM python:3.9-slim

WORKDIR /app

COPY server.py /app/
COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

ENV FLASK_APP=server.py

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]
