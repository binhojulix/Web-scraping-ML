FROM python:3.7-alpine
WORKDIR /scrap
COPY ./requirements.txt .
RUN pip install -r requirements.txt
ENV scrap 1
COPY . .
RUN pip install pytest
CMD ["python", "src/app.py"]
