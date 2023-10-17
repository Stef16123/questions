# Question service
Данный сервис получает на вход колличество вопросов, обращается к стороннему сервису для получения случайных вопросов в заданном колличестве, сохраняет их у себя в БД и возвращает клиенту.

Стэк:
 - FastApi
 - SQLalchemy
 - Postgres

Инструкция для запуска:
1. скопировать.env.dist и переименовать в .env
2. запустить команду docker-compose up --build


Пример Post-запроса к /questions/ :
Request:
```
{
  "questions_num": 3
}
```
Response
```
{
  "list": [
    {
      "id": 19766,
      "question": "Its state domestic animal is the dairy cow",
      "answer": "Wisconsin",
      "created_at": "2022-12-30T18:45:43.640000+00:00"
    },
    {
      "id": 177952,
      "question": "In 1968 Tim Rice wrote the lyrics & this man, the music for \"Joseph and the Amazing Technicolor Dreamcoat\"",
      "answer": "Andrew Lloyd Webber",
      "created_at": "2022-12-30T21:15:16.751000+00:00"
    },
    {
      "id": 209836,
      "question": "Whether on tops or dresses, puff these were one of Elle's \"9 Trends Dominating 2020\"",
      "answer": "sleeves",
      "created_at": "2022-12-30T21:58:24.070000+00:00"
    }
  ]
}

```
