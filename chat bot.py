from tkinter import *
root=Tk()
root.title("chat bot")
root.geometry('400x500')
def send():
    send = "You:"+ messagewindow.get()
    chatwindow.insert(END,"\n" + send)
    if(messagewindow.get()=='hi'):
        chatwindow.insert(END, "\n" + "Bot: hello")
        messagewindow.delete()
    elif(messagewindow.get()=='hello'):
        chatwindow.insert(END, "\n" + "Bot: hi")
    elif(messagewindow.get()=='Heyy sujju'):
        chatwindow.insert(END, "\n" + "Bot: yess,you want to tell me something")
    elif(messagewindow.get()=='what are you doing'):
        chatwindow.insert(END, "\n" + "Bot: i am doing coding")
    elif(messagewindow.get()=='okay bye'):
        chatwindow.insert(END, "\n" + "Bot:byee")
    elif (messagewindow.get() == 'how are you?'):
        chatwindow.insert(END, "\n" + "Bot: i'm fine and you?")
    elif (messagewindow.get() == "i'm fine too"):
        chatwindow.insert(END, "\n" + "Bot: nice to hear that")
    else:
        chatwindow.insert(END, "\n" + "Bot: Sorry I didnt get it.")
# create menu baar
main_menu=Menu(root)
# create submenu baar
file_menu=Menu(root)
file_menu.add_command(label="New")
file_menu.add_command(label="save as")
file_menu.add_command(label="Exit",command=root.destroy)


main_menu.add_cascade(label="File", menu=file_menu)
main_menu.add_command(label="Edit")
main_menu.add_command(label="Quit")
root.config(menu=main_menu)
scrollbar=Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)
chatwindow=Text(root,bd=1,bg="white",width=50,height=8,yscrollcommand=scrollbar.set)
chatwindow.place(x=7,y=7,height=385,width=370)
scrollbar.config(command=chatwindow.yview)
messagewindow=Entry(root,bg="skyblue",width=30)
messagewindow.place(x=110,y=400,height=30,width=280)
# e = Entry(root,width=80)
# send = Button(root,text='Send',bg='blue',width=20,command=send).grid(row=1,column=1)
# e.grid(row=1,column=0)
button=Button(root,text="send",bg="red",command=send,activebackground="light blue",width=12,height=5)
button.place(x=6,y=400,height=30,width=100)
button=Button(root,text="close",bg="gray",command=root.destroy,activebackground="light blue",width=12,height=5)
button.place(x=130,y=440,height=30,width=100)
# chatwindow.config(command=scrollbar)
root.mainloop()
