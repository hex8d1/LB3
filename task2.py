import requests
from requests.auth import HTTPBasicAuth

BASE_URL = "http://127.0.0.1:8000"

AUTH = HTTPBasicAuth("admin", "password123")

def get_all_items():
    response = requests.get(f"{BASE_URL}/items", auth=AUTH)
    print("GET /items")
    print(response.status_code, response.json())

def add_item(item):
    response = requests.post(f"{BASE_URL}/items", json=item, auth=AUTH)
    print("POST /items")
    print(response.status_code, response.json())

def get_item(item_id):
    response = requests.get(f"{BASE_URL}/items/{item_id}", auth=AUTH)
    print(f"GET /items/{item_id}")
    print(response.status_code, response.json())

def update_item(item_id, updates):
    response = requests.put(f"{BASE_URL}/items/{item_id}", json=updates, auth=AUTH)
    print(f"PUT /items/{item_id}")
    print(response.status_code, response.json())

def delete_item(item_id):
    response = requests.delete(f"{BASE_URL}/items/{item_id}", auth=AUTH)
    print(f"DELETE /items/{item_id}")
    print(response.status_code, response.json())

if __name__ == "__main__":
    get_all_items()
    add_item({"id": 1, "name": "Стіл", "price": 100.25})
    get_item(1)
    update_item(1, {"price": 150.00})
    get_item(1)
    delete_item(1)
    get_all_items()
