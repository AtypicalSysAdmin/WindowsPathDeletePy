#avoid cache
import sys 
sys.dont_write_bytecode = True


#------------------------------------------------------------------------------------------------------------------------
#import logger
from Logs.GetTracebackLogs import *
logger.warning("Application Log Started")




#------------------------------------------------------------------------------------------------------------------------
#import methods
from MethFolder.methFile import *

def clickedYes():
    try:
        dir = txt1.get()
        logger.info("Main info - Entered directory: % s" % dir)

        if is_admin():
            try:
                res=clearDir(dir)
                txt1.delete(0, END)
                #logger.info("Text box content has been reset")

                #update log listbox
                try:
                    fname=".\\Logs\\tracebacklog.txt"
                    #READ LAST 10 LINES OF LOG FILE
                    with open(".\\Logs\\tracebacklog.txt", 'r') as f:
                        LinesCount = len(f.readlines())
                    if LinesCount>10:
                        #last 10 lines
                        NumberOfLines=10
                        lines = LastNlines(fname, NumberOfLines)
                        #lb3.configure(text= lines)
                        listbox.delete(0, END)
                        for i in range (NumberOfLines-1, -1, -1): #counts 9 to 0 - reverse order, latest log first
                            listbox.insert((NumberOfLines-1)-i, lines[i])
                    #if logs are not 10 lines yet, do this instead
                    else:
                        #last lines
                        NumberOfLines=LinesCount
                        lines = LastNlines(fname, NumberOfLines)
                        #lb3.configure(text= lines)
                        listbox.delete(0, END)
                        for i in range (NumberOfLines-1, -1, -1): #counts 9 to 0 - reverse order, latest log first
                            listbox.insert((NumberOfLines-1)-i, lines[i])

        
                except Exception as e:
                    logger.error(str(e))
                    logger.error(traceback.format_exc())
                return res
            except Exception as e:
                logger.error(str(e))
                logger.error(traceback.format_exc())
        else:
            # Re-run the program with admin rights
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
            logger.error("Main Error - Access denied, admin rights required")
    except Exception as e:
        logger.error(str(e))
        logger.error(traceback.format_exc())
        





from tkinter import messagebox

def deleteClick():
    reply = messagebox.askyesno("Important Notice", "Are you sure you want to delete this?", icon ='warning')
    if reply == True:
        if clickedYes() == True:
            messagebox.showinfo('Successful','Deleted', icon='info')
        else:
            messagebox.showinfo('Error','Something went wrong, please check the logs at mainwindow or at ./Logs/tracebacklog.txt', icon ='error')
    else:
        messagebox.showinfo('Reply to deletion', 'Operation Canceled!', icon ='info')






def askExitYesNo():
    reply = messagebox.askyesno('Exit Confirmation', 'Do you really want to quit this application?')
    if reply == True:
        messagebox.showinfo('Exiting..', 'Click on OK to quit application')
        MainWindow.destroy()
    else:
        messagebox.showinfo('', 'Thanks for Staying')








#------------------------------------------------------------------------------------------------------------------------
#User interface tkinter

from tkinter import *
import tkinter as tk



#MainWindow
MainWindow = Tk()
MainWindow.title("Windows Troubleshooting app")
# photo = PhotoImage(file = "Windows.ico")
# MainWindow.iconphoto(False, photo)

MainWindow.geometry('400x220')





#info label 1
#create
lbl = Label(MainWindow, text="Enter the directory to be deleted:", font=("Arial", 10))
#position
lbl.grid(column=0, row=0)
lb2 = Label(MainWindow, text="Logs show below:", font=("Arial", 10))
lb2.grid(column=0, row=2)
#log label
lb3 = Label(MainWindow, text="Last 10 lines of logs will show in this list:", font=("Arial", 10), fg="red")
#position
lb3.grid(column=0, row=3)





#path input
txt1 = Entry(MainWindow,width=10)
txt1.grid(column=1, row=0)




#delete button
btn1 = Button(MainWindow, text="Delete",  bg="blue", fg="white", padx=20, pady=5, command=deleteClick)
btn1.grid(column=2, row=0)
#exit button
btn2 = Button(
    MainWindow,
    text='Exit',
    command=askExitYesNo,
    padx=20,
    pady=5,  bg="blue", fg="white"
)
btn2.grid(column=2, row=3)





#list box
langs = ('Java', 'C#', 'C', 'C++', 'Python',
        'Go', 'JavaScript', 'PHP', 'Swift')

langs_var = StringVar(value=langs)

listbox = Listbox(
    MainWindow,
    listvariable=langs_var,
    height=6,
    selectmode='extended')

listbox.grid(
    column=0,
    row=4,
    sticky='nwes'
)





# link a scrollbar to a list
vscrollbar = Scrollbar(
    MainWindow,
    orient='vertical',
    command=listbox.yview
)

hscrollbar = Scrollbar(
    MainWindow,
    orient='horizontal',
    command=listbox.xview
)

listbox['yscrollcommand'] = vscrollbar.set
listbox['xscrollcommand'] = hscrollbar.set

vscrollbar.grid(
    column=1,
    row=4,
    sticky='ns')

hscrollbar.grid(
    column=0,
    row=5,
    sticky='ew')














MainWindow.mainloop()


