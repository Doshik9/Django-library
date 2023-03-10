# начать сборку с определенного образа
FROM python:3.10

RUN mkdir /usr/src/app

# перенести файлы из одного места в образ
COPY . /usr/src/app

# указание рабочей директории, откуда будут производиться вызовы предыдущих команд
WORKDIR /usr/src/app

# выполнить команду
RUN pip install -r requirements.txt

# "проброс" портов для прослушивания контейнером
EXPOSE 8000