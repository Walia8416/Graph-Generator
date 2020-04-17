#MADE BY Aditya Walia 

import tkinter as tk
from matplotlib import pyplot as plt



def subbut():
	global win2,d,var3,e1,l1,xaxise,yaxise,axislabs,title_entry

	axislabs = []
	win2 = tk.Tk()
	win2.title('DATA ENTRY')
	win2.geometry('600x600')
	win2.resizable(False, False)


	textl = 'Label   -   '
	textr = 'Value'
	vsize=15
	lsize=15
	lwid = 25
	if v1.get()==3:
		textl = 'X-COORDINATE  -  '
		textr = 'Y-COORDINATE'
		vsize=12
		lwid = 5
		lsize=12

	d = {}	
	value = tk.Label(win2,text=textr,font=('Helvetica',vsize))
	value.place(y=200,x=450)

	if v1.get()==1 or v1.get()==3:
		yaxis = tk.Label(win2,text = 'Enter Y-Axis Label - ',font=('Helvetica',15))
		yaxis.place(x=50,y=50)
		yaxise = tk.Entry(win2,width='25')
		yaxise.place(y=50,x=300)


		xaxis = tk.Label(win2,text='Enter X-Axis Label - ',font = ('Helvetica',16))
		xaxis.place(x=50,y=150)
		xaxise = tk.Entry(win2,width='25')
		xaxise.place(y=150,x=300)
	

	title = tk.Label(win2,text='Title? - ',font=('Helvetica',16))
	title.place(x=50,y=100)

	title_entry = tk.Entry(win2,width=25)
	title_entry.place(x=300,y=100)


	l1 = tk.Label(win2,text = textl,font = ('Helvetica',lsize))
	l1.place(x=50,y=250)
	e1 = tk.Entry(win2 ,width=lwid)
	e1.place(x=200,y=250)
	var3 = tk.Entry(win2,width='5')
	var3.place(y=250,x=450)
	


	add_but = tk.Button(win2,text='Add Data!',fg='red',command = Add_More,font=('Helvetica',16))

	add_but.place(x=400,y=400)
	
	done_but=tk.Button(win2,text='Generate Graph?',fg='green',command=GenGraph,font=('Helvetica',16))
	done_but.place(x=150,y=400)
	

	

def Add_More():
	x = str(e1.get())
	if v1.get()==3:
		x=int(e1.get())


	d[x]=int(var3.get())
	e1.delete(0,tk.END)
	var3.delete(0,tk.END)
	


def GenGraph():

	
	label=[]
	vs = []
	for i in d:

		label.append(i)
		vs.append(d[i])

	if v1.get()==1:
		plt.bar(label,vs)
		plt.xlabel(str(xaxise.get()))
		plt.ylabel(str(yaxise.get()))
		plt.title(str(title_entry.get()))
		plt.show()


	elif v1.get()==2:
		plt.pie(vs,labels=label)
		plt.title(str(title_entry.get()))
		plt.show()

	elif v1.get()==3:
		plt.plot(label,vs)
		plt.xlabel(xaxise.get())
		plt.ylabel(yaxise.get())
		plt.title(str(title_entry.get()))
		plt.show()






win = tk.Tk()
win.geometry("500x500")
win.title('GRAPH GENERATOR')
win.resizable(False, False)

head = tk.Label(win,text='GRAPH GENERATOR',font=('Helvetica, 18'))
head.place(x=150,y=15)

name = tk.Label(win,text='By Aditya Walia',font = ('Helvetica,10'))
name.place(x=190,y=45)

select = tk.Label(win, text='PLEASE SELECT YOUR GRAPH: - ', font = ('Helvetica',12))
select.place(x=5,y=120)
v1 = tk.IntVar()

bar = tk.Radiobutton(win,text='BAR GRAPH',font = ('Helvetica',16),variable = v1,value=1)
pie = tk.Radiobutton(win,text='PIE GRAPH',font = ('Helvetica',16),variable = v1,value=2)

line = tk.Radiobutton(win,text='LINE CHART',font = ('Helvetica',16),variable=v1,value=3)
bar.place(x=150,y=165)
pie.place(x=150,y=220)
line.place(y=275,x=150)



submit = tk.Button(win,fg='black',text = 'SUBMIT',command=subbut,font=('Helvetica',16))
submit.place(x=250,y=370)






win.mainloop()
