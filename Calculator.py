import tkinter as tk
from math import *

class Calculator:
	def __init__(self, master):
		# expression that will be displayed on screen
		self.expression = ""
		# be used to store data in memory
		self.recall = ""
		# used to switch between units of rad,deg and grad
		self.convert_constant = ""
		# self.answer
		self.sum_up = ""
		# create string for text input
		text_Input = tk.StringVar()
		# assign instance to master
		self.master = master
		# set frame showing inputs and title
		top_frame = tk.Frame(master, width=650,height = 20, bd=4, relief='flat',bg = '#666666')
		top_frame.pack(side=tk.TOP)
		# set frame showing all buttons
		bottom_frame = tk.Frame(master, width=650, height = 470, bd=4, relief='flat',bg = '#666666')
		bottom_frame.pack(side=tk.BOTTOM)
		# name of calculator
		my_item = tk.Label(top_frame,text="Simple Scientific Calculator", font=('arial',14),fg='white',width=26,bg = '#666666')
		my_item.pack()
		# entry interface for inputs
		txtDisplay = tk.Entry(top_frame,font=('arial',36),relief='flat',bg = '#666666',fg='white',textvariable = text_Input,width=60,bd=4,justify = 'right')
		txtDisplay.pack()

		# row 0 
		# left bracket button
		self.btn_left_brack = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white',bg = '#666666', font=('arial', 18),width=2, height=2,
		text="(",relief='flat',activebackground="#666666",command=lambda: btnClick('('))
		self.btn_left_brack.grid(row=0, column=0)
		# right bracket button
		self.btn_right_brack = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white',bg = '#666666', font=('arial', 18),
		width=2, height=2,relief='flat',text=")",activebackground="#666666", command=lambda: btnClick(')'))
		self.btn_right_brack.grid(row=0, column=1)
		# takes e to some exponent that you insert into the function
		self.btn_exp = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white',bg = '#666666', font=('arial', 18), width=2,
		height=2,relief='flat',text="exp",activebackground="#666666", command=lambda: btnClick('exp('))
		self.btn_exp.grid(row=0, column=2)
		# constant pi
		self.btn_pi = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white',bg = '#666666', font=('arial', 18),
		width=2, height=2,relief='flat',activebackground="#666666", text="ฯ€", command=lambda: btnClick('pi'))
		self.btn_pi.grid(row=0, column=3)
		# clears self.expression
		self.btn_clear = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white',bg = '#666666', font=('arial', 18), width=2,
		height=2,text="C",relief='flat',activebackground="#666666", command=lambda: btnClearAll())
		self.btn_clear.grid(row=0, column=4)
		# deletes last string input
		self.btn_del = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white',bg = '#666666', font=('arial', 18), width=2,
		height=2,text="del",relief='flat',activebackground="#666666", command=lambda: btnClear1())
		self.btn_del.grid(row=0, column=5)
		# inputs a negative sign to the next entry
		self.btn_change_sign = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white',bg = '#666666', font=('arial', 18),
		width=2, height=2,relief='flat',text="+/-",activebackground="#666666", command=lambda: change_signs())
		self.btn_change_sign.grid(row=0, column=6)
		# division
		self.btn_div = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white',bg = '#666666', font=('arial', 18), width=2,
		height=2,text="รท",relief='flat',activebackground="#666666", command=lambda: btnClick('/'))
		self.btn_div.grid(row=0, column=7)
		# square root
		self.btn_sqrt = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white',bg = '#666666', font=('arial', 18), width=2,
		height=2,relief='flat',text="sqrt",activebackground="#666666", command=lambda: btnClick('sqrt('))
		self.btn_sqrt.grid(row=0, column=8)

		# row 1

		# changes trig function outputs to degrees
		self.btn_Deg = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white',bg = '#666666', font=('arial', 18), width=2, height=2,
		text="Deg",relief='flat',activebackground="#666666",foreground='white',activeforeground = 'orange', command=lambda:convert_deg())
		self.btn_Deg.grid(row=1, column=0)
		# changes trig function outputs to default back to radians
		self.btn_Rad = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white',bg = '#666666', font=('arial', 18), width=2,
		height=2,text="Rad",relief='flat',foreground='orange',activeforeground = 'orange',activebackground="#666666", command=lambda:convert_rad())
		self.btn_Rad.grid(row=1, column=1)

		# changes trig function outputs to gradians
		self.btn_root_of = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white',bg = '#666666', font=('arial', 18), width=2, height=2,
		text="xโ ",relief='flat',activebackground="#666666", command=lambda:btnClick('**(1/'))
		self.btn_root_of.grid(row=1, column=2)
		# takes the absolute value of an expression
		self.btn_abs = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white',bg = '#666666', font=('arial', 18), width=2,
		height=2,relief='flat', text="abs",activebackground="#666666", command=lambda: btnClick('abs' + '('))
		self.btn_abs.grid(row=1, column=3)
		# seven
		self.btn_7 = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white',bg = '#4d4d4d', font=('arial', 18), width=2, height=2,
		text="7", relief='flat',activebackground="#4d4d4d",command=lambda: btnClick(7))
		self.btn_7.grid(row=1, column=4)
		# eight
		self.btn_8 = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white',bg = '#4d4d4d', font=('arial', 18), width=2, height=2,
		text="8",relief='flat',activebackground="#4d4d4d", command=lambda: btnClick(8))
		self.btn_8.grid(row=1, column=5)
		# nine
		self.btn_9 = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white',bg = '#4d4d4d', font=('arial', 18), width=2, height=2,
		text="9",relief='flat',activebackground="#4d4d4d", command=lambda: btnClick(9))
		self.btn_9.grid(row=1, column=6)
		# multiplication
		self.btn_mult = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white',bg = '#666666', font=('arial', 18), width=2,
		height=2,relief='flat',text="x",activebackground="#666666", command=lambda: btnClick('*'))
		self.btn_mult.grid(row=1, column=7)
		# 'memory clear' button. Wipes self.recall to an empty string
		self.btn_MC = tk.Button(bottom_frame,padx=16,pady=1,bd=4,fg='white',bg = '#666666',font =('arial',18),width=2,height=2,
		text="MC",relief='flat',activebackground="#666666",command=lambda:memory_clear())
		self.btn_MC.grid(row=1,column=8)

		# row 2
		# sin function that returns value from -1 to 1 by default
		self.btn_sin = tk.Button(bottom_frame,padx=16,pady=1,bd=4,fg='white',bg = '#666666',font =('arial',18),width=2,height=2,
		text="sin",relief='flat',activebackground="#666666",command=lambda:btnClick('sin('))
		self.btn_sin.grid(row=2,column=0)
		# cos function that returns value from -1 to 1 by default
		self.btn_cos = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white',bg = '#666666', font=('arial', 18),width=2, height=2,
		text="cos",relief='flat',activebackground="#666666", command=lambda: btnClick('cos(' + self.convert_constant))
		self.btn_cos.grid(row=2, column=1)
		# tan function
		self.btn_tan = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white',bg = '#666666', font=('arial', 18), width=2,
		height=2,relief='flat',activebackground="#666666",text="tan", command=lambda: btnClick('tan(' + self.convert_constant))
		self.btn_tan.grid(row=2, column=2)
		#
		self.btn_log = tk.Button(bottom_frame,padx=16,pady=1,bd=4,fg='white',bg = '#666666',font =('arial',18),width=2,height=2,
		text="log",relief='flat',activebackground="#666666",command=lambda:btnClick('log('))
		self.btn_log.grid(row=2,column=3)
		# four
		self.btn4 = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white',bg = '#4d4d4d', font=('arial', 18), width=2, height=2,
		text="4",relief='flat',activebackground="#4d4d4d", command=lambda: btnClick(4))
		self.btn4.grid(row=2, column=4)
		# five
		self.btn5 = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white',bg = '#4d4d4d', font=('arial', 18), width=2, height=2,
		text="5",relief='flat',activebackground="#4d4d4d", command=lambda: btnClick(5))
		self.btn5.grid(row=2, column=5)
		# six
		self.btn6 = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white',bg = '#4d4d4d', font=('arial', 18), width=2, height=2,
		text="6",relief='flat',activebackground="#4d4d4d", command=lambda: btnClick(6))
		self.btn6.grid(row=2, column=6)
		# subtraction
		self.btnSub = tk.Button(bottom_frame,padx=16,pady=1,bd=4,fg='white',bg = '#666666',font =('arial',18),width=2,height=2,
		text="-",relief='flat',activebackground="#4d4d4d",command=lambda:btnClick('-'))
		self.btnSub.grid(row=2,column=7)
		# outputs what is in self.recall
		self.btn_MR = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white',bg = '#666666', font=('arial', 18), width=2, height=2,
		text="MR",relief='flat',activebackground="#666666", command=lambda: memory_recall())
		self.btn_MR.grid(row=2, column=8)
		
		# row 3
		# sin inverse function
		self.btn_sin_inverse = tk.Button(bottom_frame,padx=16,pady=1,bd=4,fg='white',bg = '#666666',font =('arial',18),width=2,height=2,
		text="sin^-1",relief='flat',activebackground="#666666",command=lambda:btnClick(self.inv_convert_constant + 'asin('))
		self.btn_sin_inverse.grid(row=3,column=0)
		# cos inverse function
		self.btn_cos_inverse = tk.Button(bottom_frame,padx=16,pady=1,bd=4,fg='white',bg = '#666666',font =('arial',18),width=2,height=2,
		text="cos^-1",relief='flat',activebackground="#666666",command=lambda:btnClick(self.inv_convert_constant + 'acos('))
		self.btn_cos_inverse.grid(row=3,column=1)
		# tan inverse function
		self.btn_tan_inverse = tk.Button(bottom_frame,padx=16,pady=1,bd=4,fg='white',bg = '#666666',font =('arial',18),width=2,height=2,
		text="tan^-1",relief='flat',activebackground="#666666",command=lambda:btnClick(self.inv_convert_constant + 'atan('))
		self.btn_tan_inverse.grid(row=3,column=2)
		# takes the natural log
		self.btn_ln = tk.Button(bottom_frame,padx=16,pady=1,bd=4,fg='white',bg = '#666666',font =('arial',18),width=2,height=2,
		text="ln",relief='flat',activebackground="#666666",command=lambda:btnClick('log1p('))
		self.btn_ln.grid(row=3,column=3)
		# one
		self.btn1 = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white',bg = '#4d4d4d', font=('arial', 18), width=2, height=2,
		text="1",relief='flat',activebackground="#4d4d4d", command=lambda: btnClick(1))
		self.btn1.grid(row=3, column=4)
		# two
		self.btn2 = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white',bg = '#4d4d4d', font=('arial', 18), width=2, height=2,
		text="2",relief='flat',activebackground="#4d4d4d", command=lambda: btnClick(2))
		self.btn2.grid(row=3, column=5)
		# three
		self.btn3 = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white',bg = '#4d4d4d', font=('arial', 18), width=2, height=2,
		text="3",relief='flat',activebackground="#4d4d4d", command=lambda: btnClick(3))
		self.btn3.grid(row=3, column=6)
		# addition
		self.btn_add = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white',bg = '#666666', font=('arial', 18), width=2, height=2,
		text="+",relief='flat',activebackground="#666666", command=lambda: btnClick('+'))
		self.btn_add.grid(row=3, column=7)
		# adds current self.expression to self.recall string
		self.btn_M_plus = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white',bg = '#666666', font=('arial', 18),width=2, height=2,
		text="M+",relief='flat',activebackground="#666666", command=lambda: memory_add())
		self.btn_M_plus.grid(row=3, column=8)
		
		# row 4
		# factorial function
		self.btn_fact = tk.Button(bottom_frame,padx=16,pady=1,bd=4,fg='white',bg = '#666666',font =('arial',18),width=2,height=2,
		text="n!",relief='flat',activebackground="#666666",command=lambda:btnClick('factorial('))
		self.btn_fact.grid(row=4,column=0)
		# square function
		self.btn_sqr = tk.Button(bottom_frame,padx=16,pady=1,bd=4,fg='white',bg = '#666666',font =('arial',18),width=2,height=2,
		text=u"x\u00B2",relief='flat',activebackground="#666666",command=lambda:btnClick('**2'))
		self.btn_sqr.grid(row=4,column=1)
		# to the power of function
		self.btn_power = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white',bg = '#666666', font=('arial', 18),width=2, height=2,
		text="x^y",relief='flat',activebackground="#666666", command=lambda: btnClick('**'))
		self.btn_power.grid(row=4, column=2)
		# stores previous expression as an answer value
		self.btn_ans = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white',bg = '#666666', font=('arial', 18), width=2, height=2,
		text="ans",relief='flat',activebackground="#666666",command=lambda:answer())
		self.btn_ans.grid(row=4, column=3)
		# zero
		self.btn_0 = tk.Button(bottom_frame, padx=16, pady=1, bd=5, fg='white',bg = '#4d4d4d', font=('arial', 18),width=7, height=2,
		text="0",relief='flat',activebackground="#4d4d4d", command=lambda: btnClick(0))
		self.btn_0.grid(row=4, column=4,columnspan=2)
		# equals button
		self.btn_eq = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white',bg = '#ff9980', font=('arial', 18), width=2, height=2,
		text="=",relief='flat',activebackground="#666666",command=lambda:btnEqual())
		self.btn_eq.grid(row=4, column=6)
		# decimal to convert to float
		self.btn_dec = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white',bg = '#666666', font=('arial', 18),width=2, height=2,
		text=".",relief='flat',activebackground="#666666", command=lambda: btnClick('.'))
		self.btn_dec.grid(row=4, column=7)
		# comma to allow for more than one parameter!
		self.btn_comma = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white',bg = '#666666', font=('arial', 18),width=2, height=2,
		text=",",relief='flat',activebackground="#666666", command=lambda: btnClick(','))
		self.btn_comma.grid(row=4, column=8)

		# functions
		# allows button you click to be put into self.expression
		def btnClick(expression_val):
			self.expression = self.expression + str(expression_val)
			text_Input.set(self.expression)
		# clears last item in string
		def btnClear1():
			self.expression = self.expression[:-1]
			text_Input.set(self.expression)
		# adds in a negative sign

		def sin(arg):
			import math
			return math.sin(self.convert_constant * arg)

		def change_signs():
			self.expression = self.expression + '-'
			text_Input.set(self.expression)
		# clears memory_recall
		def memory_clear():
			self.recall = ""
		# adds whatever is on the screen to self.recall
		def memory_add():
			self.recall = self.recall + '+' + self.expression
		# uses whatever is stored in memory_recall
		def answer():
			self.answer = self.sum_up
			text_Input.set(self.expression + self.answer)
		# uses whatever is stored in memory_recall
		def memory_recall():
			if self.expression == "":
				text_Input.set('0' + self.expression + self.recall)
			else:
				text_Input.set(self.expression + self.recall)
		# changes self.convert_constant to a string that allows degree conversion when button is clicked
		def convert_deg():
			self.convert_constant = pi/180
			self.btn_Rad["foreground"] = 'white'
			self.btn_Deg["foreground"] = 'orange'
		def convert_rad():
			self.btn_Rad["foreground"] = 'orange'
			self.btn_Deg["foreground"] = 'white'
		# clears self.expression
		def btnClearAll():
			self.expression = ""
			text_Input.set("")
		# converts self.expression into a mathematical expression and evaluates it
		def btnEqual():
			self.sum_up = str(eval(self.expression))
			text_Input.set(self.sum_up)
			self.expression = ""

# tkinter layout
root = tk.Tk()
b = Calculator(root)
root.title("Simple Scientific Calculator")
root.geometry("650x490+50+50")
root.resizable(False,False)
root.mainloop()


