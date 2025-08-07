# VMS API - Warehouse Management System API

A clean ASP.NET Core Web API (.NET 8) that integrates with an existing MSSQL 2019 database for a warehouse management system.

## 🏗️ Project Structure

```
/vms-api
├── /Controllers
│   ├── ArticlesController.cs
│   ├── CustomersController.cs
│   └── OrdersController.cs
├── /Data
│   ├── AppDbContext.cs
│   └── /Models
│       ├── Article.cs
│       ├── Customer.cs
│       ├── Order.cs
│       ├── Manager.cs
│       ├── LinkAccounting.cs
│       ├── Position.cs
│       └── SupportingModels.cs
├── /Services
│   ├── IArticleService.cs
│   ├── ArticleService.cs
│   ├── ICustomerService.cs
│   ├── CustomerService.cs
│   ├── IOrderService.cs
│   └── OrderService.cs
├── /schema
│   └── mssql_structure.md
│   └── [CSV files with actual data]
├── appsettings.json
├── appsettings.Development.json
├── Program.cs
└── vms-api.csproj
```

## 🚀 Getting Started

### Prerequisites

- .NET 8 SDK
- SQL Server or SQL Server Express
- Access to the existing VMS database

### 1. Clone and Setup

```bash
git clone <repository-url>
cd vms-api
```

### 2. Configure Database Connection

Update the connection string in `appsettings.json` and `appsettings.Development.json`:

```json
{
  "ConnectionStrings": {
    "DefaultConnection": "Server=YOUR_SERVER;Database=YOUR_DB;Trusted_Connection=True;TrustServerCertificate=True;"
  }
}
```

### 3. Install Dependencies

```bash
dotnet restore
```

### 4. Scaffold Models from Database (Optional)

If you want to generate all models from your database, you can use EF Core scaffolding:

```bash
dotnet ef dbcontext scaffold "Server=YOUR_SERVER;Database=YOUR_DB;Trusted_Connection=True;TrustServerCertificate=True;" Microsoft.EntityFrameworkCore.SqlServer -o Data/Models -f --context AppDbContext --context-dir Data
```

**Note:** This will overwrite the existing models. The current implementation includes the most important models manually created based on the schema.

### 5. Run the Application

```bash
dotnet run
```

The API will be available at:
- HTTPS: https://localhost:7000
- HTTP: http://localhost:5000
- Swagger UI: https://localhost:7000/swagger

## 📋 API Endpoints

### Articles
- `GET /api/articles` - Get all articles
- `GET /api/articles/{id}` - Get article by ID
- `POST /api/articles` - Create new article
- `PUT /api/articles/{id}` - Update article
- `DELETE /api/articles/{id}` - Delete article
- `GET /api/articles/search?searchTerm={term}` - Search articles

### Customers
- `GET /api/customers` - Get all customers
- `GET /api/customers/{id}` - Get customer by ID
- `POST /api/customers` - Create new customer
- `PUT /api/customers/{id}` - Update customer
- `DELETE /api/customers/{id}` - Delete customer
- `GET /api/customers/search?searchTerm={term}` - Search customers
- `GET /api/customers/{id}/orders` - Get customer orders

### Orders
- `GET /api/orders` - Get all orders
- `GET /api/orders/{id}` - Get order by ID
- `POST /api/orders` - Create new order
- `PUT /api/orders/{id}` - Update order
- `DELETE /api/orders/{id}` - Delete order
- `GET /api/orders/customer/{customerId}` - Get orders by customer
- `GET /api/orders/date-range?startDate={date}&endDate={date}` - Get orders by date range
- `GET /api/orders/status/{status}` - Get orders by status

## 🗃️ Database Schema

The database contains complex warehouse management data including:

- **Articles** - Product catalog
- **Customers** - Client information with contact details
- **Orders** - Sales orders with positions and sub-positions
- **Managers** - System users
- **Suppliers** - Supplier information
- **Stocks** - Warehouse locations
- **Pallets, Bundles, Boads, Rolls** - Inventory items
- **Categories, Breeds, Qualities** - Product classifications

See `/schema/mssql_structure.md` for complete database documentation.

## 🏛️ Architecture

### Clean Architecture Principles
- **Controllers** - Handle HTTP requests and responses
- **Services** - Business logic layer
- **Data** - Data access layer with Entity Framework Core
- **Models** - Database entities

### Key Features
- Entity Framework Core with Code-First approach
- Dependency Injection
- Async/await pattern
- Comprehensive error handling
- Swagger documentation
- Structured logging

## 🔧 Configuration

### Connection Strings
Update connection strings in `appsettings.json` for different environments:

```json
{
  "ConnectionStrings": {
    "DefaultConnection": "Server=localhost;Database=VMS_DB;Integrated Security=true;TrustServerCertificate=true;"
  }
}
```

### Logging
Configured for comprehensive logging including EF Core SQL commands in development.

## 🚀 Development

### Adding New Controllers
1. Create interface in `/Services`
2. Implement service class
3. Register in `Program.cs`
4. Create controller in `/Controllers`

### Database Migrations
If you modify the models:

```bash
dotnet ef migrations add MigrationName
dotnet ef database update
```

## 📦 Dependencies

- Microsoft.AspNetCore.OpenApi (8.0.0)
- Microsoft.EntityFrameworkCore.SqlServer (8.0.11)
- Microsoft.EntityFrameworkCore.Tools (8.0.11)
- Microsoft.EntityFrameworkCore.Design (8.0.11)
- Swashbuckle.AspNetCore (6.4.0)

## 🔒 Security Considerations

- Update connection strings with appropriate security
- Implement authentication/authorization as needed
- Validate input data
- Use HTTPS in production
- Implement rate limiting if required

## 📝 Next Steps

1. **Authentication & Authorization** - Add JWT or similar
2. **Validation** - Implement model validation attributes
3. **Mapping** - Add AutoMapper for DTOs
4. **Caching** - Implement response caching
5. **Testing** - Add unit and integration tests
6. **Documentation** - Enhance API documentation
7. **Full Models** - Scaffold all database tables if needed

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

This project is licensed under the MIT License.
