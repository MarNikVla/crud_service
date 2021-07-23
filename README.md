# Тестовое задание на вакансию Python developer

Ссылка на вакансию: https://hh.ru/vacancy/45850841

## Результаты

## Проблемы

## Подготовка рабочего окружения

```bash
$ npm install
```

Для работы приложения необходимо инициализировать базу данных. 

```bash
$ createdb moy-klass-db
```

И загрузить в неё дамб:

```bash
$ psql moy-klass-db < test.sql
```

## Запуск и тестирование

```bash
DATABASE_URL=postgres://localhost:<port>/moy-klass-db npm start
```

### Тестирование



```bash
DATABASE_URL=postgres://localhost:<port>/moy-klass-db npm test
```
