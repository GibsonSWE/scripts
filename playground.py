from tkinter import *
from tkinter import filedialog

#Creating an instance of tkinter frame
win = Tk()
win.geometry("750x250")

directory_path = ""

def open_directory():
    directory_path = filedialog.askdirectory()
    directory_entry.delete(0, END)    

    directory_entry.insert(END, directory_path+'/'+backup_name.get())
    return

# Defining String Object and setting the default value
var = StringVar()
#var = ""


# Directory label, entry, and browse button
directory_text = Label(text="Directory:")
directory_text.pack()

directory_entry = Entry(width=60, textvariable = directory_path+str(var))
directory_entry.pack()

browse_button = Button(text="...", command=open_directory)
browse_button.pack()



label = Label(win, text="Backup name:")
label.pack()

#Entry widget to change the variable value
backup_name = Entry(win, textvariable=var)
backup_name.pack()
win.mainloop()