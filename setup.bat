@echo off
echo VMS API - Setup Instructions
echo =================================

echo.
echo 1. Install .NET 8 SDK
echo    Download from: https://dotnet.microsoft.com/download/dotnet/8.0
echo.

echo 2. Update Database Connection String
echo    Edit appsettings.json and appsettings.Development.json
echo    Replace YOUR_SERVER and YOUR_DB with your actual values
echo.

echo 3. Restore NuGet Packages
echo    Run: dotnet restore
echo.

echo 4. Build the Project
echo    Run: dotnet build
echo.

echo 5. Run the Application
echo    Run: dotnet run
echo.

echo 6. Optional: Scaffold All Models from Database
echo    Run the following command (replace connection string):
echo    dotnet ef dbcontext scaffold "Server=YOUR_SERVER;Database=YOUR_DB;Trusted_Connection=True;TrustServerCertificate=True;" Microsoft.EntityFrameworkCore.SqlServer -o Data/Models -f --context AppDbContext --context-dir Data
echo.

echo Press any key to continue...
pause
