# World of Warcraft Backup Script by GibsonSWE
from tkinter import *
from tkinter import filedialog, messagebox
import shutil
from datetime import date


# VARIABLES

todays_date = date.today().strftime('%Y%m%d')
directory_path = ''
wtf_src_path = ''
addons_src_path = ''
wtf_backup_path = ''
addons_backup_path = ''
naming_option_var = True
window = Tk()
INVALID_CHARACTERS = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']


# FUNCTIONS

def check_invalid_char():
    for i in backup_name_input.get():
        for c in INVALID_CHARACTERS:
            if i == c:
                print('Invalid backup name.')
                print('Found character: '+c)
                status.config(text="Invalid character: "+c)
                return True

def open_wow_directory():
    file_path = filedialog.askdirectory()
    wow_directory_input.delete(0, END)
    wow_directory_input.insert(END, string=file_path)
    return

def open_backup_directory():
    global directory_path
    directory_path = filedialog.askdirectory()
    backup_directory_input.delete(0, END)    

    if naming_option_int.get() == 1:
        backup_directory_input.insert(END, directory_path+'/'+todays_date)
    elif naming_option_int.get() == 2:
        if check_invalid_char() == True:
            backup_directory_input.insert(END, directory_path+'/')
            return
        else:
            backup_directory_input.insert(END, directory_path+'/'+backup_name_input.get())
            return

def naming_option_date():
#    backup_name_input.delete(0, END)
    global naming_option_var
    naming_option_var = True
    backup_name_input.config(state=DISABLED)
    backup_directory_input.delete(0, END)
    backup_directory_input.insert(END, directory_path+'/'+todays_date)
    return

def naming_option_custom():
    global naming_option_var
    naming_option_var = False
    backup_name_input.config(state=NORMAL)
    backup_directory_input.delete(0, END)
    backup_name_input.focus()
    if check_invalid_char() == True:
        backup_directory_input.insert(END, directory_path+'/')
        return
    else:
        backup_directory_input.insert(END, directory_path+'/'+backup_name_input.get())
        return

def apply_custom_name():
    if check_invalid_char() == True:
        return
    else:
        backup_directory_input.delete(0, END)
        backup_directory_input.insert(END, directory_path+'/'+backup_name_input.get())
        status.config(text="")
        return

def run_backup():
    wtf_src_path = wow_directory_input.get()+'/'+'WTF'
    wtf_backup_path = backup_directory_input.get()+'/'+'WTF'
    addons_src_path = wow_directory_input.get()+'/'+'Interface'+'/'+'AddOns'
    addons_backup_path = backup_directory_input.get()+'/'+'AddOns'

    if len(backup_name_input.get()) == 0 and not naming_option_var:
        print('Error: No backup name.')
        messagebox.showwarning(title="Warning", message="Error: No backup name.")
        status.config(text="Error: No backup name.")
        return
    
    if wow_directory_input.get().find('_retail_') == -1:
        print('Error: Invalid installation directory.')
        messagebox.showwarning(title="Warning", message="Error: Invalid game directory.")
        status.config(text="Error: Invalid game directory. Please provide _retail_ folder.")
        return

    confirm = messagebox.askokcancel(title="Confirm", message="Your files will be copied to the following directory:\n\n"+backup_directory_input.get())
    if not confirm:
        return
    
    print('Copying WTF files.')
    print('...')
    status.config(text="Copying WTF files...")
    try:
        shutil.copytree(wtf_src_path, wtf_backup_path)
        print('From '+wtf_src_path+' to '+wtf_backup_path)
    except:
        messagebox.showerror(title="Error", message="An error occurred.")
    else:
        print('WTF Backup Complete.\n')
        status.config(text="WTF Backup Complete.")

    print('Starting Addons backup.')
    print('...')
    status.config(text="Copying addons...")
    try:
        shutil.copytree(addons_src_path, addons_backup_path)
        print('From '+addons_src_path+' to '+addons_backup_path)
    except:
        messagebox.showerror(title="Error", message="An error occurred.")
        print('An error occurred.')
        status.config(text="An error occurred.")
        return
    else:        
        print('Addons Backup Complete.\n')
        print('Backup Complete.')
        status.config(text="Backup complete.")
        messagebox.showinfo(title="Backup Complete", message="Backup Complete.")
        return


# GUI

window.title('WoW Backup Script')
window.minsize(width=600, height=300)
window.config(padx=20, pady=20)

header = Label(text="World of Warcraft Backup Script v1.0", font=("Arial", 12, "bold"))
header.grid(column=1, row=0, columnspan=4)

author = Label(text="By GibsonSWE")
author.grid(column=1, row=1, columnspan=4)


# WoW Directory

wow_directory_text = Label(text="Game directory:")
wow_directory_text.grid(column=0, row=4, sticky="E")

wow_directory_input = Entry(width=60)
wow_directory_input.grid(column=1, row=4, columnspan=4, sticky="W", pady=10)

wow_browse_button = Button(text="Browse...", width=10, command=open_wow_directory)
wow_browse_button.grid(column=5, row=4, sticky="W")


# Backup Directory

backup_directory_text = Label(text="Backup directory:")
backup_directory_text.grid(column=0, row=5, sticky="E")

backup_directory_input = Entry(width=60)
backup_directory_input.grid(column=1, row=5, columnspan=4, sticky="W", pady=10)

backup_browse_button = Button(text="Browse...", width=10, command=open_backup_directory)
backup_browse_button.grid(column=5, row=5, sticky="W")


# Backup Naming

naming_option_text = Label(text="Name of Backup:")
naming_option_text.grid(column=0, row=6, sticky="E")

naming_option_int = IntVar()
naming_option_int.set(1)
backup_name_string = StringVar()

backup_name_option1 = Radiobutton(text="Date:", value=1, variable=naming_option_int, command=naming_option_date)
backup_name_option1.grid(column=1, row=6, sticky="W")

date_text = Label(text='../'+todays_date)
date_text.grid(column=2, row=6)

backup_name_option2 = Radiobutton(text="Custom Name: ../", value=2, variable=naming_option_int, command=naming_option_custom)
backup_name_option2.grid(column=3, row=6, sticky="W")

backup_name_input = Entry(width=20, textvariable=backup_name_string, state=DISABLED)
backup_name_input.grid(column=4, row=6, sticky="W", pady=10)

apply_button = Button(text="Apply", width=10, command=apply_custom_name)
apply_button.grid(column=5,row=6)


# STATUS AND RUN

status_text = Label(text="Status: ", font=("Arial", 12))
status_text.grid(column=0, row=7, sticky="E")

status = Label(font=("Arial", "10"))
status.grid(column=1, row=7, columnspan=4, sticky="W")

run = Button(text="BACKUP", width=10, font=("Arial", 15, "bold"), command=run_backup)
run.grid(column=1,row=10, columnspan=4, pady=10)

window.mainloop()
