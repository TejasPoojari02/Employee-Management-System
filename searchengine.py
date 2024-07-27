from tkinter import*
from tkinter.messagebox import*
from tkinter.scrolledtext import*
from sqlite3 import*



def mw2vw():
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
			info=info+"id = "+str(d[0])+"\n"""+"name = "+str(d[1])+"\n"+"salary = "+str(d[2])+"\n""--------------------------------""\n"
		vw_st_data.insert(INSERT,info)
	except Exception as e:
		showerror("issue",e)
	finally:
		if con is not None:
			con.close()
			
def search():
	con=None
	try:
		vw_st_data.delete(1.0,END)
		con=connect("employee.db")
		cursor=con.cursor()
		sql="select * from employee where id = '"+str(vw_ent_search.get())+"'"+"or name ='"+str(vw_ent_search.get())+"'"+"or salary ='"+str(vw_ent_search.get())+"'"
		cursor.execute(sql)
		data=cursor.fetchall()
		info=""
		for d in data:
			info=info+"id = "+str(d[0])+"\n"""+"name = "+str(d[1])+"\n"+"salary = "+str(d[2])+"\n""--------------------------------""\n"
		vw_st_data.insert(INSERT,info)
	except Exception as e:
		showerror("issue",e)
	finally:
		if con is not None:
			con.close()
	


vw=Tk()
vw.title("View Employee")
vw.geometry("700x800+500+50")

f=("Arial",30,"bold")

vw_lab_search=Label(vw,text="search",font=f)
vw_ent_search=Entry(vw,font=f)
vw_btn_search=Button(vw,text="->",font=f,command=search)
vw_st_data=ScrolledText(vw,font=f,width=30,height=10)
vw_btn_back=Button(vw,text="Back",font=f,command=mw2vw)
vw_lab_search.pack(pady=10)
vw_ent_search.pack(pady=10)
vw_btn_search.pack(pady=10)
vw_st_data.pack(pady=10)
vw_btn_back.pack(pady=10)

vw.mainloop()


"select * from employee where id like '"+str(vw_ent_search.get())+"'"+"or name like'"+str(vw_ent_search.get())+"%'"+"or salary like'"+str(vw_ent_search.get())+"'"