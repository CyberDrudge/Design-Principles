

class InvoiceDAO:
    invoice: Invoice

    def __init__(self, invoice):
        self.invoice = invoice
        pass

    def save_to_file(self, filename):
        # Creates a file with given name and writes the invoice
        print(f"Saving Invoice as {filename}")

    def save_to_database(self):
        # Saves the invoice in database
        print("Saving Invoice In Database")


class InvoiceDatabaseDAO:
    def save(self, invoice):
        # Saves the invoice in database
        print("Saving Invoice In Database")


class InvoiceFileDAO:
    def save(self, invoice):
        # Creates a file with given name and writes the invoice
        print("Saving Invoice in file")
