
import random
from tkinter import *
from tkinter import font
from color_palette import FixedColorPalette

class Win():

	def __init__(self,master):
		self.master = master
		self.master.geometry("330x400+300+200")
		self.master.resizable(0,0)
		self.master.config(bg = "#333")
		self.master.title("password encripter v1.0")
		self.password_label = Label(self.master,text = "Enter your password here",bg = "#333",fg = "#fff").grid(row = 1,column = 1,padx = 10,pady = 2)
		self.password_entry = Entry(self.master,width = 30,bd = 0)
		self.password_entry.grid(row = 2,column = 1,padx = 25,pady = 10,ipady = 3)
		self.select_color = Label(self.master,text = "Add color to your password",bg = "#333",fg = "#fff").grid(row = 3,column = 1,padx = 10,pady = 2)
		self.color_box = FixedColorPalette(self.master)
		self.generate_button = Button(self.master,text = "encrypt password",width = 15,\
			height = 3,cursor = "hand2",bd = 0,bg = "#2951c6",fg = "#fff",\
			activebackground = "#fff",activeforeground = "#2951c6",highlightthickness=0,\
			command = self.gen_pw)
		self.generate_button.grid(row = 6,column = 1,padx = 25,pady = 3,ipadx = 10,ipady = 3)

		# show pass word
		self.show_pw = Label(self.master,text = "Your Password"\
			,bg = "#333",fg = "#fff")
		self.show_pw.grid(row = 7,column = 1,padx = 10,pady = 2)

	def gen_pw(self):
		self.new_pw = self.password_entry.get()
		self.hex_color = self.color_box.return_color()[1:8]
		self.color_split = [x for x in self.hex_color]
		self.pwd_split = [x for x in self.new_pw]
		self.new_pw = (self.color_split + self.pwd_split)
		random.shuffle(self.new_pw)
		self.show_pw.config(text = self.new_pw)
		


root = Tk()
app = Win(root)
root.mainloop()