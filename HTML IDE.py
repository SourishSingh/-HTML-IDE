from tkinter import *
from tkinter import filedialog
root=Tk()
root.geometry("800x600")

txt=Text(root,height=15,width=50,font=("Comic Sans MS",16))
txt.pack()

def clear():
    txt.delete(1.0,END)

def open_txt():
    txt=filedialog.askdirectory(title="Open Text File",filetypes=(("Text Files","*.txt"),))
    txt=open(txt,'r')
    h=text_file.read
    
    txt.insert(END,h)
    txt.close()

def close():
    root.destroy()

clear_btn=Button(root,text="clear",command=clear,font=("Roman",17))
clear_btn.place(relx=0.3,rely=0.75)

open_btn=Button(root,text="open",command=open_txt,font=("Roman",17))
open_btn.place(relx=0.5,rely=0.75)

close_btn=Button(root,text="Close",command=close,font=("Roman",17))
close_btn.place(relx=0.7,rely=0.75)

root.mainloop()
