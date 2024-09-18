import os 


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"{self.name} - ${self.price:.2f}"


class Customer:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.order = []

    def add_to_order(self, item):
        self.order.append(item)

    def view_order(self):
        print(f"\nOrder for {self.name}:")
        for item in self.order:
            print(f"  - {item}")
        print(f"Total: ${self.calculate_total():.2f}")

    def calculate_total(self):
        return sum(item.price for item in self.order)

    def generate_receipt(self):
        receipt = f"Receipt for {self.name}\n"
        receipt += f"Address: {self.address}\n"
        receipt += "-" * 30 + "\n"
        for item in self.order:
            receipt += f"{item.name:<20} ${item.price:.2f}\n"
        receipt += "-" * 30 + "\n"
        total = sum(item.price for item in self.order)
        receipt += f"{'Total':<20} ${total:.2f}\n"
        return receipt
    
    def save_receipt(self, filename=None):
        receipt = self.generate_receipt()
        directory = 'receipts'
        if not os.path.exists(directory):
            os.makedirs(directory)

        if filename is None:
            filename = f'{directory}/{self.name}.txt'  # Default to customer's name

        with open(filename, 'w') as file:
            file.write(receipt)
        print("Receipt saved.")


class Admin:
    def __init__(self, menu, books, specials):
        self.menu = menu
        self.books = books
        self.specials = specials

    def add_item(self, category, name, price):
        if category == 'menu':
            self.menu.append(Product(name, price))
        elif category == 'books':
            self.books.append(Product(name, price))
        elif category == 'specials':
            self.specials.append(Product(name, price))
        print(f"Added {name} to {category}.")

    def update_specials(self):
        print("Current Specials:")
        for i, item in enumerate(self.specials, 1):
            print(f"{i}. {item}")
        choice = int(input("Which special would you like to update? "))
        if 1 <= choice <= len(self.specials):
            new_name = input("Enter new name: ")
            new_price = float(input("Enter new price: "))
            self.specials[choice-1] = Product(new_name, new_price)
            print("Special updated successfully!")


class Bookshop:
    def __init__(self, menu=None, books=None, specials=None):
        # Initialize the menu, books, and specials as empty lists if not provided
        self.menu = menu if menu is not None else []
        self.books = books if books is not None else []
        self.specials = specials if specials is not None else []
        self.customers = []  # List to hold customer details

        # Populate default items in menu and books for the demonstration
        self.menu += [
            Product("Sandwich", 5.00),
            Product("Soup", 4.50),
            Product("Cake", 3.00),
            Product("Coffee", 2.50),
            Product("Tea", 2.00)
        ]

        self.specials += [
            Product("Stir Fry", 7.50),
            Product("Spaghetti Bolognese", 8.00),
            Product("Oreo Cheesecake", 4.50)
        ]

        self.books += [
            Product("Book A", 15.99),
            Product("Book B", 12.50),
            Product("Book C", 22.00)
        ]

        self.admin = Admin(self.menu, self.books, self.specials)

        # Add default customer details for testing
        self.customers += [
            Customer("Anna", "anna@gmail.com, 1234 Street"),
            Customer("Stuart", "stuart@gmail.com, 5678 Street"),
            Customer("John", "john@gmail.com, 4536 Street"),
            Customer("Shamreena", "shamreena@gmail.com, 4536 Street")
        ]

    def show_food_menu(self):
        print("\n--- Food & Drink Menu ---")
        for item in self.menu:
            print(item)

    def show_food_specials(self):
        print("\n--- Specials ---")
        for item in self.specials:
            print(item)

    def show_books(self):
        print("\n--- Books Available ---")
        for book in self.books:
            print(book)

    def customer_order(self):
        name = input("Enter your name: ")
        address = input("Enter your address: ")
        customer = Customer(name, address)

        # Add the customer to the list
        self.customers.append(customer)

        # Shmareena
        while True:
            # Show both food menu and books for customers to order from
            self.show_food_menu()
            self.show_food_specials()
            self.show_books()

            choice = input("\nChoose item to add to your order (or type 'done' to finish): ").lower()
            if choice == 'done':
                break

            # Search in both menu and books
            found = False
            for item in self.menu + self.books + self.specials:
                if item.name.lower() == choice:
                    customer.add_to_order(item)
                    print(f"Added {item.name} to your order.")
                    found = True
                    break

            if not found:
                print("Item not found. Try again.")

        # Show the final order and total
        customer.view_order()
        # Print the receipt to the terminal
        print(customer.generate_receipt())
        # Save the receipt to a .txt file
        customer.save_receipt()

    def employee_actions(self):
        print("\n--- Employee Access ---")
        print("1. Add Menu Item")
        print("2. Add Book")
        print("3. Update Specials")
        print("4. View Customer Details")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter food/drink name: ")
            price = float(input("Enter price: "))
            self.admin.add_item('menu', name, price)
        elif choice == '2':
            title = input("Enter book title: ")
            price = float(input("Enter price: "))
            self.admin.add_item('books', title, price)
        elif choice == '3':
            self.admin.update_specials()
        elif choice == '4':
            self.customer_details()

    def customer_details(self):
        name = input("Enter customer name: ").lower()

        # Search for customer by name
        for customer in self.customers:
            if customer.name.lower() == name:
                print(f"\nCustomer: {customer.name}\nAddress: {customer.address}")
                return

        print("Customer not found.")

    def main(self):
        while True:
            print("\n--- Bookshop Cafe ---")
            print("1. Customer Order")
            print("2. Employee Access")
            print("3. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                self.customer_order()
            elif choice == '2':
                self.employee_actions()
            elif choice == '3':
                print("Goodbye!")
                break
            else:
                print("Invalid choice, try again.")


if __name__ == "__main__":
    app = Bookshop()
    app.main()
