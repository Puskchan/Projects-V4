import tkinter
import tkinter.messagebox
import pickle

root = tkinter.Tk()
root.title("To-Do list by @aditya")

def add_task():
    task = entry_field.get()
    if task != "":
        listbox_task.insert(tkinter.END, task)
        entry_field.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Warning!", message="You must enter a task.")

def remo_task():
    try:
        task_index = listbox_task.curselection()[0]
        listbox_task.delete(task_index)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="You must select a task.")

def load_list():
    try:
        tasks = pickle.load(open("tasks.dat", "rb"))
        listbox_task.delete(0, tkinter.END)
        for task in tasks:
            listbox_task.insert(tkinter.END, task)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="Cannot find the file.")

def save_list():
    tasks = listbox_task.get(0, listbox_task.size())
    pickle.dump(tasks, open("tasks.dat", "wb"))


# Create GUI
frame_tsk = tkinter.Frame(root)
frame_tsk.pack()

listbox_task = tkinter.Listbox(frame_tsk, width=50)
listbox_task.pack(fill=tkinter.BOTH, side=tkinter.LEFT)

scrollbar_tsk = tkinter.Scrollbar(frame_tsk)
scrollbar_tsk.pack(side=tkinter.RIGHT, fill=tkinter.Y)

listbox_task.config(yscrollcommand=scrollbar_tsk.set)
scrollbar_tsk.config(command=listbox_task.yview)

entry_field = tkinter.Entry(root, width=50)
entry_field.pack(fill=tkinter.BOTH)

add_button = tkinter.Button(root, text='Add item', width=48, height=1, command=add_task)
add_button.pack(fill=tkinter.BOTH)

remove_button = tkinter.Button(root, text='Remove item', width=48, height=1, command=remo_task)
remove_button.pack(fill=tkinter.BOTH)

load_button = tkinter.Button(root, text='Load list', width=48, height=1, command=load_list)
load_button.pack(fill=tkinter.BOTH)

save_button = tkinter.Button(root, text='Save list', width=48, height=1, command=save_list)
save_button.pack(fill=tkinter.BOTH)

root.mainloop()
