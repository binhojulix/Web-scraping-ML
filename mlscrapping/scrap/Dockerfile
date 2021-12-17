FROM python:3.7-alpine
WORKDIR /scrap
COPY ./requirements.txt .
RUN apt-get update && \
    apt-get -y install python3-pandas
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ENV scrap 1
COPY . .
CMD ["python", "src/app.py"]

