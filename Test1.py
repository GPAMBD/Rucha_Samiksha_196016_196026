
from tkinter import *
import sqlite3
from tkinter import messagebox

def logic():
  base = Tk()
  base.title("-----")
  base.geometry("1000x750+0+0")

  con = sqlite3.connect("Restaurant_Billing_Project.db")

  def total():
       fobj = open("Hotel.txt","a")
       t7 = str(txt8.get())
       t8 = str(txt9.get())
       t1 = int(txt1.get())
       t2 = int(txt2.get())
       t3 = int(txt3.get())
       t4 = int(txt4.get())
       t5 = int(txt5.get())
       t6 = int(txt6.get())

       pb1 = t1 * 80
       md1 = t2 * 70
       mr1 = t3 * 100
       pt1 = t4 * 140
       pp1 = t5 * 50
       vb1 = t6 * 90

       tot = pb1 + md1 + mr1 + pt1 + pp1 + vb1
       txt7.insert(0, int(tot))

       l = Label(base, text=tot, bg="skyblue", font="25", fg="red")
       l.place(x=260, y=620)

       fobj.write(str(t7)+",\t\t\t\t"+str(t8)+",\t\t\t"+str(t1)+",\t\t\t\t"+str(t2)+",\t\t\t\t"+str(t3)+",\t\t\t\t"+str(t4)+",\t\t\t\t\t"+str(t5)+",\t\t\t\t\t"+str(t6)+",\t\t\t\t"+str(tot)+"\n")
       fobj.close()
       print("DATA SAVED...!")


       fob = open("Rough.txt","a")
       fob.write(str(t7) + "," + str(t8) + "," + str(t1) + "," + str(t2) + "," + str(t3) + "," + str(t4) + "," + str(t5) + "," + str(t6) + "," + str(tot) + "\n")
       fob.close()

       fobj = open("Rough.txt", "r")
       for line in fobj:
            a = line.split(",")
            a1 = a[0]
            a2 = a[1]
            a3 = a[2]
            a4 = a[3]
            a5 = a[4]
            a6 = a[5]
            a7 = a[6]
            a8 = a[7]
            a9 = a[8]

            query = f"insert into Resto_info values('{a1}','{a2}','{a3}','{a4}','{a5}','{a6}','{a7}','{a8}','{a9}')"

       con.execute(query)
       con.commit()
       con.close()


  def clear():

         txt1.delete(0, END)
         txt2.delete(0, END)
         txt3.delete(0, END)
         txt4.delete(0, END)
         txt5.delete(0, END)
         txt6.delete(0, END)
         txt7.delete(0, END)
         txt8.delete(0, END)
         txt9.delete(0, END)
         txt1.focus()




  lb1 =Label(base,text="RS Restaurant",font="50",bg="sky blue",fg="red",width="50")
  lb1.place(x=160,y=30,height="40")


  lb13 = Label(base,text="Name: ",font="40")
  lb13.place(x=40,y=140)

  txt8 = Entry(base,width="50")
  txt8.place(x=120,y=140,height="25")


  lb14 = Label(base,text="Phone No: ",font="40")
  lb14.place(x=490,y=140)

  txt9 = Entry(base,width="30")
  txt9.place(x=610,y=140,height="25")


  lb2 = Label(base,text="Select your Items:",font="40")
  lb2.place(x=90,y=190)

  lb3 = Label(base,text="PAV BHAJI",font="10")
  lb3.place(x=20,y=240)

  txt1 = Entry(base,width="20")
  txt1.place(x=20,y=275,height="25")

  lb4 = Label(base,text="MASALA DOSA",font="10")
  lb4.place(x=20,y=340)

  txt2 = Entry(base,width="20")
  txt2.place(x=20,y=375,height="25")

  lb5 = Label(base,text="MANTURIAN",font="10")
  lb5.place(x=200,y=240)

  txt3 = Entry(base,width="20")
  txt3.place(x=200,y=275,height="25")

  lb6 = Label(base,text="PANEER TIKKA",font="10")
  lb6.place(x=200,y=340)

  txt4 = Entry(base,width="20")
  txt4.place(x=200,y=375,height="25")

  lb7 = Label(base,text="PANI PURI",font="10")
  lb7.place(x=380,y=240)

  txt5 = Entry(base,width="20")
  txt5.place(x=380,y=275,height="25")

  lb8 = Label(base,text="VEG BIRYANI",font="10")
  lb8.place(x=380,y=340)

  txt6 = Entry(base,width="20")
  txt6.place(x=380,y=375,height="25")

  btn1 = Button(base,text="BILL",width="20",bg="silver",command=total)
  btn1.place(x=190,y=470,height="45")

  lb13 = Label(base,text="BILL AMOUNT:",font="10")
  lb13.place(x=50,y=550)


  lb13 = Label(base,text="BILL AMOUNT:",font="10")
  lb13.place(x=50,y=620)

  btn2 = Button(base,text="CLEAR",width="10",font="30",bg="silver",fg="red",command=clear)
  btn2.place(x=770,y=600,height="40")

  txt7 = Entry(base,width="40")
  txt7.place(x=240,y=550,height="30")

  lb9 = Label(base,text="MENU",font="30")
  lb9.place(x=780,y=200)

  lb0 = Label(base,text="PAV BHAJI \t Rs.80",font="30")
  lb0.place(x=700,y=250)

  lb11 = Label(base,text="MASALA DOSA \t Rs.70",font="30")
  lb11.place(x=700,y=280)

  lb12 = Label(base,text="MANTURIAN \t Rs.100",font="30")
  lb12.place(x=700,y=310)

  lb12 = Label(base,text="PANEER TIKKA \t Rs.140",font="30")
  lb12.place(x=700,y=340)

  lb12 = Label(base,text="PANI PURI \t Rs.50",font="30")
  lb12.place(x=700,y=370)

  lb12 = Label(base,text="VEG BIRYANI \t Rs.90",font="30")
  lb12.place(x=700,y=400)

  base.mainloop()



root= Tk()
root.geometry("1400x750+0+0")
root.title("Restaurant Billing System")
root.configure(background='sky blue')

Tops = Frame(root, bg='dark blue', bd=25, pady=20, relief=GROOVE)
Tops.pack(side=TOP)

lblTitle = Label(Tops, font=('arial', 30, 'bold'), text='Restaurant Billing System', bd=15, bg='sky blue',fg='dark blue', justify=CENTER)
lblTitle.grid(row=0)

ReceiptCal_Function = Frame(root, bg='dark blue', bd=10, relief=GROOVE)
ReceiptCal_Function.pack(side=LEFT)

Buttons_Function = Frame(ReceiptCal_Function, bg='dark blue', bd=3, relief=GROOVE)
Buttons_Function.pack(side=TOP)

Calculator_Function = Frame(ReceiptCal_Function, bg='dark blue', bd=6, relief=GROOVE)
Calculator_Function.pack(side=BOTTOM)

Receipt_Function = Frame(ReceiptCal_Function, bg='dark blue', bd=4, relief=GROOVE)
Receipt_Function.pack(side=BOTTOM)

MenuFrame = Frame(root, bg='dark blue', bd=32, relief=GROOVE)
MenuFrame.pack(side=RIGHT)
Total_Function = Frame(MenuFrame, bg='sky blue', bd=4)
Total_Function.pack(side=BOTTOM)
Drinks_Function = Frame(MenuFrame, bg='sky blue', bd=4)
Drinks_Function.pack(side=TOP)

Drinks_Function = Frame(MenuFrame, bg='sky blue', bd=4, relief=GROOVE)
Drinks_Function.pack(side=LEFT)
Food_Function = Frame(MenuFrame, bg='sky blue', bd=4, relief=GROOVE)
Food_Function.pack(side=RIGHT)

ll1 = Label(text="CLICK ON BUTTON BELOW...",font="20")
ll1.place(x=550,y=350)

b1 = Button(text="Welcome..!",font="20",width="40",height="5",bg="pink",command=logic)
b1.place(x=470,y=400)

root.mainloop()

