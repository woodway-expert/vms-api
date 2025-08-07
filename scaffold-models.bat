@echo off
echo EF Core Scaffolding Script
echo ==========================

echo.
echo This script will scaffold all models from your MSSQL database.
echo It will OVERWRITE existing models in Data/Models folder.
echo.

set /p connectionString="Enter your connection string: "

if "%connectionString%"=="" (
    echo No connection string provided. Exiting...
    pause
    exit /b 1
)

echo.
echo Scaffolding models from database...
echo.

dotnet ef dbcontext scaffold "%connectionString%" Microsoft.EntityFrameworkCore.SqlServer -o Data/Models -f --context AppDbContext --context-dir Data

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ✅ Scaffolding completed successfully!
    echo Models have been generated in Data/Models folder.
    echo AppDbContext has been updated in Data folder.
) else (
    echo.
    echo ❌ Scaffolding failed. Please check your connection string and database access.
)

echo.
pause
