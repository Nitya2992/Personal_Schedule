# import all functions from the tkinter
# import messagebox class from tkinter
from tkinter import *
from tkinter import messagebox

tasks_list = []
counter = 1

# Function for checking input error
def inputError():
    # check for enter task field is empty or not
    if enterTaskField.get() == "":
        # show the error message
        messagebox.showerror("Input Error")

        return 0

    return 1


# Function for clearing the contents
def clear_taskNumberField():
    taskNumberField.delete(0.0, END)


def clear_timeField():
    enterTimeField.delete(0, END)

# Function for clearing the contents
def clear_taskField():
    enterTaskField.delete(0, END)


# Function for inserting the contents
def insertTask():
    global counter
    value = inputError()
    if value == 0:
        return

    content = enterTaskField.get() + "\n"
    global time
    time=enterTimeField.get()+"\n"
    tasks_list.append(content)

    TextArea.insert(END,time+"[ " + str(counter) + " ] " + content)
    counter += 1

    clear_taskField()
    clear_timeField()


# function for deleting the specified task
def delete():
    global counter

    if len(tasks_list) == 0:
        messagebox.showerror("No task")
        return

    number = taskNumberField.get(1.0, END)

    if number == "\n":
        messagebox.showerror("input error")
        return

    else:
        task_no = int(number)

    clear_taskNumberField()

    tasks_list.pop(task_no - 1)
    counter -= 1
    TextArea.delete(1.0, END)

    # rewriting the task after deleting one task at a time
    for i in range(len(tasks_list)):
        TextArea.insert(END,"[ " + str(i + 1) + " ] " +time+tasks_list[i])


# Driver code
if __name__ == "__main__":
    gui = Tk()
    gui.configure(background="plum2")
    gui.title("Personal Schedule")
    gui.geometry("900x650")
    enterTask = Label(gui, text="Task", bg="DarkOrchid1",fg="black")
    enterTime = Label(gui,text="Time",bg="DarkOrchid1",fg="black")

    enterTaskField = Entry(gui)
    enterTimeField = Entry(gui)

    Submit = Button(gui, text="Submit", fg="Black", bg="DarkOrchid1", command=insertTask)
    TextArea = Text(gui, height=20, width=50, font="lucida 13")

    taskNumber = Label(gui, text="Delete Task Number", bg="DarkOrchid1")
    taskNumberField = Text(gui, height=1, width=2, font="lucida 13")
    delete = Button(gui, text="Delete", fg="light cyan", bg="DeepSkyBlue2", command=delete)
    Exit = Button(gui, text="Exit", fg="light cyan", bg="orange red", command=exit)

    enterTask.grid(row=0, column=3,padx=10,pady=9)
    enterTime.grid(row=0,column=1,padx=10,pady=9)
    enterTaskField.grid(row=1, column=3, ipadx=50)
    enterTimeField.grid(row=1,column=1,ipadx=30)
    Submit.grid(row=2, column=2 , ipadx=60,ipady=7)

    TextArea.grid(row=3, column=2, padx=10, sticky=W)
    taskNumber.grid(row=4, column=2, pady=5)
    taskNumberField.grid(row=5, column=2)
    delete.grid(row=6, column=2, pady=5)
    Exit.grid(row=7, column=2)

    gui.mainloop()
