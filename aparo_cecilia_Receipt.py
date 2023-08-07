import tkinter as tk
from tkinter import messagebox


def calculate_total():
    try:
        items = item_entry.get("1.0", tk.END).splitlines()
        quantities = quantity_entry.get("1.0", tk.END).splitlines()
        total = 0
        receipt = ""

        for item, quantity in zip(items, quantities):
            item = item.strip()
            quantity = quantity.strip()

            if item and quantity:
                try:
                    quantity = int(quantity)
                    price = quantity * 1000  # Assuming each item costs $10
                    total += price
                    receipt += f"{item} x {quantity}: ${price}\n"
                except ValueError:
                    messagebox.showerror(
                        "FatalError", "Please Enter a Value.")

        receipt += f"\nTotal: ${total}"
        receipt_text.delete("1.0", tk.END)
        receipt_text.insert(tk.END, receipt)

    except Exception as e:
        messagebox.showerror("Error", str(e))


# Create the main window
window = tk.Tk()
window.title("My Receipt")

# Item details
item_label = tk.Label(window, text="Item Details:(each costs UGX1,000)")
item_label.pack()
item_entry = tk.Text(window, height=5, width=50)
item_entry.pack()

# Quantities
quantity_label = tk.Label(
    window, text="Quantities:(enter corresponding qty values)")
quantity_label.pack()
quantity_entry = tk.Text(window, height=5, width=50)
quantity_entry.pack()

# Calculate button
calculate_button = tk.Button(
    window, text="Total", command=calculate_total)
calculate_button.pack()

# Receipt display
receipt_label = tk.Label(window, text="Receipt:")
receipt_label.pack()
receipt_text = tk.Text(window, height=15, width=50)
receipt_text.pack()

# Start the main event loop
window.mainloop()
