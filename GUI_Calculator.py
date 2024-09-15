import tkinter as tk

Calculatr = tk.Tk()
Calculatr.title("!...GUI_Calculater...!")
Calculatr.geometry("485x770")
Calculatr.config(bg="Mint cream")

#   Exit Switch Code
Front = ("Courier New",16,'bold')

def calculate_result():
    try:
        result = eval(entry.get())
        entry.delete(0,tk.END)
        entry.insert(tk.END,str(result))
    except Exception as e:
        entry.delete(0,tk.END)
        entry.insert(tk.END, "Error")

def Clear(): #
    entry.delete(0,tk.END)




Exit = tk.Button(Calculatr,text="Exit",width=16,height=3,
                 font=Front, bg="red", command=exit)

Exit.grid(row=1, column=0,columnspan=2, padx=10, pady=10)

Switch = [
                              ('pow',1,2), ('%', 1, 3),
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
    ('0', 5, 0), ('.', 5, 2),              ('+', 5, 3),
]

entry = tk.Entry(Calculatr, font=("Arial",38,'bold'),
                 width=16, bg="DarkGray")

entry.grid(row=0, column=0, columnspan=10, padx=5, pady=30)

for (txt, rw, col) in Switch:
    button = tk.Button(Calculatr, text=txt,
                       width=(16 if txt=='0' else 7),
                       height=(8 if txt=='+' else 3),
                       font=Front, bg="PowderBlue", 
                       command=lambda t=('**' if txt=='pow' else txt): entry.insert(tk.END, t))
    
    button.grid(row= rw, rowspan=(2 if txt=='+' else 1),
                column=col,columnspan=(2 if txt=='0' else 1),
                padx=10, pady=10)


Clear = tk.Button(Calculatr, text="AC", width=7, height=3,
                  font=Front,bg="Thistle", command=Clear)

Clear.grid(row=6, column=0, padx=10, pady=10)

enter = tk.Button(Calculatr, text="Enter", width=16, 
                  height=3, font=Front, bg='SeaGreen',
                  command=calculate_result)

enter.grid(row=6, column=1,columnspan=2, padx=10, pady=10)

Calculatr.mainloop()


