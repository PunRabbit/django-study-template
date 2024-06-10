# Builder stage
FROM python:3.10 AS builder

ENV TZ Asia/Seoul

WORKDIR /src

RUN apt-get update && apt-get install -y \
    gcc \
    libmariadb-dev \
    && apt-get clean

COPY ./req.txt .
RUN pip install --no-cache-dir -r req.txt

COPY ./ ./

# wait-for-it 스크립트 추가
ADD https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh


# Final stage
FROM python:3.10-slim

ENV TZ Asia/Seoul
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y \
    gcc \
    libmariadb-dev \
    && apt-get clean

WORKDIR /src

COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin
COPY --from=builder /src /src
COPY --from=builder /wait-for-it.sh /wait-for-it.sh

ARG COMMAND
ENV COMMAND $COMMAND

ENTRYPOINT ["sh", "-c", "${COMMAND}"]

#CMD ["/wait-for-it.sh", "toss-mariadb:3306", "--timeout=60", "--strict", "--", "python", "manager.py", "runserver"]