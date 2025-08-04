# VMS API

A FastAPI-based Vendor Management System API that provides endpoints for managing currencies, customers, orders, and inventory.

## Features

- **Currency Management**: Track exchange rates for EUR, USD, and RUB
- **Customer Management**: Manage customer information, contacts, and statistics
- **Order Management**: Handle orders, payments, and shipments
- **Inventory Management**: Track goods, stock levels, and sales
- **Sub-Positions**: Manage order line items and positions

## Quick Start

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Set Environment Variables**:
   Copy `.env.example` to `.env` and configure your database connection:
   ```bash
   cp .env.example .env
   ```

3. **Run Database Migrations**:
   ```bash
   alembic upgrade head
   ```

4. **Start the API**:
   ```bash
   uvicorn app.main:app --reload
   ```

5. **Access API Documentation**:
   - Swagger UI: http://localhost:8000/docs
   - ReDoc: http://localhost:8000/redoc

## Project Structure

```
vms-api/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application entry point
│   ├── config.py            # Configuration settings
│   ├── database.py          # Database connection setup
│   ├── models/              # SQLAlchemy database models
│   │   ├── __init__.py
│   │   ├── currency.py
│   │   ├── customer.py
│   │   ├── order.py
│   │   ├── inventory.py
│   │   └── subposition.py
│   ├── schemas/             # Pydantic request/response schemas
│   │   ├── __init__.py
│   │   ├── currency.py
│   │   ├── customer.py
│   │   ├── order.py
│   │   ├── inventory.py
│   │   └── subposition.py
│   ├── routers/             # API route handlers
│   │   ├── __init__.py
│   │   ├── currencies.py
│   │   ├── customers.py
│   │   ├── orders.py
│   │   ├── inventory.py
│   │   └── subpositions.py
│   └── services/            # Business logic
│       ├── __init__.py
│       ├── currency_service.py
│       ├── customer_service.py
│       ├── order_service.py
│       ├── inventory_service.py
│       └── subposition_service.py
├── alembic/                 # Database migrations
├── tests/                   # Test files
├── requirements.txt         # Python dependencies
├── .env.example            # Environment variables template
└── README.md               # This file
```

## API Endpoints

### Currencies
- `GET /api/v1/currencies/` - List all currency rates
- `GET /api/v1/currencies/{id}` - Get specific currency rate
- `POST /api/v1/currencies/` - Create new currency rate
- `PUT /api/v1/currencies/{id}` - Update currency rate
- `DELETE /api/v1/currencies/{id}` - Delete currency rate

### Customers
- `GET /api/v1/customers/` - List all customers
- `GET /api/v1/customers/{id}` - Get specific customer
- `POST /api/v1/customers/` - Create new customer
- `PUT /api/v1/customers/{id}` - Update customer
- `DELETE /api/v1/customers/{id}` - Delete customer

### Orders
- `GET /api/v1/orders/` - List all orders
- `GET /api/v1/orders/{id}` - Get specific order
- `POST /api/v1/orders/` - Create new order
- `PUT /api/v1/orders/{id}` - Update order
- `DELETE /api/v1/orders/{id}` - Delete order

### Inventory
- `GET /api/v1/inventory/` - List all goods
- `GET /api/v1/inventory/{id}` - Get specific good
- `POST /api/v1/inventory/` - Create new good
- `PUT /api/v1/inventory/{id}` - Update good
- `DELETE /api/v1/inventory/{id}` - Delete good

### Sub-Positions
- `GET /api/v1/subpositions/` - List all sub-positions
- `GET /api/v1/subpositions/{id}` - Get specific sub-position
- `POST /api/v1/subpositions/` - Create new sub-position
- `PUT /api/v1/subpositions/{id}` - Update sub-position
- `DELETE /api/v1/subpositions/{id}` - Delete sub-position

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `DATABASE_URL` | Database connection string | `mssql+pymssql://user:password@server/database` |
| `SECRET_KEY` | JWT secret key | `your-secret-key` |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | JWT token expiration | `30` |
| `DEBUG` | Enable debug mode | `False` |

## Database Support

The API supports both SQL Server and PostgreSQL databases. Configure your connection string in the `.env` file:

**SQL Server:**
```
DATABASE_URL=mssql+pymssql://username:password@server/database
```

**PostgreSQL:**
```
DATABASE_URL=postgresql://username:password@server/database
```

## Development

1. **Install development dependencies**:
   ```bash
   pip install -r requirements-dev.txt
   ```

2. **Run tests**:
   ```bash
   pytest
   ```

3. **Format code**:
   ```bash
   black app/
   ```

4. **Lint code**:
   ```bash
   flake8 app/
   ```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Run tests and ensure they pass
6. Submit a pull request

## License

This project is licensed under the MIT License.

