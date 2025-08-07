# Виправлення API документації KeyCRM

## Коригування webhook-ів

### Webhook endpoints було неправильно

```http
POST /api/keycrm/webhook/order-updated
POST /api/keycrm/webhook/order-created
POST /api/keycrm/webhook/payment-updated
POST /api/keycrm/webhook/buyer-updated
```

### Webhook endpoints стало правильно

```http
POST /api/keycrm/webhook/order-created
POST /api/keycrm/webhook/order-updated
POST /api/keycrm/webhook/order-status-changed
POST /api/keycrm/webhook/payment-created
POST /api/keycrm/webhook/payment-updated
POST /api/keycrm/webhook/buyer-created
POST /api/keycrm/webhook/buyer-updated
```

## Коригування типів подій

### Неправильні назви подій

- order.created
- order.updated
- payment.updated
- buyer.updated

### Правильні назви подій

- order_created
- order_updated
- order_status_changed
- payment_created
- payment_updated
- buyer_created
- buyer_updated

## Оновлені інтерфейси сервісів

```csharp
public interface IWebhookProcessingService
{
    Task ProcessOrderCreatedWebhookAsync(KeyCrmOrderWebhook webhook);
    Task ProcessOrderUpdatedWebhookAsync(KeyCrmOrderWebhook webhook);
    Task ProcessOrderStatusChangedWebhookAsync(KeyCrmOrderWebhook webhook);
    Task ProcessPaymentCreatedWebhookAsync(KeyCrmPaymentWebhook webhook);
    Task ProcessPaymentUpdatedWebhookAsync(KeyCrmPaymentWebhook webhook);
    Task ProcessBuyerCreatedWebhookAsync(KeyCrmBuyerWebhook webhook);
    Task ProcessBuyerUpdatedWebhookAsync(KeyCrmBuyerWebhook webhook);
    Task<bool> ValidateWebhookSignatureAsync(string payload, string signature);
}
```

## Статус виправлень

- ✅ Оновлено keycrm-integration-plan.md
- ✅ Оновлено keycrm-implementation-guide.md
- ✅ Створено keycrm-tz-ukrainian.md
- ✅ Webhook endpoints виправлено
- ✅ Типи подій виправлено
- ✅ Інтерфейси сервісів оновлено

## Примітки

Всі зміни базуються на офіційній документації KeyCRM OpenAPI специфікації, яка була завантажена з `https://keycrm.s3.eu-central-1.amazonaws.com/static/open-api.yml`.
