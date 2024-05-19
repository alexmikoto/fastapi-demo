FROM python:3.10

WORKDIR /usr/src/app

COPY dist/demo-0.0.1.tar.gz ./
RUN pip install demo-0.0.1.tar.gz

CMD [ "fastapi run demo" ]
