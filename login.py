from tkinter import*
from tkinter import ttk
from PIL import Image , ImageTk 
from tkinter import messagebox


class Login_Window:
    def __init__(self , root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1300x700+0+0")

        self.bg = ImageTk.PhotoImage(file = r"C:\Users\HP\OneDrive\Desktop\coding\login form\image\login.jpg")
        lbl_bg = Label(self.root , image = self.bg)
        lbl_bg.place(x=0 , y=0 , relwidth=1 , relheight=1)

        frame = Frame(self.root , bg = "#b8b2a6")
        frame.place(x=500 , y=170 , width = 340 , height=450)

        img1 = Image.open(r"C:\Users\HP\OneDrive\Desktop\coding\login form\image\logo.png")
        img1 = img1.resize((120,120) , Image.Resampling.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(image = self.photoimage1 , bg = "#b8b2a6" , borderwidth = 0)
        lblimg1.place(x=620 , y = 175 , width = 100 , height = 100)

        get_str = Label(frame , text = "Get Started" , font = ("times new roman" , 20 , "bold") , fg = "#962071" , bg = "#b8b2a6")
        get_str.place(x = 92 , y = 100)

        # Labels 
        username = lbl = Label(frame , text = "Username" , font= ("times new roman",15,"bold"), fg = "#962071", bg ="#b8b2a6")
        username.place(x=70 , y=155)

        self.txtuser = ttk.Entry(frame , font = ("times new roman", 15 , "bold"))
        self.txtuser.place(x=40 , y = 180 , width = 270)

        password = lbl = Label(frame , text = "Password" , font= ("times new roman",15,"bold"), fg = "#962071", bg ="#b8b2a6")
        password.place(x=70 , y=225)

        self.txtpass = ttk.Entry(frame , font = ("times new roman", 15 , "bold") , show = "*")
        self.txtpass.place(x=40 , y = 250 , width = 270)


    # ===================Icon image ============

        img2 = Image.open(r"C:\Users\HP\OneDrive\Desktop\coding\login form\image\logo2.png")
        img2 = img2.resize((25,25) , Image.Resampling.LANCZOS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        lblimg2 = Label(image = self.photoimage2 , bg = "#b8b2a6" , borderwidth = 0)
        lblimg2.place(x=545 , y = 322 , width = 25 , height = 25)

        img3 = Image.open(r"C:\Users\HP\OneDrive\Desktop\coding\login form\image\passwordlogo.png")
        img3 = img3.resize((25,25) , Image.Resampling.LANCZOS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        lblimg3 = Label(image = self.photoimage3 , bg = "#b8b2a6" , borderwidth = 0)
        lblimg3.place(x=545 , y = 393, width = 25 , height = 25)

    # ==============login button ===========

        loginbtn = Button(frame ,command= self.login, text = "Login" , font = ("times new roman" , 15 , "bold") , bd = 3 ,relief=RIDGE, fg = "white" , bg = "red")
        loginbtn.place(x = 110 , y = 300 , width = 120 , height = 35)

    # register button
        registerbtn = Button(frame , text = "New user registration" , font = ("times new roman" , 10 , "bold") , borderwidth=0 , fg = "#962071" , bg = "#b8b2a6" , activeforeground= "white" ,activebackground= "#b8b2a6")
        registerbtn.place(x = 20 , y = 350 , width = 160)

    # forgot button 
        forgotbtn = Button(frame , text = "Forgot Password" , font = ("times new roman" , 10 , "bold") , borderwidth=0 , fg = "#962071" , bg = "#b8b2a6" , activeforeground= "white" ,activebackground= "#b8b2a6")
        forgotbtn.place(x = 7 , y = 370 , width = 160)


    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error", "all field required")
        elif self.txtuser.get()=="abcd" and self.txtpass.get() =="1234":
            messagebox.showinfo("Success","Welcome to my page")
        else:
            messagebox.showerror("Invalid","Invalid username and password")
             

        





if __name__ == "__main__":
    root = Tk()
    app = Login_Window(root)
    root.mainloop()
