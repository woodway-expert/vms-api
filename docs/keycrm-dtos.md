# KeyCRM Data Transfer Objects (DTOs)

This file contains all the necessary DTOs for KeyCRM integration.

```csharp
// DTOs/KeyCrmDtos.cs
using System.Text.Json.Serialization;

namespace VmsApi.DTOs
{
    // Base Response Classes
    public class PagedResponse<T>
    {
        [JsonPropertyName("total")]
        public int Total { get; set; }

        [JsonPropertyName("current_page")]
        public int CurrentPage { get; set; }

        [JsonPropertyName("per_page")]
        public int PerPage { get; set; }

        [JsonPropertyName("data")]
        public List<T> Data { get; set; } = new();

        [JsonPropertyName("first_page_url")]
        public string? FirstPageUrl { get; set; }

        [JsonPropertyName("last_page_url")]
        public string? LastPageUrl { get; set; }

        [JsonPropertyName("next_page_url")]
        public string? NextPageUrl { get; set; }
    }

    // Order DTOs
    public class KeyCrmOrderRequest
    {
        [JsonPropertyName("source_id")]
        public int SourceId { get; set; }

        [JsonPropertyName("source_uuid")]
        public string? SourceUuid { get; set; }

        [JsonPropertyName("buyer_comment")]
        public string? BuyerComment { get; set; }

        [JsonPropertyName("manager_id")]
        public int? ManagerId { get; set; }

        [JsonPropertyName("manager_comment")]
        public string? ManagerComment { get; set; }

        [JsonPropertyName("promocode")]
        public string? Promocode { get; set; }

        [JsonPropertyName("discount_percent")]
        public decimal? DiscountPercent { get; set; }

        [JsonPropertyName("discount_amount")]
        public decimal? DiscountAmount { get; set; }

        [JsonPropertyName("shipping_price")]
        public decimal? ShippingPrice { get; set; }

        [JsonPropertyName("wrap_price")]
        public decimal? WrapPrice { get; set; }

        [JsonPropertyName("gift_message")]
        public string? GiftMessage { get; set; }

        [JsonPropertyName("is_gift")]
        public bool? IsGift { get; set; }

        [JsonPropertyName("gift_wrap")]
        public bool? GiftWrap { get; set; }

        [JsonPropertyName("taxes")]
        public decimal? Taxes { get; set; }

        [JsonPropertyName("ordered_at")]
        public string? OrderedAt { get; set; }

        [JsonPropertyName("buyer")]
        public KeyCrmBuyerInfo Buyer { get; set; } = new();

        [JsonPropertyName("shipping")]
        public KeyCrmShippingInfo? Shipping { get; set; }

        [JsonPropertyName("marketing")]
        public KeyCrmMarketingInfo? Marketing { get; set; }

        [JsonPropertyName("products")]
        public List<KeyCrmOrderProduct> Products { get; set; } = new();

        [JsonPropertyName("payments")]
        public List<KeyCrmOrderPayment> Payments { get; set; } = new();

        [JsonPropertyName("custom_fields")]
        public List<KeyCrmCustomField> CustomFields { get; set; } = new();
    }

    public class KeyCrmOrderUpdateRequest
    {
        [JsonPropertyName("buyer_comment")]
        public string? BuyerComment { get; set; }

        [JsonPropertyName("manager_comment")]
        public string? ManagerComment { get; set; }

        [JsonPropertyName("status_id")]
        public int? StatusId { get; set; }

        [JsonPropertyName("discount_percent")]
        public decimal? DiscountPercent { get; set; }

        [JsonPropertyName("discount_amount")]
        public decimal? DiscountAmount { get; set; }

        [JsonPropertyName("products")]
        public List<KeyCrmOrderProductUpdate> Products { get; set; } = new();

        [JsonPropertyName("shipping")]
        public KeyCrmShippingInfo? Shipping { get; set; }

        [JsonPropertyName("custom_fields")]
        public List<KeyCrmCustomField> CustomFields { get; set; } = new();
    }

    public class KeyCrmOrderResponse
    {
        [JsonPropertyName("id")]
        public int Id { get; set; }

        [JsonPropertyName("source_id")]
        public int SourceId { get; set; }

        [JsonPropertyName("source_uuid")]
        public string? SourceUuid { get; set; }

        [JsonPropertyName("buyer_comment")]
        public string? BuyerComment { get; set; }

        [JsonPropertyName("manager_comment")]
        public string? ManagerComment { get; set; }

        [JsonPropertyName("status_id")]
        public int StatusId { get; set; }

        [JsonPropertyName("payment_status")]
        public string? PaymentStatus { get; set; }

        [JsonPropertyName("total_price")]
        public decimal TotalPrice { get; set; }

        [JsonPropertyName("currency_code")]
        public string? CurrencyCode { get; set; }

        [JsonPropertyName("ordered_at")]
        public string? OrderedAt { get; set; }

        [JsonPropertyName("created_at")]
        public string? CreatedAt { get; set; }

        [JsonPropertyName("updated_at")]
        public string? UpdatedAt { get; set; }

        [JsonPropertyName("buyer")]
        public KeyCrmBuyerResponse? Buyer { get; set; }

        [JsonPropertyName("products")]
        public List<KeyCrmOrderProductResponse> Products { get; set; } = new();

        [JsonPropertyName("payments")]
        public List<KeyCrmPaymentResponse> Payments { get; set; } = new();

        [JsonPropertyName("shipping")]
        public KeyCrmShippingResponse? Shipping { get; set; }

        [JsonPropertyName("status")]
        public KeyCrmStatus? Status { get; set; }
    }

    // Buyer DTOs
    public class KeyCrmBuyerInfo
    {
        [JsonPropertyName("full_name")]
        public string? FullName { get; set; }

        [JsonPropertyName("email")]
        public string? Email { get; set; }

        [JsonPropertyName("phone")]
        public string? Phone { get; set; }
    }

    public class KeyCrmBuyerRequest
    {
        [JsonPropertyName("full_name")]
        public string FullName { get; set; } = string.Empty;

        [JsonPropertyName("birthday")]
        public string? Birthday { get; set; }

        [JsonPropertyName("email")]
        public List<string> Email { get; set; } = new();

        [JsonPropertyName("phone")]
        public List<string> Phone { get; set; } = new();

        [JsonPropertyName("note")]
        public string? Note { get; set; }

        [JsonPropertyName("company_id")]
        public int? CompanyId { get; set; }

        [JsonPropertyName("manager_id")]
        public int? ManagerId { get; set; }

        [JsonPropertyName("custom_fields")]
        public List<KeyCrmCustomField> CustomFields { get; set; } = new();
    }

    public class KeyCrmBuyerUpdateRequest : KeyCrmBuyerRequest { }

    public class KeyCrmBuyerResponse
    {
        [JsonPropertyName("id")]
        public int Id { get; set; }

        [JsonPropertyName("full_name")]
        public string FullName { get; set; } = string.Empty;

        [JsonPropertyName("birthday")]
        public string? Birthday { get; set; }

        [JsonPropertyName("email")]
        public List<string> Email { get; set; } = new();

        [JsonPropertyName("phone")]
        public List<string> Phone { get; set; } = new();

        [JsonPropertyName("note")]
        public string? Note { get; set; }

        [JsonPropertyName("created_at")]
        public string? CreatedAt { get; set; }

        [JsonPropertyName("updated_at")]
        public string? UpdatedAt { get; set; }

        [JsonPropertyName("company")]
        public KeyCrmCompanyResponse? Company { get; set; }

        [JsonPropertyName("manager")]
        public KeyCrmManagerResponse? Manager { get; set; }
    }

    // Product DTOs
    public class KeyCrmOrderProduct
    {
        [JsonPropertyName("sku")]
        public string? Sku { get; set; }

        [JsonPropertyName("price")]
        public decimal Price { get; set; }

        [JsonPropertyName("purchased_price")]
        public decimal? PurchasedPrice { get; set; }

        [JsonPropertyName("discount_percent")]
        public decimal? DiscountPercent { get; set; }

        [JsonPropertyName("discount_amount")]
        public decimal? DiscountAmount { get; set; }

        [JsonPropertyName("quantity")]
        public decimal Quantity { get; set; }

        [JsonPropertyName("unit_type")]
        public string? UnitType { get; set; }

        [JsonPropertyName("name")]
        public string Name { get; set; } = string.Empty;

        [JsonPropertyName("comment")]
        public string? Comment { get; set; }

        [JsonPropertyName("picture")]
        public string? Picture { get; set; }

        [JsonPropertyName("properties")]
        public List<KeyCrmProductProperty> Properties { get; set; } = new();
    }

    public class KeyCrmOrderProductUpdate
    {
        [JsonPropertyName("sku")]
        public string? Sku { get; set; }

        [JsonPropertyName("id")]
        public int? Id { get; set; }

        [JsonPropertyName("name")]
        public string? Name { get; set; }

        [JsonPropertyName("comment")]
        public string? Comment { get; set; }

        [JsonPropertyName("price")]
        public decimal? Price { get; set; }

        [JsonPropertyName("purchased_price")]
        public decimal? PurchasedPrice { get; set; }

        [JsonPropertyName("discount_amount")]
        public decimal? DiscountAmount { get; set; }

        [JsonPropertyName("discount_percent")]
        public decimal? DiscountPercent { get; set; }

        [JsonPropertyName("quantity")]
        public decimal? Quantity { get; set; }

        [JsonPropertyName("product_status_id")]
        public int? ProductStatusId { get; set; }
    }

    public class KeyCrmOrderProductResponse
    {
        [JsonPropertyName("id")]
        public int Id { get; set; }

        [JsonPropertyName("sku")]
        public string? Sku { get; set; }

        [JsonPropertyName("name")]
        public string Name { get; set; } = string.Empty;

        [JsonPropertyName("price")]
        public decimal Price { get; set; }

        [JsonPropertyName("quantity")]
        public decimal Quantity { get; set; }

        [JsonPropertyName("total_price")]
        public decimal TotalPrice { get; set; }

        [JsonPropertyName("picture")]
        public string? Picture { get; set; }

        [JsonPropertyName("properties")]
        public List<KeyCrmProductProperty> Properties { get; set; } = new();
    }

    public class KeyCrmProductProperty
    {
        [JsonPropertyName("name")]
        public string Name { get; set; } = string.Empty;

        [JsonPropertyName("value")]
        public string Value { get; set; } = string.Empty;
    }

    public class KeyCrmProductRequest
    {
        [JsonPropertyName("name")]
        public string Name { get; set; } = string.Empty;

        [JsonPropertyName("description")]
        public string? Description { get; set; }

        [JsonPropertyName("sku")]
        public string? Sku { get; set; }

        [JsonPropertyName("category_id")]
        public int? CategoryId { get; set; }

        [JsonPropertyName("unit_type")]
        public string? UnitType { get; set; }

        [JsonPropertyName("weight")]
        public decimal? Weight { get; set; }

        [JsonPropertyName("length")]
        public decimal? Length { get; set; }

        [JsonPropertyName("width")]
        public decimal? Width { get; set; }

        [JsonPropertyName("height")]
        public decimal? Height { get; set; }

        [JsonPropertyName("offers")]
        public List<KeyCrmOfferRequest> Offers { get; set; } = new();
    }

    public class KeyCrmProductUpdateRequest : KeyCrmProductRequest { }

    public class KeyCrmProductResponse
    {
        [JsonPropertyName("id")]
        public int Id { get; set; }

        [JsonPropertyName("name")]
        public string Name { get; set; } = string.Empty;

        [JsonPropertyName("description")]
        public string? Description { get; set; }

        [JsonPropertyName("sku")]
        public string? Sku { get; set; }

        [JsonPropertyName("category_id")]
        public int? CategoryId { get; set; }

        [JsonPropertyName("min_price")]
        public decimal? MinPrice { get; set; }

        [JsonPropertyName("max_price")]
        public decimal? MaxPrice { get; set; }

        [JsonPropertyName("quantity")]
        public decimal Quantity { get; set; }

        [JsonPropertyName("created_at")]
        public string? CreatedAt { get; set; }

        [JsonPropertyName("updated_at")]
        public string? UpdatedAt { get; set; }
    }

    // Offer DTOs
    public class KeyCrmOfferRequest
    {
        [JsonPropertyName("sku")]
        public string? Sku { get; set; }

        [JsonPropertyName("barcode")]
        public string? Barcode { get; set; }

        [JsonPropertyName("price")]
        public decimal Price { get; set; }

        [JsonPropertyName("purchased_price")]
        public decimal? PurchasedPrice { get; set; }

        [JsonPropertyName("quantity")]
        public decimal Quantity { get; set; }

        [JsonPropertyName("weight")]
        public decimal? Weight { get; set; }

        [JsonPropertyName("properties")]
        public List<KeyCrmProductProperty> Properties { get; set; } = new();
    }

    public class KeyCrmOfferResponse
    {
        [JsonPropertyName("id")]
        public int Id { get; set; }

        [JsonPropertyName("product_id")]
        public int ProductId { get; set; }

        [JsonPropertyName("sku")]
        public string? Sku { get; set; }

        [JsonPropertyName("barcode")]
        public string? Barcode { get; set; }

        [JsonPropertyName("price")]
        public decimal Price { get; set; }

        [JsonPropertyName("purchased_price")]
        public decimal? PurchasedPrice { get; set; }

        [JsonPropertyName("quantity")]
        public decimal Quantity { get; set; }

        [JsonPropertyName("properties")]
        public List<KeyCrmProductProperty> Properties { get; set; } = new();
    }

    public class KeyCrmStockUpdateRequest
    {
        [JsonPropertyName("quantity")]
        public decimal Quantity { get; set; }

        [JsonPropertyName("price")]
        public decimal? Price { get; set; }

        [JsonPropertyName("purchased_price")]
        public decimal? PurchasedPrice { get; set; }
    }

    // Payment DTOs
    public class KeyCrmOrderPayment
    {
        [JsonPropertyName("payment_method_id")]
        public int? PaymentMethodId { get; set; }

        [JsonPropertyName("payment_method")]
        public string? PaymentMethod { get; set; }

        [JsonPropertyName("amount")]
        public decimal Amount { get; set; }

        [JsonPropertyName("description")]
        public string? Description { get; set; }

        [JsonPropertyName("payment_date")]
        public string? PaymentDate { get; set; }

        [JsonPropertyName("status")]
        public string? Status { get; set; }
    }

    public class KeyCrmPaymentRequest
    {
        [JsonPropertyName("payment_method_id")]
        public int? PaymentMethodId { get; set; }

        [JsonPropertyName("payment_method")]
        public string? PaymentMethod { get; set; }

        [JsonPropertyName("amount")]
        public decimal Amount { get; set; }

        [JsonPropertyName("status")]
        public string Status { get; set; } = "paid";

        [JsonPropertyName("description")]
        public string? Description { get; set; }

        [JsonPropertyName("payment_date")]
        public string? PaymentDate { get; set; }
    }

    public class KeyCrmPaymentUpdateRequest
    {
        [JsonPropertyName("status")]
        public string? Status { get; set; }

        [JsonPropertyName("description")]
        public string? Description { get; set; }
    }

    public class KeyCrmPaymentResponse
    {
        [JsonPropertyName("id")]
        public int Id { get; set; }

        [JsonPropertyName("amount")]
        public decimal Amount { get; set; }

        [JsonPropertyName("status")]
        public string Status { get; set; } = string.Empty;

        [JsonPropertyName("description")]
        public string? Description { get; set; }

        [JsonPropertyName("payment_date")]
        public string? PaymentDate { get; set; }

        [JsonPropertyName("created_at")]
        public string? CreatedAt { get; set; }

        [JsonPropertyName("updated_at")]
        public string? UpdatedAt { get; set; }
    }

    // Shipping DTOs
    public class KeyCrmShippingInfo
    {
        [JsonPropertyName("delivery_service_id")]
        public int? DeliveryServiceId { get; set; }

        [JsonPropertyName("tracking_code")]
        public string? TrackingCode { get; set; }

        [JsonPropertyName("shipping_service")]
        public string? ShippingService { get; set; }

        [JsonPropertyName("shipping_address_city")]
        public string? ShippingAddressCity { get; set; }

        [JsonPropertyName("shipping_address_country")]
        public string? ShippingAddressCountry { get; set; }

        [JsonPropertyName("shipping_address_region")]
        public string? ShippingAddressRegion { get; set; }

        [JsonPropertyName("shipping_address_zip")]
        public string? ShippingAddressZip { get; set; }

        [JsonPropertyName("shipping_secondary_line")]
        public string? ShippingSecondaryLine { get; set; }

        [JsonPropertyName("shipping_receive_point")]
        public string? ShippingReceivePoint { get; set; }

        [JsonPropertyName("recipient_full_name")]
        public string? RecipientFullName { get; set; }

        [JsonPropertyName("recipient_phone")]
        public string? RecipientPhone { get; set; }

        [JsonPropertyName("warehouse_ref")]
        public string? WarehouseRef { get; set; }

        [JsonPropertyName("shipping_date")]
        public string? ShippingDate { get; set; }
    }

    public class KeyCrmShippingResponse : KeyCrmShippingInfo
    {
        [JsonPropertyName("id")]
        public int Id { get; set; }
    }

    // Marketing DTOs
    public class KeyCrmMarketingInfo
    {
        [JsonPropertyName("utm_source")]
        public string? UtmSource { get; set; }

        [JsonPropertyName("utm_medium")]
        public string? UtmMedium { get; set; }

        [JsonPropertyName("utm_campaign")]
        public string? UtmCampaign { get; set; }

        [JsonPropertyName("utm_term")]
        public string? UtmTerm { get; set; }

        [JsonPropertyName("utm_content")]
        public string? UtmContent { get; set; }
    }

    // Custom Fields
    public class KeyCrmCustomField
    {
        [JsonPropertyName("uuid")]
        public string Uuid { get; set; } = string.Empty;

        [JsonPropertyName("value")]
        public object? Value { get; set; }
    }

    public class KeyCrmCustomFieldDefinition
    {
        [JsonPropertyName("id")]
        public int Id { get; set; }

        [JsonPropertyName("uuid")]
        public string Uuid { get; set; } = string.Empty;

        [JsonPropertyName("name")]
        public string Name { get; set; } = string.Empty;

        [JsonPropertyName("type")]
        public string Type { get; set; } = string.Empty;

        [JsonPropertyName("model")]
        public string Model { get; set; } = string.Empty;

        [JsonPropertyName("required")]
        public bool Required { get; set; }

        [JsonPropertyName("options")]
        public List<KeyCrmCustomFieldOption> Options { get; set; } = new();
    }

    public class KeyCrmCustomFieldOption
    {
        [JsonPropertyName("id")]
        public int Id { get; set; }

        [JsonPropertyName("value")]
        public string Value { get; set; } = string.Empty;
    }

    // Reference Data DTOs
    public class KeyCrmStatus
    {
        [JsonPropertyName("id")]
        public int Id { get; set; }

        [JsonPropertyName("name")]
        public string Name { get; set; } = string.Empty;

        [JsonPropertyName("color")]
        public string? Color { get; set; }

        [JsonPropertyName("is_system")]
        public bool IsSystem { get; set; }
    }

    public class KeyCrmSource
    {
        [JsonPropertyName("id")]
        public int Id { get; set; }

        [JsonPropertyName("name")]
        public string Name { get; set; } = string.Empty;

        [JsonPropertyName("color")]
        public string? Color { get; set; }
    }

    public class KeyCrmPaymentMethod
    {
        [JsonPropertyName("id")]
        public int Id { get; set; }

        [JsonPropertyName("name")]
        public string Name { get; set; } = string.Empty;

        [JsonPropertyName("is_active")]
        public bool IsActive { get; set; }
    }

    public class KeyCrmCompanyResponse
    {
        [JsonPropertyName("id")]
        public int Id { get; set; }

        [JsonPropertyName("name")]
        public string Name { get; set; } = string.Empty;

        [JsonPropertyName("title")]
        public string? Title { get; set; }

        [JsonPropertyName("bank_account")]
        public string? BankAccount { get; set; }
    }

    public class KeyCrmManagerResponse
    {
        [JsonPropertyName("id")]
        public int Id { get; set; }

        [JsonPropertyName("first_name")]
        public string? FirstName { get; set; }

        [JsonPropertyName("last_name")]
        public string? LastName { get; set; }

        [JsonPropertyName("full_name")]
        public string? FullName { get; set; }

        [JsonPropertyName("email")]
        public string? Email { get; set; }

        [JsonPropertyName("phone")]
        public string? Phone { get; set; }
    }

    // Filter DTOs
    public class KeyCrmOrderFilter
    {
        public int? Page { get; set; } = 1;
        public int? Limit { get; set; } = 15;
        public string? Include { get; set; }
        public string? Sort { get; set; }
        public int? StatusId { get; set; }
        public int? SourceId { get; set; }
        public string? SourceUuid { get; set; }
        public string? BuyerPhone { get; set; }
        public string? BuyerEmail { get; set; }
        public string? CreatedBetween { get; set; }
        public string? UpdatedBetween { get; set; }
        public string? PaymentStatus { get; set; }
    }

    public class KeyCrmBuyerFilter
    {
        public int? Page { get; set; } = 1;
        public int? Limit { get; set; } = 15;
        public string? Include { get; set; }
        public string? Sort { get; set; }
        public string? Search { get; set; }
    }

    // Webhook DTOs
    public class KeyCrmOrderWebhook
    {
        [JsonPropertyName("id")]
        public int Id { get; set; }

        [JsonPropertyName("event")]
        public string Event { get; set; } = string.Empty;

        [JsonPropertyName("data")]
        public KeyCrmOrderResponse Data { get; set; } = new();

        [JsonPropertyName("timestamp")]
        public string? Timestamp { get; set; }
    }

    public class KeyCrmBuyerWebhook
    {
        [JsonPropertyName("id")]
        public int Id { get; set; }

        [JsonPropertyName("event")]
        public string Event { get; set; } = string.Empty;

        [JsonPropertyName("data")]
        public KeyCrmBuyerResponse Data { get; set; } = new();

        [JsonPropertyName("timestamp")]
        public string? Timestamp { get; set; }
    }

    public class KeyCrmPaymentWebhook
    {
        [JsonPropertyName("id")]
        public int Id { get; set; }

        [JsonPropertyName("event")]
        public string Event { get; set; } = string.Empty;

        [JsonPropertyName("data")]
        public KeyCrmPaymentResponse Data { get; set; } = new();

        [JsonPropertyName("timestamp")]
        public string? Timestamp { get; set; }
    }

    // Sync Mapping Models
    public class KeyCrmSyncMapping
    {
        public int Id { get; set; }
        public string EntityType { get; set; } = string.Empty;
        public int VmsEntityId { get; set; }
        public int KeyCrmEntityId { get; set; }
        public DateTime LastSyncDate { get; set; }
        public string SyncStatus { get; set; } = string.Empty;
        public string? ErrorMessage { get; set; }
        public DateTime CreatedAt { get; set; }
        public DateTime UpdatedAt { get; set; }
    }

    public class KeyCrmWebhookEvent
    {
        public int Id { get; set; }
        public string EventType { get; set; } = string.Empty;
        public string PayloadJson { get; set; } = string.Empty;
        public DateTime? ProcessedAt { get; set; }
        public string ProcessingStatus { get; set; } = string.Empty;
        public string? ErrorMessage { get; set; }
        public DateTime ReceivedAt { get; set; }
    }
}
```
