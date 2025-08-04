#!/usr/bin/env python3
"""
VMS API Demo Script

This script demonstrates the basic functionality of the VMS API by:
1. Creating sample data
2. Retrieving data
3. Updating data
4. Showing relationships

Run this after starting the API server.
"""

import requests
import json
from datetime import datetime, date
from uuid import uuid4

# API base URL
BASE_URL = "http://localhost:8000/api/v1"


def demo_currencies():
    """Demonstrate currency operations"""
    print("\n=== Currency Operations Demo ===")

    # Create a currency rate
    currency_data = {
        "CurrencyDate": "2024-01-15T10:00:00",
        "CourseEur": 1.08,
        "CourseUsd": 0.92,
        "CourseRub": 88.5,
        "Comments": "Demo currency rate",
        "NbuEur": 1.10,
        "NbuUsd": 0.90,
        "NbuRub": 90.0,
    }

    print("Creating currency rate...")
    response = requests.post(f"{BASE_URL}/currencies/", json=currency_data)
    if response.status_code == 200:
        currency = response.json()
        print(f"✓ Created currency rate ID: {currency['CourseCurrencyID']}")

        # Get the currency rate
        currency_id = currency["CourseCurrencyID"]
        response = requests.get(f"{BASE_URL}/currencies/{currency_id}")
        if response.status_code == 200:
            print(
                f"✓ Retrieved currency rate: EUR={currency['CourseEur']}, USD={currency['CourseUsd']}"
            )

        return currency_id
    else:
        print(f"✗ Error creating currency: {response.text}")
        return None


def demo_customers():
    """Demonstrate customer operations"""
    print("\n=== Customer Operations Demo ===")

    # Create a customer
    customer_data = {
        "CompanyName": "Demo Tech Solutions",
        "ContactName": "Jane Smith",
        "Phone": "+1-555-0123",
        "EMail": "jane@demotech.com",
        "City": "New York",
        "Address": "123 Demo Street",
        "PostalCode": "10001",
    }

    print("Creating customer...")
    response = requests.post(f"{BASE_URL}/customers/", json=customer_data)
    if response.status_code == 200:
        customer = response.json()
        print(
            f"✓ Created customer ID: {customer['CustomerID']} - {customer['CompanyName']}"
        )

        # Update customer
        update_data = {"Phone": "+1-555-0124"}
        customer_id = customer["CustomerID"]
        response = requests.put(f"{BASE_URL}/customers/{customer_id}", json=update_data)
        if response.status_code == 200:
            updated_customer = response.json()
            print(f"✓ Updated customer phone: {updated_customer['Phone']}")

        return customer_id
    else:
        print(f"✗ Error creating customer: {response.text}")
        return None


def demo_orders(customer_id):
    """Demonstrate order operations"""
    print("\n=== Order Operations Demo ===")

    if not customer_id:
        print("No customer available for order demo")
        return None

    # Create an order
    order_data = {
        "CustomerID": customer_id,
        "NumberOrder": f"ORD-{datetime.now().strftime('%Y%m%d')}-001",
        "OrderDate": datetime.now().isoformat(),
        "Descriptions": "Demo order for testing",
        "OrderSum": 1500.00,
        "OrderStatus": 1,
        "PaymentType": 1,
        "IsActive": True,
        "CountSoldItems": 5,
    }

    print("Creating order...")
    response = requests.post(f"{BASE_URL}/orders/", json=order_data)
    if response.status_code == 200:
        order = response.json()
        print(f"✓ Created order: {order['NumberOrder']} for ${order['OrderSum']}")
        return order["OrderID"]
    else:
        print(f"✗ Error creating order: {response.text}")
        return None


def demo_api_info():
    """Show API information"""
    print("\n=== API Information ===")

    # Root endpoint
    response = requests.get("http://localhost:8000/")
    if response.status_code == 200:
        info = response.json()
        print(f"✓ API: {info['message']}")
        print(f"✓ Version: {info['version']}")
        print(f"✓ Documentation: http://localhost:8000{info['docs']}")

    # Health check
    response = requests.get("http://localhost:8000/health")
    if response.status_code == 200:
        health = response.json()
        print(f"✓ Health: {health['status']}")


def main():
    """Run the complete demo"""
    print("VMS API Demo Script")
    print("=" * 50)

    try:
        # Check if API is running
        response = requests.get("http://localhost:8000/health", timeout=5)
        if response.status_code != 200:
            print("❌ API is not responding. Please start the API server first.")
            print("Run: python run.py")
            return
    except requests.exceptions.RequestException:
        print("❌ Cannot connect to API. Please start the API server first.")
        print("Run: python run.py")
        return

    print("✓ API is running!")

    # Run demos
    demo_api_info()
    currency_id = demo_currencies()
    customer_id = demo_customers()
    order_id = demo_orders(customer_id)

    print("\n=== Demo Summary ===")
    print(f"Currency ID: {currency_id}")
    print(f"Customer ID: {customer_id}")
    print(f"Order ID: {order_id}")

    print("\n=== Available Endpoints ===")
    endpoints = [
        "GET    /api/v1/currencies/     - List all currency rates",
        "POST   /api/v1/currencies/     - Create currency rate",
        "GET    /api/v1/customers/      - List all customers",
        "POST   /api/v1/customers/      - Create customer",
        "GET    /api/v1/orders/         - List all orders",
        "POST   /api/v1/orders/         - Create order",
        "GET    /docs                   - API documentation",
        "GET    /health                 - Health check",
    ]

    for endpoint in endpoints:
        print(f"  {endpoint}")

    print(f"\n🚀 Visit http://localhost:8000/docs for interactive API documentation")


if __name__ == "__main__":
    main()
