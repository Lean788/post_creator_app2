FROM python:3.9.16-alpine
WORKDIR /src
COPY ./src .
RUN apk add --no-cache mariadb-connector-c-dev build-base && \
    pip install -r requirements.txt && \
    apk del build-base
EXPOSE 5000
CMD ["python", "application.py"]
