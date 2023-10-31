FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

WORKDIR /project
COPY . /project
COPY requirements.txt .
COPY main.py .
COPY appconfig.py .

RUN mkdir -p /project/logs
RUN chmod 777 /project/logs*

RUN mkdir -p /project/server
RUN chmod 777 /project/server*

COPY server/* /project/server

RUN python3 -m pip install --upgrade pip
RUN pip3 install -r requirements.txt

EXPOSE 5000
CMD ["python3", "/project/main.py"]