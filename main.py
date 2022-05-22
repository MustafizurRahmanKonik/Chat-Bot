from tkinter import *
root = Tk()
def send():
    send = "You:"+ e.get()
    text.insert(END,"\n" + send)
    if(e.get()=='hi'):
        text.insert(END, "\n" + "Bot: hello, How can i help you?")
    elif(e.get()=='hello'):
        text.insert(END, "\n" + "Bot: hi")
    elif (e.get() == 'how are you?'):
        text.insert(END, "\n" + "Bot: i'm fine and you?")
    elif (e.get() == "i'm fine too"):
        text.insert(END, "\n" + "Bot: nice to hear that")
    elif (e.get()== 'need an appoinment please'):
        text.insert(END, "\n" + "Bot: Doctor name: Sahana Sultana ,DIU! Serial no: 26 ,tommorow 6 pm to 9 pm at our address!")
    elif (e.get() == 'please send Doc. address'):
        text.insert(END, "\n" + "Bot: 03/45, khagan savar diu")
    elif (e.get() == 'Phone number please?'):
        text.insert(END, "\n" + "Bot: 01799063771 ")
    elif (e.get() == 'Thanks'):
        text.insert(END, "\n" + "Bot: Chat with you later,Bye! STAY HOME STAY SAFE")
    else:
        text.insert(END, "\n" + "Bot: Sorry I didnt get it.")
text = Text(root,bg='yellow')
text.grid(row=0,column=0,columnspan=2)
e = Entry(root,width=80)
send = Button(root,text='Send',bg='blue',width=20,command=send).grid(row=1,column=1)
e.grid(row=1,column=0)

root.title('DOC.CHATBOT CHATS:')
root.mainloop()