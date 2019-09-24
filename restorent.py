from tkinter import *
import random
import time;

root = Tk()
root.geometry("1600x800+0+0")
root.title("resaurant Management System")

text_Input = StringVar()
operator=""

Tops = Frame(root, width=1600,height = 50,bg="powder blue", relief=SUNKEN)
Tops.pack(side=TOP)

f1=Frame(root,width=800, height=700, relief=SUNKEN)
f1.pack(side =LEFT)

f2 = Frame(root,width =300,height =700, relief=SUNKEN)
f2.pack(side=RIGHT)

#2222222222222222222222222222222222222222222222222222222

localtime=time.asctime(time.localtime(time.time()))

#--------------time------------------------------------

lblInfo = Label(Tops,font=('arial',30,'bold'),text="Restaurant Management System",fg="Steel Blue", bd=10,anchor='w')
lblInfo.grid(row=0,column=0)

lblInfo = Label(Tops,font=('arial',20,'bold'),text=localtime,fg="Steel Blue", bd=10,anchor='w')
lblInfo.grid(row=1,column=0)

#111111111111111111111111111111111111111111111111111111

def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator=""
    text_Input.set("")

def btnEqualsInput():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator=""

def Ref():
    x=random.randint(10908,500876)
    randomRef = str(x)
    rand.set(randomRef)

    CoF=float(fries.get())
    CoD=float(Drinks.get())
    CoFilet =float(Filet.get())
    CoBurger=float(Burger.get())
    CoChicken_Burger=float(Chicken_Burger.get())
    CoCheese_Burger=float(Cheese_Burger.get())
    CoTea = float(Tea.get())
    CoBanana =float(Bananasake.get())
    CoPapaya =float(Papayasake.get())
    CoMilksake=float(Milksake.get())

    Costoffries= CoF * 15.00
    CostofDrinks= CoD * 5.00
    CostofFilet=CoFilet * 25
    CostofBurger=CoBurger * 30
    CostChicken_Burger=CoChicken_Burger * 50
    CostCheese_Burger=CoCheese_Burger * 40
    CostofTea=CoTea * 5.00
    CostofBanana=CoBanana * 20.00   
    CostofPapaya = CoPapaya * 20.00
    CostofMilkSake = CoMilksake * 20.00

    CostofMean = "Σ" ,str('%.2f' % (Costoffries + CostofDrinks+CostofFilet+CostofBurger+CostChicken_Burger+CostCheese_Burger+CostofTea+ CostofBanana+CostofPapaya+CostofMilkSake))
    
    PayTax = ((Costoffries + CostofDrinks+CostofFilet+CostofBurger+CostChicken_Burger+CostCheese_Burger+CostofTea+ CostofBanana+CostofPapaya+CostofMilkSake)*0.2)
    

    TotalCost=(Costoffries + CostofDrinks+CostofFilet+CostofBurger+CostChicken_Burger+CostCheese_Burger+CostofTea+ CostofBanana+CostofPapaya+CostofMilkSake)

    Ser_Charge = ((Costoffries + CostofDrinks+CostofFilet+CostofBurger+CostChicken_Burger+CostCheese_Burger+CostofTea+ CostofBanana+CostofPapaya+CostofMilkSake)/99)

    Service = "Σ", str('%.2f' % Ser_Charge)

    OverAllCost = "Σ", str('%.2f' % (PayTax + TotalCost + Ser_Charge))
    PaidTax = "Σ", str('%.2f' % PayTax)

    Service_Charge.set(Service)

    Cost.set(CostofMean)
    Tax.set(PaidTax)

    SubTotal.set(CostofMean)
    Total.set(OverAllCost)                          
def qExit():
    root.destroy()


def Reset():
    rand.set("")
    fries.set("")
    Burger.set("")
    Filet.set("")
    SubTotal.set("")
    Total.set("")
    Service_Charge.set("")
    Drinks.set("")
    Tax.set("")
    Cost.set("")
    Chicken_Burger.set("")
    Cheese_Burger.set("")
    Bananasake.set("")
    Papayasake.set("")
    Milksake.set("")
    Tea.set("")
    
txtDisplay = Entry(f2,font=('arial',20,'bold'),textvariable=text_Input,bd=30, insertwidth=4,bg="powder blue",justify="left")
txtDisplay.grid(columnspan=4)
btn7=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',15,'bold'),text="7",bg="powder blue",command=lambda: btnClick(7)).grid(row=2,column=0)

btn8=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',15,'bold'),text="8",bg="powder blue",command=lambda: btnClick(8)).grid(row=2,column=1)

btn9=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',15,'bold'),text="9",bg="powder blue",command=lambda: btnClick(9)).grid(row=2,column=2)

Addition=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',15,'bold'),text="+",bg="powder blue",command=lambda: btnClick("+")).grid(row=2,column=3)

#----------------------------------------------------------------------------------
btn4=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',15,'bold'),text="4",bg="powder blue",command=lambda: btnClick(4)).grid(row=3,column=0)

btn5=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',15,'bold'),text="5",bg="powder blue",command=lambda: btnClick(5)).grid(row=3,column=1)

btn6=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',15,'bold'),text="6",bg="powder blue",command=lambda: btnClick(6)).grid(row=3,column=2)

Subtraction=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',15,'bold'),text="-",bg="powder blue",command=lambda: btnClick("-")).grid(row=3,column=3)

#--------------------------------------------------------------------------------------

btn1=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',15,'bold'),text="1",bg="powder blue",command=lambda: btnClick(1)).grid(row=4,column=0)

btn2=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',15,'bold'),text="2",bg="powder blue",command=lambda: btnClick(2)).grid(row=4,column=1)

btn3=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',15,'bold'),text="3",bg="powder blue",command=lambda: btnClick(3)).grid(row=4,column=2)

Multiply=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',15,'bold'),text="*",bg="powder blue",command=lambda: btnClick("*")).grid(row=4,column=3)

#--------------------------------------------------------------------------------------

btnclear=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',15,'bold'),text="C",bg="powder blue",command=btnClearDisplay).grid(row=5,column=0)

btn0=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',15,'bold'),text="0",bg="powder blue",command=lambda: btnClick(0)).grid(row=5,column=1)

btnequal=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',15,'bold'),text="=",bg="powder blue",command=btnEqualsInput).grid(row=5,column=2)

Division=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',15,'bold'),text="/",bg="powder blue",command=lambda: btnClick("/")).grid(row=5,column=3)

#------------------------------------------------------------------------------------------

rand=StringVar()
fries=StringVar()
Burger=StringVar()
Filet=StringVar()
SubTotal=StringVar()
Total=StringVar()
Service_Charge=StringVar()
Drinks=StringVar()
Tax=StringVar()
Cost=StringVar()
Chicken_Burger=StringVar()
Cheese_Burger=StringVar()
Bananasake=StringVar()
Papayasake=StringVar()
Milksake=StringVar()
Tea=StringVar()


lblReference = Label(f1,font=('arial',16,'bold'),text="Reference No",bd=16,anchor='w')
lblReference.grid(row=0,column=0)
txtReference=Entry(f1,font=('arial',12,'bold'),textvariable=rand,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtReference.grid(row=0,column=1)

lblfries = Label(f1,font=('arial',16,'bold'),text="Fries",bd=16,anchor='w')
lblfries.grid(row=1,column=0)
txtfries=Entry(f1,font=('arial',12,'bold'),textvariable=fries,bd=10,insertwidth=4,bg="powder blue",justify='left')
txtfries.grid(row=1,column=1)


lblBurger = Label(f1,font=('arial',16,'bold'),text="Burger",bd=16,anchor='w')
lblBurger.grid(row=2,column=0)
txtBurger=Entry(f1,font=('arial',12,'bold'),textvariable=Burger,bd=10,insertwidth=4,bg="powder blue",justify='left')
txtBurger.grid(row=2,column=1)

lblFilet = Label(f1,font=('arial',16,'bold'),text="Filet",bd=16,anchor='w')
lblFilet.grid(row=3,column=0)
txtFilet=Entry(f1,font=('arial',12,'bold'),textvariable=Filet,bd=10,insertwidth=4,bg="powder blue",justify='left')
txtFilet.grid(row=3,column=1)

lblChicken = Label(f1,font=('arial',16,'bold'),text="Chicken",bd=16,anchor='w')
lblChicken.grid(row=4,column=0)
txtChicken=Entry(f1,font=('arial',12,'bold'),textvariable=Chicken_Burger,bd=10,insertwidth=4,bg="powder blue",justify='left')
txtChicken.grid(row=4,column=1)

lblCheese_Burger = Label(f1,font=('arial',16,'bold'),text="Cheese Burger",bd=16,anchor='w')
lblCheese_Burger.grid(row=5,column=0)
txtCheese_Burger=Entry(f1,font=('arial',12,'bold'),textvariable=Cheese_Burger,bd=10,insertwidth=4,bg="powder blue",justify='left')
txtCheese_Burger.grid(row=5,column=1)


lblTea = Label(f1,font=('arial',16,'bold'),text="Tea",bd=16,anchor='w')
lblTea.grid(row=6,column=0)
txtTea=Entry(f1,font=('arial',12,'bold'),textvariable=Tea,bd=10,insertwidth=4,bg="powder blue",justify='left')
txtTea.grid(row=6,column=1)

lblBananasake = Label(f1,font=('arial',16,'bold'),text="Banana sake",bd=16,anchor='w')
lblBananasake.grid(row=7,column=0)
txtBananasake=Entry(f1,font=('arial',12,'bold'),textvariable=Bananasake,bd=10,insertwidth=4,bg="powder blue",justify='left')
txtBananasake.grid(row=7,column=1)


#-----------------------------------information----------------------------------------------------

lblDrinks = Label(f1,font=('arial',16,'bold'),text="Drinks",bd=16,anchor='w')
lblDrinks.grid(row=0,column=2)
txtDrinks=Entry(f1,font=('arial',12,'bold'),textvariable=Drinks,bd=10,insertwidth=4,bg="powder blue",justify='left')
txtDrinks.grid(row=0,column=3)


lblPapayasake = Label(f1,font=('arial',16,'bold'),text="Papaya sake",bd=16,anchor='w')
lblPapayasake.grid(row=1,column=2)
txtPapayasake=Entry(f1,font=('arial',12,'bold'),textvariable=Papayasake,bd=10,insertwidth=4,bg="powder blue",justify='left')
txtPapayasake.grid(row=1,column=3)


lblMilksake = Label(f1,font=('arial',16,'bold'),text="milk sake",bd=16,anchor='w')
lblMilksake.grid(row=2,column=2)
txtMilksake=Entry(f1,font=('arial',12,'bold'),textvariable=Milksake,bd=10,insertwidth=4,bg="powder blue",justify='left')
txtMilksake.grid(row=2,column=3)



lblCost = Label(f1,font=('arial',16,'bold'),text="Cost of Mean",bd=16,anchor='w')
lblCost.grid(row=3,column=2)
txtCost=Entry(f1,font=('arial',12,'bold'),textvariable=Cost,bd=10,insertwidth=4,bg="white",justify='left')
txtCost.grid(row=3,column=3)


lblService_Charge = Label(f1,font=('arial',16,'bold'),text="Service_Charge",bd=16,anchor='w')
lblService_Charge.grid(row=4,column=2)
txtService_Charge=Entry(f1,font=('arial',12,'bold'),textvariable=Service_Charge,bd=10,insertwidth=4,bg="white",justify='left')
txtService_Charge.grid(row=4,column=3)

lblTax = Label(f1,font=('arial',16,'bold'),text="Tax",bd=16,anchor='w')
lblTax.grid(row=5,column=2)
txtTax=Entry(f1,font=('arial',12,'bold'),textvariable=Tax,bd=10,insertwidth=4,bg="white",justify='left')
txtTax.grid(row=5,column=3)

lblSubTotal = Label(f1,font=('arial',16,'bold'),text="SubTotal",bd=16,anchor='w')
lblSubTotal.grid(row=6,column=2)
txtSubTotal=Entry(f1,font=('arial',12,'bold'),textvariable=SubTotal,bd=10,insertwidth=4,bg="white",justify='left')
txtSubTotal.grid(row=6,column=3)

lblTotal = Label(f1,font=('arial',16,'bold'),text="Total",bd=16,anchor='w')
lblTotal.grid(row=7,column=2)
txtTotal=Entry(f1,font=('arial',12,'bold'),textvariable=Total,bd=10,insertwidth=4,bg="white",justify='left')
txtTotal.grid(row=7,column=3)

#-------------------------------------------------------------------------------

btnTotal=Button(f1,padx=16,pady=16,fg="black",font=('arial',16,'bold'),width=10,text="Total",bg="powder blue",command=Ref).grid(row=8,column=1)

btnReset=Button(f1,padx=16,pady=16,fg="black",font=('arial',16,'bold'),width=10,text="Reset",bg="powder blue",command=Reset).grid(row=8,column=2)

btnExit=Button(f1,padx=16,pady=16,fg="black",font=('arial',16,'bold'),width=10,text="Exit",bg="powder blue",command=qExit).grid(row=8,column=3)
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

root.mainloop()
