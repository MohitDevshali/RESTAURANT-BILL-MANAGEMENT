from tkinter import *
import random

root = Tk()
root.geometry("1600x8000")
root.title("Restaurant Management System")

text_Input = StringVar()
operator = ""

Tops = Frame(root, width=1600, relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width=800, height=700, relief=SUNKEN)
f1.pack(side=LEFT)

lblInfo = Label(Tops, font=('arial', 50, 'bold'), text="MMM DEVSHALI RESTAURANT ", fg="Steel Blue", bd=10, anchor='w')
lblInfo.grid(row=0, column=0)

lblInfo = Label(Tops, font=('arial', 20, 'bold'), text='Bill Management', fg="Steel Blue", bd=10, anchor='w')
lblInfo.grid(row=1, column=0)


# ========================================================================
#                  PROGRAM
# ========================================================================

def Ref():
    x = random.randint(10908, 500876)
    randomRef = str(x)
    rand.set(randomRef)

    if (Idly.get() == ""):
        CoIdly = 0
    else:
        CoIdly = float(Idly.get())

    if (Dosa.get() == ""):
        CoDosa = 0
    else:
        CoDosa = float(Dosa.get())

    if (IceCream.get() == ""):
        CoIceCream = 0
    else:
        CoIceCream = float(IceCream.get())

    if (Pulav.get() == ""):
        CoPulav = 0
    else:
        CoPulav = float(Pulav.get())

    if (Tea.get() == ""):
        CoTea = 0
    else:
        CoTea = float(Tea.get())

    if (Drinks.get() == ""):
        CoD = 0
    else:
        CoD = float(Drinks.get())

    CostofIdly = CoIdly * 25
    CostofDrinks = CoD * 20
    CostofDosa = CoDosa * 25
    CostofIceCream = CoIceCream * 30
    CostPulav = CoPulav * 50
    CostTea = CoTea * 5

    Central_GST = (((CostofIdly + CostofDrinks + CostofDosa + CostofIceCream + CostPulav + CostTea) * 2.5) / 100)

    State_GST = (((CostofIdly + CostofDrinks + CostofDosa + CostofIceCream + CostPulav + CostTea) * 2.5) / 100)

    Total_cost = (CostofIdly + CostofDrinks + CostofDosa + CostofIceCream + CostPulav + CostTea)

    CostofMeal = "Rs", str('%.2f' % (CostofIdly + CostofDrinks + CostofDosa + CostofIceCream + CostPulav + CostTea))
    C_gst = "Rs", str('%.2f' % Central_GST)
    S_gst = "Rs", str('%.2f' % State_GST)
    OverAllCost = "Rs", str('%.2f' % (Total_cost + Central_GST + State_GST))

    Sgst.set(S_gst)
    Cost.set(CostofMeal)
    Cgst.set(C_gst)
    Total.set(OverAllCost)


def qExit():
    root.destroy()


def Reset():
    Tea.set("")
    Idly.set("")
    Dosa.set("")
    IceCream.set("")
    Pulav.set("")
    Drinks.set("")

    rand.set("")

    Total.set("")
    Sgst.set("")
    Cgst.set("")
    Cost.set("")


# ========================================================================
#                  RESTAURANT MENU
# ========================================================================
Tea = StringVar()
Idly = StringVar()
Dosa = StringVar()
IceCream = StringVar()
Pulav = StringVar()
Drinks = StringVar()
rand = StringVar()
Cost = StringVar()
Sgst = StringVar()
Cgst = StringVar()
Total = StringVar()

lblTea = Label(f1, font=('arial', 16, 'bold'), text="Tea", bd=16, anchor="w")
lblTea.grid(row=0, column=0)
lblTea = Entry(f1, font=('arial', 16, 'bold'), textvariable=Tea, bd=10, insertwidth=4, bg="white", justify='right')
lblTea.grid(row=0, column=1)

lblDrinks = Label(f1, font=('arial', 16, 'bold'), text="Drinks", bd=16, anchor="w")
lblDrinks.grid(row=1, column=0)
txtDrinks = Entry(f1, font=('arial', 16, 'bold'), textvariable=Drinks, bd=10, insertwidth=4, bg="white",
                  justify='right')
txtDrinks.grid(row=1, column=1)

lblIceCream = Label(f1, font=('arial', 16, 'bold'), text="Ice-Cream", bd=16, anchor="w")
lblIceCream.grid(row=2, column=0)
lblIceCream = Entry(f1, font=('arial', 16, 'bold'), textvariable=IceCream, bd=10, insertwidth=4, bg="white",
                    justify='right')
lblIceCream.grid(row=2, column=1)

lblIdly = Label(f1, font=('arial', 16, 'bold'), text="Idly", bd=16, anchor="w")
lblIdly.grid(row=3, column=0)
txtIdly = Entry(f1, font=('arial', 16, 'bold'), textvariable=Idly, bd=10, insertwidth=4, bg="white", justify='right')
txtIdly.grid(row=3, column=1)

lblDosa = Label(f1, font=('arial', 16, 'bold'), text="Dosa", bd=16, anchor="w")
lblDosa.grid(row=4, column=0)
txtDosa = Entry(f1, font=('arial', 16, 'bold'), textvariable=Dosa, bd=10, insertwidth=4, bg="white", justify='right')
txtDosa.grid(row=4, column=1)

lblPulav = Label(f1, font=('arial', 16, 'bold'), text="Rice-Plate", bd=16, anchor="w")
lblPulav.grid(row=5, column=0)
txtPulav = Entry(f1, font=('arial', 16, 'bold'), textvariable=Pulav, bd=10, insertwidth=4, bg="white", justify='right')
txtPulav.grid(row=5, column=1)

# ========================================================================
#                  RESTAURANT BILL INFO
# ========================================================================

lblReference = Label(f1, font=('arial', 16, 'bold'), text="Reference", bd=16, anchor="w")
lblReference.grid(row=0, column=2)
txtReference = Entry(f1, font=('arial', 16, 'bold'), textvariable=rand, bd=10, insertwidth=4, bg="light grey",
                     justify='right')
txtReference.grid(row=0, column=3)

lblCost = Label(f1, font=('arial', 16, 'bold'), text="Cost of Meal", bd=16, anchor="w")
lblCost.grid(row=1, column=2)
txtCost = Entry(f1, font=('arial', 16, 'bold'), textvariable=Cost, bd=10, insertwidth=4, bg="light grey",
                justify='right')
txtCost.grid(row=1, column=3)

lblSgst = Label(f1, font=('arial', 16, 'bold'), text="SGST", bd=16, anchor="w")
lblSgst.grid(row=2, column=2)
txtSgst = Entry(f1, font=('arial', 16, 'bold'), textvariable=Sgst, bd=10, insertwidth=4, bg="light grey",
                justify='right')
txtSgst.grid(row=2, column=3)

lblCgst = Label(f1, font=('arial', 16, 'bold'), text="CGST", bd=16, anchor="w")
lblCgst.grid(row=3, column=2)
txtCgst = Entry(f1, font=('arial', 16, 'bold'), textvariable=Cgst, bd=10, insertwidth=4, bg="light grey",
                justify='right')
txtCgst.grid(row=3, column=3)

lblTotalCost = Label(f1, font=('arial', 16, 'bold'), text="Total Cost", bd=16, anchor="w")
lblTotalCost.grid(row=4, column=2)
txtTotalCost = Entry(f1, font=('arial', 16, 'bold'), textvariable=Total, bd=10, insertwidth=4, bg="light grey",
                     justify='right')
txtTotalCost.grid(row=4, column=3)

# ========================================================================
#                  BUTTONS
# ========================================================================
btnTotal = Button(f1, padx=16, pady=8, bd=16, fg="black", font=('arial', 16, 'bold'), width=10, text="Total",
                  bg="powder blue", command=Ref).grid(row=7, column=1)

btnReset = Button(f1, padx=16, pady=8, bd=16, fg="black", font=('arial', 16, 'bold'), width=10, text="Reset",
                  bg="powder blue", command=Reset).grid(row=7, column=2)

btnExit = Button(f1, padx=16, pady=8, bd=16, fg="black", font=('arial', 16, 'bold'), width=10, text="Exit",
                 bg="powder blue", command=qExit).grid(row=7, column=3)

root.mainloop()


