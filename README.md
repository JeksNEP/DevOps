# VSEMAIKY

![Python](https://img.shields.io/badge/Python_3.10-blue?logo=python&logoColor=yellow)
![SQLite](https://img.shields.io/badge/SQLite-purple?logo=SQLite&logoColor=blue)
![Docker](https://img.shields.io/badge/Docker-grey?logo=Docker&logoColor=blue)
![DockerCompose](https://img.shields.io/badge/DockerCompose-blue)
![Static Badge](https://img.shields.io/badge/FastAPI-black?logo=FastAPI)







Данный парсер предназначен для сбора информации о товарах, отсортированных по мужским новинкам, на сайте одежды ВсеМайки. Это позволит пользователю быстро посмотреть какие вещи он может купить на данном сайте.



###### Информация, которая будет парситься с этого сайта:
- Название товара
- Тип товара
- Описание товара
- Ссылка на фото товара
- Цена товара
- Ссылка на товар


###### Структура проекта
    │
    ├── backend 
    │   └── app.py
    │
    ├── database
    │   └── db.py
    │
    ├── main.py
    └── parser.py



### Установка и настройка
###### Клонируем репозиторий:
    git clone https://github.com/JeksNEP/DevOps.git

###### Переходим в директорию проекта 
    cd DevOps

###### Сборка и запуск контейнеров Docker
    docker-compose up --build


### Ссылка, с которой работает парсер:
    https://www.vsemayki.ru/catalog/view/manwear?sort=new
