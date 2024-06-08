![example workflow](https://github.com/github/docs/actions/workflows/lining_and_type_checking.yml/badge.svg)

# IdeaBox Frontend

Фронтенд для проекта IdeaBox

## Локальный запуск

1. Сборка образа

```commandline
docker build . -t ideabox_frontend 
```

2. Запуск контейнера. Вместо `<host_port>` укажите порт на хосте

```commandline
docker run --rm -d -p <host_port>:8000 eytes/ideabox_frontend
```

3. Перейдите в браузере на `http://localhost:<host_port>/`