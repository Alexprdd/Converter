import tkinter as tk

def convertkg():
    gram=1000*float(weightEntry.get())
    pound=2.20462*float(weightEntry.get())
    ounce=35.27*float(weightEntry.get())

    gramsEntry.delete(0, tk.END) 
    poundsEntry.delete(0, tk.END)
    ouncesEntry.delete(0, tk.END)

    gramsEntry.insert(tk.END,gram)
    poundsEntry.insert(tk.END,pound)
    ouncesEntry.insert(tk.END,ounce)



# Window
window = tk.Tk()
window.geometry("510x150")

# Weight label
weightLabel = tk.Label(window, text="Enter the weight in Kg", font=("Helvetica", 10), fg="black")


# Entry for weight
weightEntry = tk.Entry(window, bg="white", fg="black", bd=2)


# Convert button
convert = tk.Button(window, text="Convert", font=("Helvetica", 10), bg="white", fg="black", bd=2, relief=tk.RIDGE, command=convertkg)


# Grams, pounds, ounces labels
grams = tk.Label(window, text="Grams", font=("Helvetica", 10), fg="black")


pounds = tk.Label(window, text="Pounds", font=("Helvetica", 10), fg="black")


ounces = tk.Label(window, text="Ounces", font=("Helvetica", 10), fg="black")


# Entries for grams, pounds, ounces
gramsEntry = tk.Entry(window, bg="white", fg="black", bd=2)


poundsEntry = tk.Entry(window, bg="white", fg="black", bd=2)

ouncesEntry = tk.Entry(window, bg="white", fg="black", bd=2)


# Make columns expand
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)


weightLabel.grid(column=0, row=0, padx=10, pady=10)
weightEntry.grid(column=1, row=0, padx=10, pady=10)
convert.grid(column=2, row=0, padx=10, pady=10)
grams.grid(column=0, row=1, padx=10, pady=10)
pounds.grid(column=1, row=1, padx=10, pady=10)
ounces.grid(column=2, row=1, padx=10, pady=10)
gramsEntry.grid(column=0, row=2, sticky='ew', padx=10, pady=10)
poundsEntry.grid(column=1, row=2, sticky='ew', padx=10, pady=10)
ouncesEntry.grid(column=2, row=2, sticky='ew', padx=10, pady=10)


window.mainloop()