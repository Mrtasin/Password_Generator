import tkinter as tk
from tkinter import messagebox
import time

countdowm = tk.Tk()
countdowm.title('Countdown App')
countdowm.geometry('444x222')
countdowm.config(bg="MintCream")
MM = tk.StringVar()
SS = tk.StringVar()
MM.set('00')
SS.set("30")

front = ("Arial",18,"bold")

MinutEntry= tk.Entry(countdowm, width=3, font=front,
                     textvariable=MM)
MinutEntry.place(x = 180, y = 30)

SecondEntry = tk.Entry(countdowm, width=3, font = front,
                       textvariable=SS)
SecondEntry.place(x = 230, y = 30)

def Submit():
    try:
        temp = int(MM.get())*60 + int(SS.get())
    except:
        print("Please input the right value")
    while temp>=0:
        mins, secs = divmod(temp, 60)
        MM.set(str(mins))
        SS.set(str(secs))
        countdowm.update()
        time.sleep(1)
        temp -= 1
    else:
        messagebox.showinfo("Time Countdown", "Time's up ")

Time_Input = tk.Button(countdowm, text='Set Time', font=front,
                       bg = 'blue',command=Submit)
Time_Input.place(x = 175, y = 100)

countdowm.mainloop()