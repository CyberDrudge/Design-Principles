from invoice import Invoice


class InvoicePrinter:
    invoice: Invoice

    def __init__(self, invoice):
        self.invoice = invoice

    def print_invoice(self):
        print(f"{self.invoice.quantity} x {self.invoice.item.name} = {self.invoice.item.price}$")
        print(f"Discount Rate: {self.invoice.discount_rate}")
        print(f"Tax Rate: {self.invoice.tax_rate}")
        print(f"Total: {self.invoice.total}")


class InvoiceDAO:
    invoice: Invoice

    def __init__(self, invoice):
        self.invoice = invoice
        pass

    def save_to_file(self, filename):
        # Creates a file with given name and writes the invoice
        print(f"Saving Invoice as {filename}")
