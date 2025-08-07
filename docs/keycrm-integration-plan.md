# KeyCRM Two-Way Integration Plan

## Overview

This document outlines a comprehensive plan to implement two-way integration between the VMS API and KeyCRM, enabling full synchronization of warehouse operations with customer relationship management.

## Architecture Components

### 1. Outbound Integration (VMS → KeyCRM)
Send data from our warehouse system to KeyCRM when warehouse events occur.

### 2. Inbound Integration (KeyCRM → VMS)
Receive updates from KeyCRM via webhooks and update our warehouse system accordingly.

### 3. Real-time Notifications (Optional)
Implement SignalR for real-time client notifications about CRM events.

## Implementation Plan

### Phase 1: Foundation Setup

#### 1.1 Create KeyCRM Service Layer

**Files to Create:**
- `/Services/IKeyCrmService.cs` - Interface for KeyCRM operations
- `/Services/KeyCrmService.cs` - Implementation with HttpClient
- `/DTOs/KeyCrmDtos.cs` - Data transfer objects for KeyCRM integration
- `/Models/KeyCrmWebhook.cs` - Webhook payload models

**Key Features:**
- Order synchronization (create, update)
- Customer/Buyer management
- Product/Offer synchronization
- Payment tracking
- Shipping updates

#### 1.2 Create Webhook Controller

**Files to Create:**
- `/Controllers/KeyCrmWebhookController.cs` - Handle incoming webhooks
- `/Services/IWebhookProcessingService.cs` - Process webhook events
- `/Services/WebhookProcessingService.cs` - Implementation

#### 1.3 Configuration Updates

**Files to Modify:**
- `Program.cs` - Register services and configure HttpClient
- `appsettings.json` - Add KeyCRM configuration

### Phase 2: Core Integration Features

#### 2.1 Order Synchronization

**Outbound (VMS → KeyCRM):**
- When order is created in VMS → Create order in KeyCRM
- When order status changes → Update order status in KeyCRM
- When payment is received → Add payment to KeyCRM order
- When shipping info is updated → Update tracking in KeyCRM

**Inbound (KeyCRM → VMS):**
- When order is updated in KeyCRM → Update order in VMS
- When payment status changes → Update payment status in VMS
- When order is canceled → Update order status in VMS

#### 2.2 Customer Synchronization

**Outbound (VMS → KeyCRM):**
- New customer created → Create buyer in KeyCRM
- Customer details updated → Update buyer in KeyCRM

**Inbound (KeyCRM → VMS):**
- Buyer information updated → Update customer in VMS
- New buyer created → Create customer in VMS

#### 2.3 Product/Inventory Synchronization

**Outbound (VMS → KeyCRM):**
- Product stock changes → Update offer quantities in KeyCRM
- New products added → Create products/offers in KeyCRM
- Price changes → Update offer prices in KeyCRM

**Inbound (KeyCRM → VMS):**
- Product details updated → Update article information in VMS

### Phase 3: Advanced Features

#### 3.1 Real-time Notifications (SignalR)

**Files to Create:**
- `/Hubs/KeyCrmHub.cs` - SignalR hub for real-time updates
- `/Services/INotificationService.cs` - Notification abstraction
- `/Services/SignalRNotificationService.cs` - SignalR implementation

#### 3.2 Conflict Resolution

**Features:**
- Timestamp-based conflict resolution
- Manual conflict resolution interface
- Data validation and error handling

#### 3.3 Audit Trail

**Features:**
- Track all synchronization events
- Error logging and retry mechanisms
- Performance monitoring

## Technical Implementation Details

### Service Registration (Program.cs)

```csharp
// KeyCRM HTTP Client
builder.Services.AddHttpClient<IKeyCrmService, KeyCrmService>(client =>
{
    client.BaseAddress = new Uri(builder.Configuration["KeyCRM:BaseUrl"]);
    client.DefaultRequestHeaders.Add("Authorization",
        $"Bearer {builder.Configuration["KeyCRM:ApiKey"]}");
    client.DefaultRequestHeaders.Add("Accept", "application/json");
});

// KeyCRM Services
builder.Services.AddScoped<IKeyCrmService, KeyCrmService>();
builder.Services.AddScoped<IWebhookProcessingService, WebhookProcessingService>();
builder.Services.AddScoped<IKeyCrmSyncService, KeyCrmSyncService>();

// SignalR (Optional)
builder.Services.AddSignalR();
builder.Services.AddScoped<INotificationService, SignalRNotificationService>();

// Background Services for periodic sync
builder.Services.AddHostedService<KeyCrmSyncBackgroundService>();
```

### Configuration (appsettings.json)

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
      "SyncIntervalMinutes": 5
    }
  }
}
```

### Database Changes

**New Tables to Create:**
```sql
-- KeyCRM Sync Mapping
CREATE TABLE KeyCrmSyncMapping (
    Id int IDENTITY(1,1) PRIMARY KEY,
    EntityType nvarchar(50) NOT NULL, -- 'Order', 'Customer', 'Article'
    VmsEntityId int NOT NULL,
    KeyCrmEntityId int NOT NULL,
    LastSyncDate datetime2 NOT NULL,
    SyncStatus nvarchar(20) NOT NULL, -- 'Synced', 'Pending', 'Error'
    ErrorMessage nvarchar(max) NULL,
    CreatedAt datetime2 NOT NULL DEFAULT GETUTCDATE(),
    UpdatedAt datetime2 NOT NULL DEFAULT GETUTCDATE()
);

-- Webhook Events Log
CREATE TABLE KeyCrmWebhookEvents (
    Id int IDENTITY(1,1) PRIMARY KEY,
    EventType nvarchar(50) NOT NULL,
    PayloadJson nvarchar(max) NOT NULL,
    ProcessedAt datetime2 NULL,
    ProcessingStatus nvarchar(20) NOT NULL, -- 'Pending', 'Processed', 'Error'
    ErrorMessage nvarchar(max) NULL,
    ReceivedAt datetime2 NOT NULL DEFAULT GETUTCDATE()
);
```

## API Endpoints

### Webhook Endpoints

```
POST /api/keycrm/webhook/order-created
POST /api/keycrm/webhook/order-updated
POST /api/keycrm/webhook/order-status-changed
POST /api/keycrm/webhook/payment-created
POST /api/keycrm/webhook/payment-updated
POST /api/keycrm/webhook/buyer-created
POST /api/keycrm/webhook/buyer-updated
```

### Manual Sync Endpoints

```
POST /api/keycrm/sync/orders/{orderId}
POST /api/keycrm/sync/customers/{customerId}
POST /api/keycrm/sync/articles/{articleId}
GET /api/keycrm/sync/status
```

### SignalR Hubs

```
/hubs/keycrm - Real-time notifications for CRM events
```

## Error Handling Strategy

### Retry Logic
- Exponential backoff for failed API calls
- Maximum 3 retry attempts
- Dead letter queue for failed webhooks

### Validation
- Schema validation for webhook payloads
- Business rule validation before sync
- Duplicate detection and prevention

### Monitoring
- Health checks for KeyCRM API connectivity
- Performance metrics and logging
- Alert system for sync failures

## Security Considerations

### Authentication
- Bearer token authentication for KeyCRM API
- Webhook signature validation
- Rate limiting protection

### Data Protection
- Sensitive data encryption in transit
- PII handling compliance
- Audit logging for all operations

## Testing Strategy

### Unit Tests
- Service layer testing with mocked dependencies
- Webhook processing logic validation
- Error handling scenarios

### Integration Tests
- End-to-end sync scenarios
- Webhook delivery testing
- Performance and load testing

### Monitoring
- Real-time sync status dashboard
- Error rate monitoring
- Performance metrics tracking

## Deployment Considerations

### Environment Configuration
- Separate KeyCRM API keys per environment
- Feature flags for gradual rollout
- Configuration validation on startup

### Rollback Strategy
- Database migration rollback scripts
- Service deployment rollback plan
- Data consistency verification

## Success Metrics

### Performance
- Sync latency < 5 seconds for real-time events
- 99.9% webhook processing success rate
- < 1% data inconsistency rate

### Business Value
- Reduced manual data entry
- Improved customer experience
- Real-time inventory visibility
- Enhanced order tracking

## Timeline

### Phase 1 (Weeks 1-2): Foundation
- Service layer implementation
- Basic webhook handling
- Configuration setup

### Phase 2 (Weeks 3-4): Core Features
- Order synchronization
- Customer synchronization
- Basic error handling

### Phase 3 (Weeks 5-6): Advanced Features
- Real-time notifications
- Conflict resolution
- Performance optimization

### Phase 4 (Week 7): Testing & Deployment
- Integration testing
- Performance testing
- Production deployment

## Risk Mitigation

### Technical Risks
- API rate limiting → Implement backoff strategy
- Network connectivity → Retry logic and queuing
- Data conflicts → Timestamp-based resolution

### Business Risks
- Data inconsistency → Comprehensive validation
- Performance impact → Asynchronous processing
- User adoption → Training and documentation
