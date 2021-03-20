import json
import requests
from tkinter import *
def getdata():
    link = r"https://official-joke-api.appspot.com/jokes/programming/random"
    data = requests.get(link)
    convdata = json.loads(data.text)
    for i in  convdata:
        type_s = i["setup"]
        type_p = i["punchline"]
        listbox_1.delete(0,END)
        listbox_1.delete(1,END)
        listbox_1.insert(0,f"{type_s}")
        listbox_1.insert(1,f"{type_p}")


root = Tk()
root.title("Random Jokes Generator")
root.geometry("850x350")
root.resizable(0,0)
label_1 = Label(root,text="Random Jokes",font="fonte 20 bold")
label_1.pack()
listbox_1 = Listbox(root,font="Cambria 15",width=100,bg="gray10",fg="white")
listbox_1.pack()
Button_1 = Button(root,text="Click me for an another joke",command=getdata,width=35,height=2,font="Cambria 15 bold")
Button_1.pack()
root.mainloop()
