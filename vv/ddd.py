from tkinter import *
from openpyxl import Workbook, load_workbook
rt = Tk()



    

rt.title("con cac")
rt.minsize(width= 500, height= 500)

Label(rt,text="TOOL ĐÁNH GIÁ CÔNG DÂN",font="arial 20 bold",width=40).grid(row=0,columnspan=2)

lb = Label(rt,text='ĐƯỜNG DẪN CHROME')
lb.grid(row=1,column=0, sticky='w')
entry1 = Entry(rt,bd=3,width=30)
entry1.grid(row=1,column=1, sticky='w')

lb = Label(rt,text='TÊN FILE EXCEL')
lb.grid(row=2,column=0, sticky='w')
entry2 = Entry(rt,bd=3,width=30)
entry2.grid(row=2,column=1, sticky='w')

lb = Label(rt,text='ĐIỀN SHEET')
lb.grid(row=3,column=0, sticky='w')
entry3 = Entry(rt,bd=3,width=30)
entry3.grid(row=3,column=1, sticky='w')

lb = Label(rt,text='ĐIỀN CỘT')
lb.grid(row=4,column=0, sticky='w')
entry4 = Entry(rt,bd=3,width=30)
entry4.grid(row=4,column=1, sticky='w')


bt = Button(rt,text="THAY ĐỔI MÃ",width=40)
bt.grid(row=5,columnspan=2)
bt = Button(rt,text="VÀO LÀM BÀI KIỂM TRA",width=40)
bt.grid(row=6,columnspan=2)
bt = Button(rt,text="ĐĂNG KÍ TÀI KHOẢN",width=40)
bt.grid(row=7,columnspan=2)


rt.mainloop()