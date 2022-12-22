# importing whole module
from tkinter import *
 
from time import strftime

# creating tkinter window
root = Tk()
root.title('Clock')

# This function is used to
# display time on the label
def rtime():
	estring = strftime('%H:%M:%S %p')
	lbl.config(text = estring)
	lbl.after(200, rtime)

# Styling the label widget so that clock
# will look more attractive
lbl = Label(root, font = ('calibri', 30, 'bold'),
			background = 'green',
			foreground = 'white')

# Placing clock at the centre
# of the tkinter window
lbl.pack()
rtime()
root.mainloop()
