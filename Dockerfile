FROM python:3.12-slim

ENV workingdirectory=/docker/app/webapp

RUN mkdir -p $workingdirectory

WORKDIR $workingdirectory

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV HOSTNAMEANDPORT=none

RUN pip install --upgrade pip

COPY ./HomeStorageManager $workingdirectory
COPY requirements.txt $workingdirectory

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]