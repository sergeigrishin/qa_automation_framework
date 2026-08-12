# API Test Cases

## API-001 — Получение списка продуктов

**Шаги:**
1. Выполнить GET запрос на эндпоинт https://automationexercise.com/api/productsList

**Ожидаемый результат:**
Код ответа: 200
Products существует и содержит хотя бы один элемент.
Каждый product содержит основные поля: 
- id 
- name 
- price
- category
- brand 


## API-002 — Поиск товара

**Тестовые данные:**
"search_product": "Blue Top"

**Шаги:**
1. Выполнить POST запрос на эндпоинт https://automationexercise.com/api/searchProduct c указанием товара "Blue Top"

**Ожидаемый результат:**
Код ответа: 200
Products существует и содержит хотя бы один элемент.
В результатах поиска присутствует товар с name: "Blue Top"


## API-003 — Поиск несуществующего товара

**Тестовые данные:**
"search_product": "qwerty_nonexistent"

**Шаги:**
1. Выполнить POST запрос на эндпоинт https://automationexercise.com/api/searchProduct c указанием несуществующего товара "qwerty_nonexistent"

**Ожидаемый результат:**
код ответа: 200, 
Products содержит пустой список.


## API-004 — Неподдерживаемый HTTP-метод

**Тестовые данные:**
GET /api/searchProduct

**Шаги:**
1. Выполнить GET-запрос на /api/searchProduct

**Ожидаемый результат:**
Код ответа: 405
message: "This request method is not supported."




