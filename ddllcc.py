from tkinter import *
from tkinter import Menu

def b():
    Label(text='nigger').pack()

win = Tk()

#########
win.title('tool đánh giá cd')
win.geometry('600x600')
win.attributes('-topmost', True)


#menu

win.grid_rowconfigure(2, weight=3) 

menubar = Menu(win)
win.config(menu= menubar)
file_menu = Menu(menubar,tearoff= False)
menubar.add_cascade(label= 'NIGA',menu=file_menu)
file_menu.add_command(label= "niggas",command= b)

opt_frame  = Frame(win, bg='#778899', height= 50)
opt_frame.pack(fill=X, expand=False)

mainframe = Frame(win, bg="lightblue",
                  highlightthickness=2,
                  highlightbackground='#9FB6CD')
mainframe.pack(fill=BOTH, expand=True)

thay_ma_btn  = Button(opt_frame,text='ĐỔI MÃ',fg='#2F4F4F')
thay_ma_btn.grid(row=0,column=0, sticky="nsew",)
thay_ma_btn  = Button(opt_frame,text='LÀM KIỂM TRA',fg='#2F4F4F')
thay_ma_btn.grid(row=0,column=1, sticky="nsew")
thay_ma_btn  = Button(opt_frame,text='ĐĂNG KÝ',fg='#2F4F4F')
thay_ma_btn.grid(row=0,column=2, sticky="nsew")
##########
win.mainloop()

