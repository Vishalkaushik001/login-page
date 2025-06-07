from tkinter import*
from tkinter import ttk
from PIL import Image , ImageTk 
from tkinter import messagebox
import pymysql

def main():
    win = Tk()
    app = Login_Window(win)
    win.mainloop()




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
        lblimg1.place(x=620 , y = 175 , width = 100 , height=100)

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
        registerbtn = Button(frame , text = "New user registration" , command = self.register_window , font = ("times new roman" , 10 , "bold") , borderwidth=0 , fg = "#962071" , bg = "#b8b2a6" , activeforeground= "white" ,activebackground= "#b8b2a6")
        registerbtn.place(x = 20 , y = 350 , width = 160)

    # forgot button 
        forgotbtn = Button(frame , text = "Forgot Password" , font = ("times new roman" , 10 , "bold") , borderwidth=0 , fg = "#962071" , bg = "#b8b2a6" , activeforeground= "white" ,activebackground= "#b8b2a6")
        forgotbtn.place(x = 7 , y = 370 , width = 160)


    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)


    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error", "all field required")
        elif self.txtuser.get()=="abcd" and self.txtpass.get() =="1234":
            messagebox.showinfo("Success","Welcome to my page")
        else:
            conn = pymysql.connect(host = "localhost" , user="root" , password ="12345678" , database ="my_data")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from register where email = %s and password = %s",(
                                                                                            self.txtuser.get(),
                                                                                            self.txtpass.get()
                                                                                        ))

            row = my_cursor.fetchone()
            if row != None:
                messagebox.showerror("Error", "Invalid Username & Password")
            else:
                open_main=messagebox.askyesno("Access Granted", "Welcome Admin, Continue?")
                # if open_main>0:
                #     self.new_window = Toplevel(self.new_window)
                #     self.app = 


class Register:
    def __init__(self , root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1300x700+0+0")

        # ==============Variables ============
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()


    # =============bg image =========
        self.bg = ImageTk.PhotoImage(file =r"C:\Users\HP\OneDrive\Desktop\coding\login form\image\login.jpg")
        bg_lbl = Label(self.root , image = self.bg)
        bg_lbl.place(x=0,y=0 ,relwidth=1 , relheight=1)

        # ======main frame ==========

        frame = Frame(self.root , bg = "#b8b2a6")
        frame.place(x=280 , y = 100 , width = 700, height = 550)

        img1 = Image.open(r"C:\Users\HP\OneDrive\Desktop\coding\login form\image\registerlogo.png")
        img1 = img1.resize((90,90) , Image.Resampling.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(image = self.photoimage1 , bg = "#b8b2a6" , borderwidth = 0)
        lblimg1.place(x=570 , y = 100 , width = 100 , height = 100)

        register_lbl = Label(frame , text = "REGISTER HERE" , font = ("times new roman" , 20 , "bold") , fg = "#0B1D51" , bg = "#b8b2a6")
        register_lbl.place(x = 20 , y = 20)

        # ===============label and entry=========

        # -------------------------row1

        fname = Label(frame , text = "First Name" , font = ("times new roman",15 , "bold") ,fg = "#962071" ,bg = "#b8b2a6")
        fname.place(x = 50 , y = 100)

        self.fname_entry = ttk.Entry(frame , textvariable=self.var_fname , font = ("times new roman" , 15 , "bold"))
        self.fname_entry.place(x = 50 , y = 130 , width = 250)

        l_name = Label(frame , text = "Last Name" , font = ("times new roman",15,"bold"),bg = "#b8b2a6" , fg = "#962071")
        l_name.place(x=370 , y = 100)

        self.txt_lname = ttk.Entry(frame , textvariable= self.var_lname ,font = ("times new roman" , 15 , "bold" ))
        self.txt_lname.place(x=370 , y = 130 , width = 250)


        # --------------------------row2

        contact = Label(frame , text = "Contact No" , font = ("times new roman" , 15 , "bold") , fg = "#962071" , bg = "#b8b2a6")
        contact.place(x=50 , y = 170)

        self.txt_contact = ttk.Entry(frame , textvariable=self.var_contact ,font = ("times new roman" , 15))
        self.txt_contact.place(x=50 , y = 200 , width = 250)

        email = Label(frame , text = "Email" , font = ("times new roman" , 15 ,"bold") , bg = "#b8b2a6" , fg = "#962071")
        email.place(x = 370 , y = 170)

        self.txt_email = ttk.Entry(frame ,textvariable= self.var_email, font = ("times new roman" , 15))
        self.txt_email.place(x=370 , y = 200 , width = 250)

        #-----------------row3

        security_Q = Label(frame , text = "Select Security Question" , font = ("times new roman" , 15 ,"bold") , bg = "#b8b2a6" , fg = "#962071")
        security_Q.place(x = 50 , y = 240) 

        self.combo_security_Q = ttk.Combobox(frame ,  textvariable= self.var_securityQ, font = ("times new roman", 15 , "bold") , state = "readonly")
        self.combo_security_Q["values"] = ("Select" , "Your Birth Place" , "Your Nick Name" , "Your Pet Name")
        self.combo_security_Q.place(x=50 , y = 270 , width = 250)
        self.combo_security_Q.current(0)

        security_A = Label(frame , text = "Security Answer" , font = ("times new roman" , 15 ,"bold") , bg = "#b8b2a6" , fg = "#962071")
        security_A.place(x = 370 , y = 240)

        self.txt_security = ttk.Entry(frame ,textvariable= self.var_securityA ,font = ("times new roman" , 15))
        self.txt_security.place(x=370 , y = 270 , width = 250)



        # -----------------row4

        pswd= Label(frame , text = "Password" , font = ("times new roman" , 15 ,"bold") , bg = "#b8b2a6" , fg = "#962071")
        pswd.place(x = 50 , y = 310)

        self.txt_pswd = ttk.Entry(frame ,textvariable= self.var_pass , font = ("times new roman" , 15))
        self.txt_pswd.place(x=50 , y = 340 , width = 250)


        confirm_pswd= Label(frame , text = "Confirm Password" , font = ("times new roman" , 15 ,"bold") , bg = "#b8b2a6" , fg = "#962071")
        confirm_pswd.place(x = 370 , y = 310)

        self.txt_confirm_pswd = ttk.Entry(frame ,textvariable= self.var_confpass, font = ("times new roman" , 15))
        self.txt_confirm_pswd.place(x=370 , y = 340 , width = 250)


        # =================check button ==============
        self.var_check = IntVar()
        checkbtn = Checkbutton(frame ,variable=self.var_check, text = "I agree the Terms & Conditions" , font = ("times new roman" , 12 , "bold") ,onvalue=1,offvalue=0, bg = "#b8b2a6" , fg = "#962071" , activeforeground= "white" , activebackground= "#b8b2a6")
        checkbtn.place(x =50 , y = 380)

        # ==========Button ==========

        img = Image.open(r"C:\Users\HP\OneDrive\Desktop\coding\login form\image\registernow.png")
        img = img.resize((200,50) , Image.Resampling.LANCZOS)
        self.photoimage = ImageTk.PhotoImage(img)
        b1 = Button(frame,image = self.photoimage ,command= self.register_data,  borderwidth = 0 , cursor = "hand2" , bg = "#b8b2a6" , activeforeground= "white" , activebackground= "#b8b2a6")
        b1.place(x = 50, y = 420 , width = 200)

        img1 = Image.open(r"C:\Users\HP\OneDrive\Desktop\coding\login form\image\logo2.png")
        img1 = img1.resize((75,75) , Image.Resampling.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        b1 = Button(frame,image = self.photoimage1 , borderwidth = 0 , cursor = "hand2" , bg = "#b8b2a6" , activeforeground= "white" , activebackground= "#b8b2a6")
        b1.place(x = 400, y = 400 , width = 100)


        # =============================function declaration ===============

        
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error", "All fields are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error", "password & confirm password should be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error", "Please agree our terms ane condition")
        else:
            conn = pymysql.connect(host = "localhost" , user="root" , password ="12345678" , database ="my_data")
            my_cursor = conn.cursor()
            query = ("select * from register where email = %s")
            value = (self.var_email.get(),)
            my_cursor.execute(query , value)
            row = my_cursor.fetchone()
            if row != None:
                messagebox.showerror("Error", "User already exits , please try another email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_securityQ.get(),
                                                                                        self.var_securityA.get(),
                                                                                        self.var_pass.get()

                                                                                    ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "succesfully register")
             

        





if __name__ == "__main__":
    main()
    # root = Tk()
    # app = Login_Window(root)
    # root.mainloop()
