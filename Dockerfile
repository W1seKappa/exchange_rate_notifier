FROM python:3.9-slim

# Установим tzdata и настроим зону
RUN apt-get update && \
    apt-get install -y tzdata && \
    ln -snf /usr/share/zoneinfo/Europe/Moscow /etc/localtime && \
    echo "Europe/Moscow" > /etc/timezone && \
    dpkg-reconfigure -f noninteractive tzdata

# Дальше как обычно
COPY src/ .
COPY config/ .
RUN pip install --no-cache-dir requests telebot toml apscheduler bs4

ENV TZ=Europe/Moscow

CMD ["python", "main.py"]