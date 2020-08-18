from tkinter import *
from stream import *
from connection import connect_account
import logging


logging.basicConfig(level=logging.INFO, filename='app.log',
                    filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

api = connect_account()


def buttonPressed():
    """
    Functions in stream.py are called when the button is pressed
    """
    print("Button pressed")
    # print(v.get())
    l = e1.get().split(",")

    if v.get() == 1:
        print("Hashtags :", l)
        # call function to search for these hashtags from stream file
        listen(api, l)

    elif v.get() == 2:
        print("Usernames :", l)
        # call function to search for these usernames and follow them
        follow_usernames(api, l)

    else:
        print("Invalid")


root = Tk(className='Input Hashtags and usernames.')
root.title('FollowandLikeBot')
# widgets added here
# Message to be displayed in the window
ourMessage = 'Input hastags with # amd usernames without @. For example #freedom and NiveditaS. Choose input'
messageVar = Message(root, text=ourMessage)
messageVar.config(bg='lightgreen')
messageVar.pack()

# whether user wants to input hashtags or usernames
v = IntVar()
Radiobutton(root, text='Hashtags', variable=v, value=1).pack(anchor=W)
Radiobutton(root, text='Usernames', variable=v, value=2).pack(anchor=W)

# the values
label = Label(
    root, text='Enter the values for your choice separated by , for example: usernames as NiveditaS, Nita')
e1 = Entry(root)
label.pack()
e1.pack()


button = Button(root, text="Start!", command=buttonPressed)
button.pack()


root.mainloop()
