from item import Item


class Invoice:
    item: Item
    quantity: int
    discount_rate: float
    tax_rate: float
    total: float

    def __init__(self, item, quantity, discount_rate, tax_rate):
        self.item = item
        self.quantity = quantity
        self.discount_rate = discount_rate
        self.tax_rate = tax_rate
        self.total = self.calculate_total()

    def calculate_total(self):
        price = (self.item.price - self.item.price * self.discount_rate) * self.quantity
        price_after_tax = price * (1 + self.tax_rate)
        return price_after_tax

    def print_invoice(self):
        print(f"{self.quantity} x {self.item.name} = {self.item.price}$")
        print(f"Discount Rate: {self.discount_rate}")
        print(f"Tax Rate: {self.tax_rate}")
        print(f"Total: {self.total}")

    def save_in_file(self):
        # Saves the invoice in a file
        print("Saving Invoice In a File")
