# VMS API - Copilot Instructions

## Project Overview

This is a FastAPI-based Vendor Management System (VMS) that manages currencies, customers, orders, and inventory with SQL Server as the primary database.

## Architecture Patterns

### Data Layer Structure

- **Models** (`app/models/`): SQLAlchemy ORM models with specific SQL Server field naming (e.g., `CustomerID`, `CompanyName`)
- **Schemas** (`app/schemas/`): Pydantic models for request/response validation, following the pattern: `Base`, `Create`, `Update`, and full schemas
- **Routers** (`app/routers/`): FastAPI route handlers with consistent pagination (`skip`, `limit`) and filtering patterns

### Database Configuration

- Uses `pymssql` driver for SQL Server connectivity with `mssql+pymssql://` connection strings
- Graceful database connection handling in `main.py` - API starts even if DB is unavailable
- Alembic migrations configured with models imported in `alembic/env.py`

### Development Workflow Commands

```bash
# Setup (Windows PowerShell)
.\setup.ps1                    # Automated setup script

# Development
python run.py                  # Start with custom runner (port 8000, auto-reload in DEBUG mode)
uvicorn app.main:app --reload  # Alternative start method

# Database
alembic upgrade head           # Apply migrations
alembic revision --autogenerate -m "description"  # Generate migrations

# Testing
python test_setup.py           # Validate setup
pytest tests/                  # Run test suite (uses SQLite for testing)

# Docker
docker-compose up              # Full stack with SQL Server container
```

## Project-Specific Conventions

### Field Naming

- Database fields use PascalCase (`CustomerID`, `CompanyName`) matching existing SQL Server schema
- API responses maintain this naming for consistency with legacy systems
- Reference `table_schemas.csv` for complete field specifications

### Router Patterns

- All routers use `/api/v1` prefix via `settings.API_V1_STR`
- Standard CRUD endpoints with pagination: `skip` (≥0), `limit` (1-1000, default 50)
- Query parameters for filtering (e.g., `company_name`, `city` in customers)
- Consistent error handling with FastAPI HTTPException

### Configuration Management

- Environment-driven config in `app/config.py` using `python-decouple`
- Copy `.env.example` to `.env` for local development
- Database URL format: `mssql+pymssql://username:password@server/database`

### Model Relationships

- SQLAlchemy relationships defined (e.g., `Customer.orders`)
- Foreign keys follow existing schema conventions
- Models include `__repr__` methods for debugging

## Key Integration Points

### External Systems

- **Binotel integration**: Customer model includes `CustomerIdAtBinotel`, `LastCallingDateAtBinotel` fields
- **Currency management**: Daily exchange rate tracking for EUR/USD/RUB with difference calculations

### Cross-Component Communication

- Dependency injection pattern: `db: Session = Depends(get_db)`
- CORS middleware configured for multiple origins via `BACKEND_CORS_ORIGINS`
- Centralized settings in `app.config.settings`

## Development Notes

- Tests use SQLite override for `get_db` dependency
- Production deployment expects SQL Server with specific table structure
- Graceful degradation: API starts without database but operations will fail
- PowerShell scripts provided for Windows development environment

## Testing Requirements

### Comprehensive Test Coverage

When adding new features, always include comprehensive tests:

- **Unit tests**: Test individual functions and methods in isolation
- **Integration tests**: Test API endpoints with database interactions
- **Schema validation tests**: Verify Pydantic models handle edge cases
- **Error handling tests**: Test all error conditions and HTTP status codes

### Test Structure Pattern

Follow the existing test patterns in `tests/`:

```python
# tests/test_[module_name].py
def test_create_[entity]_success():
    """Test successful entity creation"""

def test_create_[entity]_validation_error():
    """Test validation error handling"""

def test_get_[entity]_pagination():
    """Test pagination functionality"""
```

### Test Database Setup

- Use SQLite in-memory database for tests (`sqlite:///./test.db`)
- Override `get_db` dependency for isolated test environment
- Clean up test data between test runs

## Code Organization

### Folder Structure Maintenance

Keep the project structure clean and consistent:

```text
app/
├── models/          # SQLAlchemy ORM models only
├── schemas/         # Pydantic models only
├── routers/         # FastAPI route handlers only
└── [new_modules]/   # Follow same pattern for new features
```

### File Naming Conventions

- **Models**: Singular entity names (`customer.py`, `order.py`)
- **Schemas**: Match model names (`customer.py`, `order.py`)
- **Routers**: Plural entity names (`customers.py`, `orders.py`)
- **Tests**: Prefix with `test_` (`test_customers.py`, `test_orders.py`)

### Module Organization Rules

- One main entity per file (Customer model in `customer.py`)
- Related schemas in corresponding schema file
- Import all models in `models/__init__.py` for Alembic
- Keep routers focused on single entity CRUD operations

## Language Support

### Bilingual Documentation (English/Ukrainian)

When writing summaries, commit messages, or documentation, provide bilingual support:

- **English**: Primary language for code comments and technical documentation
- **Ukrainian**: Use for work summaries, progress reports, and user-facing content
- Format bilingual content as: "English description / Українське описання"

**Examples:**

- Commit messages: `feat: add customer pagination / додано пагінацію клієнтів`
- Work summaries: `Implemented currency exchange rate tracking / Реалізовано відстеження курсів валют`
- API descriptions: `Retrieve customer list / Отримати список клієнтів`

**Ukrainian technical terms:**

- API → АПІ
- Database → База даних
- Customer → Клієнт
- Order → Замовлення
- Currency → Валюта
- Pagination → Пагінація
- Authentication → Автентифікація
- Configuration → Конфігурація
