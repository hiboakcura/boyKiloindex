import math
from tkinter import *

window = Tk()
window.minsize(height=400, width=250)
window.title("BIM Calculator")
window.config(padx=30, pady=30)


def click_calculate():
    x1 = my_entry1.get()
    x2 = my_entry2.get()
    if x1 == '' or x2 == '':
       my_label3.config(text="Lütfen verileri doğru girdiğinize emin olunuz")



    else:
        try:

            a1 = float(x1)
            a2 = float(x2)
            bim = round((a1 / ((a2 ** 2)/10000)), 2)



            if bim>18.5 and bim<25:
                my_label3["text"] = f"BIM: {bim} Normal "

            elif bim < 18.5:
                my_label3["text"] = f"BIM: {bim} Under Weight "

            elif 25 <= bim < 30:
                my_label3["text"] = f"BIM: {bim} Over Weight "

            elif 30 <= bim < 40:
                my_label3["text"] = f"BIM: {bim} Obesity "

            elif bim >= 40:
                my_label3["text"] = f"BIM: {bim} Extreme Obesity "

        except:
            my_label3.config(text="Lütfen verileri değer olarak giriş yapınız!!!")




my_label1 = Label(text="Enter Your Weight (kg) ", font=('Arial', 15, 'italic'))
my_label1.pack()

my_entry1 = Entry(width=20)
my_entry1.pack()


my_label2 = Label(text="Enter Your Height (cm) ", font=('Arial', 15, 'italic'))
my_label2.pack()


my_entry2 = Entry(width=20)
my_entry2.pack()


my_button = Button(text="Calculate", command=click_calculate)
my_button.pack()

my_label3 = Label(text="", font=('Arial', 15, 'italic'))
my_label3.pack()



window.mainloop()