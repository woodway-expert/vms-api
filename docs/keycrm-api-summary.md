# KeyCRM API Documentation Summary

## Overview

KeyCRM provides a comprehensive REST API for managing e-commerce and CRM operations. The API supports full CRUD operations for orders, customers, products, and other business entities.

## Base URL and Authentication

- **Base URL**: `https://openapi.keycrm.app/v1`
- **Authentication**: Bearer token (API Key)
- **Rate Limit**: 60 requests per minute per IP address
- **Time Zone**: All timestamps are in UTC (GMT+0)

## Core Entities

### 1. Orders (`/order`)

**Supported Operations:**
- `GET /order` - List orders with pagination and filtering
- `POST /order` - Create new order
- `POST /order/import` - Bulk create orders (up to 50 per request)
- `GET /order/{orderId}` - Get order by ID
- `PUT /order/{orderId}` - Update existing order
- `POST /order/{orderId}/payment` - Add payment to order
- `PUT /order/{orderId}/payment/{paymentId}` - Update payment
- `POST /order/{orderId}/expense` - Add expense to order
- `PUT /order/{orderId}/expense/{expenseId}` - Update expense
- `POST /order/{orderId}/tag/{tagId}` - Add tag to order
- `DELETE /order/{orderId}/tag/{tagId}` - Remove tag from order
- `POST /order/{orderId}/attachment/{fileId}` - Add file to order
- `DELETE /order/{orderId}/attachment/{fileId}` - Remove file from order

**Key Features:**
- Full order lifecycle management
- Payment tracking with multiple payment methods
- Shipping and delivery management
- UTM tracking for marketing analytics
- Custom fields support
- File attachments
- Tags and categorization

### 2. Buyers/Customers (`/buyer`)

**Supported Operations:**
- `GET /buyer` - List buyers with filtering
- `POST /buyer` - Create new buyer
- `GET /buyer/{buyerId}` - Get buyer by ID
- `PUT /buyer/{buyerId}` - Update buyer
- `DELETE /buyer/{buyerId}` - Delete buyer

**Key Features:**
- Customer profile management
- Multiple contact methods (email, phone)
- Company associations
- Loyalty program integration
- Shipping addresses
- Custom fields
- Manager assignments

### 3. Companies (`/company`)

**Supported Operations:**
- `GET /company` - List companies
- `POST /company` - Create new company
- `GET /company/{companyId}` - Get company by ID
- `PUT /company/{companyId}` - Update company
- `DELETE /company/{companyId}` - Delete company

**Key Features:**
- B2B customer management
- Banking details
- Manager assignments
- Custom fields
- Buyer associations

### 4. Products and Offers (`/product`, `/offers`)

**Supported Operations:**
- `GET /product` - List products
- `POST /product` - Create product
- `GET /product/{productId}` - Get product by ID
- `PUT /product/{productId}` - Update product
- `GET /offers` - List product variants/offers
- `POST /offers` - Create offer
- `GET /offers/{offerId}` - Get offer by ID
- `PUT /offers/{offerId}` - Update offer
- `GET /offers/stocks` - Get stock levels

**Key Features:**
- Product catalog management
- Variant/offer management
- Inventory tracking
- Pricing management
- Product categories
- Properties and attributes
- Images and attachments

### 5. Pipelines/Funnels (`/pipelines`)

**Supported Operations:**
- `GET /pipelines` - List pipeline cards
- `POST /pipelines` - Create pipeline card
- `GET /pipelines/{cardId}` - Get card by ID
- `PUT /pipelines/{cardId}` - Update card
- `DELETE /pipelines/{cardId}` - Delete card

**Key Features:**
- Sales funnel management
- Lead tracking
- Stage management
- Task assignments
- Activity tracking

### 6. Storage/Files (`/storage`)

**Supported Operations:**
- `GET /storage` - List files
- `POST /storage/upload` - Upload file
- `GET /storage/attachment/{entityType}/{entityId}` - Get entity files

**Key Features:**
- File upload and management
- Entity attachments
- File type validation
- Size limits (10MB max)

### 7. Custom Fields (`/custom-fields`)

**Supported Operations:**
- `GET /custom-fields` - List custom fields with options

**Key Features:**
- Dynamic field definitions
- Multiple field types (text, number, date, select, etc.)
- Entity-specific fields
- Validation rules

## Reference Data Endpoints

### Order Management
- `GET /order/tag` - Order tags
- `GET /order/source` - Order sources
- `GET /order/status` - Order statuses
- `GET /order/payment-method` - Payment methods
- `GET /order/expense-type` - Expense types
- `GET /order/delivery-service` - Delivery services
- `GET /order/product-status` - Product statuses

### Product Management
- `GET /product/category` - Product categories

## Webhook Support

KeyCRM supports webhooks for real-time event notifications. Based on the API structure, webhooks are likely available for:

- Order created/updated
- Payment status changes
- Buyer/customer updates
- Product/inventory changes
- Pipeline card updates

## Advanced Features

### Filtering and Sorting
- Complex filtering using query parameters
- Multiple sort options
- Date range filtering
- Status-based filtering

### Pagination
- Limit/offset pagination
- Page-based navigation
- Total count information
- Navigation URLs

### Includes/Relationships
- Related entity inclusion using `include` parameter
- Nested data retrieval
- Relationship mapping

### Bulk Operations
- Order import (up to 50 orders)
- Batch processing support

## Data Models

### Order Structure
```json
{
  "id": 123,
  "source_id": 1,
  "source_uuid": "external-id",
  "buyer_comment": "Customer note",
  "manager_comment": "Internal note",
  "status_id": 1,
  "payment_status": "paid",
  "total_price": 123.45,
  "buyer": { /* buyer object */ },
  "products": [ /* product array */ ],
  "payments": [ /* payment array */ ],
  "shipping": { /* shipping object */ },
  "marketing": { /* UTM data */ },
  "custom_fields": [ /* custom field array */ ]
}
```

### Product/Offer Structure
```json
{
  "id": 456,
  "name": "Product Name",
  "sku": "SKU123",
  "price": 99.99,
  "purchased_price": 50.00,
  "quantity": 100,
  "properties": [ /* variant properties */ ],
  "category_id": 1,
  "images": [ /* image URLs */ ]
}
```

### Buyer Structure
```json
{
  "id": 789,
  "full_name": "John Doe",
  "email": ["john@example.com"],
  "phone": ["+1234567890"],
  "company": { /* company object */ },
  "manager": { /* manager object */ },
  "loyalty": [ /* loyalty programs */ ],
  "shipping": [ /* addresses */ ]
}
```

## Integration Best Practices

### Authentication
- Store API key securely
- Use environment-specific keys
- Implement token refresh if needed

### Error Handling
- Handle rate limiting (429 responses)
- Implement retry logic
- Log API errors appropriately

### Data Synchronization
- Use timestamps for conflict resolution
- Implement idempotent operations
- Validate data before sending

### Performance
- Use pagination for large datasets
- Implement caching where appropriate
- Monitor API usage and limits

## Security Considerations

- API key protection
- HTTPS-only communication
- Input validation
- Rate limiting compliance
- Webhook signature verification (if available)

This API provides comprehensive e-commerce and CRM functionality suitable for full two-way integration with warehouse management systems.
