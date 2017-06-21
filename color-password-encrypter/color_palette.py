
"""

Color palette for GUIs
    Copyright (C) 2017  Joel Benjamin

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

""""

Contains 2 classes. One for a color canvas built into the master window.
And the other one for a separate window showing color palette.

"""

import random
from tkinter import *
from colors import COLORS
#from MoveWindow import MovableWindow

BG_COLOR = "#333"


class FixedColorPalette():

	def __init__(self,master):
		self.master = master
		self.def_color = "#3a3bdd"
		self.ColorPaletteCanvas = Canvas(self.master,width = 210,height = 80,bg = 'white',cursor = 'tcross')
		self.ColorPaletteCanvas.grid(row = 4,column=1,padx = 10,pady = 10)
				# colors inside the palette
		self.x_pos = 0
		self.y_pos = 0

		self.const_color = "#3a3bdd"
				# final x coord of the canvas is 200
				# and y coord is 100. -20 from them
		for c in COLORS:
			self.colorsInside = self.ColorPaletteCanvas.create_rectangle(self.x_pos,self.y_pos,self.x_pos+10,self.y_pos+10,fill = c,tags=("{0}".format(c)))
			#showing all the colors on the screen
			self.x_pos += 10
			if self.x_pos > 200:
				self.y_pos += 10
				self.x_pos = 0
		# current is a keyword. It points to the current object. Alternative: CURRENT
		# gets the current clicked color from the palette
		self.ColorPaletteCanvas.tag_bind("current",'<Button-1>',self.get_color)

		self.col_can = Canvas(self.master,width = 30,height = 30,bg = self.def_color )
		self.col_can.grid(row = 5,column=1,padx = 100,pady = 10,sticky = W)
		self.col_lab = Label(self.master,text = self.def_color,bg = BG_COLOR,fg = "#fff")
		self.col_lab.grid(row = 5,column=1,padx = 50,pady = 3,sticky = E)

	def get_color(self,*args):
		# this function updates the color canvas and current color variable
		self.current_color = self.ColorPaletteCanvas.itemcget("current","tags")
		#print(self.current_color[1:8])
		self.col_can.config(bg =self.current_color[1:8])
		self.col_lab.config(text=self.current_color[1:8])
		self.master.update()
		self.const_color = self.current_color
		

	def return_color(self):
		# use this function to get the current color
		return self.const_color


class ColorPalette():

	def __init__(self,master):
		self.master = master 
		self.child_win = Toplevel(self.master)
		self.child_win.geometry("300x320+300+200")
		self.child_win.config(bg=BG_COLOR)
		self.child_win.resizable(0,0)
		self.child_win.title("color pallette")
		self.child_win.overrideredirect(1)
		# default color
		self.move_window_canvas = MovableWindow(self.child_win)
		self.def_color = "#ffffff"
		# color-palette canvas
		self.ColorPaletteCanvas = Canvas(self.child_win,width = 210,height = 220,bg = 'white',cursor = 'tcross')
		self.ColorPaletteCanvas.grid(row = 1,column=1,padx = 10,pady = 10)
		# colors inside the palette
		self.x_pos = 0
		self.y_pos = 0
		# final x coord of the canvas is 200
		# and y coord is 100. -20 from them
		for c in COLORS:
			self.colorsInside = self.ColorPaletteCanvas.create_rectangle(self.x_pos,self.y_pos,self.x_pos+10,self.y_pos+10,fill = c,tags=("{0}".format(c)))
			#showing all the colors on the screen
			self.x_pos += 10
			if self.x_pos > 200:
				self.y_pos += 10
				self.x_pos = 0
		# current is a keyword. It points to the current object. Alternative: CURRENT
		# gets the current clicked color from the palette
		self.ColorPaletteCanvas.tag_bind("current",'<Button-1>',self.get_color)

		self.col_can = Canvas(self.child_win,width = 30,height = 30,bg = self.def_color )
		self.col_can.grid(row = 2,column=1,padx = 100,pady = 10,sticky = W)
		self.col_lab = Label(self.child_win,text = self.def_color,bg = BG_COLOR,fg = "#fff")
		self.col_lab.grid(row = 2,column=1,padx = 50,pady = 3,sticky = E)

	def filter_colornames(self,name):
		# this function filters the color names.
		# The palette used real-color names before, so it had to filter the names
		# now it uses hex-color values, so you can ignore this function
		self.name = name
		self.f_name = ""
		for x in range(0,len(self.name)):
			if self.name[x] == " ":
				break 
			self.f_name += self.name[x]
		return self.f_name


	def update_color(self,*args):
		self.current_color = self.ColorPaletteCanvas.itemcget("current","tags")
		self.col_can.config(bg = self.filter_colornames(self.current_color))
		self.col_lab.config(text=self.filter_colornames(self.current_color))
		self.child_win.update()
		self.def_color = self.current_color
		

	def get_color(self):
		# use this function to get the current color
		return self.def_color
		
