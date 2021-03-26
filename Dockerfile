FROM python:3.8.5

RUN apt-get update && apt-get -y install firefox-esr xvfb python3-pip

COPY ./ ./

RUN pip3 install -r requirements.txt

EXPOSE 80

CMD ["uvicorn", "webservice.main:app", "--host", "0.0.0.0", "--port", "80"]
