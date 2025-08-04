@echo off
echo Setting up VMS API...

echo.
echo 1. Installing Python dependencies...
pip install -r requirements.txt

echo.
echo 2. Creating .env file from template...
if not exist .env (
    copy .env.example .env
    echo Please edit .env file with your database configuration
) else (
    echo .env file already exists
)

echo.
echo 3. Testing the installation...
python -c "from app.main import app; print('Installation successful!')"

echo.
echo Setup complete!
echo.
echo To start the API:
echo   python run.py
echo.
echo Or with uvicorn directly:
echo   uvicorn app.main:app --reload
echo.
echo API Documentation will be available at:
echo   http://localhost:8000/docs
pause
