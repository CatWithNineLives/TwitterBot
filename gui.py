from tkinter import *
from stream import *
# main function should be added to this file instead
# api connections should be formed and then call stream functions


def buttonPressed():

    print("Button pressed")
    print(v.get())
    l = e1.get().split(",")

    if v.get() == 1:
        print("Hashtags :", l)
        # call stream function from stream file
    elif v.get() == 2:
        print("Usernames :", l)
        # call stream function

    else:
        print("Invalid")


root = Tk(className='Input Hashtags and usernames.')
root.title('FollowandLikeBot')
# widgets added here
ourMessage = 'Input hastags with # amd usernames without @. For example #freedom and NiveditaS. Choose input'
messageVar = Message(root, text=ourMessage)
messageVar.config(bg='lightgreen')
messageVar.pack()

v = IntVar()
Radiobutton(root, text='Hashtags', variable=v, value=1).pack(anchor=W)
Radiobutton(root, text='Usernames', variable=v, value=2).pack(anchor=W)

label = Label(
    root, text='Enter choice separated by , for example: usernames as NiveditaS, Nita')
e1 = Entry(root)
label.pack()
e1.pack()


button = Button(root, text="Start!", command=buttonPressed)
button.pack()


root.mainloop()
