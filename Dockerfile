FROM python:3.8

WORKDIR /

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD [ "uvicorn", "main:app", "--port", "5000", "--host", "0.0.0.0" ]
