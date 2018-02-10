FROM python:3-slim

ENV APP_DIR=/ewbf-statsd
WORKDIR $APP_DIR

COPY ./requirements.txt $APP_DIR

RUN   pip install -r requirements.txt

COPY . $APP_DIR

ENTRYPOINT ["./main"]