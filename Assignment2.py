class Customer:
    """
    Represents a customer with personal details.
    """
    def __init__(self, name, contact_info):  # Corrected from _init_ to __init__
        self._name = name  # private attribute
        self._contact_info = contact_info  # private attribute

    def get_name(self):  # Used for getting the name
        return self._name

    def set_name(self, name):  # Used for setting the name
        self._name = name

    def get_contact(self):  # Used for getting the contact info
        return self._contact_info

    def set_contact(self, new_contact):  # Used for setting the contact info
        self._contact_info = new_contact

    def __str__(self):  # Corrected from _str_ to __str__
        return "Customer: " + self._name + ", Contact: " + self._contact_info


class LoyalCustomer(Customer):
    """
    Represents a loyal customer with additional loyalty attributes.
    """
    def __init__(self, name, contact_info, points=0, status="Normal"):  # Corrected from _init_ to __init__
        super().__init__(name, contact_info)
        self._points = points  # private attribute for loyalty points
        self._status = status  # private attribute for membership status

    def get_points(self):  # Used for getting the loyalty points
        return self._points

    def set_points(self, points):  # Used for setting the loyalty points
        self._points = points

    def get_status(self):  # Used for getting the membership status
        return self._status

    def set_status(self, status):  # Used for setting the membership status
        self._status = status

    def add_points(self, points):  # Used for adding loyalty points
        self._points += points

    def apply_discount(self, total_price):  # Used for applying a loyalty discount
        return total_price * 0.9  # 10% discount for loyal customers

    def __str__(self):  # Corrected from _str_ to __str__
        return "Loyal Customer: " + self.get_name() + ", Contact: " + self.get_contact() + ", Points: " + str(self._points) + ", Status: " + self._status


class EBook:
    """
    Represents an e-book with relevant details.
    """
    def __init__(self, title, author, publication_date, genre, price):  # Corrected from _init_ to __init__
        self._title = title  # private attribute
        self._author = author  # private attribute
        self._publication_date = publication_date  # private attribute
        self._genre = genre  # private attribute
        self._price = price  # private attribute

    def get_title(self):  # Used for getting the title
        return self._title

    def set_title(self, title):  # Used for setting the title
        self._title = title

    def get_author(self):  # Used for getting the author
        return self._author

    def set_author(self, author):  # Used for setting the author
        self._author = author

    def get_publication_date(self):  # Used for getting the publication date
        return self._publication_date

    def set_publication_date(self, date):  # Used for setting the publication date
        self._publication_date = date

    def get_genre(self):  # Used for getting the genre
        return self._genre

    def set_genre(self, genre):  # Used for setting the genre
        self._genre = genre

    def get_price(self):  # Used for getting the price
        return self._price

    def set_price(self, new_price):  # Used for setting the price
        self._price = new_price

    def __str__(self):  # Corrected from _str_ to __str__
        return "E-Book: Title: " + self._title + ", Author: " + self._author + ", Published: " + self._publication_date + ", Genre: " + self._genre + ", Price: " + str(self._price)


class ShoppingCart:
    """
    Represents a shopping cart containing e-books.
    """
    def __init__(self):  # Corrected from _init_ to __init__
        self._items = []  # list to hold EBook objects

    def get_items(self):  # Used for getting the items
        return self._items

    def add_item(self, ebook):  # Used for adding an item to the cart
        self._items.append(ebook)

    def remove_item(self, ebook):  # Used for removing an item from the cart
        if ebook in self._items:
            self._items.remove(ebook)

    def calculate_total(self):  # Used for calculating the total price
        return sum(ebook.get_price() for ebook in self._items)

    def __str__(self):  # Corrected from _str_ to __str__
        item_list = " ".join(str(item) for item in self._items)
        return "Shopping Cart: " + item_list + " Total: " + str(self.calculate_total())


class Order:
    """
    Represents an order with e-books and order details.
    """
    def __init__(self, customer):  # Corrected from _init_ to __init__
        self._customer = customer  # private attribute
        self._cart = ShoppingCart()  # composition
        self._order_date = None  # to be set during order completion

    def get_customer(self):  # Used for getting the customer
        return self._customer

    def set_customer(self, customer):  # Used for setting the customer
        self._customer = customer

    def get_order_date(self):  # Used for getting the order date
        return self._order_date

    def set_order_date(self, date):  # Used for setting the order date
        self._order_date = date

    def get_cart(self):  # Used for getting the cart
        return self._cart

    def add_to_cart(self, ebook):  # Used for adding an item to the cart
        self._cart.add_item(ebook)

    def complete_order(self, date):  # Used for completing the order
        self._order_date = date
        return "Order completed on " + self._order_date + " for " + self._customer.get_name()

    def __str__(self):  # Corrected from _str_ to __str__
        return "Order for " + self._customer.get_name() + ", Date: " + str(self._order_date) + " " + str(self._cart)


class Invoice:
    """
    Represents an invoice detailing the order.
    """
    def __init__(self, order):  # Corrected from _init_ to __init__
        self._order = order  # composition
        self._vat_rate = 0.08  # private attribute

    def get_order(self):  # Used for getting the order
        return self._order

    def set_order(self, order):  # Used for setting the order
        self._order = order

    def get_vat_rate(self):  # Used for getting the VAT rate
        return self._vat_rate

    def set_vat_rate(self, rate):  # Used for setting the VAT rate
        self._vat_rate = rate

    def generate_invoice(self):  # Used for generating the invoice
        subtotal = self._order.get_cart().calculate_total()
        vat_amount = subtotal * self._vat_rate
        total = subtotal + vat_amount
        return "Invoice for " + self._order.get_customer().get_name() + " Subtotal: " + str(subtotal) + " VAT (8%): " + str(vat_amount) + " Total: " + str(total)

    def __str__(self):  # Corrected from _str_ to __str__
        return self.generate_invoice()
