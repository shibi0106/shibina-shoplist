import requests
def fetch_products():
    """Fetch 5 products from FakeStoreAPI."""
    url = "https://fakestoreapi.com/products?limit=5"
    response = requests.get(url)
    products = response.json()
    print("\nAvailable Products:")
    for i, p in enumerate(products, start=1):
        print(f"{i}. {p['title']}")
    return products
def add_item(shopping_list, item):
    shopping_list.append(item)
    print(f"'{item}' added to your shopping list.")
def remove_item(shopping_list, item):
    if item in shopping_list:
        shopping_list.remove(item)
        print(f" '{item}' removed from your shopping list.")

def show_list(shopping_list):
    if not shopping_list:
        print("🛒 Your shopping list is empty.")
    else:
        print("\nYour Shopping List:")
        for i, item in enumerate(shopping_list, start=1):
            print(f"{i}. {item}")
print("Welcome to Simple Shopping List App!")
shopping_list = []
products = fetch_products()
while True:
    print("\nMenu:")
    print("1. View ")
    print("2. Add ")
    print("3. Remove ")
    print("4. View shopping list")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        products = fetch_products()

    elif choice == "2":
        try:
            num = int(input("Enter product number to add: ")) - 1
            if 0 <= num < len(products):
                add_item(shopping_list, products[num]['title'])
            else:
                print("Invalid product number.")
        except ValueError:
            print("Please enter a number.")

    elif choice == "3":
        show_list(shopping_list)
        item = input("Enter exact name to remove: ")
        remove_item(shopping_list, item)

    elif choice == "4":
        show_list(shopping_list)

    elif choice == "5":
        print("See you next time")
        break  # ✅ valid, inside loop

    else:
        print("Please choose between 1 and 5.")
