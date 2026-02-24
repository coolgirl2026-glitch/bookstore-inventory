import json

new_book = {
    "title": "atomic habits",
    "author": "james clear",
    "price": 14.99,
    "in_stock": True
}

with open("inventory.json", "r") as file:
    inventory = json.load(file)

print("total books in inventory:", len(inventory))

inventory.append(new_book)
with open("inventory.json", "w")as file:
    json.dump(inventory, file, indent=4)

print("new book added and file updated.")

with open("inventory.json", "r") as file:
    updated_inventory = json.load(file)

print("\nbook details:")
for book in updated_inventory:
    print(f"Title: {book['title']}  | Author: {book['author']}  | Price: ${book['price']}")
    