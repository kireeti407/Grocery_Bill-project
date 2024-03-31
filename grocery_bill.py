import tkinter as tk
from tkinter import*
import random as ram
fod= {"bread":40,"candy":30,"hotdog":40,"burger":60,"sandwich":50}
groce={"rice":60,"food-oil":100,"salt":20,"wheat":70,"sugur":40}
othe={"gatorade":30,"coke":80,"juice":50,"waffer":80,"biscuits":40}
print(fod["bread"])
item={
	"fod":{"bread":0,"candy":0,"hotdog":0,"burger":0,"sandwich":0},
	"groce":{"rice":0,"food-oil":0,"salt":0,"wheat":0,"sugur":0},
	"othe":{"gatorade":0,"coke":0,"juice":0,"waffer":0,"biscuits":0}
}
detail=['','','']
li=[0,0,0]
def krt():
	a=[fod,groce,othe]
	ai=0
	for i in item:
		tol=0
		for j in item[i]:
			tol+=item[i][j]*a[ai][j]
		li[ai]=tol
		ai+=1
print(fod,groce,othe)
class tkin(tk.Tk): 
	def __init__(self, *args, **kwargs): 
		tk.Tk.__init__(self, *args, **kwargs)
		container = tk.Frame(self) 
		container.pack(side = "top", fill = "both", expand = True) 
		container.grid_rowconfigure(0, weight = 1)
		container.grid_columnconfigure(0, weight = 1)
		self.frames = {} 
		for F in (main, Food, grocery,other,bill):
			frame = F(container, self)
			self.frames[F] = frame
			frame.grid(row = 0, column = 0, sticky ="nsew")
		self.show_frame(main)
	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()

class main(tk.Frame):
	def __init__(self, parent, contoller): 
		tk.Frame.__init__(self, parent,background="#2742FF")
		tk.Label(self,text="SHOP-HERE",font=100,bg="#08222D",width=35,fg="white").place(y=20)
		tk.Button(self,text="Food-items",background="#00ED64",borderwidth=0,width=10,height=2,fg="black",activeforeground="black",command = lambda : contoller.show_frame(Food)).place(x=115,y=80)
		tk.Button(self,text="grocery",background="#00ED64",borderwidth=0,width=10,height=2,fg="black",activeforeground="black",command = lambda : contoller.show_frame(grocery)).place(x=115,y=150)
		tk.Button(self,text="other",background="#00ED64",borderwidth=0,width=10,height=2,fg="black",activeforeground="black",command=lambda : contoller.show_frame(other)).place(x=115,y=220)
		tk.Label(self,text="Customer details",fg="white",bg="#08222D",width=35,font=20).place(y=300)
		tk.Label(self,text="Customer Name :",bg="#2742FF").place(x=40,y=360)
		t=tk.Entry(self,borderwidth=0,width=19)
		t.place(x=140,y=360)
		tk.Label(self,text="     Phone No       :",bg="#2742FF").place(x=40,y=400)
		t1=tk.Entry(self,borderwidth=0,width=19)
		t1.place(x=140,y=400)
		tk.Label(self,text="     Bill No             :",bg="#2742FF").place(x=40,y=440)
		tk.Label(self,width=16,borderwidth=0).place(x=140,y=440)
		ra=ram.randint(100,5000)
		def enter():
			detail[0]=t.get()
			detail[1]=t1.get()
			r=ram.randint(100,5000)
			t2=tk.Label(self,text=r,width=16,borderwidth=0)
			t2.place(x=140,y=440)
			detail[2]=r
		tk.Button(self,text="Enter",borderwidth=0,width=10,height=2,background="#00ED64",command=enter).place(x=115,y=490)
		print(ra)
class Food(tk.Frame):
	def __init__(self, parent, contoller):	
		tk.Frame.__init__(self, parent,background="#2742FF")
		tk.Label(self,text="FOOD-ITEMS",bg="#08222D",width=35,font=120,height=2,borderwidth=4,fg="white").place(y=20)

		def bread():
			item["fod"]["bread"]+=int(k.get())
			print(item["fod"]["bread"])
		tk.Label(self,text="BREAD\nRs-40",bg='gray',width=10,height=4,fg="black",borderwidth=4).place(y=100,x=30)
		k=tk.Entry(self,width=10,borderwidth=0)
		k.place(y=180,x=20)
		tk.Button(self,text="add-cart",height=1,bg="gold",activebackground="white",borderwidth=0,command=bread).place(y=178,x=90)
		
		def candy():
			item["fod"]["candy"]+=int(l.get())
		tk.Label(self,text="CANDY\nRs-30",bg='gray',width=10,height=4,fg="black",borderwidth=4).place(y=100,x=180)
		l=tk.Entry(self,width=10,borderwidth=0)
		l.place(y=180,x=160)
		tk.Button(self,text="add-cart",height=1,bg="gold",activebackground="white",borderwidth=0,command=candy).place(y=178,x=230)
		
		def Burger():
			item["fod"]["burger"]+=int(m.get())
		tk.Label(self,text="BURGER\nRs-60",bg='gray',width=10,height=4,fg="black",borderwidth=4).place(y=220,x=30)
		m=tk.Entry(self,width=10,borderwidth=0)
		m.place(y=300,x=20)
		tk.Button(self,text="add-cart",height=1,bg="gold",activebackground="white",borderwidth=0,command=Burger).place(y=298,x=90)
		
		def hotdog():
			item["fod"]["hotdog"]+=int(n.get())
		tk.Label(self,text="HOTDOG\nRs-40",bg='gray',width=10,height=4,fg="black",borderwidth=4).place(y=220,x=180)
		n=tk.Entry(self,width=10,borderwidth=0)
		n.place(y=300,x=160)
		tk.Button(self,text="add-cart",height=1,bg="gold",activebackground="white",borderwidth=0,command=hotdog).place(y=298,x=230)
		
		def sandwich():
			item["fod"]["sandwich"]+=int(o.get())
		tk.Label(self,text="SANDWICH\nRs-50",bg='gray',width=10,height=4,fg="black",borderwidth=4).place(y=340,x=115)
		o=tk.Entry(self,width=10,borderwidth=0)
		o.place(y=420,x=95)
		tk.Button(self,text="add-cart",height=1,bg="gold",activebackground="white",borderwidth=0,command=sandwich).place(y=418,x=165)
		tk.Button(self,text='HOME',width=8,command = lambda : contoller.show_frame(main),background="#00ED64",borderwidth=0).place(y=470,x=30)
		tk.Button(self,text='OTHER',width=8,command = lambda : contoller.show_frame(other),background="#00ED64",borderwidth=0).place(y=510,x=30)
		tk.Button(self,text='GROCERY',width=8,command = lambda : contoller.show_frame(grocery),background="#00ED64",borderwidth=0).place(y=470,x=200)
		def comm():
			krt()
			contoller.show_frame(bill)
		tk.Button(self,text='BILL',width=8,command = comm,background="#00ED64",borderwidth=0).place(y=510,x=200)

class grocery(tk.Frame): 
	def __init__(self, parent, contoller):
		tk.Frame.__init__(self, parent,background="#2742FF")
		tk.Label(self,text="GROCERY-ITEMS",bg="#08222D",width=35,font=120,height=2,borderwidth=4,fg="white").place(y=20)
		
		def rice():
			item["groce"]["rice"]+=int(a1.get())
		tk.Label(self,text="RICE\nRs-60",bg='gray',width=10,height=4,fg="black",borderwidth=4).place(y=100,x=30)
		a1=tk.Entry(self,width=10,borderwidth=0)
		a1.place(y=180,x=20)
		tk.Button(self,text="add-cart",height=1,bg="gold",activebackground="white",borderwidth=0,command=rice).place(y=178,x=90)

		def foodoil():
			item["groce"]["food-oil"]+=int(a2.get())
		tk.Label(self,text="FOOD-OIL\nRs-100",bg='gray',width=10,height=4,fg="black",borderwidth=4).place(y=100,x=180)
		a2=tk.Entry(self,width=10,borderwidth=0)
		a2.place(y=180,x=160)
		tk.Button(self,text="add-cart",height=1,bg="gold",activebackground="white",borderwidth=0,command=foodoil).place(y=178,x=230)

		def salt():
			item["groce"]["salt"]+=int(a3.get())
		tk.Label(self,text="SALT\nRs-20",bg='gray',width=10,height=4,fg="black",borderwidth=4).place(y=220,x=30)
		a3=tk.Entry(self,width=10,borderwidth=0)
		a3.place(y=300,x=20)
		tk.Button(self,text="add-cart",height=1,bg="gold",activebackground="white",borderwidth=0,command=salt).place(y=298,x=90)

		def wheat():
			item["groce"]["wheat"]+=int(a4.get())
		tk.Label(self,text="WHEAT\nRs-70",bg='gray',width=10,height=4,fg="black",borderwidth=4).place(y=220,x=180)
		a4=tk.Entry(self,width=10,borderwidth=0)
		a4.place(y=300,x=160)
		tk.Button(self,text="add-cart",height=1,bg="gold",activebackground="white",borderwidth=0,command=wheat).place(y=298,x=230)
		
		def sugur():
			item["groce"]["sugur"]+=int(a5.get())
		tk.Label(self,text="SUGUR\nRs-40",bg='gray',width=10,height=4,fg="black",borderwidth=4).place(y=340,x=115)
		a5=tk.Entry(self,width=10,borderwidth=0)
		a5.place(y=420,x=95)
		tk.Button(self,text="add-cart",height=1,bg="gold",activebackground="white",borderwidth=0,command=sugur).place(y=418,x=165)

		tk.Button(self,text='HOME',width=8,command = lambda : contoller.show_frame(main),background="#00ED64",borderwidth=0).place(y=470,x=30)
		tk.Button(self,text='OTHER',width=8,command = lambda : contoller.show_frame(other),background="#00ED64",borderwidth=0).place(y=510,x=30)
		tk.Button(self,text='FOOD',width=8,command = lambda : contoller.show_frame(Food),background="#00ED64",borderwidth=0).place(y=470,x=200)
		def comm():
			krt()
			contoller.show_frame(bill)
		tk.Button(self,text='BILL',width=8,command = comm,background="#00ED64",borderwidth=0).place(y=510,x=200)

class other(tk.Frame):
	def __init__(self,parent,contoller):
		tk.Frame.__init__(self,parent)
		tk.Frame.__init__(self, parent,background="#2742FF")
		tk.Label(self,text="OTHER-ITEMS",bg="#08222D",width=35,font=120,height=2,borderwidth=4,fg="white").place(y=20)

		def gat():
			item['othe']["gatorade"]+=int(b1.get())
		tk.Label(self,text="GATORADE\nRs-30",bg='gray',width=10,height=4,fg="black",borderwidth=4).place(y=100,x=30)
		b1=tk.Entry(self,width=10,borderwidth=0)
		b1.place(y=180,x=20)
		tk.Button(self,text="add-cart",height=1,bg="gold",activebackground="white",borderwidth=0,command=gat).place(y=178,x=90)

		def coak():
			item['othe']["coke"]+=int(b2.get())
		tk.Label(self,text="COKE\nRs-80",bg='gray',width=10,height=4,fg="black",borderwidth=4).place(y=100,x=180)
		b2=tk.Entry(self,width=10,borderwidth=0)
		b2.place(y=180,x=160)
		tk.Button(self,text="add-cart",height=1,bg="gold",activebackground="white",borderwidth=0,command=coak).place(y=178,x=230)

		def juice():
			item['othe']["juice"]+=int(b3.get())
		tk.Label(self,text="JUICE\nRs-50",bg='gray',width=10,height=4,fg="black",borderwidth=4).place(y=220,x=30)
		b3=tk.Entry(self,width=10,borderwidth=0)
		b3.place(y=300,x=20)
		tk.Button(self,text="add-cart",height=1,bg="gold",activebackground="white",borderwidth=0,command=juice).place(y=298,x=90)

		def waffer():
			item['othe']["waffer"]+=int(b4.get())
		tk.Label(self,text="WAFFER\nRs-80",bg='gray',width=10,height=4,fg="black",borderwidth=4).place(y=220,x=180)
		b4=tk.Entry(self,width=10,borderwidth=0)
		b4.place(y=300,x=160)
		tk.Button(self,text="add-cart",height=1,bg="gold",activebackground="white",borderwidth=0,command=waffer).place(y=298,x=230)

		def bis():
			item['othe']["biscuits"]+=int(b5.get())
		tk.Label(self,text="BISCUITS\nRs-40",bg='gray',width=10,height=4,fg="black",borderwidth=4).place(y=340,x=115)
		b5=tk.Entry(self,width=10,borderwidth=0)
		b5.place(y=420,x=95)
		tk.Button(self,text="add-cart",height=1,bg="gold",activebackground="white",borderwidth=0,command=bis).place(y=418,x=165)

		tk.Button(self,text='HOME',width=8,command = lambda : contoller.show_frame(main),borderwidth=0,background="#00ED64").place(y=470,x=30)
		tk.Button(self,text='FOOD',width=8,command = lambda : contoller.show_frame(Food),borderwidth=0,background="#00ED64").place(y=510,x=30)
		tk.Button(self,text='GROCERY',width=8,command = lambda : contoller.show_frame(grocery),borderwidth=0,background="#00ED64").place(y=470,x=200)

		def comm():
			krt()
			contoller.show_frame(bill)
		tk.Button(self,text='BILL',width=8,command = comm,borderwidth=0,background="#00ED64").place(y=510,x=200)
class bill(tk.Frame):
	def __init__(self,parent,contoller):
		tk.Frame.__init__(self,parent,background="#2742FF")
		tk.Label(self,text="BILL-MENU",fg="white",font="bold",width=30,bg="#2742FF").place(y=0)
		tk.Label(self,text="Food Total:",borderwidth=1,bg="#2742FF").place(x=50,y=30)
		tk.Label(self,text="Grocery Total:",borderwidth=1,bg="#2742FF").place(x=50,y=50)
		tk.Label(self,text="Other Total:",borderwidth=1,bg="#2742FF").place(x=50,y=70)
		tk.Label(self,text="Food Tax:",borderwidth=1,bg="#2742FF").place(x=170,y=30)
		tk.Label(self,text="Grocery Tax:",borderwidth=1,bg="#2742FF").place(x=170,y=50)
		tk.Label(self,text="Other Tax :",borderwidth=1,bg="#2742FF").place(x=170,y=70)
		def com():	
			tk.Label(self,borderwidth=0,text=li[0],bg="#2742FF").place(x=130,y=30)
			tk.Label(self,borderwidth=0,text=li[1],bg="#2742FF").place(x=130,y=50)
			tk.Label(self,borderwidth=0,text=li[2],bg="#2742FF").place(x=130,y=70)
			tk.Label(self,borderwidth=0,text=li[0]*0.1,bg="#2742FF").place(x=240,y=30)
			tk.Label(self,borderwidth=0,text=li[1]*0.2,bg="#2742FF").place(x=240,y=50)
			tk.Label(self,borderwidth=0,text=li[2]*0.2,bg="#2742FF").place(x=240,y=70)
			su=(li[0]*0.1+li[1]*0.2+li[2]*0.2)
			tk.Label(self,text="============Customer-Details================",fg="white",bg="#2742FF").place(x=0,y=115)
			tk.Label(self,text="customer Name  :",bg="#2742FF").place(x=60,y=130)
			tk.Label(self,text="Phone No             :",bg="#2742FF").place(x=60,y=150)
			tk.Label(self,text="Bill No                   :",bg="#2742FF").place(x=60,y=170)
			tk.Label(self,text=detail[0],bg="#2742FF").place(x=160,y=130)
			tk.Label(self,text=detail[1],bg="#2742FF").place(x=160,y=150)
			tk.Label(self,text=detail[2],bg="#2742FF").place(x=160,y=170)
			tk.Label(self,text="===items====no.items==============price==================",fg="white",bg="#2742FF").place(y=190)
			xa=210
			a=[fod,groce,othe]
			ai=0
			for i in item:
				for j in item[i]:
					if item[i][j] !=0:
						tk.Label(self,text=j,bg="#2742FF",borderwidth=0).place(x=20,y=xa)
						tk.Label(self,text=item[i][j],bg="#2742FF",borderwidth=0).place(x=110,y=xa)
						tk.Label(self,text=(a[ai][j]*item[i][j]),bg="#2742FF",borderwidth=0).place(x=250,y=xa)
						xa+=17
				ai+=1
			tk.Label(self,text="=============================================",fg="white",bg="#2742FF").place(y=xa)
			tk.Label(self,text="total+tax :",bg="#2742FF").place(x=170,y=xa+20)
			tk.Label(self,text=sum(li)+su,bg="#2742FF").place(x=250,y=xa+20)
			def clear():
				tk.Label(self,width=330,height=29,bg="#2742FF").place(y=120)
				tk.Label(self,text='      ',bg="#2742FF").place(x=130,y=30)
				tk.Label(self,text='      ',bg="#2742FF").place(x=130,y=50)
				tk.Label(self,text='      ',bg="#2742FF").place(x=130,y=70)
				tk.Label(self,text='      ',bg="#2742FF").place(x=240,y=30)
				tk.Label(self,text='      ',bg="#2742FF").place(x=240,y=50)
				tk.Label(self,text="       ",bg="#2742FF").place(x=240,y=70)
				i=0
				for k in item:
					detail[i]=' '
					li[i]=0
					for j in item[k]:
						item[k][j]=0
					i+=1
				contoller.show_frame(main)
			tk.Button(self,text="clear and home",bg="#00ED64",borderwidth=0,fg="black",command=clear).place(x=105,y=xa+50)
		tk.Button(self,text="print",command=com,borderwidth=0,background="#00ED64",fg="black",width=8,).place(x=115,y=95)
gro = tkin()
gro.geometry("300x550")
gro.resizable(False,False)
gro.title("Grocery-bill")
gro.mainloop()