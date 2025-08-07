# KeyCRM Integration Implementation Guide

## Service Layer Implementation

### 1. KeyCRM Service Interface

Create the main service interface for KeyCRM operations:

```csharp
// Services/IKeyCrmService.cs
using VmsApi.DTOs;

namespace VmsApi.Services
{
    public interface IKeyCrmService
    {
        // Order Management
        Task<KeyCrmOrderResponse> CreateOrderAsync(KeyCrmOrderRequest order);
        Task<KeyCrmOrderResponse> UpdateOrderAsync(int orderId, KeyCrmOrderUpdateRequest order);
        Task<KeyCrmOrderResponse> GetOrderAsync(int orderId);
        Task<PagedResponse<KeyCrmOrderResponse>> GetOrdersAsync(KeyCrmOrderFilter filter);

        // Payment Management
        Task<KeyCrmPaymentResponse> AddPaymentAsync(int orderId, KeyCrmPaymentRequest payment);
        Task<KeyCrmPaymentResponse> UpdatePaymentAsync(int orderId, int paymentId, KeyCrmPaymentUpdateRequest payment);

        // Buyer Management
        Task<KeyCrmBuyerResponse> CreateBuyerAsync(KeyCrmBuyerRequest buyer);
        Task<KeyCrmBuyerResponse> UpdateBuyerAsync(int buyerId, KeyCrmBuyerUpdateRequest buyer);
        Task<KeyCrmBuyerResponse> GetBuyerAsync(int buyerId);
        Task<PagedResponse<KeyCrmBuyerResponse>> GetBuyersAsync(KeyCrmBuyerFilter filter);

        // Product Management
        Task<KeyCrmProductResponse> CreateProductAsync(KeyCrmProductRequest product);
        Task<KeyCrmProductResponse> UpdateProductAsync(int productId, KeyCrmProductUpdateRequest product);
        Task<KeyCrmOfferResponse> UpdateOfferStockAsync(int offerId, KeyCrmStockUpdateRequest stock);

        // Reference Data
        Task<List<KeyCrmStatus>> GetOrderStatusesAsync();
        Task<List<KeyCrmSource>> GetOrderSourcesAsync();
        Task<List<KeyCrmPaymentMethod>> GetPaymentMethodsAsync();
    }
}
```

### 2. KeyCRM Service Implementation

```csharp
// Services/KeyCrmService.cs
using System.Net.Http.Json;
using System.Text.Json;
using VmsApi.DTOs;

namespace VmsApi.Services
{
    public class KeyCrmService : IKeyCrmService
    {
        private readonly HttpClient _httpClient;
        private readonly ILogger<KeyCrmService> _logger;
        private readonly JsonSerializerOptions _jsonOptions;

        public KeyCrmService(HttpClient httpClient, ILogger<KeyCrmService> logger)
        {
            _httpClient = httpClient;
            _logger = logger;
            _jsonOptions = new JsonSerializerOptions
            {
                PropertyNamingPolicy = JsonNamingPolicy.SnakeCaseLower,
                WriteIndented = false
            };
        }

        public async Task<KeyCrmOrderResponse> CreateOrderAsync(KeyCrmOrderRequest order)
        {
            try
            {
                var response = await _httpClient.PostAsJsonAsync("order", order, _jsonOptions);
                response.EnsureSuccessStatusCode();

                var result = await response.Content.ReadFromJsonAsync<KeyCrmOrderResponse>(_jsonOptions);
                _logger.LogInformation("Created order in KeyCRM with ID: {OrderId}", result?.Id);

                return result;
            }
            catch (HttpRequestException ex)
            {
                _logger.LogError(ex, "Failed to create order in KeyCRM: {Error}", ex.Message);
                throw new KeyCrmApiException("Failed to create order in KeyCRM", ex);
            }
        }

        public async Task<KeyCrmOrderResponse> UpdateOrderAsync(int orderId, KeyCrmOrderUpdateRequest order)
        {
            try
            {
                var response = await _httpClient.PutAsJsonAsync($"order/{orderId}", order, _jsonOptions);
                response.EnsureSuccessStatusCode();

                var result = await response.Content.ReadFromJsonAsync<KeyCrmOrderResponse>(_jsonOptions);
                _logger.LogInformation("Updated order in KeyCRM with ID: {OrderId}", orderId);

                return result;
            }
            catch (HttpRequestException ex)
            {
                _logger.LogError(ex, "Failed to update order {OrderId} in KeyCRM: {Error}", orderId, ex.Message);
                throw new KeyCrmApiException($"Failed to update order {orderId} in KeyCRM", ex);
            }
        }

        // Additional methods following the same pattern...
    }
}
```

### 3. Webhook Processing Service

```csharp
// Services/IWebhookProcessingService.cs
namespace VmsApi.Services
{
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
}

// Services/WebhookProcessingService.cs
using System.Security.Cryptography;
using System.Text;

namespace VmsApi.Services
{
    public class WebhookProcessingService : IWebhookProcessingService
    {
        private readonly IOrderService _orderService;
        private readonly ICustomerService _customerService;
        private readonly IKeyCrmSyncService _syncService;
        private readonly IConfiguration _configuration;
        private readonly ILogger<WebhookProcessingService> _logger;

        public WebhookProcessingService(
            IOrderService orderService,
            ICustomerService customerService,
            IKeyCrmSyncService syncService,
            IConfiguration configuration,
            ILogger<WebhookProcessingService> logger)
        {
            _orderService = orderService;
            _customerService = customerService;
            _syncService = syncService;
            _configuration = configuration;
            _logger = logger;
        }

        public async Task ProcessOrderWebhookAsync(KeyCrmOrderWebhook webhook)
        {
            try
            {
                var mapping = await _syncService.GetSyncMappingAsync("Order", webhook.Id);
                if (mapping == null)
                {
                    _logger.LogWarning("No sync mapping found for KeyCRM order {OrderId}", webhook.Id);
                    return;
                }

                var vmsOrder = await _orderService.GetOrderByIdAsync(mapping.VmsEntityId);
                if (vmsOrder == null)
                {
                    _logger.LogWarning("VMS order {OrderId} not found for KeyCRM order {KeyCrmOrderId}",
                        mapping.VmsEntityId, webhook.Id);
                    return;
                }

                // Update VMS order based on webhook data
                var updateRequest = MapKeyCrmOrderToVmsOrder(webhook, vmsOrder);
                await _orderService.UpdateOrderAsync(vmsOrder.OrderID, updateRequest);

                // Update sync mapping
                await _syncService.UpdateSyncMappingAsync(mapping.Id, "Synced", null);

                _logger.LogInformation("Successfully processed KeyCRM order webhook for order {OrderId}", webhook.Id);
            }
            catch (Exception ex)
            {
                _logger.LogError(ex, "Failed to process KeyCRM order webhook for order {OrderId}: {Error}",
                    webhook.Id, ex.Message);
                throw;
            }
        }

        public async Task<bool> ValidateWebhookSignatureAsync(string payload, string signature)
        {
            try
            {
                var secret = _configuration["KeyCRM:WebhookSecret"];
                if (string.IsNullOrEmpty(secret))
                {
                    _logger.LogWarning("KeyCRM webhook secret not configured");
                    return false;
                }

                var expectedSignature = ComputeHmacSha256(payload, secret);
                return string.Equals(signature, expectedSignature, StringComparison.OrdinalIgnoreCase);
            }
            catch (Exception ex)
            {
                _logger.LogError(ex, "Failed to validate webhook signature: {Error}", ex.Message);
                return false;
            }
        }

        private string ComputeHmacSha256(string payload, string secret)
        {
            using (var hmac = new HMACSHA256(Encoding.UTF8.GetBytes(secret)))
            {
                var hash = hmac.ComputeHash(Encoding.UTF8.GetBytes(payload));
                return Convert.ToHexString(hash).ToLowerInvariant();
            }
        }

        // Additional mapping methods...
    }
}
```

### 4. Sync Service for Data Mapping

```csharp
// Services/IKeyCrmSyncService.cs
namespace VmsApi.Services
{
    public interface IKeyCrmSyncService
    {
        Task<KeyCrmSyncMapping> CreateSyncMappingAsync(string entityType, int vmsEntityId, int keyCrmEntityId);
        Task<KeyCrmSyncMapping> GetSyncMappingAsync(string entityType, int keyCrmEntityId);
        Task UpdateSyncMappingAsync(int mappingId, string status, string errorMessage);
        Task<bool> SyncOrderToKeyCrmAsync(int orderId);
        Task<bool> SyncCustomerToKeyCrmAsync(int customerId);
        Task<bool> SyncArticleToKeyCrmAsync(int articleId);
    }
}

// Services/KeyCrmSyncService.cs
namespace VmsApi.Services
{
    public class KeyCrmSyncService : IKeyCrmSyncService
    {
        private readonly AppDbContext _context;
        private readonly IKeyCrmService _keyCrmService;
        private readonly IOrderService _orderService;
        private readonly ICustomerService _customerService;
        private readonly IArticleService _articleService;
        private readonly ILogger<KeyCrmSyncService> _logger;

        public KeyCrmSyncService(
            AppDbContext context,
            IKeyCrmService keyCrmService,
            IOrderService orderService,
            ICustomerService customerService,
            IArticleService articleService,
            ILogger<KeyCrmSyncService> logger)
        {
            _context = context;
            _keyCrmService = keyCrmService;
            _orderService = orderService;
            _customerService = customerService;
            _articleService = articleService;
            _logger = logger;
        }

        public async Task<bool> SyncOrderToKeyCrmAsync(int orderId)
        {
            try
            {
                var order = await _orderService.GetOrderByIdAsync(orderId);
                if (order == null)
                {
                    _logger.LogWarning("Order {OrderId} not found for KeyCRM sync", orderId);
                    return false;
                }

                // Check if already synced
                var existingMapping = await _context.KeyCrmSyncMappings
                    .FirstOrDefaultAsync(m => m.EntityType == "Order" && m.VmsEntityId == orderId);

                if (existingMapping != null)
                {
                    // Update existing order in KeyCRM
                    var updateRequest = MapVmsOrderToKeyCrmUpdate(order);
                    await _keyCrmService.UpdateOrderAsync(existingMapping.KeyCrmEntityId, updateRequest);

                    existingMapping.LastSyncDate = DateTime.UtcNow;
                    existingMapping.SyncStatus = "Synced";
                    existingMapping.ErrorMessage = null;
                }
                else
                {
                    // Create new order in KeyCRM
                    var createRequest = MapVmsOrderToKeyCrmCreate(order);
                    var keyCrmOrder = await _keyCrmService.CreateOrderAsync(createRequest);

                    // Create sync mapping
                    await CreateSyncMappingAsync("Order", orderId, keyCrmOrder.Id);
                }

                await _context.SaveChangesAsync();
                _logger.LogInformation("Successfully synced order {OrderId} to KeyCRM", orderId);
                return true;
            }
            catch (Exception ex)
            {
                _logger.LogError(ex, "Failed to sync order {OrderId} to KeyCRM: {Error}", orderId, ex.Message);

                // Update mapping with error status
                var mapping = await _context.KeyCrmSyncMappings
                    .FirstOrDefaultAsync(m => m.EntityType == "Order" && m.VmsEntityId == orderId);

                if (mapping != null)
                {
                    mapping.SyncStatus = "Error";
                    mapping.ErrorMessage = ex.Message;
                    await _context.SaveChangesAsync();
                }

                return false;
            }
        }

        // Additional sync methods...
    }
}
```

### 5. Webhook Controller

```csharp
// Controllers/KeyCrmWebhookController.cs
using Microsoft.AspNetCore.Mvc;
using System.Text.Json;

namespace VmsApi.Controllers
{
    [ApiController]
    [Route("api/keycrm/webhook")]
    public class KeyCrmWebhookController : ControllerBase
    {
        private readonly IWebhookProcessingService _webhookService;
        private readonly ILogger<KeyCrmWebhookController> _logger;

        public KeyCrmWebhookController(
            IWebhookProcessingService webhookService,
            ILogger<KeyCrmWebhookController> logger)
        {
            _webhookService = webhookService;
            _logger = logger;
        }

        [HttpPost("order-created")]
        public async Task<IActionResult> OrderCreatedWebhook([FromBody] JsonElement payload)
        {
            try
            {
                var signature = Request.Headers["X-KeyCRM-Signature"].FirstOrDefault();
                var payloadString = payload.GetRawText();

                if (!await _webhookService.ValidateWebhookSignatureAsync(payloadString, signature))
                {
                    _logger.LogWarning("Invalid webhook signature for order created webhook");
                    return Unauthorized("Invalid signature");
                }

                var webhook = JsonSerializer.Deserialize<KeyCrmOrderWebhook>(payloadString);
                await _webhookService.ProcessOrderCreatedWebhookAsync(webhook);

                return Ok(new { status = "processed" });
            }
            catch (Exception ex)
            {
                _logger.LogError(ex, "Failed to process order created webhook: {Error}", ex.Message);
                return StatusCode(500, new { error = "Internal server error" });
            }
        }

        [HttpPost("order-updated")]
        public async Task<IActionResult> OrderUpdatedWebhook([FromBody] JsonElement payload)
        {
            try
            {
                var signature = Request.Headers["X-KeyCRM-Signature"].FirstOrDefault();
                var payloadString = payload.GetRawText();

                if (!await _webhookService.ValidateWebhookSignatureAsync(payloadString, signature))
                {
                    _logger.LogWarning("Invalid webhook signature for order updated webhook");
                    return Unauthorized("Invalid signature");
                }

                var webhook = JsonSerializer.Deserialize<KeyCrmOrderWebhook>(payloadString);
                await _webhookService.ProcessOrderUpdatedWebhookAsync(webhook);

                return Ok(new { status = "processed" });
            }
            catch (Exception ex)
            {
                _logger.LogError(ex, "Failed to process order updated webhook: {Error}", ex.Message);
                return StatusCode(500, new { error = "Internal server error" });
            }
        }

        [HttpPost("order-status-changed")]
        public async Task<IActionResult> OrderStatusChangedWebhook([FromBody] JsonElement payload)
        {
            try
            {
                var signature = Request.Headers["X-KeyCRM-Signature"].FirstOrDefault();
                var payloadString = payload.GetRawText();

                if (!await _webhookService.ValidateWebhookSignatureAsync(payloadString, signature))
                {
                    _logger.LogWarning("Invalid webhook signature for order status changed webhook");
                    return Unauthorized("Invalid signature");
                }

                var webhook = JsonSerializer.Deserialize<KeyCrmOrderWebhook>(payloadString);
                await _webhookService.ProcessOrderStatusChangedWebhookAsync(webhook);

                return Ok(new { status = "processed" });
            }
            catch (Exception ex)
            {
                _logger.LogError(ex, "Failed to process order status changed webhook: {Error}", ex.Message);
                return StatusCode(500, new { error = "Internal server error" });
            }
        }

        [HttpPost("payment-created")]
        public async Task<IActionResult> PaymentCreatedWebhook([FromBody] JsonElement payload)
        {
            try
            {
                var signature = Request.Headers["X-KeyCRM-Signature"].FirstOrDefault();
                var payloadString = payload.GetRawText();

                if (!await _webhookService.ValidateWebhookSignatureAsync(payloadString, signature))
                {
                    _logger.LogWarning("Invalid webhook signature for payment created webhook");
                    return Unauthorized("Invalid signature");
                }

                var webhook = JsonSerializer.Deserialize<KeyCrmPaymentWebhook>(payloadString);
                await _webhookService.ProcessPaymentCreatedWebhookAsync(webhook);

                return Ok(new { status = "processed" });
            }
            catch (Exception ex)
            {
                _logger.LogError(ex, "Failed to process payment created webhook: {Error}", ex.Message);
                return StatusCode(500, new { error = "Internal server error" });
            }
        }

        [HttpPost("payment-updated")]
        public async Task<IActionResult> PaymentUpdatedWebhook([FromBody] JsonElement payload)
        {
            try
            {
                var signature = Request.Headers["X-KeyCRM-Signature"].FirstOrDefault();
                var payloadString = payload.GetRawText();

                if (!await _webhookService.ValidateWebhookSignatureAsync(payloadString, signature))
                {
                    _logger.LogWarning("Invalid webhook signature for payment updated webhook");
                    return Unauthorized("Invalid signature");
                }

                var webhook = JsonSerializer.Deserialize<KeyCrmPaymentWebhook>(payloadString);
                await _webhookService.ProcessPaymentUpdatedWebhookAsync(webhook);

                return Ok(new { status = "processed" });
            }
            catch (Exception ex)
            {
                _logger.LogError(ex, "Failed to process payment updated webhook: {Error}", ex.Message);
                return StatusCode(500, new { error = "Internal server error" });
            }
        }

        [HttpPost("buyer-created")]
        public async Task<IActionResult> BuyerCreatedWebhook([FromBody] JsonElement payload)
        {
            try
            {
                var signature = Request.Headers["X-KeyCRM-Signature"].FirstOrDefault();
                var payloadString = payload.GetRawText();

                if (!await _webhookService.ValidateWebhookSignatureAsync(payloadString, signature))
                {
                    _logger.LogWarning("Invalid webhook signature for buyer created webhook");
                    return Unauthorized("Invalid signature");
                }

                var webhook = JsonSerializer.Deserialize<KeyCrmBuyerWebhook>(payloadString);
                await _webhookService.ProcessBuyerCreatedWebhookAsync(webhook);

                return Ok(new { status = "processed" });
            }
            catch (Exception ex)
            {
                _logger.LogError(ex, "Failed to process buyer created webhook: {Error}", ex.Message);
                return StatusCode(500, new { error = "Internal server error" });
            }
        }

        [HttpPost("buyer-updated")]
        public async Task<IActionResult> BuyerUpdatedWebhook([FromBody] JsonElement payload)
        {
            try
            {
                var signature = Request.Headers["X-KeyCRM-Signature"].FirstOrDefault();
                var payloadString = payload.GetRawText();

                if (!await _webhookService.ValidateWebhookSignatureAsync(payloadString, signature))
                {
                    _logger.LogWarning("Invalid webhook signature for buyer updated webhook");
                    return Unauthorized("Invalid signature");
                }

                var webhook = JsonSerializer.Deserialize<KeyCrmBuyerWebhook>(payloadString);
                await _webhookService.ProcessBuyerUpdatedWebhookAsync(webhook);

                return Ok(new { status = "processed" });
            }
            catch (Exception ex)
            {
                _logger.LogError(ex, "Failed to process buyer updated webhook: {Error}", ex.Message);
                return StatusCode(500, new { error = "Internal server error" });
            }
        }
    }
}
        {
            try
            {
                var signature = Request.Headers["X-KeyCRM-Signature"].FirstOrDefault();
                var payloadString = payload.GetRawText();

                if (!await _webhookService.ValidateWebhookSignatureAsync(payloadString, signature))
                {
                    _logger.LogWarning("Invalid webhook signature for buyer webhook");
                    return Unauthorized("Invalid signature");
                }

                var webhook = JsonSerializer.Deserialize<KeyCrmBuyerWebhook>(payloadString);
                await _webhookService.ProcessBuyerWebhookAsync(webhook);

                return Ok(new { status = "processed" });
            }
            catch (Exception ex)
            {
                _logger.LogError(ex, "Failed to process buyer webhook: {Error}", ex.Message);
                return StatusCode(500, new { error = "Internal server error" });
            }
        }

        [HttpPost("payment")]
        public async Task<IActionResult> PaymentWebhook([FromBody] JsonElement payload)
        {
            try
            {
                var signature = Request.Headers["X-KeyCRM-Signature"].FirstOrDefault();
                var payloadString = payload.GetRawText();

                if (!await _webhookService.ValidateWebhookSignatureAsync(payloadString, signature))
                {
                    _logger.LogWarning("Invalid webhook signature for payment webhook");
                    return Unauthorized("Invalid signature");
                }

                var webhook = JsonSerializer.Deserialize<KeyCrmPaymentWebhook>(payloadString);
                await _webhookService.ProcessPaymentWebhookAsync(webhook);

                return Ok(new { status = "processed" });
            }
            catch (Exception ex)
            {
                _logger.LogError(ex, "Failed to process payment webhook: {Error}", ex.Message);
                return StatusCode(500, new { error = "Internal server error" });
            }
        }
    }
}
```

### 6. Manual Sync Controller

```csharp
// Controllers/KeyCrmSyncController.cs
using Microsoft.AspNetCore.Mvc;

namespace VmsApi.Controllers
{
    [ApiController]
    [Route("api/keycrm/sync")]
    public class KeyCrmSyncController : ControllerBase
    {
        private readonly IKeyCrmSyncService _syncService;
        private readonly ILogger<KeyCrmSyncController> _logger;

        public KeyCrmSyncController(IKeyCrmSyncService syncService, ILogger<KeyCrmSyncController> logger)
        {
            _syncService = syncService;
            _logger = logger;
        }

        [HttpPost("orders/{orderId}")]
        public async Task<IActionResult> SyncOrder(int orderId)
        {
            try
            {
                var success = await _syncService.SyncOrderToKeyCrmAsync(orderId);
                if (success)
                {
                    return Ok(new { message = "Order synced successfully", orderId });
                }
                else
                {
                    return BadRequest(new { error = "Failed to sync order", orderId });
                }
            }
            catch (Exception ex)
            {
                _logger.LogError(ex, "Error syncing order {OrderId}: {Error}", orderId, ex.Message);
                return StatusCode(500, new { error = "Internal server error" });
            }
        }

        [HttpPost("customers/{customerId}")]
        public async Task<IActionResult> SyncCustomer(int customerId)
        {
            try
            {
                var success = await _syncService.SyncCustomerToKeyCrmAsync(customerId);
                if (success)
                {
                    return Ok(new { message = "Customer synced successfully", customerId });
                }
                else
                {
                    return BadRequest(new { error = "Failed to sync customer", customerId });
                }
            }
            catch (Exception ex)
            {
                _logger.LogError(ex, "Error syncing customer {CustomerId}: {Error}", customerId, ex.Message);
                return StatusCode(500, new { error = "Internal server error" });
            }
        }

        [HttpGet("status")]
        public async Task<IActionResult> GetSyncStatus()
        {
            try
            {
                // Implementation to return sync status dashboard data
                return Ok(new { message = "Sync status endpoint - implementation needed" });
            }
            catch (Exception ex)
            {
                _logger.LogError(ex, "Error getting sync status: {Error}", ex.Message);
                return StatusCode(500, new { error = "Internal server error" });
            }
        }
    }
}
```

### 7. Program.cs Configuration

```csharp
// Add to Program.cs

// KeyCRM HTTP Client Configuration
builder.Services.AddHttpClient<IKeyCrmService, KeyCrmService>(client =>
{
    var keyCrmConfig = builder.Configuration.GetSection("KeyCRM");
    client.BaseAddress = new Uri(keyCrmConfig["BaseUrl"]!);
    client.DefaultRequestHeaders.Add("Authorization", $"Bearer {keyCrmConfig["ApiKey"]}");
    client.DefaultRequestHeaders.Add("Accept", "application/json");
    client.Timeout = TimeSpan.FromSeconds(30);
});

// KeyCRM Services
builder.Services.AddScoped<IKeyCrmService, KeyCrmService>();
builder.Services.AddScoped<IWebhookProcessingService, WebhookProcessingService>();
builder.Services.AddScoped<IKeyCrmSyncService, KeyCrmSyncService>();

// Background service for periodic sync (optional)
builder.Services.AddHostedService<KeyCrmSyncBackgroundService>();

// SignalR for real-time notifications (optional)
builder.Services.AddSignalR();
builder.Services.AddScoped<INotificationService, SignalRNotificationService>();
```

### 8. Exception Handling

```csharp
// Exceptions/KeyCrmApiException.cs
namespace VmsApi.Exceptions
{
    public class KeyCrmApiException : Exception
    {
        public string? ApiResponse { get; }
        public int? StatusCode { get; }

        public KeyCrmApiException(string message) : base(message) { }

        public KeyCrmApiException(string message, Exception innerException)
            : base(message, innerException) { }

        public KeyCrmApiException(string message, string apiResponse, int statusCode)
            : base(message)
        {
            ApiResponse = apiResponse;
            StatusCode = statusCode;
        }
    }
}
```

This implementation provides a solid foundation for two-way integration with KeyCRM, including proper error handling, logging, and extensibility for future enhancements.
