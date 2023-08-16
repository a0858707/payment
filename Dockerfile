FROM python:latest

WORKDIR /paysystem

COPY . /paysystem

RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--reload"]
