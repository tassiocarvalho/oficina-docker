# client.py

import requests
import json
import os

base_url = 'http://127.0.0.1:5000/items'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu():
    clear_screen()
    print("CRUD operations:")
    print("1. Create")
    print("2. Read")
    print("3. Update")
    print("4. Delete")
    print("5. Exit")

def create(item):
    response = requests.post(base_url, json=item)
    return response.json()

def read():
    response = requests.get(base_url)
    return response.json()

def update(item_id, item):
    response = requests.put(f"{base_url}/{item_id}", json=item)
    return response.json()

def delete(item_id):
    response = requests.delete(f"{base_url}/{item_id}")
    return response.json()

if __name__ == "__main__":
    while True:
        display_menu()
        
        try:
            choice = int(input("\nChoose operation: "))

            if choice == 1:
                item = json.loads(input("Enter item as JSON: "))
                print(create(item))
                input(f"\nValue sent to {base_url}. Press any key to continue.")
            elif choice == 2:
                items = read()
                for idx, item in enumerate(items):
                    print(idx, item)
                input("\nPress any key to continue.")
            elif choice == 3:
                item_id = int(input("Enter item ID to update: "))
                item = json.loads(input("Enter updated item as JSON: "))
                print(update(item_id, item))
                input(f"\nValue updated at {base_url}/{item_id}. Press any key to continue.")
            elif choice == 4:
                item_id = int(input("Enter item ID to delete: "))
                print(delete(item_id))
                input(f"\nValue deleted from {base_url}/{item_id}. Press any key to continue.")
            elif choice == 5:
                break
            else:
                input("Invalid choice. Press any key to continue.")
        except Exception as e:
            input(f"Error: {e}. Press any key to continue.")
