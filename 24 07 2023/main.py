import tkinter

def hello():
    print("Hello World")
    


if __name__ == '__main__':
    
    window = tkinter.Tk()
    window.title("Tkinter First App")
    window.geometry('600x400')

    frame = tkinter.Frame(window)
    frame.pack()

    label = tkinter.Label (frame, text = "Hello World", fg = "red", width= 50)
    label.pack()

    textentry = tkinter.Entry(frame,bg = "pink", width= 50)
    textentry.pack()

    button = tkinter.Button(frame, text = "Hellow World", command=hello, fg ="black", activebackground= "yellow",activeforeground="red")
    button.pack()

    #state= tkinter.DISABLED use for disable textbox an Active use enable textbox
    #show = "*" use for show * in textbox ex. password field


    window.mainloop()