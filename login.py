from tkinter import*
from tkinter import ttk
from PIL import Image , ImageTk 


class Login_Window:
    def __init__(self , root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        self.bg = ImageTk.PhotoImage(file =workspaces/login-page/images/bg.jpg)
        lbl_bg = Label(self.root , image = self.bg)


if __name__ == "__main__":
    root = Tk()
    app = Login_Window(root)
    root.mainloop()
