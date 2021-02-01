FROM python:3.8
WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ./ml_template_api/ .
CMD [ "python", "./main.py" ]