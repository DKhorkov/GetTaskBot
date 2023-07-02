FROM python:3
LABEL authors="dkhorkov"

WORKDIR /app

COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app
RUN mkdir ./src/database

CMD [ "python", "src/main.py" ]
