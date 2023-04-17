# Imports
from tkinter import *
from tkinter import messagebox
import tkinter.messagebox
import sqlite3

# Globals

rows = []

# Database Connection
conn = sqlite3.connect('events.db')
c = conn.cursor()

# Table Creation
c.execute('CREATE TABLE IF NOT EXISTS eventInfo(event TEXT, timeNeeded TEXT, dueDate TEXT, priority INTEGER)')

# Function(s)

def display():

    list1.delete(0, END)
    list2.delete(0, END)
    list3.delete(0, END)
    list4.delete(0, END)
    
    c.execute("SELECT * FROM eventInfo ORDER BY priority ASC")
    for event in c.fetchall():
        list1.insert(END, event[0])
        list2.insert(END, event[1])
        list3.insert(END, event[2])
        list4.insert(END, event[3])
        

def yscroll1(*args):
    if list2.yview() != list1.yview():
        list2.yview_moveto(args[0])
    elif list3.yview() != list1.yview():
        list3.yview_moveto(args[0])
    elif list4.yview() != list1.yview():
        list4.yview_moveto(args[0])

def yscroll2(*args):
    if list1.yview() != list2.yview():
        list1.yview_moveto(args[0])
    elif list3.yview() != list2.yview():
        list3.yview_moveto(args[0])
    elif list4.yview() != list2.yview():
        list4.yview_moveto(args[0])

def yscroll3(*args):
    if list1.yview() != list3.yview():
        list1.yview_moveto(args[0])
    elif list2.yview() != list3.yview():
        list2.yview_moveto(args[0])
    elif list4.yview() != list3.yview():
        list4.yview_moveto(args[0])

def yscroll4(*args):
    if list1.yview() != list4.yview():
        list1.yview_moveto(args[0])
    elif list2.yview() != list4.yview():
        list2.yview_moveto(args[0])
    elif list3.yview() != list4.yview():
        list3.yview_moveto(args[0])

def yview(*args):
    list1.yview(*args)
    list2.yview(*args)
    list3.yview(*args)
    list4.yview(*args)

def destroy():
    eventView_Window.destroy()
    eventAdd_Window.destroy()

#Button Commands
def appendEvents():

    try:
        intPriority = int(priority_entry.get())
    except:
        messagebox.showinfo('Number!', 'You need to put a number in the priority field!')
        return

    c.execute("INSERT INTO eventInfo(event, timeNeeded, dueDate, priority) VALUES(?, ?, ?, ?)",
              (event_entry.get(), timeNeeded_entry.get(), dateDue_entry.get(), priority_entry.get()))
    conn.commit()
    
    event_entry.delete(0, END)
    timeNeeded_entry.delete(0, END)
    dateDue_entry.delete(0, END)
    priority_entry.delete(0, END)

    display()

def switchTabs_addEvents():
    eventAdd_Window.deiconify()

def closeAdd():
    eventAdd_Window.withdraw()

def deleteRow():
        
    event_delete = list1.curselection()
    time_delete = list2.curselection()
    due_delete = list3.curselection()
    priority_delete = list4.curselection()

    if event_delete != ():
        eventId = list1.get(event_delete)
        timeId = list2.get(event_delete)
        dueId = list3.get(event_delete)
        priorityId = list4.get(event_delete)

        answer = tkinter.messagebox.askquestion('Delete', 'Are you sure you want to delete this entry?')

        if answer == 'yes':
            c.execute("DELETE FROM eventInfo WHERE event=? AND timeNeeded=? AND dueDate=? AND priority=?", (eventId, timeId, dueId, priorityId))
            conn.commit()
        else:
            return

    elif time_delete != ():
        eventId = list1.get(time_delete)
        timeId = list2.get(time_delete)
        dueId = list3.get(time_delete)
        priorityId = list4.get(time_delete)

        answer = tkinter.messagebox.askquestion('Delete', 'Are you sure you want to delete this entry?')

        if answer == 'yes':
            c.execute("DELETE FROM eventInfo WHERE event=? AND timeNeeded=? AND dueDate=? AND priority=?", (eventId, timeId, dueId, priorityId))
            conn.commit()
        else:
            return

    elif due_delete != ():
        eventId = list1.get(due_delete)
        timeId = list2.get(due_delete)
        dueId = list3.get(due_delete)
        priorityId = list4.get(due_delete)

        answer = tkinter.messagebox.askquestion('Delete', "Are you sure you want to delete this entry?")
        
        if answer == 'yes':
            c.execute("DELETE FROM eventInfo WHERE event=? AND timeNeeded=? AND dueDate=? AND priority=?", (eventId, timeId, dueId, priorityId))
            conn.commit()
        else:
            return

    elif priority_delete != ():
        eventId = list1.get(priority_delete)
        timeId = list2.get(priority_delete)
        dueId = list3.get(priority_delete)
        priorityId = list4.get(priority_delete)

        answer = tkinter.messagebox.askquestion('Delete', "Are you sure you want to delete this entry?")
        
        if answer == 'yes':
            c.execute("DELETE FROM eventInfo WHERE event=? AND timeNeeded=? AND dueDate=? AND priority=?", (eventId, timeId, dueId, priorityId))
            conn.commit()
        else:
            return

    list1.delete(0, END)
    list2.delete(0, END)
    list3.delete(0, END)
    list4.delete(0, END)
    
    display()

# Master Widget
eventView_Window = Tk()
eventView_Window.title("Event Viewer")
eventView_Window.protocol("WM_DELETE_WINDOW", destroy)

eventAdd_Window = Tk()
eventAdd_Window.title("Event Adder")
eventAdd_Window.withdraw()
eventAdd_Window.protocol("WM_DELETE_WINDOW", closeAdd)

# Label Info
addEvent_label = Label(eventAdd_Window, text='Add Events', font=('Courier', 18))
event_label = Label(eventAdd_Window, text='Event: ', font=('Courier', 14))
timeNeeded_label = Label(eventAdd_Window, text='Time Needed: ', font=('Courier', 14))
dateDue_label = Label(eventAdd_Window, text='Date Due: ', font=('Courier', 14))
priority_label = Label(eventAdd_Window, text='Priority Rank: ', font=('Courier', 14))

closeButton = Button(eventAdd_Window, text = "Close", font = ('Courier', 10), command = closeAdd)

title_label = Label(eventView_Window, text='Events', font = ("Courier", 18))

displayFrame = Frame(eventView_Window)
displayFrame.pack_propagate(False)

scrollbar = Scrollbar(displayFrame, orient='vertical')
list1 = Listbox(displayFrame, height='10', width='20', yscrollcommand=yscroll1)
list2 = Listbox(displayFrame, height='10', width='20', yscrollcommand=yscroll2)
list3 = Listbox(displayFrame, height='10', width='20', yscrollcommand=yscroll3)
list4 = Listbox(displayFrame, height='10', width='20', yscrollcommand=yscroll4)
scrollbar.config(command=yview)

switchButton_addEvents = Button(eventView_Window, text = "Add Events", font = ('Courier', 14), command = switchTabs_addEvents)
deleteEvents_Button = Button(eventView_Window, text = "Delete Selected Events", font = ('Courier', 14), command = deleteRow)


# Entries Info
event_entry = Entry(eventAdd_Window, font=('Courier', 14))
timeNeeded_entry = Entry(eventAdd_Window, font=('Courier', 14))
dateDue_entry = Entry(eventAdd_Window, font=('Courier', 14))
priority_entry = Entry(eventAdd_Window, font=('Courier', 14))
addEventInfo = Button(eventAdd_Window, text='Add Event', font=('Courier', 14), command=appendEvents)

# Label Grid/Pack
addEvent_label.grid(columnspan=3, row=0)
event_label.grid(row=1, sticky=E, padx=3)
timeNeeded_label.grid(row=2, sticky=E, padx=3)
dateDue_label.grid(row=3, sticky=E, padx=3)
priority_label.grid(row=4, sticky=E, padx=3)

closeButton.grid(row = 7, column = 2)

title_label.pack()
displayFrame.pack()
scrollbar.grid(row=0, column=4, sticky='nes')
list1.grid(row=0, column=0)
list2.grid(row=0, column=1)
list3.grid(row=0, column=2)
list4.grid(row=0, column=3)

switchButton_addEvents.pack()
deleteEvents_Button.pack()

# Entries Grid
event_entry.grid(columnspan=3, row=1, column=1, padx=2, pady=2, sticky=W)
timeNeeded_entry.grid(columnspan=3, row=2, column=1, padx=2, pady=2, sticky=W)
dateDue_entry.grid(columnspan=3, row=3, column=1, padx=2, pady=2, sticky=W)
priority_entry.grid(columnspan=3, row=4, column=1, padx=2, pady=2, sticky=W)
addEventInfo.grid(columnspan=3, pady=4, row=6)

display()
mainloop()
