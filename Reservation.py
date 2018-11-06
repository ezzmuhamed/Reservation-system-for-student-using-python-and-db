
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from DbConnect import DBConnect
from ListRequest import ListTicket

#object from my class
DbConnect = DBConnect()
root = Tk()
root.title("ticket reservation")
root.configure(background = '#e1d8b2')
#style
style = ttk.Style()
style.theme_use('classic')
style.configure('TLabel',background = '#e1d8b2')
style.configure('TButton',background = '#e1d8b2')
style.configure('TRadiobutton',background = '#e1d8b2')

#fullname
ttk.Label(root,text = "Full Name:").grid(row=0,column = 0 ,padx =10 ,pady=10)
EntryFullName = ttk.Entry(root,width = 30,font=('Arial',16))
EntryFullName.grid(row=0,column = 1,columnspan = 2 ,pady=10)

#gender
ttk.Label(root,text = "GENDER:").grid(row =1,column = 0)
SpanGender = StringVar()
ttk.Radiobutton(root,text = "Male",variable = SpanGender,value ="Male").grid(row=1,column = 1)
ttk.Radiobutton(root,text = "Female",variable = SpanGender,value ="Female").grid(row=1,column = 2)

#comments
ttk.Label(root,text = "Comments:").grid(row =2,column = 0)
TextComments = Text(root,width = 30,height = 15 , font=('Arial',16))
TextComments.grid(row=2,column = 1,columnspan = 2 )

#buttons
buSUMMBIT = ttk.Button(root,text = "Submit")
buSUMMBIT.grid(row=3,column = 3 )

buLIST = ttk.Button(root,text = "ReadList")
buLIST.grid(row=3,column = 2 )



def SaveButtonData():
   # print('FullName:{}'.format(EntryFullName.get()))
   # print('GENDER:{}'.format(SpanGender.get()))
   # print('COMMENTS:{}'.format(TextComments.get(1.0,'end')))
    msg =DbConnect.Add(EntryFullName.get(),SpanGender.get(),TextComments.get(1.0,'end'))
    messagebox.showinfo(title = 'Add info',message = msg)
    EntryFullName.delete(0,'end')
    TextComments.delete(1.0,'end')

def buListData():
    #print('not!')
    listrequest = ListTicket()
