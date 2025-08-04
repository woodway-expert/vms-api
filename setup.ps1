#!/usr/bin/env pwsh

Write-Host "Setting up VMS API..." -ForegroundColor Green

Write-Host "`n1. Installing Python dependencies..." -ForegroundColor Yellow
pip install -r requirements.txt

Write-Host "`n2. Creating .env file from template..." -ForegroundColor Yellow
if (-not (Test-Path .env)) {
    Copy-Item .env.example .env
    Write-Host "Please edit .env file with your database configuration" -ForegroundColor Cyan
}
else {
    Write-Host ".env file already exists" -ForegroundColor Green
}

Write-Host "`n3. Testing the installation..." -ForegroundColor Yellow
try {
    python -c "from app.main import app; print('Installation successful!')"
    Write-Host "Installation test passed!" -ForegroundColor Green
}
catch {
    Write-Host "Installation test failed. Please check the error above." -ForegroundColor Red
}

Write-Host "`nSetup complete!" -ForegroundColor Green
Write-Host "`nTo start the API:" -ForegroundColor Cyan
Write-Host "  python run.py" -ForegroundColor White
Write-Host "`nOr with uvicorn directly:" -ForegroundColor Cyan
Write-Host "  uvicorn app.main:app --reload" -ForegroundColor White
Write-Host "`nAPI Documentation will be available at:" -ForegroundColor Cyan
Write-Host "  http://localhost:8000/docs" -ForegroundColor White

Read-Host "`nPress Enter to continue"
