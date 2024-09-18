class Menu:
    def __init__(self):
        self.foods = ['burger', 'sandwich', 'muffins']
        self.drinks = ['fresh juice', 'Tea', 'coffee']
        self.books = ['magic mindset', 'Ikigai', 'Think like a monk']
 
    def show_menu(self):
        print("\nMenu Items:")
        print("Foods:")
        for food in self.foods:
            print(f"- {food}")
        print("\nDrinks:")
        for drink in self.drinks:
            print(f"- {drink}")
        print("\nBooks:")
        for book in self.books:
            print(f"- {book}")
 
    def update_food(self, food_item):
        self.foods.append(food_item)
        print(f"{food_item} added to the food menu!")
 
    def update_drink(self, drink_item):
        self.drinks.append(drink_item)
        print(f"{drink_item} added to the drinks menu!")
 
    def update_books(self, book_item):
        self.books.append(book_item)
        print(f"{book_item} added to the book list!")


class Customer:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def customer_details(self):
        print(f"Customer Name: {self.name}")
        print(f"Delivery Address: {self.address}")


def main():
    # Show menu
    cafe_menu = Menu()
    cafe_menu.show_menu()

    # Get customer order details
    add_food = input("\nEnter the food you'd like to order: ")
    add_drink = input("Enter the drink you'd like to order: ")
    add_book = input("Enter the book you'd like to order: ")

    print(f"\nYou have ordered: {add_food}, {add_drink}, and {add_book}.")

    # Get customer details for delivery
    customer_name = input("\nEnter your name: ")
    customer_address = input("Enter your delivery address: ")
    
    customer = Customer(customer_name, customer_address)

    # Show customer details
    print("\nCustomer Details:")
    customer.customer_details()


if __name__ == "__main__":
    main()
