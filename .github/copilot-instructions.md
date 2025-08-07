
# VMS API Copilot Instructions

## Project Overview

This is a **Warehouse Management System API** built with **ASP.NET Core 8**. It integrates with a **pre-existing MSSQL 2019 database** (see `/schema/mssql_structure.md`). The API exposes REST endpoints for managing articles, customers, orders, and related warehouse operations.

## Architecture & Key Patterns

- **Controllers** (`/Controllers`): Handle HTTP requests, use `[ApiController]`, `[Route("api/[controller]")]`, and structured logging (`ILogger<T>`). All controller actions use try-catch for error handling and return appropriate HTTP status codes.
- **Services** (`/Services`): Business logic layer, always interface-driven (e.g., `ICustomerService`/`CustomerService`). All methods are async and use EF `.Include()` for related data. Register all services with `AddScoped` in `Program.cs`.
- **Data** (`/Data`): Entity Framework Core models and `AppDbContext`. Models are manually curated to match the existing DB schema—**do not use migrations**. See `/schema/mssql_structure.md` for schema details.
- **DTOs** (`/DTOs`): Data transfer objects define API contracts. Use DTOs for create/update/read operations (see `CustomerDtos.cs`, `ArticleDtos.cs`).
- **Middleware** (`/Middleware/GlobalExceptionMiddleware.cs`): Global exception handler returns structured JSON error responses for all unhandled exceptions.

## Database Integration

- **Database-First**: Models are manually created to match the existing MSSQL schema. Never use EF migrations. To update models, run `scaffold-models.bat` (overwrites `/Data/Models`).
- **Connection Strings**: Set in `appsettings.Development.json` and `appsettings.json`. Always use `Trusted_Connection=True;TrustServerCertificate=True;`.

## Development Workflow

**Build & Run:**
```pwsh
dotnet restore
dotnet build
dotnet run
```

**API Access:**
- Swagger UI: `https://localhost:7000/`
- Health check: `GET /health`

**Scaffolding Models:**
- Use `scaffold-models.bat` to regenerate models from the database. This will overwrite `/Data/Models` and update `AppDbContext`.

## Project-Specific Conventions

- **Entity Naming:** Database IDs use suffixes (`CustomerID`, `OrderID`, etc). Entity properties match DB column names exactly.
- **Service Methods:** Always use `Async` suffix. Always include related entities with `.Include()` in queries.
- **Error Handling:** All errors are logged and returned as structured JSON. Controllers use try-catch; global middleware handles unhandled exceptions.
- **Business Rules:**
  - Customer recalculation date is updated on modifications
  - Orders have complex state (status, payment, shipment)
  - Warehouse operations track managers and timestamps
  - Pricing supports multiple currencies and markups

## Key Files & Examples

- `/Data/AppDbContext.cs`: EF model configuration
- `/schema/mssql_structure.md`: Full DB schema
- `/Services/CustomerService.cs`: Service layer pattern
- `/Controllers/CustomersController.cs`: Controller pattern
- `/Middleware/GlobalExceptionMiddleware.cs`: Error handling
- `/DTOs/CustomerDtos.cs`, `/DTOs/ArticleDtos.cs`: DTO conventions

## Integration & Extending

- **New Entity:** Add to `AppDbContext.cs` (no migrations)
- **New Service:** Create interface + implementation, register in DI
- **New Controller:** Follow existing controller/service pattern
- **New DTOs:** Add to `/DTOs` and use in controllers

**Always consider the complex warehouse domain and existing database constraints when making changes.**
