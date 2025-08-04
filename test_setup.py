#!/usr/bin/env python3
"""
Simple test script to validate the VMS API setup
"""

print("🔍 Testing VMS API Setup...")

try:
    print("1. Testing basic imports...")
    import fastapi

    print("   ✅ FastAPI imported successfully")

    import sqlalchemy

    print("   ✅ SQLAlchemy imported successfully")

    import pydantic

    print("   ✅ Pydantic imported successfully")

    print("\n2. Testing app configuration...")
    from app.config import settings

    print("   ✅ Config imported successfully")
    print(f"   📊 API Version: {settings.API_V1_STR}")
    print(f"   🐛 Debug Mode: {settings.DEBUG}")

    print("\n3. Testing database setup...")
    from app.database import Base, engine

    print("   ✅ Database setup imported successfully")

    print("\n4. Testing models...")
    from app.models import currency, customer, order

    print("   ✅ Models imported successfully")

    print("\n5. Testing schemas...")
    from app.schemas import currency as currency_schema

    print("   ✅ Schemas imported successfully")

    print("\n6. Testing routers...")
    from app.routers import currencies, customers, orders

    print("   ✅ Routers imported successfully")

    print("\n7. Testing main app...")
    from app.main import app

    print("   ✅ Main app imported successfully")
    print(f"   🎯 App Title: {app.title}")

    print("\n🎉 All tests passed! Your VMS API is ready to run.")
    print("\n🚀 To start the API, run:")
    print("   python run.py")
    print("\n📚 Then visit: http://localhost:8000/docs")

except ImportError as e:
    print(f"\n❌ Import Error: {e}")
    print("   Some dependencies might be missing.")

except Exception as e:
    print(f"\n❌ Unexpected Error: {e}")
    import traceback

    traceback.print_exc()

print("\n" + "=" * 50)
