# Технічне завдання: Двостороння інтеграція з KeyCRM

## 1. Загальна інформація

### 1.1 Мета проекту
Реалізувати повну двосторонню інтеграцію між системою управління складом (VMS API) та CRM-системою KeyCRM для автоматичної синхронізації даних про замовлення, клієнтів та товари.

### 1.2 Область застосування
Інтеграція застосовується до наявної системи VMS API (ASP.NET Core 8) з базою даних MSSQL 2019 та зовнішньої CRM-системи KeyCRM через REST API та вебхуки.

### 1.3 Основні бізнес-вимоги
- Автоматична синхронізація замовлень між VMS та KeyCRM
- Двостороння синхронізація даних клієнтів
- Оновлення залишків товарів в реальному часі
- Відстеження статусів платежів та доставки
- Обробка конфліктів даних та помилок синхронізації

## 2. Функціональні вимоги

### 2.1 Вихідна інтеграція (VMS → KeyCRM)

#### 2.1.1 Синхронізація замовлень
**Тригери:**
- Створення нового замовлення у VMS
- Зміна статусу замовлення
- Оновлення інформації про платіж
- Додавання інформації про доставку

**Дії:**
```
- Створити замовлення в KeyCRM при створенні в VMS
- Оновити статус замовлення в KeyCRM при зміні в VMS
- Додати платіж до замовлення в KeyCRM
- Оновити трекінг-інформацію в KeyCRM
```

#### 2.1.2 Синхронізація клієнтів
**Тригери:**
- Реєстрація нового клієнта
- Оновлення контактних даних клієнта
- Зміна сегменту клієнта

**Дії:**
```
- Створити профіль покупця в KeyCRM
- Оновити контактну інформацію в KeyCRM
- Синхронізувати історію замовлень
```

#### 2.1.3 Синхронізація товарів
**Тригери:**
- Зміна кількості товару на складі
- Додавання нового товару
- Оновлення цін

**Дії:**
```
- Оновити кількість пропозицій у KeyCRM
- Створити нові товари/пропозиції в KeyCRM
- Синхронізувати ціни товарів
```

### 2.2 Вхідна інтеграція (KeyCRM → VMS)

#### 2.2.1 Обробка вебхуків
**Події від KeyCRM:**
- order.created - створено замовлення
- order.updated - оновлено замовлення
- payment.updated - оновлено платіж
- buyer.updated - оновлено дані покупця

**Дії у VMS:**
```
- Створити/оновити замовлення в VMS
- Оновити статус платежу в VMS
- Синхронізувати дані клієнта в VMS
```

### 2.3 Сповіщення в реальному часі (опціонально)
- Використання SignalR для push-сповіщень клієнтам
- Сповіщення про зміни статусів замовлень
- Повідомлення про оновлення платежів

## 3. Технічні вимоги

### 3.1 Архітектура системи

#### 3.1.1 Шар сервісів
```csharp
// Інтерфейси сервісів
IKeyCrmService - основний сервіс для роботи з KeyCRM API
IWebhookProcessingService - обробка вхідних вебхуків
IKeyCrmSyncService - управління синхронізацією
INotificationService - сервіс сповіщень
```

#### 3.1.2 Контролери
```csharp
KeyCrmWebhookController - прийом вебхуків від KeyCRM
KeyCrmSyncController - ручна синхронізація та статус
```

#### 3.1.3 Фонові сервіси
```csharp
KeyCrmSyncBackgroundService - періодична синхронізація
```

### 3.2 База даних

#### 3.2.1 Нові таблиці
```sql
-- Мапінг синхронізації між VMS та KeyCRM
KeyCrmSyncMapping:
- Id (int, PK, Identity)
- EntityType (nvarchar(50)) -- 'Order', 'Customer', 'Article'
- VmsEntityId (int) -- ID сутності в VMS
- KeyCrmEntityId (int) -- ID сутності в KeyCRM
- LastSyncDate (datetime2) -- дата останньої синхронізації
- SyncStatus (nvarchar(20)) -- 'Synced', 'Pending', 'Error'
- ErrorMessage (nvarchar(max)) -- повідомлення про помилку
- CreatedAt (datetime2)
- UpdatedAt (datetime2)

-- Лог подій вебхуків
KeyCrmWebhookEvents:
- Id (int, PK, Identity)
- EventType (nvarchar(50)) -- тип події
- PayloadJson (nvarchar(max)) -- JSON payload
- ProcessedAt (datetime2) -- час обробки
- ProcessingStatus (nvarchar(20)) -- 'Pending', 'Processed', 'Error'
- ErrorMessage (nvarchar(max))
- ReceivedAt (datetime2)
```

### 3.3 Конфігурація

#### 3.3.1 appsettings.json
```json
{
  "KeyCRM": {
    "BaseUrl": "https://openapi.keycrm.app/v1",
    "ApiKey": "your-api-key-here",
    "WebhookSecret": "your-webhook-secret",
    "SyncSettings": {
      "EnableRealTimeSync": true,
      "BatchSize": 50,
      "RetryAttempts": 3,
      "SyncIntervalMinutes": 5,
      "MaxConcurrentRequests": 10
    }
  }
}
```

### 3.4 API Endpoints

#### 3.4.1 Вебхуки (вхідні)
```
POST /api/keycrm/webhook/order-created
POST /api/keycrm/webhook/order-updated
POST /api/keycrm/webhook/payment-updated
POST /api/keycrm/webhook/buyer-updated
```

#### 3.4.2 Ручна синхронізація
```
POST /api/keycrm/sync/orders/{orderId}
POST /api/keycrm/sync/customers/{customerId}
POST /api/keycrm/sync/articles/{articleId}
GET /api/keycrm/sync/status
POST /api/keycrm/sync/full-resync
```

#### 3.4.3 SignalR Hub
```
/hubs/keycrm - хаб для real-time сповіщень
```

## 4. Нефункціональні вимоги

### 4.1 Продуктивність
- Час відгуку API < 2 секунд для синхронізації
- Обробка вебхуків < 5 секунд
- Підтримка до 100 одночасних запитів
- Пакетна обробка до 50 записів за раз

### 4.2 Надійність
- Доступність сервісу 99.9%
- Автоматичне відновлення після збоїв
- Механізм повторних спроб (3 спроби з експоненційною затримкою)
- Валідація та перевірка цілісності даних

### 4.3 Безпека
- Використання Bearer Token для автентифікації
- Валідація підписів вебхуків
- Шифрування чутливих даних при передачі
- Обмеження швидкості запитів (rate limiting)
- Аудит всіх операцій синхронізації

### 4.4 Моніторинг та логування
- Структуроване логування всіх операцій
- Метрики продуктивності синхронізації
- Сповіщення про критичні помилки
- Dashboard для відстеження статусу синхронізації

## 5. Технічна реалізація

### 5.1 Етап 1: Базова інфраструктура (1-2 тижні)

#### 5.1.1 Файли для створення:
```
/Services/IKeyCrmService.cs
/Services/KeyCrmService.cs
/Services/IWebhookProcessingService.cs
/Services/WebhookProcessingService.cs
/DTOs/KeyCrmDtos.cs
/Models/KeyCrmWebhook.cs
/Controllers/KeyCrmWebhookController.cs
```

#### 5.1.2 Реєстрація сервісів у Program.cs:
```csharp
// HTTP клієнт для KeyCRM
builder.Services.AddHttpClient<IKeyCrmService, KeyCrmService>(client =>
{
    client.BaseAddress = new Uri(builder.Configuration["KeyCRM:BaseUrl"]);
    client.DefaultRequestHeaders.Add("Authorization",
        $"Bearer {builder.Configuration["KeyCRM:ApiKey"]}");
    client.Timeout = TimeSpan.FromSeconds(30);
});

// Сервіси синхронізації
builder.Services.AddScoped<IKeyCrmService, KeyCrmService>();
builder.Services.AddScoped<IWebhookProcessingService, WebhookProcessingService>();
builder.Services.AddScoped<IKeyCrmSyncService, KeyCrmSyncService>();
```

### 5.2 Етап 2: Основна синхронізація (3-4 тижні)

#### 5.2.1 Синхронізація замовлень
```csharp
// У OrderService додати виклики KeyCRM
public async Task<Order> CreateOrderAsync(CreateOrderDto orderDto)
{
    var order = await _baseCreateOrder(orderDto);

    // Синхронізація з KeyCRM
    await _keyCrmService.CreateOrderAsync(order);

    return order;
}
```

#### 5.2.2 Обробка вебхуків
```csharp
[HttpPost("webhook/order-updated")]
public async Task<IActionResult> HandleOrderUpdated([FromBody] KeyCrmOrderWebhook webhook)
{
    await _webhookProcessor.ProcessOrderUpdateAsync(webhook);
    return Ok();
}
```

### 5.3 Етап 3: Розширені функції (5-6 тижні)

#### 5.3.1 SignalR для real-time оновлень
```csharp
// У WebhookProcessingService
public async Task ProcessOrderUpdateAsync(KeyCrmOrderWebhook webhook)
{
    // Оновити замовлення в базі
    await UpdateOrderFromKeycrm(webhook);

    // Надіслати real-time сповіщення
    await _hubContext.Clients.All.SendAsync("OrderUpdated", webhook.OrderId);
}
```

#### 5.3.2 Вирішення конфліктів
```csharp
public async Task<ConflictResolution> ResolveDataConflictAsync(
    int entityId, string entityType)
{
    // Порівняти timestamps
    // Застосувати стратегію вирішення конфліктів
    // Зберегти результат в аудит-лог
}
```

## 6. Тестування

### 6.1 Unit тести
- Тестування логіки синхронізації
- Мокування KeyCRM API викликів
- Валідація обробки помилок

### 6.2 Інтеграційні тести
- End-to-end тестування синхронізації
- Тестування вебхуків з реальними payload
- Навантажувальне тестування

### 6.3 Ручне тестування
- Перевірка UI для статусу синхронізації
- Тестування сценаріїв відновлення після збоїв
- Валідація real-time сповіщень

## 7. Розгортання

### 7.1 Підготовка середовища
- Налаштування KeyCRM API ключів
- Створення webhook endpoints у KeyCRM
- Налаштування сертифікатів для HTTPS

### 7.2 Міграція бази даних
```sql
-- Створити нові таблиці
-- Додати індекси для продуктивності
-- Налаштувати права доступу
```

### 7.3 Поетапне розгортання
1. Розгортання в тестовому середовищі
2. Тестування з обмеженим набором даних
3. Поступове увімкнення функцій
4. Повне розгортання в продакшн

## 8. Моніторинг та підтримка

### 8.1 Метрики для відстеження
- Кількість успішних/неуспішних синхронізацій
- Час відгуку KeyCRM API
- Кількість необроблених вебхуків
- Розмір черги синхронізації

### 8.2 Алерти
- Критичні помилки синхронізації
- Недоступність KeyCRM API
- Перевищення часу обробки
- Переповнення черги помилок

### 8.3 Регулярне обслуговування
- Очищення старих логів (90 днів)
- Оптимізація індексів бази даних
- Оновлення API ключів
- Аналіз продуктивності

## 9. Ризики та мітигація

### 9.1 Технічні ризики
| Ризик | Імовірність | Вплив | Мітигація |
|-------|-------------|-------|-----------|
| Недоступність KeyCRM API | Середня | Високий | Черга повторних спроб, fallback режим |
| Конфлікти даних | Висока | Середній | Timestamp-based resolution, ручне вирішення |
| Перевантаження системи | Низька | Високий | Rate limiting, асинхронна обробка |

### 9.2 Бізнес ризики
| Ризик | Імовірність | Вплив | Мітигація |
|-------|-------------|-------|-----------|
| Втрата даних при синхронізації | Низька | Критичний | Валідація, аудит, backup |
| Неприйняття користувачами | Середня | Середній | Навчання, поступове впровадження |
| Збільшення часу обробки | Середня | Низький | Оптимізація, кешування |

## 10. Критерії готовності

### 10.1 Функціональні критерії
- ✅ Успішна синхронізація всіх типів сутностей
- ✅ Обробка всіх типів вебхуків
- ✅ Функціонування conflict resolution
- ✅ Real-time сповіщення працюють

### 10.2 Технічні критерії
- ✅ Покриття unit тестами > 80%
- ✅ Пройдені всі інтеграційні тести
- ✅ Документація завершена
- ✅ Налаштований моніторинг

### 10.3 Критерії продуктивності
- ✅ Час синхронізації < 5 секунд
- ✅ Успішність обробки > 99%
- ✅ Час відгуку API < 2 секунд
- ✅ Немає втрат даних

## 11. Графік виконання

| Етап | Тривалість | Відповідальний | Результат |
|------|------------|----------------|-----------|
| Аналіз та проектування | 3 дні | Tech Lead | Технічний дизайн |
| Етап 1: Інфраструктура | 10 днів | Backend Developer | Базові сервіси |
| Етап 2: Основна синхронізація | 10 днів | Backend Developer | CRUD синхронізація |
| Етап 3: Розширені функції | 10 днів | Backend Developer | Real-time, конфлікти |
| Тестування | 5 днів | QA Engineer | Тест-звіти |
| Розгортання | 3 дні | DevOps Engineer | Продакшн |
| **Загальна тривалість** | **41 день (~8 тижнів)** | | **Готова інтеграція** |

## 12. Бюджет та ресурси

### 12.1 Людські ресурси
- Tech Lead: 40 годин (аналіз, архітектура, код-рев'ю)
- Backend Developer: 200 годин (основна розробка)
- QA Engineer: 60 годин (тестування)
- DevOps Engineer: 20 годин (розгортання)

### 12.2 Інфраструктурні витрати
- KeyCRM API ліміти: ~$100/місяць
- Додаткові серверні ресурси: ~$50/місяць
- Моніторинг та логування: ~$30/місяць

## 13. Успішність проекту

### 13.1 KPI
- Скорочення ручного введення даних на 90%
- Час синхронізації замовлень < 30 секунд
- Зменшення помилок даних на 80%
- Покращення задоволеності користувачів на 25%

### 13.2 ROI
- Економія часу персоналу: 10 годин/тиждень
- Зменшення помилок: економія $500/місяць
- Покращення customer experience: збільшення retention на 5%

---

**Документ підготовлено:** 07.08.2025
**Версія:** 1.0
**Статус:** На затвердження