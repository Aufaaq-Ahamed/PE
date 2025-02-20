FROM python:3.10-slim

WORKDIR /app

COPY . /app
#pip install --upgrade pip &&
RUN pip install -r requirements.txt

CMD ["python","app2dock.py"]