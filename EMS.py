from tkinter import *
from tkinter.messagebox import*
from tkinter.scrolledtext import*
from sqlite3 import*
from requests import*
from PIL import ImageTk,Image


def mw2aw():
    mw.withdraw()
    aw.deiconify()

def mw2vw():
	mw.withdraw()
	vw.deiconify()
	vw_st_data.delete(1.0,END)
	con=None
	try:
		con=connect("employee.db")
		cursor=con.cursor()
		sql="select * from employee order by id"
		cursor.execute(sql)
		data=cursor.fetchall()
		info=""
		for d in data:
			info=info+"id = "+str(d[0])+"\n"+"name = "+str(d[1])+"\n"+"salary = "+str(d[2])+"\n""--------------------------------""\n"
		vw_st_data.insert(INSERT,info)
	except Exception as e:
		showerror("issue",e)
	finally:
		if con is not None:
			con.close()

def mw2dw():
    mw.withdraw()
    dw.deiconify()

def mw2uw():
    mw.withdraw()
    uw.deiconify()
    
def mw2cw():
	mw.withdraw()
	cw.deiconify()
	con=None
	try:
		con=connect("employee.db")
		cursor=con.cursor()
		sql="select * from employee order by salary desc limit 5;"
		cursor.execute(sql)
		data=cursor.fetchall()
		info=""
		for d in data:
			info=info+"id = "+str(d[0])+"\n"""+"name = "+str(d[1])+"\n"+"salary = "+str(d[2])+"\n""--------------------------------""\n"
		cw_st_data.insert(INSERT,info)
	except Exception as e:
		showerror("issue",e)
	finally:
		if con is not None:
			con.close()


def aw2mw():
    aw.withdraw()
    mw.deiconify()

def vw2mw():
    vw.withdraw()
    mw.deiconify()

def dw2mw():
    dw.withdraw()
    mw.deiconify()

def uw2mw():
    uw.withdraw()
    mw.deiconify() 
    
def cw2mw():
    cw.withdraw()
    mw.deiconify()

def add():
	con=	None
	try:
		con=connect("employee.db")
		cursor=con.cursor()
		sql="insert into employee values('%s','%s','%f')"
		try:
			id=int(aw_ent_id.get())
			if id<1:
				showerror("Failed","ID should be Valid" )
				return
				
		except ValueError:
			showerror("issue","ID should be integer only")
			return
		name=aw_ent_name.get()
		if not name.isalpha():
			showerror("issue","Invalid Name")
			return
		if len(name)<2:
			showerror("issue","Invalid Name")
			return
		try:
			sal=float(aw_ent_sal.get())
			if sal<1:
				showerror("Failed","Salary should be Valid" )
				return

		except ValueError:
			showerror("issue","Salary should be Valid")
			return
		cursor.execute(sql%(id,name,sal))
		con.commit()
		showinfo("Success","Employee record added")
	except Exception as e:
		con.rollback()
		showerror("Issue ",e)
	finally:
		if con is not None:
			con.close()
			aw_ent_id.delete(0,END)
			aw_ent_name.delete(0,END)
			aw_ent_sal.delete(0,END)	
			aw_ent_id.focus() 	

def search():
	con=None
	try:
		vw_st_data.delete(1.0,END)
		con=connect("employee.db")
		cursor=con.cursor()
		if vw_ent_search.get()=="":
			vw_st_data.delete(1.0,END)
			sql="select * from employee order by id"
			cursor.execute(sql)
			data=cursor.fetchall()
			info=""
			for d in data:
				info="id = "+str(d[0])+"\n"+"name = "+str(d[1])+"\n"+"salary = "+str(d[2])+"\n""--------------------------------""\n"
				vw_st_data.insert(INSERT,info)
		else:
			sql="select * from employee where id like '"+str(vw_ent_search.get())+"'"+"or name like'"+str(vw_ent_search.get())+"%'"+"or salary like'"+str(vw_ent_search.get())+"'"
			cursor.execute(sql)
			data=cursor.fetchall()
			for d in data:
				info="\n""id = "+str(d[0])+"\n"""+"name = "+str(d[1])+"\n"+"salary = "+str(d[2])+"\n""--------------------------------""\n"
				vw_st_data.insert(INSERT,info)

				
	except Exception as e:
		showerror("issue",e)
	finally:
		if con is not None:
			con.close()
			
def delete():
	con=None
	try:
		con=connect("employee.db")
		cursor=con.cursor()
		sql="delete from employee where id='%s'"
		id=dw_ent_id.get()
		cursor.execute(sql%(id))
		if cursor.rowcount==1:
			con.commit()
			showinfo("Success","Employee record deleted")
		else:
			showinfo("Failed","Record does not exist")
	except Exception as e:
		showerror("issue",e)
	finally:
		if con is not None:
			con.close()
			dw_ent_id.delete(0,END)
			dw_ent_id.focus()
			
			
def update():
	con=None
	try:
		con=connect("employee.db")
		cursor=con.cursor()
		sql="update employee set name='%s',salary='%f' where id='%s'"
		id=uw_ent_id.get()
		name=uw_ent_name.get()
		if not name.isalpha():
			showerror("issue","Invalid Name")
			return
		if len(name)<2:
			showerror("issue","Invalid Name")
			return
		try:
			sal=float(uw_ent_sal.get())
		except ValueError:
			showerror("issue","Salary should be valid")
			return
		
		cursor.execute(sql%(name,sal,id))
		if cursor.rowcount==1:
			con.commit()
			showinfo("Success","Employee record updated")
		else:
			showerror("Failed","Record does not exist")
	except Exception as e:
		showerror("issue",e)
	finally:
		if con is not None:
			con.close()
			uw_ent_id.delete(0,END)
			uw_ent_name.delete(0,END)
			uw_ent_sal.delete(0,END)	
			uw_ent_id.focus()

def temper():
	try:
		wa="https://ipinfo.io/"
		res=get(wa)
		data=res.json()
		city=data["city"]
		a1="https://api.openweathermap.org/data/2.5/weather"
		a2="?q="+city
		a3="&appid="+"c6e315d09197cec231495138183954bd"
		a4="&units="+"metric"
		wa=a1+a2+a3+a4
		res=get(wa)
		data=res.json()
		temp=data["main"]["temp"]
		ans_live.configure(text="Location = "+str(city)+"        "+"Temp = "+str(temp)+"°C")

	except Exception as e:
		showinfo("issue ",e)
		
		


# Main Window
mw=Tk()
mw.title("Employee Management System")
mw.geometry("600x700+500+50")
mw.configure(bg="deep sky blue")
f=("Arial",30,"bold")



#bgfile=Image.open("bg1.jpg")
#resized=bgfile.resize((800,700),Image.ANTIALIAS)
#newbg=ImageTk.PhotoImage(resized)
#img=ImageTk.PhotoImage(Image.open("bg1.jpg"))
#bg=Label(mw,image=newbg)

#bg.place(x=0,y=0)

add_btn=Button(mw,text="ADD",font=f,bg="peachpuff2",command=mw2aw)
view_btn=Button(mw,text="VIEW",font=f,bg="peachpuff2",command=mw2vw)
delete_btn=Button(mw,text="DELETE",font=f,bg="peachpuff2",command=mw2dw)
update_btn=Button(mw,text="UPDATE",font=f,bg="peachpuff2",command=mw2uw)
charts_btn=Button(mw,text="CHARTS",font=f,bg="peachpuff2",command=mw2cw)
ans_live=Label(mw,font=("Arial",20,"bold"),fg="green",bg="white")


add_btn.pack(pady=20)
view_btn.pack(pady=20)
delete_btn.pack(pady=20)
update_btn.pack(pady=20)
charts_btn.pack(pady=20)
ans_live.pack(pady=33)
ans_live.configure(text=temper())


# Add Window
aw=Toplevel(mw)
aw.title("Add Employee")
aw.geometry("700x600+500+50")
aw.configure(bg="deep sky blue")




aw_lab_id=Label(aw,text="Enter Employee ID:",font=f,bg="deep sky blue")
aw_ent_id=Entry(aw,font=f,bg="light grey")
aw_lab_name=Label(aw,text="Enter Employee Name:",font=f,bg="deep sky blue")
aw_ent_name=Entry(aw,font=f,bg="light grey")
aw_lab_sal=Label(aw,text="Enter Employee Salary:",font=f,bg="deep sky blue")
aw_ent_sal=Entry(aw,font=f,bg="light grey")
aw_lab_id.pack(pady=10)
aw_ent_id.pack(pady=10)
aw_lab_name.pack(pady=10)
aw_ent_name.pack(pady=10)
aw_lab_sal.pack(pady=10)
aw_ent_sal.pack(pady=10)
aw_btn_save=Button(aw,text="Save",font=f,bg="peachpuff2",command=add)
aw_btn_back=Button(aw,text="Back",font=f,bg="peachpuff2",command=aw2mw)
aw_btn_save.pack(pady=10)
aw_btn_back.pack(pady=10)
aw.withdraw()


# View Window
vw=Toplevel()
vw.title("View Employee")
vw.geometry("700x800+500+50")
vw.configure(bg="deep sky blue")



f=("Arial",30,"bold")

vw_lab_search=Label(vw,text="Search",font=f,bg="white")
vw_ent_search=Entry(vw,font=f,bg="light grey")
vw_btn_search=Button(vw,text="=>",font=f,bg="peachpuff2",command=search)
vw_st_data=ScrolledText(vw,font=f,bg="light grey",width=30,height=10)
vw_btn_back=Button(vw,text="Back",font=f,bg="peachpuff2",command=vw2mw)
vw_lab_search.pack(pady=10)
vw_ent_search.pack(pady=10)
vw_btn_search.pack(pady=10)
vw_st_data.pack(pady=10)
vw_btn_back.pack(pady=10)
vw.withdraw()


# Delete Window
dw=Toplevel()
dw.title("Delete Employee")
dw.geometry("700x600+500+50")
dw.configure(bg="deep sky blue")



dw_lab_id=Label(dw,text="Enter Employee ID:",font=f,bg="deep sky blue")
dw_ent_id=Entry(dw,font=f,bg="light grey")
dw_btn_delete=Button(dw,text="DELETE",font=f,bg="peachpuff2",command=delete)
dw_btn_back=Button(dw,text="Back",font=f,bg="peachpuff2",command=dw2mw)

dw_lab_id.pack(pady=15)
dw_ent_id.pack(pady=15)
dw_btn_delete.pack(pady=15)
dw_btn_back.pack(pady=15)
dw.withdraw()


# Update Window
uw=Toplevel()
uw.title("Update Employee")
uw.geometry("700x600+500+50")
uw.configure(bg="deep sky blue")


uw_lab_id=Label(uw,text="Enter Employee ID:",font=f,bg="deep sky blue")
uw_ent_id=Entry(uw,font=f,bg="light grey")
uw_lab_name=Label(uw,text="Enter Employee Name:",font=f,bg="deep sky blue")
uw_ent_name=Entry(uw,font=f,bg="light grey")
uw_lab_sal=Label(uw,text="Enter Employee Salary:",font=f,bg="deep sky blue")
uw_ent_sal=Entry(uw,font=f,bg="light grey")
uw_lab_id.pack(pady=10)
uw_ent_id.pack(pady=10)
uw_lab_name.pack(pady=10)
uw_ent_name.pack(pady=10)
uw_lab_sal.pack(pady=10)
uw_ent_sal.pack(pady=10)
uw_btn_save=Button(uw,text="Save",font=f,bg="peachpuff2",command=update)
uw_btn_back=Button(uw,text="Back",font=f,bg="peachpuff2",command=uw2mw)
uw_btn_save.pack(pady=10)
uw_btn_back.pack(pady=10)
uw.withdraw()


# Chart Window
cw=Toplevel()
cw.title("Top Employees")
cw.geometry("700x700+500+50")
cw.configure(bg="deep sky blue")



cw_lab_top=Label(cw,text="Top 5 Highest Paid Employees",font=f,bg="deep sky blue")
cw_st_data=ScrolledText(cw,font=f,bg="light grey",width=30,height=10)
cw_btn_back=Button(cw,text="Back",font=f,bg="peachpuff2",command=cw2mw)
cw_lab_top.pack(pady=10)
cw_st_data.pack(pady=10)
cw_btn_back.pack(pady=10)
cw.withdraw()




mw.mainloop()

