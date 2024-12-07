FROM python:3.12-slim

ENV workingdirectory=/hsm
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV HOSTNAMEANDPORT=none

SHELL ["/bin/bash", "-c"]

RUN mkdir -p $workingdirectory

COPY ./HomeStorageManager $workingdirectory
COPY requirements.txt $workingdirectory

WORKDIR $workingdirectory

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000

#RUN python manage.py makemigrations

#RUN python manage.py migrate

CMD ["python", "manage.py", "runserver", "--insecure", "0.0.0.0:8000"]