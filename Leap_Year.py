from tkinter import *
  
root = Tk() 
  
root.title("Leap Year Calculation") 
root.geometry('250x200') 
  
name = Label(root, text = "Enter Any Year ") 
name.grid(column = 0,row =0) 

year = Entry(root, width=15) 
year.grid(column = 1,row =0) 
  
result = Label(root) 
result.grid(column = 1,row =2) 
  
  
def clicked(): 
    res = int(year.get())
    found = ""
    if res % 4 == 0:
       if res % 100 == 0:
           if res % 400 == 0:
               found = "leap year"
           else:
               found = "not leap year"
       else:
           found = "leap year"
    else:
       found = "not leap year"
       
    result.configure(text = found)
  

btn = Button(root, text = "Show" , fg = "blue", command=clicked) 
  
btn.grid(column=0, row=2) 
  
root.mainloop()
