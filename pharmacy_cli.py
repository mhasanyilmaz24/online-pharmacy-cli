class Product:

    def __init__(self, name, stock, price):
        self.name = name
        self.stock = stock
        self.price = price

    def add_to_cart(self, quantity):
        if quantity <= self.stock:
            self.stock -= quantity
            return True
        else:
            return False

    def restock(self, quantity):
        self.stock += quantity

class Cart:

    def __init__(self):
        self.items = {}

    def add_item(self, product, quantity):
        if product.add_to_cart(quantity):
            if product.name not in self.items:
                self.items[product.name] = {"quantity": 0, "price": product.price}
            self.items[product.name]["quantity"] += quantity
            print(f"{quantity} units of {product.name} added to the cart.")
        else:
            print(f"Insufficient stock for {product.name}. Current stock: {product.stock}")

    def remove_item(self, product_name, quantity):
        if product_name in self.items:
            if self.items[product_name]["quantity"] >= quantity:
                self.items[product_name]["quantity"] -= quantity
            for product in products:
                if product.name == product_name:
                    product.restock(quantity)
                    break
            if self.items[product_name]["quantity"] == 0:
                del self.items[product_name]
                print(f"{quantity} units of {product_name} removed from the cart and stock updated.")
            else:
                print(f"You do not have {quantity} units of {product_name} in your cart.")
        else:
            print(f"{product_name} is not in the cart.")



    def show_cart(self):
        if not self.items:
            print("Your cart is empty!")
        else:
            print("\nYour Cart:")
            total_price = 0
            for name, details in self.items.items():
                quantity = details["quantity"]
                price = details["price"]
                total = quantity * price
                total_price += total
                print(f"- {name}: {quantity} units, Total: ${total:.2f}")
            print(f"Total Price: ${total_price:.2f}")

products = [
    Product("Paracetamol", 15, 5.00),
    Product("Ibuprofen", 20, 7.50),
    Product("Amoxicillin", 10, 12.00),
    Product("Losartan", 12, 8.50),
    Product("Omeprazole", 13, 10.00),
    Product("Cetirizine", 17, 4.50)
]

cart = Cart()
admin_password = "admin123"
discount_codes = {"PHAR50": 0.50, "PHAR75": 0.75}

def show_products():
    print("\nAvailable Products:")
    for i, product in enumerate(products):
        print(f"{i + 1}. {product.name} (Stock: {product.stock}, Price: ${product.price:.2f})")

def add_new_product():
    name = input("Enter the product name: ").strip()
    stock = int(input("Enter the stock quantity: "))
    price = float(input("Enter the product price: "))
    products.append(Product(name, stock, price))
    print(f"Product {name} added successfully.")

def restock_product():
    show_products()
    try:
        choice = int(input("Select a product to restock: ")) - 1
        if 0 <= choice < len(products):
            quantity = int(input("Enter the quantity to add: "))
            products[choice].restock(quantity)
            print(f"{products[choice].name} restocked. New stock: {products[choice].stock}")
        else:
            print("Invalid product selection.")
    except ValueError:
        print("Please enter a valid number.")

def delete_product():
    show_products()
    try:
        choice = int(input("Select a product to delete: ")) - 1
        if 0 <= choice < len(products):
            removed_product = products.pop(choice)
            if removed_product.name in cart.items:
                cart_stock = cart.items.pop(removed_product.name)["quantity"]
                removed_product.restock(cart_stock)
            print(f"Product {removed_product.name} deleted successfully.")
        else:
            print("Invalid product selection.")
    except ValueError:
        print("Please enter a valid number.")

def choose_delivery_option():
    print("\nDelivery Options:")
    print("1. Home Delivery")
    print("2. Store Pickup")
    choice = input("\nChoose your delivery option (1-2): ")
    if choice == "1":
        address = input("Enter your delivery address: ").strip()
        print("\nYou chose Home Delivery.")
        return "Home Delivery", 5.00
    elif choice == "2":
        print("\nYou chose Store Pickup.")
        print("\nAvailable Stores:")
        print("1. Store1")
        print("2. Store2")
        print("3. Store3")
        store_choice = input("Choose a store (1-3): ")
        if store_choice == "1":
            return "Store1", 0.00
        elif store_choice == "2":
            return "Store2", 0.00
        elif store_choice == "3":
            return "Store3", 0.00
        else:
            print("Invalid choice! Defaulting to Store1.")
            return "Store1", 0.00
    else:
        print("Invalid choice! Defaulting to Store Pickup at Store1.")
        return "Store1", 0.00

def apply_discount(grand_total):
    code = input("Enter discount code (or press Enter to skip): ").strip()
    if code in discount_codes:
        discount = discount_codes[code]
        discounted_total = grand_total * (1 - discount)
        print(f"Discount code applied! You saved {discount * 100:.0f}%.")
        print("\nPlease choose your delivery option after applying the discount.")
        delivery_option, delivery_fee = choose_delivery_option()
        return discounted_total, delivery_option, delivery_fee
    elif code:
        print("Invalid discount code. No discount applied.")
    return grand_total, None, 0.00

def admin_menu():
    while True:
        print("\nAdmin Menu:")
        print("1. Add New Product")
        print("2. Restock Product")
        print("3. Delete Product")
        print("4. Back to Main Menu")
        choice = input("\nChoose an option: ")
        if choice == "1":
            add_new_product()
        elif choice == "2":
            restock_product()
        elif choice == "3":
            delete_product()
        elif choice == "4":
            break
        else:
            print("Invalid option. Please try again.")

def main():
    while True:
        print("\nMain Menu:")
        print("1. Show Products")
        print("2. Add Product to Cart")
        print("3. Show Cart")
        print("4. Remove Product from Cart")
        print("5. Checkout")
        print("6. Admin Login")
        print("7. Exit")
        choice = input("\nChoose an option: ")
        if choice == "1":
            show_products()
        elif choice == "2":
            show_products()
            try:
                product_choice = int(input("\nSelect a product to add to the cart: ")) - 1
                if 0 <= product_choice < len(products):
                    selected_product = products[product_choice]
                    quantity = int(input(f"Enter quantity for {selected_product.name}: "))
                    cart.add_item(selected_product, quantity)
                else:
                    print("Invalid choice. Please select a valid product.")
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "3":
            cart.show_cart()
        elif choice == "4":
            product_name = input("Enter the product name to remove: ").strip()
            try:
                quantity = int(input(f"Enter quantity to remove from {product_name}: "))
                cart.remove_item(product_name, quantity)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == "5":
            if cart.items:
                print("\nOrder Summary:")
                cart.show_cart()
                grand_total = sum(details['quantity'] * details['price'] for details in cart.items.values())
                grand_total, delivery_option, delivery_fee = apply_discount(grand_total)
                if not delivery_option:
                    delivery_option, delivery_fee = choose_delivery_option()
                print(f"Delivery Option: {delivery_option}")
                print(f"Delivery Fee: ${delivery_fee:.2f}")
                print(f"Grand Total: ${grand_total + delivery_fee:.2f}")
                print("\nThank you for shopping with us!")
                break
            else:
                print("Your cart is empty! Please add items before checking out.")
        elif choice == "6":
            password = input("Enter admin password: ").strip()
            if password == admin_password:
                admin_menu()
            else:
                print("Incorrect password. Access denied.")
        elif choice == "7":
            print("Thank you for using the Pharmacy Shopping System. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()                      