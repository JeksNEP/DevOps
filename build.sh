#!/bin/bash

# Сборка Docker-образа
docker-compose build

# Запуск сервисов
docker-compose up -d

echo "Всё робит http://127.0.0.1:5000"

# Отслеживание журналов
docker-compose logs -f