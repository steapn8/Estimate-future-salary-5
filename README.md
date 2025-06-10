# Получение статистики вакансий по языкам программирования с помощью с HeadHunter и SuperJob

Программа получает вакансии с сайтов HeadHunter и SuperJob, получает данные из них и делает таблицы со средним значением зарплаты с помощью AsciiTable.

### Как установить

Python3 должен быть уже установлен. 

Зарегистрируйте приложение на [SuperJob](https://nn.superjob.ru/auth/login/?returnUrl=https%3A%2F%2Fapi.superjob.ru%2Fregister%2F)
Получите его Secret key.

Создайте файл .env и там переменную ID_SJ, именно в нее надо вписывать свой Secret key.
Пример:
```
ID_SJ="v3.h.4897191.g4f83n7h3u3n7ghf38gbgg3f793tg3gf93g4r4g4ygvs3"
```

Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Как запустить

```python table.py```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).