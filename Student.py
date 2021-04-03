from tkinter import*
from tkinter import ttk
import pymysql
from tkinter import messagebox
class Student:
	def __init__(self,root):
		self.root=root
		self.root.title("Student Management System")
		self.root.geometry("1350x700+0+0")

		title=Label(self.root, text="Student Management System",bd=10, relief=GROOVE, font=("times new roman",40, "bold"), bg="yellow", fg="red")
		title.pack(side=TOP, fill=X)
#All variables for database===
		self.Reg_No_var=StringVar()
		self.Name_var=StringVar()
		self.Email_var=StringVar()
		self.Gender_var=StringVar()
		self.Contact_var=StringVar()
		self.Department_var=StringVar()

		self.search_by=StringVar()
		self.search_txt=StringVar()
	


#manage frame=============
		Manage_Frame=Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
		Manage_Frame.place(x=20, y=100, width=450, height=580)

		m_title=Label(Manage_Frame, text="Manage Students", bg="crimson", fg="white", font=("times new roman",30, "bold"))
		m_title.grid(row=0, columnspan=2, pady=10)

		lbl_reg=Label(Manage_Frame, text="Reg No. ", bg="crimson", fg="white", font=("times new roman",20, "bold"))
		lbl_reg.grid(row=1, column=0, pady=10, padx=20, sticky="w")
#for reg no entry======
		txt_reg=Entry(Manage_Frame, textvariable=self.Reg_No_var, font=("times new roman",15, "bold"), bd=5, relief=GROOVE)
		txt_reg.grid(row=1, column=1, pady=10, padx=20, sticky="w")
#name entry======
		lbl_name=Label(Manage_Frame, text="Name", bg="crimson", fg="white", font=("times new roman",20, "bold"))
		lbl_name.grid(row=2, column=0, pady=10, padx=20, sticky="w")

		txt_name=Entry(Manage_Frame, textvariable=self.Name_var, font=("times new roman",15, "bold"), bd=5, relief=GROOVE)
		txt_name.grid(row=2, column=1, pady=10, padx=20, sticky="w")
#Email entry=====
		lbl_Email=Label(Manage_Frame, text="Email", bg="crimson", fg="white", font=("times new roman",20, "bold"))
		lbl_Email.grid(row=3, column=0, pady=10, padx=20, sticky="w")

		txt_Email=Entry(Manage_Frame, textvariable=self.Email_var, font=("times new roman",15, "bold"), bd=5, relief=GROOVE)
		txt_Email.grid(row=3, column=1, pady=10, padx=20, sticky="w")
#Gender entry=======
		lbl_Gender=Label(Manage_Frame, text="Gender", bg="crimson", fg="white", font=("times new roman",20, "bold"))
		lbl_Gender.grid(row=4, column=0, pady=10, padx=20, sticky="w")

		combo_gender=ttk.Combobox(Manage_Frame, textvariable=self.Gender_var, font=("times new roman",13, "bold"), state='readonly')
		combo_gender['values']=("Male", "Female", "Other")
		combo_gender.grid(row=4, column=1, padx=20, pady=10)
#contact entry====
		lbl_contact=Label(Manage_Frame, text="Contact", bg="crimson", fg="white", font=("times new roman",20, "bold"))
		lbl_contact.grid(row=5, column=0, pady=10, padx=20, sticky="w")

		txt_contact=Entry(Manage_Frame, textvariable= self.Contact_var, font=("times new roman",15, "bold"), bd=5, relief=GROOVE)
		txt_contact.grid(row=5, column=1, pady=10, padx=20, sticky="w")
#department entry
		lbl_dept=Label(Manage_Frame, text="Department", bg="crimson", fg="white", font=("times new roman",20, "bold"))
		lbl_dept.grid(row=6, column=0, pady=10, padx=20, sticky="w")

		combo_dept=ttk.Combobox(Manage_Frame, textvariable=self.Department_var, font=("times new roman",13, "bold"), state='readonly')
		combo_dept['values']=("MCA I", "MCA II", "MCA III", "MCA IV", "MCA V", "MCA VI", "MSC I", "MSC II", "MSC III", "MSC IV")
		combo_dept.grid(row=6, column=1, padx=20, pady=10)

		
#address entry
		lbl_address=Label(Manage_Frame, text="Address", bg="crimson", fg="white", font=("times new roman",20, "bold"))
		lbl_address.grid(row=7, column=0, pady=10, padx=20, sticky="w")

		self.txt_address=Text(Manage_Frame, width=30, height=4, font=("", 10))
		self.txt_address.grid(row=7, column=1, pady=10, padx=20, sticky="w")

#button frame========
		btn_Frame=Frame(Manage_Frame, bd=4, relief=RIDGE, bg="crimson")
		btn_Frame.place(x=15, y=500, width=420)

		Addbtn=Button(btn_Frame, text="Add", width=10, command=self.add_students).grid(row=0, column=0,padx=10, pady=10)
		updatebtn=Button(btn_Frame, text="Update", width=10, command=self.update_data).grid(row=0, column=1,padx=10, pady=10)
		deletebtn=Button(btn_Frame, text="Delete", width=10, command=self.delete_data).grid(row=0, column=2,padx=10, pady=10)
		clearbtn=Button(btn_Frame, text="Clear", width=10, command=self.clear).grid(row=0, column=3,padx=10, pady=10)

        
#Detail frame========
		Detail_Frame=Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
		Detail_Frame.place(x=500, y=100, width=800, height=580)

		lbl_search=Label(Detail_Frame, text="Search By", bg="crimson", fg="white", font=("times new roman",20, "bold"))
		lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")

		combo_search=ttk.Combobox(Detail_Frame, textvariable=self.search_by, width=10, font=("times new roman",13, "bold"), state='readonly')
		combo_search['values']=("Reg_No", "Name", "Contact")
		combo_search.grid(row=0, column=1, padx=20, pady=10)

		txt_search=Entry(Detail_Frame, textvariable=self.search_txt, width=20, font=("times new roman",10, "bold"), bd=5, relief=GROOVE)
		txt_search.grid(row=0, column=2, pady=10, padx=20, sticky="w")

		searchbtn=Button(Detail_Frame, text="Search", width=10, pady=5, command=self.search_data).grid(row=0, column=3,padx=10, pady=10)
		showallbtn=Button(Detail_Frame, text="Show All", width=10, pady=5, command=self.fetch_data).grid(row=0, column=4,padx=10, pady=10)

#table frame======>>>
		Table_Frame=Frame(Detail_Frame, bd=4, relief=RIDGE, bg="crimson")
		Table_Frame.place(x=10, y=70, width=760, height=500)

		scroll_x=Scrollbar(Table_Frame, orient=HORIZONTAL)
		scroll_y=Scrollbar(Table_Frame, orient=VERTICAL)

		self.Student_table=ttk.Treeview(Table_Frame, columns=("Reg No", "Name", "Email", "Gender", "Contact", "Department", "Address"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
		scroll_x.pack(side=BOTTOM, fill=X)
		scroll_y.pack(side=RIGHT, fill=Y)
		scroll_x.config(command=self.Student_table.xview)
		scroll_y.config(command=self.Student_table.yview)

		self.Student_table.heading("Reg No", text="Register No")
		self.Student_table.heading("Name", text="Name")
		self.Student_table.heading("Email", text="Email")
		self.Student_table.heading("Gender", text="Gender")
		self.Student_table.heading("Contact", text="Contact")
		self.Student_table.heading("Department", text="Department")
		self.Student_table.heading("Address", text="Address")
		self.Student_table['show']='headings'
#for styling column names in table frame=====		
		self.Student_table.column("Reg No", width=100)
		self.Student_table.column("Name", width=100)
		self.Student_table.column("Email", width=100)
		self.Student_table.column("Gender", width=100)
		self.Student_table.column("Contact", width=100)
		self.Student_table.column("Department", width=100)
		self.Student_table.column("Address", width=150)

		self.Student_table.pack(fill=BOTH, expand=1)
		self.Student_table.bind("<ButtonRelease-1>", self.get_cursor)
		self.fetch_data()
#for database connection====
	def add_students(self):

		if self.Reg_No_var.get()=="" or self.Name_var.get()=="" or self.Email_var.get()=="" or self.Gender_var.get()=="" or self.Contact_var.get()=="" or self.Department_var.get()=="":
			messagebox.showerror("Error", "All fields are required!!")
		else:	
			con=pymysql.connect(host="localhost", user="root", password="",database="stm")
			cur=con.cursor()
			cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)",( self.Reg_No_var.get(),
			                                                                  self.Name_var.get(),
			                                                                  self.Email_var.get(),
			                                                                  self.Gender_var.get(),
			                                                                  self.Contact_var.get(),
			                                                                  self.Department_var.get(),
			                                                                  self.txt_address.get('1.0',END)



				                                                             ))
			con.commit()
			self.fetch_data()
			self.clear()
			con.close()
			messagebox.showinfo("Success","Record has been inserted")
#for showing data in display table====		
	def fetch_data(self):
		con=pymysql.connect(host="localhost", user="root", password="",database="stm")
		cur=con.cursor()
		cur.execute("select * from students")
		rows=cur.fetchall()
		if len(rows)!=0:
			self.Student_table.delete(*self.Student_table.get_children())
			for row in rows:
				self.Student_table.insert('',END, values=row)
			con.commit()	
		con.close()
	def clear(self):
		self.Reg_No_var.set("")
		self.Name_var.set("")
		self.Email_var.set("")
		self.Gender_var.set("")
		self.Contact_var.set("")
		self.Department_var.set("")
		self.txt_address.delete('1.0',END)

#for fetching data from student table when click on the name	
	def get_cursor(self, ev):
		cursor_row=self.Student_table.focus()
		contents=self.Student_table.item(cursor_row)
		row=contents['values']

		self.Reg_No_var.set(row[0])
		self.Name_var.set(row[1])
		self.Email_var.set(row[2])
		self.Gender_var.set(row[3])
		self.Contact_var.set(row[4])
		self.Department_var.set(row[5])
		self.txt_address.delete('1.0',END)
		self.txt_address.insert(END, row[6])

#for update button
	def update_data(self):
		con=pymysql.connect(host="localhost", user="root", password="",database="stm")
		cur=con.cursor()
		cur.execute("update students set Name=%s,Email=%s,Gender=%s,Contact=%s,Department=%s,Address=%s where Reg_No=%s",( 
		                                                                  self.Name_var.get(),
		                                                                  self.Email_var.get(),
		                                                                  self.Gender_var.get(),
		                                                                  self.Contact_var.get(),
		                                                                  self.Department_var.get(),
		                                                                  self.txt_address.get('1.0',END),
		                                                                  self.Reg_No_var.get()



			                                                             ))
		con.commit()
		self.fetch_data()
		self.clear()
		con.close()

#Delete button function===
	def delete_data(self):
		con=pymysql.connect(host="localhost", user="root", password="",database="stm")
		cur=con.cursor()
		cur.execute("delete from students where Reg_No=%s", self.Reg_No_var.get())
		con.commit()
		con.close()
		self.fetch_data()
		self.clear()

#search button function===
	def search_data(self):
		con=pymysql.connect(host="localhost", user="root", password="",database="stm")
		cur=con.cursor()
		cur.execute("select * from students where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
		rows=cur.fetchall()
		if len(rows)!=0:
			self.Student_table.delete(*self.Student_table.get_children())
			for row in rows:
				self.Student_table.insert('',END, values=row)
			con.commit()	
		con.close()	



		




root=Tk()
ob=Student(root)		
root.mainloop()