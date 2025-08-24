# buggy_calculator.py
import requests

def add(a, b):
    resp = requests.get(f"https://math-api/add/{a}/{b}")
    return resp.json()["result"]

def multiply(a, b):
    return a * b

# 👉 Here, mocking is perfect, because:
# You don’t want your tests to call a real HTTP API.
# You can mock requests.get and return a fake result.
# This isolates your test to check your function logic (not the API).