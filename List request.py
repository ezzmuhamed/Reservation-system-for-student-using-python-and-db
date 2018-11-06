from tkinter import *
from tkinter import ttk
from DbConnect import DBConnect

dbConnect = DBConnect()
class ListTicket:
    
    def __init__(self):
        self._root = Tk()
        #butDelete = ttk.Button(self._root,text = "Delete")
        #butDelete.pack()
        #butDelete.grid(row=0,column = 0 )

        #butUpdate = ttk.Button(self._root,text = "Update")
        #butUpdate.pack()
        #butUpdate.grid(row=1,column = 0 )

        self._dbconnect = DBConnect()
        tv = ttk.Treeview(self._root)
        tv.pack()
        tv.heading('#0',text = 'ID')
        tv.configure(column =('#Name','#Gender','#Comment'))
        tv.heading('#Name',text = 'IName')
        tv.heading('#Gender',text = 'Gender')
        tv.heading('#Comment',text = 'Comment')
        cursor = self._dbconnect.ListRequest()
        for row in cursor:
            tv.insert('','end','#{}'.format(row['ID']),text = row['ID'] )
            tv.set('#{}'.format(row['ID']),'#Name',row['Name'])
            tv.set('#{}'.format(row['ID']),'#Gender',row['Gender'])
            tv.set('#{}'.format(row['ID']),'#Comment',row['Comment'])
