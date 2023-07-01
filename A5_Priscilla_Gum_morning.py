import tkinter as tk

class ReceiptPrintingApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Priscilla's Receipt Printing App")
        
        self.item_list = []
        self.total_amount = 0.0
        
        self.item_entry = tk.Entry(self.window)
        self.item_entry.pack()

        self.add_button = tk.Button(self.window, text="Add Item", command=self.add_item)
        self.add_button.pack()

        self.print_button = tk.Button(self.window, text="Print Receipt", command=self.print_receipt)
        self.print_button.pack()

        self.receipt_text = tk.Text(self.window, height=20, width=50)
        self.receipt_text.pack()

    def add_item(self):
        item = self.item_entry.get()
        self.item_list.append(item)
        self.item_entry.delete(0, tk.END)

    def print_receipt(self):
        self.receipt_text.delete("1.0", tk.END)
        
        self.receipt_text.insert(tk.END, "----- Receipt -----\n")
        for item in self.item_list:
            self.receipt_text.insert(tk.END, item + "\n")
        
        self.receipt_text.insert(tk.END, "-------------------\n")
        self.receipt_text.insert(tk.END, "Total Amount: $" + str(self.total_amount))

    def run(self):
        self.window.mainloop()

# Create and run the app
app = ReceiptPrintingApp()
app.run()
