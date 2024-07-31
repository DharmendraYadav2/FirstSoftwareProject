import tkinter as tk
import customtkinter as ctk
from PIL import Image,ImageDraw,ImageTk,ImageFont
import pymysql as sql
import mysql.connector as mysql
import re
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import messagebox as m
from tkinter import ttk
from tkcalendar import *
import datetime
import time
from time import *
from datetime import*
import subprocess
import os
import matplotlib.pyplot as plt
from tkinter.ttk import Progressbar
import keyboard
import pywhatkit

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        global customer_en,f5_docs,email_1,medn_h,lic_h
        self.title("Medical Billing Software")
        self.width=self.winfo_screenwidth()
        self.height=self.winfo_screenheight()
        self.geometry(f"{self.width}x{self.height}+0+0")
        self.iconbitmap("38_113706.ico")
        self.withdraw()
        self.load_screen() 
    def load_screen(self):
        self.original_image = Image.open("pharm12-removebg-preview.png")
        self.resized_image = self.original_image.resize((300, 300))
        self.image = ImageTk.PhotoImage(self.resized_image)

        height = 470
        width = 500
        x = (self.winfo_screenwidth()//2) - (width//2)
        y = (self.winfo_screenheight()//2) - (height//2)
        self.root = ctk.CTkToplevel()
        self.root.geometry(f"{width}x{height}+{x}+{y}")
        self.root.overrideredirect(True)
        self.root.config(background="#77E4C8")

        welcome_label = tk.Label(self.root, text="MED CONNECT", bg="#77E4C8", font=("MERRIWEATHER", 25, "bold"), fg="navyblue", relief=tk.GROOVE)
        welcome_label.place(x=150, y=15)

        bg_label = tk.Label(self.root, image=self.image, bg="#77E4C8")
        bg_label.place(x=160, y=70)

        self.progress_label =tk.Label(self.root, text="Loading....", font=("Trebuchet Ms", 15, "bold"), fg="navyblue", bg="#77E4C8")
        self.progress_label.place(x=220, y=380)

        progress_style = ttk.Style()
        progress_style.theme_use("clam")

        progress_style.configure("giphy.webp",
                                    troughcolor='#77E4C8',  
                                    background="navyblue",
                                    lightcolor='navyblue',
                                    darkcolor='navyblue',
                                    thickness=20,
                                    borderwidth=1,
                                    relief='flat')
        self.progress = Progressbar(self.root, orient="horizontal",length=400, mode="determinate", style="red.Horizontal.TProgressbar")
        self.progress.place(x=120, y=420)

        self.i = 0
        self.load()
    def load(self):
        if self.i <= 100:
            txt = "Loading... " + (str(self.i) + "%")
            self.progress_label.config(text=txt)
            self.progress["value"] = self.i
            self.i += 1
            self.progress_label.after(45, self.load)
        else:
            self.root.destroy()
            self.show_main_window()
    def show_main_window(self):
        self.deiconify()  
        self.header()
   
    def header(self):
        f1=tk.Frame(self,width=1905,height=175,relief="ridge",borderwidth=7,border=4,background="#E1F7F5", highlightcolor="navyblue")
        customer_label=ctk.CTkLabel(f1,text="license no:",font=("Cascadia Mono SemiBold",18),text_color="#1C1678")
        customer_label.place(x=520,y=26)
        lic_h=ctk.CTkLabel(f1,text="123456",font=("Cascadia Mono SemiBold",18),text_color="#1C1678")
        lic_h.place(x=650,y=26)
        medn_h=ctk.CTkLabel(f1,text="Health Care Chemist and Druggist ",font=("Cascadia Mono SemiBold",18),text_color="#1C1678")
        medn_h.place(x=270,y=75)
        medical_logo=ctk.CTkImage(light_image=Image.open("pharmacy.png"),dark_image=Image.open("pharmacy.png"),size=(140,130))
        med_label_image1=ctk.CTkLabel(f1,text="",image=medical_logo)
        med_label_image1.place(x=1350,y=3)
        mediine=ctk.CTkImage(light_image=Image.open("home2-removebg-preview.png"),dark_image=Image.open("home2-removebg-preview.png"),size=(200,90))
        med_label_image2=ctk.CTkLabel(f1,text="",image=mediine)
        med_label_image2.place(x=3,y=40)
        mediine1=ctk.CTkImage(light_image=Image.open("home2-removebg-preview222.png"),dark_image=Image.open("home2-removebg-preview222.png"),size=(200,90))
        med_label_image3=ctk.CTkLabel(f1,text="",image=mediine1)
        med_label_image3.place(x=3,y=1)
        logo_nm=ctk.CTkLabel(med_label_image3,text="Med Connect",font=("Cascadia Mono SemiBold",22),text_color="#1C1678")
        logo_nm.place(x=27,y=45)
        customer_en=ctk.CTkLabel(f1,text="",font=("Cascadia Mono SemiBold",18),text_color="#1C1678")
        customer_en.place(x=650,y=26)
        medical_name12=ctk.CTkLabel(f1,text="",font=("Cascadia Mono SemiBold",18),text_color="#1C1678")
        medical_name12.place(x=300,y=90)
        f1.place(x=2,y=3)
        
        def date1():
        
            today_date = datetime.today()
            day = today_date.day
            month = today_date.month
            year = today_date.year
            # day1=datetime.now()
            dayname=today_date.strftime("%A")
            date_label.configure(text = f"{day}/{month}/{year} ({dayname})")
        
        date_label=ctk.CTkLabel(f1,text="date",text_color="#1C1678",fg_color="transparent",bg_color="#E1F7F5",font=("Cascadia Mono SemiBold",17))
        
        
        def time1():
            hours = strftime("%I")  
            minute = strftime("%M")
            second = strftime("%S")
            am_pm = strftime("%p")
            time_label.configure(text = f"{hours}:{minute}:{second} {am_pm}")
            time_label.after(1000,time1)
            
        time_label=ctk.CTkLabel(f1,text="",text_color="#1C1678",fg_color="transparent",bg_color="#E1F7F5",font=("Cascadia Mono SemiBold",17))
        date_label.place(x=250,y=30)
        time_label.place(x=1200,y=100)
        
        search_fr = tk.Frame(self,borderwidth=6, background="#DDDDDD", height=300,width=650,relief="raised")
        hd_frame=tk.Frame(search_fr,width=630,height=38,bg="navyblue")
        header_create=ctk.CTkLabel(hd_frame,text="Login",width=0,font=("'helvetica",26),text_color="white",anchor="center")
        header_create.place(x=210,y=2)
        name_label=ctk.CTkLabel(search_fr,text="Name:",font=("Cascadia Mono SemiBold",25))
        name_en=ctk.CTkEntry(search_fr,width=280,font=("Cascadia",26),height=32,corner_radius=0)  
        pass_label=ctk.CTkLabel(search_fr,text="Password:",font=("Cascadia Mono SemiBold",25))
        pass_en=ctk.CTkEntry(search_fr,width=280,show="*",font=("Cascadia",26),height=32,corner_radius=0)       
          
     
        def login():
               
            name=name_en.get()
            password=pass_en.get()
            if name == "" or password == "":
                m.showerror("Invalid", "Please enter both username and password")
                return
            if name=="Admin" and password=="Admin":
                self.withdraw()
                self.homepage()
            else:
                m.showerror("Invalid", "Incorrect username or password")
        ser_bt=ctk.CTkButton(search_fr,text="Login",width=100,height=34,text_color="navyblue",corner_radius=20,bg_color="#E2DFD0",fg_color="#D8EFD3",border_width=1,hover_color="#FF7D29",command=login)
        ser_bt.place(x=350,y=160)
        name_label.place(x=10,y=60)
        name_en.place(x=140,y=60)
        pass_label.place(x=10,y=100)
        pass_en.place(x=140,y=100)
        hd_frame.place(x=3,y=3)
        search_fr.place(x=590,y=300)
        date1()
        time1()
     
            
    def homepage(self):
        
            
        home=ctk.CTkToplevel(self)
        home.title("MED CONNECT")
        home.width=self.winfo_screenwidth()
        home.height=self.winfo_screenheight()
        home.geometry(f"{self.width}x{self.height}+0+0")
        home.iconbitmap("38_113706.ico")
        home.config(bg="white")
        f1=tk.Frame(home,width=1905,height=175,relief="ridge",borderwidth=7,border=4,background="#E1F7F5", highlightcolor="navyblue")
       
        customer_label=ctk.CTkLabel(f1,text="license no:",font=("Cascadia Mono SemiBold",18),text_color="#1C1678")
        customer_label.place(x=520,y=26)
        
        lic_h=ctk.CTkLabel(f1,text="123456",font=("Cascadia Mono SemiBold",18),text_color="#1C1678")
        lic_h.place(x=650,y=26)
        
        medn_h=ctk.CTkLabel(f1,text="Health Care Chemist and Druggist ",font=("Cascadia Mono SemiBold",18),text_color="#1C1678")
        medn_h.place(x=270,y=75)
        medical_logo=ctk.CTkImage(light_image=Image.open("pharmacy.png"),dark_image=Image.open("pharmacy.png"),size=(140,130))
        med_label_image1=ctk.CTkLabel(f1,text="",image=medical_logo)
        med_label_image1.place(x=1350,y=3)
        mediine=ctk.CTkImage(light_image=Image.open("home2-removebg-preview.png"),dark_image=Image.open("home2-removebg-preview.png"),size=(200,90))
        med_label_image2=ctk.CTkLabel(f1,text="",image=mediine)
        med_label_image2.place(x=3,y=40)
        mediine1=ctk.CTkImage(light_image=Image.open("home2-removebg-preview222.png"),dark_image=Image.open("home2-removebg-preview222.png"),size=(200,90))
        med_label_image3=ctk.CTkLabel(f1,text="",image=mediine1)
        med_label_image3.place(x=3,y=1)
        logo_nm=ctk.CTkLabel(med_label_image3,text="Med Connect",font=("Cascadia Mono SemiBold",22),text_color="#1C1678")
        logo_nm.place(x=27,y=45)
        customer_en=ctk.CTkLabel(f1,text="",font=("Cascadia Mono SemiBold",18),text_color="#1C1678")
        customer_en.place(x=650,y=26)
        medical_name12=ctk.CTkLabel(f1,text="",font=("Cascadia Mono SemiBold",18),text_color="#1C1678")
        medical_name12.place(x=300,y=90)
        f1.place(x=2,y=3)
        
        def date1():
        
            today_date = datetime.today()
            day = today_date.day
            month = today_date.month
            year = today_date.year
            # day1=datetime.now()
            dayname=today_date.strftime("%A")
            date_label.configure(text = f"{day}/{month}/{year} ({dayname})")
        
        date_label=ctk.CTkLabel(home,text="date",text_color="#1C1678",fg_color="transparent",bg_color="#E1F7F5",font=("Cascadia Mono SemiBold",17))
        
        
        def time1():
            hours = strftime("%I")  #I - for 12 hours clock
            minute = strftime("%M")
            second = strftime("%S")
            am_pm = strftime("%p")

            time_label.configure(text = f"{hours}:{minute}:{second} {am_pm}")
            time_label.after(1000,time1)
            
            
            
        time_label=ctk.CTkLabel(home,text="",text_color="#1C1678",fg_color="transparent",bg_color="#E1F7F5",font=("Cascadia Mono SemiBold",17))
       
    
                
        def master_hover(ev):
            heading_.configure(text="Maintain Master Information")
            Master_informat.configure(text="Add,Change or Delete Information regarding Products,Customers etc")
            
           
        def master_leave(self):
            heading_.configure(text="")
            Master_informat.configure(text="")
            
        def Vocher_hover(self):
            heading_.configure(text="Feed-Day-to-Day-Transactions")
            Master_informat.configure(text="Feed all day-to-day transaction like Sale,Purchase etc.")
            
        def Vocher_leave(self):
            heading_.configure(text="")
            Master_informat.configure(text="")
            
        def Display_hover(self):
            heading_.configure(text="Reports")
            Master_informat.configure(text="View various reports on screen.")
        def Display_leave(self):
            heading_.configure(text="")
            Master_informat.configure(text="")
        
        def master_pressed():
            global master_fr1
            def distributor_pressed():
                self.withdraw()
                self.update()
                distributor()
                
            def doctor_pressed():
                self.withdraw()
                self.update()
                Doctor()
            def patient_pressed():
                self.withdraw()
                self.update()
                Patient()
            def product_pressed():
                self.withdraw()
                self.update()
                Product()
                
            def  back_pressed():
               master_fr1.destroy()
               
            master_fr1=ctk.CTkFrame(home,width=500,height=688,border_color="#1C1678",border_width=2,fg_color="#DDDDDD",bg_color="#E2DFD0",corner_radius=4)
            
            
            mastermenu_label=ctk.CTkLabel(master_fr1,text="Master",width=493,height=50,text_color="#1C1678",fg_color="transparent",bg_color="#EEF5FF",font=("Cascadia Mono Bold",44))
           
            
            doctor_button=ctk.CTkButton(master_fr1,border_width=0,text_color="Navy Blue",border_color=None,fg_color="#DDDDDD",width=493,corner_radius=0,bg_color="#DDDDDD",hover_color="#EEF5FF",font=("Cascadia Mono SemiBold",35),text="Doctor",command=doctor_pressed)
            
            
            patient_button=ctk.CTkButton(master_fr1,border_width=0,text_color="Navy Blue",border_color=None,fg_color="#DDDDDD",width=493,corner_radius=0,bg_color="#DDDDDD",hover_color="#EEF5FF",font=("Cascadia Mono SemiBold",35),text="Patient",command=patient_pressed)
        
            distributor_bt=ctk.CTkButton(master_fr1,border_width=0,text_color="Navy Blue",border_color=None,fg_color="#DDDDDD",width=493,corner_radius=0,bg_color="#DDDDDD",hover_color="#EEF5FF",font=("Cascadia Mono SemiBold",35),text="Distributor",command=distributor_pressed)
        
            product_bt=ctk.CTkButton(master_fr1,border_width=0,text_color="Navy Blue",border_color=None,fg_color="#DDDDDD",width=493,corner_radius=0,bg_color="#DDDDDD",hover_color="#EEF5FF",font=("Cascadia Mono SemiBold",35),text="Product",command=product_pressed)
            doctor_button.place(x=2,y=90)
            patient_button.place(x=2,y=150)
            distributor_bt.place(x=2,y=210)
            product_bt.place(x=2,y=270)
            
            back_bt=ctk.CTkButton(master_fr1,text="back",fg_color="navyblue",border_width=1,width=170,height=32,command=back_pressed)
           
            mastermenu_label.place(x=3,y=2)
            back_bt.place(x=300,y=600)
            master_fr1.place(x=1,y=144)
       
        def voucher_pressed():
            def purchase_pressed():
                self.withdraw()
                self.update()
                Purchase()
                
            def sale_1():
                self.withdraw()
                self.update()
                Sale()
            def ordered_pressed():
                self.withdraw()
                self.update()
                Order()
           
                
            def  back_pressed():
                master_fr2.destroy()
               
            master_fr2=ctk.CTkFrame(home,width=500,height=688,border_color="#1C1678",border_width=2,fg_color="#DDDDDD",bg_color="#E2DFD0",corner_radius=4)
            mastermenu_label=ctk.CTkLabel(master_fr2,text="Voucher Entry",width=493,height=50,text_color="#1C1678",fg_color="transparent",bg_color="#EEF5FF",font=("Cascadia Mono Bold",44))
            purchase_button=ctk.CTkButton(master_fr2,border_width=0,text_color="Navy Blue",border_color=None,fg_color="#DDDDDD",width=493,corner_radius=0,bg_color="#DDDDDD",hover_color="#EEF5FF",font=("Cascadia Mono SemiBold",35),text="Purchase",command=purchase_pressed)
            
            
            
            
            sale_button=ctk.CTkButton(master_fr2,border_width=0,text_color="Navy Blue",border_color=None,fg_color="#DDDDDD",width=493,corner_radius=0,bg_color="#DDDDDD",hover_color="#EEF5FF",font=("Cascadia Mono SemiBold",35),text="Sale",command=sale_1)
            
            ordered_button=ctk.CTkButton(master_fr2,border_width=0,text_color="Navy Blue",border_color=None,fg_color="#DDDDDD",width=493,corner_radius=0,bg_color="#DDDDDD",hover_color="#EEF5FF",font=("Cascadia Mono SemiBold",35),text="Order",command=ordered_pressed)
            purchase_button.place(x=2,y=90)
            sale_button.place(x=2,y=150)
            ordered_button.place(x=2,y=210)
            back_bt=ctk.CTkButton(master_fr2,text="back",fg_color="navyblue",border_width=1,width=170,height=32,command=back_pressed)
           
            mastermenu_label.place(x=3,y=2)
            back_bt.place(x=300,y=600)
            master_fr2.place(x=1,y=144)
        
        def display_pressed():
            def product_pressed():
                self.withdraw()
                self.update()
                product_report()
            def sale_rep():
                self.withdraw()
                self.update()
                sale_report()
            def pur_rep():
                self.withdraw()
                self.update()
                Purchase_report()
            
            def back_pressed():
                display_fr.destroy()
               
                
            display_fr=ctk.CTkFrame(home,width=500,height=688,border_color="#1C1678",border_width=2,fg_color="#DDDDDD",bg_color="#E2DFD0",corner_radius=4)
            
            
            displaymenu_label=ctk.CTkLabel(display_fr,text="Display",width=493,height=50,text_color="#1C1678",fg_color="transparent",bg_color="#EEF5FF",font=("Cascadia Mono Bold",44))
            
            product_button=ctk.CTkButton(display_fr,border_width=0,text_color="Navy Blue",border_color=None,fg_color="#DDDDDD",width=493,corner_radius=0,bg_color="#DDDDDD",hover_color="#EEF5FF",font=("Cascadia Mono SemiBold",35),text="Stock Report",command=product_pressed)
            
            sale_button=ctk.CTkButton(display_fr,border_width=0,text_color="Navy Blue",border_color=None,fg_color="#DDDDDD",width=493,corner_radius=0,bg_color="#DDDDDD",hover_color="#EEF5FF",font=("Cascadia Mono SemiBold",35),text="Sale Report",command=sale_rep)
            
            
            purchase_button=ctk.CTkButton(display_fr,border_width=0,text_color="Navy Blue",border_color=None,fg_color="#DDDDDD",width=493,corner_radius=0,bg_color="#DDDDDD",hover_color="#EEF5FF",font=("Cascadia Mono SemiBold",35),text="Purchase Report",command=pur_rep)
            
            back_bt=ctk.CTkButton(display_fr,text="back",fg_color="navyblue",border_width=1,width=170,height=32,command=back_pressed)
            product_button.place(x=2,y=90)
            sale_button.place(x=2,y=150)
            purchase_button.place(x=2,y=210)
            back_bt.place(x=300,y=600)
           
            
           
            displaymenu_label.place(x=3,y=2)
            
            display_fr.place(x=1,y=144)
        def back_to_login():
            self.withdraw()
           
            
           
        menu_fr=ctk.CTkFrame(home,width=500,height=688,border_color="#1C1678",border_width=2,fg_color="#DDDDDD",bg_color="#E2DFD0",corner_radius=4)
        
        
        mainmenu_label=ctk.CTkLabel(menu_fr,text="Main menu",width=493,height=50,text_color="#1C1678",fg_color="transparent",bg_color="#EEF5FF",font=("Cascadia Mono Bold",44))
        
       
        Master_button=ctk.CTkButton(menu_fr,border_width=0,text_color="Navy Blue",border_color=None,fg_color="#DDDDDD",width=493,corner_radius=0,bg_color="#DDDDDD",hover=True,hover_color="#EEF5FF",font=("Cascadia Mono SemiBold", 35),text="Master",command=master_pressed)
       
        Vocher_button=ctk.CTkButton(menu_fr,border_width=0,text_color="Navy Blue",border_color=None,fg_color="#DDDDDD",width=493,corner_radius=0,bg_color="#DDDDDD",hover_color="#EEF5FF",font=("Cascadia Mono SemiBold",35),text="Voucher Entry",command=voucher_pressed)
       
        Display_button=ctk.CTkButton(menu_fr,border_width=0,text_color="Navy Blue",border_color=None,fg_color="#DDDDDD",width=493,corner_radius=0,bg_color="#DDDDDD",hover_color="#EEF5FF",font=("Cascadia Mono SemiBold",35),text="Display",command=display_pressed)
        
        Quit_button=ctk.CTkButton(menu_fr,border_width=0,text_color="Navy Blue",border_color=None,fg_color="#DDDDDD",width=493,corner_radius=0,bg_color="#DDDDDD",hover_color="#EEF5FF",font=("Cascadia Mono SemiBold",35),text="Quit",command=back_to_login)
        separator = ctk.CTkFrame(menu_fr, height=2, width=490, fg_color="Navyblue", bg_color="#DDDDDD")
        separator.place(x=3,y=350)
       
        f1_sale=ctk.CTkLabel(menu_fr,text="F1:Sale",text_color="#1C1678",fg_color="transparent",bg_color="#DDDDDD",font=("Cascadia Mono Bold",23))
        f1_sale.place(x=10,y=355)
        f2_pt=ctk.CTkLabel(menu_fr,text="F2:Patient",text_color="#1C1678",fg_color="transparent",bg_color="#DDDDDD",font=("Cascadia Mono Bold",23))
        f2_pt.place(x=10,y=395)
        
        f3_d=ctk.CTkLabel(menu_fr,text="F3:Doctor",text_color="#1C1678",fg_color="transparent",bg_color="#DDDDDD",font=("Cascadia Mono Bold",23))
        f3_d.place(x=10,y=435)
        
        f3_doct=ctk.CTkLabel(menu_fr,text="F4:Stock",text_color="#1C1678",fg_color="transparent",bg_color="#DDDDDD",font=("Cascadia Mono Bold",23))
        f3_doct.place(x=10,y=475)
        
    
       
        
        M_master=ctk.CTkLabel(menu_fr,text="M:Master",text_color="#1C1678",fg_color="transparent",bg_color="#DDDDDD",font=("Cascadia Mono Bold",23))
        M_master.place(x=320,y=355)
        
        
        V_vouc=ctk.CTkLabel(menu_fr,text="V:Voucher",text_color="#1C1678",fg_color="transparent",bg_color="#DDDDDD",font=("Cascadia Mono Bold",23))
        V_vouc.place(x=320,y=395)
        
        D_dis=ctk.CTkLabel(menu_fr,text="D:Display",text_color="#1C1678",fg_color="transparent",bg_color="#DDDDDD",font=("Cascadia Mono Bold",23))
        D_dis.place(x=320,y=435)
        
        
      
        Master_button.place(x=2,y=90)
        Vocher_button.place(x=2,y=150)
        Display_button.place(x=2,y=210)
        Quit_button.place(x=2,y=270)
        
        

        Master_button.bind("<Enter>",master_hover)
        Master_button.bind("<Leave>", master_leave)
        Vocher_button.bind("<Enter>", Vocher_hover)
        Vocher_button.bind("<Leave>",Vocher_leave)
        Display_button.bind("<Enter>", Display_hover)
        Display_button.bind("<Leave>",Display_leave)
      
        
        keyboard.add_hotkey('m', master_pressed)
        keyboard.add_hotkey('v', voucher_pressed)
        keyboard.add_hotkey('d', display_pressed)

        keyboard.add_hotkey('f1', lambda:Sale())
       
        keyboard.add_hotkey('f2', lambda:Patient())
        keyboard.add_hotkey('f3', lambda:Doctor())
        keyboard.add_hotkey('f4',lambda:product_report())
        
        
        date_label.place(x=250,y=30)
        time_label.place(x=1200,y=100)
        menu_fr.place(x=1,y=144)
        
        mainmenu_label.place(x=3,y=2)
      
        # f1.place(x=2,y=3)
        #----side menu---#
        
        side_frame=menu_fr=ctk.CTkFrame(home,width=1050,height=688,border_color=None,border_width=2,fg_color="white",bg_color="white",corner_radius=0)
         
         
        Master_informat=ctk.CTkLabel(side_frame,font=("Cascadia Mono SemiBold",18),text="")
        
        heading_=ctk.CTkLabel(side_frame,font=("Cascadia Mono SemiBold",35),text="")
        heading_.place(x=20,y=70)
        Master_informat.place(x=20,y=130)
        
        
        side_frame.place(x=501,y=145)
        date_label.place(x=250,y=30)
        time_label.place(x=1200,y=100)
        
        date1()
        time1()
class distributor(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        global time
        global visit_dy_en
        global medical_nmd
        global lic_nmd

        
        self.title("Distributor")
        self.width=self.winfo_screenwidth()
        self.height=self.winfo_screenheight()
        self.geometry(f"{self.width}x{self.height}+0+0")
        self.iconbitmap("38_113706.ico")
        self.grab_set()
        f1=tk.Frame(self,width=1905,height=175,relief="ridge",borderwidth=7,border=4,background="#E1F7F5", highlightcolor="navyblue")
        
        customer_label=ctk.CTkLabel(f1,text="license no:",font=("Cascadia Mono SemiBold",18),text_color="#1C1678")
        customer_label.place(x=520,y=26)
            
        lic_h=ctk.CTkLabel(f1,text="123456",font=("Cascadia Mono SemiBold",18),text_color="#1C1678")
        lic_h.place(x=650,y=26)
            
        medn_h=ctk.CTkLabel(f1,text="Health Care Chemist and Druggist ",font=("Cascadia Mono SemiBold",18),text_color="#1C1678")
        medn_h.place(x=270,y=75)
        
            
                    
                    
        medical_logo=ctk.CTkImage(light_image=Image.open("pharmacy.png"),dark_image=Image.open("pharmacy.png"),size=(140,130))
        
        med_label_image1=ctk.CTkLabel(f1,text="",image=medical_logo)
            
        med_label_image1.place(x=1350,y=3)
            
            
        mediine=ctk.CTkImage(light_image=Image.open("home2-removebg-preview.png"),dark_image=Image.open("home2-removebg-preview.png"),size=(200,90))
            
        med_label_image2=ctk.CTkLabel(f1,text="",image=mediine)
            
        med_label_image2.place(x=3,y=40)
            
            
        mediine1=ctk.CTkImage(light_image=Image.open("home2-removebg-preview222.png"),dark_image=Image.open("home2-removebg-preview222.png"),size=(200,90))
            
        med_label_image3=ctk.CTkLabel(f1,text="",image=mediine1)
            
        med_label_image3.place(x=3,y=1)
            
        logo_nm=ctk.CTkLabel(med_label_image3,text="Med Connect",font=("Cascadia Mono SemiBold",22),text_color="#1C1678")
        logo_nm.place(x=27,y=45)
            
        
            
        customer_en=ctk.CTkLabel(f1,text="",font=("Cascadia Mono SemiBold",18),text_color="#1C1678")
        customer_en.place(x=650,y=26)
            
        medical_name12=ctk.CTkLabel(f1,text="",font=("Cascadia Mono SemiBold",18),text_color="#1C1678")
        medical_name12.place(x=300,y=90)
        f1.place(x=2,y=3)
        
        
        def date1():
        
            today_date = datetime.today()
            day = today_date.day
            month = today_date.month
            year = today_date.year
            # day1=datetime.now()
            dayname=today_date.strftime("%A")
            date_label.configure(text = f"{day}/{month}/{year} ({dayname})")
        
        date_label=ctk.CTkLabel(self,text="date",text_color="#1C1678",fg_color="transparent",bg_color="#E1F7F5",font=("Cascadia Mono SemiBold",17))
        
        def time12():
            self.hours = strftime("%I")  #I - for 12 hours clock
            self.minute = strftime("%M")
            self.second = strftime("%S")
            self.am_pm = strftime("%p")

            time_label.configure(text = f"{self.hours}:{self.minute}:{self.second} {self.am_pm}")
            time_label.after(1000,time12)
       
            
            
        time_label=ctk.CTkLabel(self,text="",text_color="#1C1678",fg_color="transparent",bg_color="#E1F7F5",font=("Cascadia Mono SemiBold",17))
        
        date_label.place(x=250,y=30)
       
        time_label.place(x=1200,y=100)
        
        
        
        date1()
        time12()
        
        
        def calendar(event):
            global visit_dy_en
            global cal
            global nw
            nw=ctk.CTkToplevel()
            nw.geometry("500x300+200+500")
            nw.title("calnder")
            nw.resizable(False,False)
        
            cal=Calendar(nw,selectmode="day",year=2024,month=4,day=23,date_pattern="yyyy-mm-dd",bg="red")
            cal.pack(fill=tk.BOTH,expand=True)
            
            dt_bu=ctk.CTkButton(nw,text="pick date",fg_color="lightblue",text_color="black",border_width=2,border_color="black",width=100,font=("Cascadia",15),hover_color="pink",command=grab_dt).pack(pady=20)
            nw.grab_set()
            
        def grab_dt():
            global visit_dy_en
            global root 
            global nw
            date = cal.get_date()
            val.set("")
            val.set(date)
            nw.destroy()
        def add_1():
           
            
            name=name_en.get()
            addr=addres_en.get()
         
            mob=mobile_en.get()
            cred=credit_en.get()
           
            cont=contact_per_en.get()
          
            visitday=visit_dy_en.get()
            g=gst_dy_en.get()
            email=email_dy_en.get()
            
            conn = mysql.connect(host="localhost", user="root", password="dharm", charset="utf8", database="pharmacy", port=3307)
            cur = conn.cursor()
            
        
                # Insert into supplier table
            ins1 = ("INSERT INTO supplier(name, addr,telephone, credit, contactperson, visitday, gstno, email) "
                        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")
            cur.execute(ins1, (name, addr, mob, cred, cont, visitday, g, email))
            conn.commit()
                
                # Fetch the supplier ID
            cur.execute("SELECT supid FROM supplier WHERE name=%s", (name,))
            s_id = cur.fetchone()
                
            if s_id:
                su_id = s_id[0]
                print(f"Supplier ID: {su_id}")
              

            
                cur.execute("SELECT med_id FROM medicines WHERE company=%s", (name,))
                medid_list = cur.fetchall()
                print(medid_list) 
             
                for medid in medid_list:
                    cur.execute("INSERT INTO medicine_supplier (med_id, supid) VALUES (%s, %s)", (medid[0], su_id))
                conn.commit()
                m.showinfo("Successfully","Your supplier is created")
              
            
          
            conn.close()
            data_query_d()
            clearentry()
        def update_11(e):
            selected = distributor1_tree.focus()
    
    
            name = name_en.get()
            addr = addres_en.get()
           
            mob = mobile_en.get()
            cred = credit_en.get()
         
            cont = contact_per_en.get()
           
            visitday = visit_dy_en.get()
            g = gst_dy_en.get()
            email = email_dy_en.get()

            # Update record in the database
            selected_items = distributor1_tree.selection()
    
            if selected_items:
                # Update each selected row in the database
                conn = mysql.connect(host="localhost", user="root", password="dharm", charset="utf8", database="pharmacy", port=3307)
                cur = conn.cursor()
                
                for item in selected_items:
                    # Get the values from the selected row
                    values = distributor1_tree.item(item, "values")
                    # Extract the srno from the values tuple
                    srno = values[0]
                   
                    cur.execute("UPDATE supplier SET name=%s, addr=%s, telephone=%s, credit=%s, contactperson=%s, visitday=%s, gstno=%s, email=%s WHERE  supid=%s", (name, addr, mob, cred, cont, visitday, g, email, srno))
        
                    conn.commit()
                    conn.close()
                    m.showinfo("Success", "Records updated successfully")

                   
                    data_query_d()
            else:
                m.showinfo("Error", "Please select records to update")
                
    
                   
        def delete_dis(e):
            selected_items = distributor1_tree.selection()
    
            if selected_items:
                
                confirm = m.askyesno("Confirm Deletion", "Are you sure you want to delete the selected records?")
                
                if confirm:
                   
                    conn = mysql.connect(host="localhost", user="root", password="dharm", charset="utf8", database="pharmacy", port=3307)
                    cur = conn.cursor()
                    
                    for item in selected_items:
                        values = distributor1_tree.item(item, "values")
                        srno = values[0]
                        cur.execute("delete from medicine_supplier where supid=%s",(srno,))
                        cur.execute("DELETE FROM supplier WHERE supid=%s", (srno,))
                        distributor1_tree.delete(item)
                        
                    conn.commit()
                    conn.close()
                    
                    m.showinfo("Success", "Selected records deleted successfully")
                    clearentry()
            else:
                m.showinfo("Error", "Please select records to delete")
                
                
                
        
        supplier_fr=tk.Frame(self,height=700,width=700,bd=4,relief="raised",background="#DDDDDD")
      
        
        supplier_create=ctk.CTkLabel(supplier_fr,text="Create(Distributor)",width=550,font=("helvetica",30),text_color="#121481",bg_color="#EEF5FF",fg_color="#EEF7FF",anchor="center")
        supplier_create.place(x=2,y=3)
        
        
        
        
        name_label=ctk.CTkLabel(supplier_fr,text="Company:",font=("'helvetica",25))
        global name_en
        name_en=ctk.CTkEntry(supplier_fr,width=280,height=32,font=("Cascadia",15),corner_radius=0)
        
        
        addres_label=ctk.CTkLabel(supplier_fr,text="Address",font=("'helvetica",25))
        
        addres_en=ctk.CTkEntry(supplier_fr,width=280,height=32,font=("Cascadia",15),corner_radius=0)
       
        
        mobile_label=ctk.CTkLabel(supplier_fr,text="Mobile",font=("'helvetica",24))
        
        mobile_en=ctk.CTkEntry(supplier_fr,width=280,height=32,font=("Cascadia",15),corner_radius=0)
        
        contact_per_label=ctk.CTkLabel(supplier_fr,text="Contact Person",font=("'helvetica",25))
        
        contact_per_en=ctk.CTkEntry(supplier_fr,width=280,height=32,font=("Cascadia",15),corner_radius=0)
        
       
        
        credit_label=ctk.CTkLabel(supplier_fr,text="Credit Period",font=("'helvetica",25))
        
        credit_en=ctk.CTkEntry(supplier_fr,width=280,height=32,font=("Cascadia",15),corner_radius=0)
        
        
       
        
        visit_dy_label=ctk.CTkLabel(supplier_fr,text="Visit Day",font=("helvetica",25))
        
        val=tk.StringVar()
        visit_dy_en=ctk.CTkEntry(supplier_fr,width=280,height=32,font=("Cascadia",15),corner_radius=0,textvariable=val)
        
        visit_dy_en.bind("<Enter>",calendar)
        
        
            
            
            
       
        
        
        
        gst_dy_label=ctk.CTkLabel(supplier_fr,text="GST NO",font=("helvetica",25))
        
        gst_dy_en=ctk.CTkEntry(supplier_fr,width=280,height=32,font=("Cascadia",15),corner_radius=0)
        
        
        email_dy_label=ctk.CTkLabel(supplier_fr,text="Email",font=("helvetica",25))
        
        email_dy_en=ctk.CTkEntry(supplier_fr,width=280,height=32,font=("Cascadia",15),corner_radius=0)
    
       
        #
        

    

        
           

                
        def data_query_d():
            global distributor1_tree
            conn = mysql.connect(host="localhost", user="root", password="dharm", charset="utf8", database="pharmacy", port=3307)

            cur = conn.cursor()
            cur.execute("SELECT *FROM supplier")
            records = cur.fetchall()
            for item in distributor1_tree.get_children():
                distributor1_tree.delete(item)
            for count, record in enumerate(records):
                if count % 2 == 0:
                    distributor1_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3],record[4],record[5],record[6],record[7],record[8]), tags=("evenrow",))
                else:
                     distributor1_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3],record[4],record[5],record[6],record[7],record[8]), tags=("oddrow",))
            conn.commit()
            conn.close()
        def on_entry_change(event):
            
            global distributor1_tree
            global enter_en

            if not enter_en.get():  # Entry field is empty
                data_query_d() 
        def search(event):
            global distributor1_tree
            global enter_en
            
            search_item =enter_en.get()
            for record in distributor1_tree.get_children():
               distributor1_tree.delete(record)
                
            conn = mysql.connect(host="localhost", user="root", password="dharm", charset="utf8", database="pharmacy", port=3307)

            cur = conn.cursor()
            cur.execute("SELECT * FROM supplier where name=%s",(search_item,))
            
            records = cur.fetchall()

            count = 0
            for record in records:
                if count%2 == 0:
                    distributor1_tree.insert(parent = "", index=tk.END, iid = count, values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[7],record[8]), tags=("evenrow",))
                else:
                    distributor1_tree.insert(parent = "", index=tk.END, iid = count, values = (record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[7],record[8]),  tags=("oddrow",)) 

                count += 1
                distributor1_tree.update()

            #commit the changes
            conn.commit()

            #close the connection
            conn.close()
        def clearentry():
            global distributor1_tree
            name_en.delete(0,tk.END)
            addres_en.delete(0,tk.END)
           
            mobile_en.delete(0,tk.END)
            credit_en.delete(0,tk.END)
          
            contact_per_en.delete(0,tk.END)
           
            visit_dy_en.delete(0,tk.END)
            gst_dy_en.delete(0,tk.END)
            email_dy_en.delete(0,tk.END)
            
        def select_rcord(e):
            global distributor1_tree
    
  
            clearentry()
            
            # Get the selected row
            selected = distributor1_tree.focus()
            
            # Get values from the selected row
            values = distributor1_tree.item(selected, 'values')
            
            # Populate entry widgets with the values from the selected row
            name_en.insert(0, values[1])
            addres_en.insert(0, values[2])
          
            mobile_en.insert(0, values[3])
            credit_en.insert(0, values[4]) 
         
            contact_per_en.insert(0, values[5]) 
         
            visit_dy_en.insert(0, values[6])      
            gst_dy_en.insert(0, values[7]) 
            email_dy_en.insert(0, values[8])
        
            
        
                
            
            
       
               
        global distributor1_tree
        global enter_en
        side_fr=tk.Frame(self,height=370,width=1100,relief="raised",borderwidth=5)
        
        header_1=ctk.CTkFrame(side_fr,height=35,width=870,border_width=2,corner_radius=0,bg_color="#EEF5FF",fg_color="#EEF7FF",border_color="navyblue")
        header_1.place(x=0,y=1)
        
        find_h=ctk.CTkLabel(header_1,text="Find(Distributor)",width=0,font=("'helvetica",18),text_color="#121481",anchor="center")
        find_h.place(x=2,y=2)
        side_fr.place(x=800,y=230)         
        style_dr=ttk.Style()
        style_dr.theme_use('default')

        style_dr.configure("Treeview", 
                        background = "#68D2E8",
                        rowheight = 25,
                        foreground="black",
                        fieldbackground = "white", font = ("Consolas", 12))
        style_dr.configure("Treeview",background=[('selected',"#347083")])
        style_dr.configure("Treeview.Heading", background="#CDE8E5",font = ("Consolas", 12))
            # tree_frame=tk.Frame(root,width=100)
            # tree_frame.place(x=10,y=50)
        tree_fr=tk.Frame(side_fr,borderwidth=3,height=260,width=1053)
        tree_fr.pack_propagate(False)
        tree_fr.place(x=10,y=100)
        tree_scroll=tk.Scrollbar(tree_fr)
        tree_scroll.pack(side=tk.RIGHT,fill=tk.Y)
        tree_scrolx=tk.Scrollbar(tree_fr,orient=tk.HORIZONTAL)
        tree_scrolx.pack(side=tk.BOTTOM ,fill=tk.X)
            
        distributor1_tree=ttk.Treeview(tree_fr,yscrollcommand=tree_scroll.set,selectmode="extended",xscrollcommand=tree_scrolx.set)
        distributor1_tree.pack(fill="both",expand=True)
        tree_scroll.config(command=distributor1_tree.yview)
        tree_scrolx.config(command=distributor1_tree.xview)
        enter_nm=ctk.CTkLabel(side_fr,text="Enter Name",font=("helvetica",15))
        distributor1_tree['columns']=('Sr no','Name','addr','telephone','Credit','contactper','visitday','gst','email')
        distributor1_tree.column("#0",width=0,stretch=tk.NO)
        distributor1_tree.column('Sr no',anchor=tk.W,width=80)
        distributor1_tree.column('Name',anchor=tk.W,width=120)
        distributor1_tree.column('addr',anchor=tk.W,width=120)
     
        distributor1_tree.column('telephone',anchor=tk.CENTER,width=120)
        distributor1_tree.column('Credit',anchor=tk.W,width=120)
        distributor1_tree.column('contactper',anchor=tk.W,width=120)
        
        distributor1_tree.column('visitday',anchor=tk.W,width=120)
        distributor1_tree.column('gst',anchor=tk.W,width=120)
        distributor1_tree.column('email',anchor=tk.CENTER,width=120)
            
            
        distributor1_tree.heading("#0",text="",anchor="w")
        distributor1_tree.heading("Sr no",text="Sr no",anchor="w")
        distributor1_tree.heading("Name",text="Company",anchor="w")
        distributor1_tree.heading("addr",text="address",anchor="w")
       
        distributor1_tree.heading("telephone",text="telephone",anchor="w")
        distributor1_tree.heading("Credit",text="Credit",anchor="w",)
      
        distributor1_tree.heading("contactper",text="contactperson",anchor="w")
     
        distributor1_tree.heading("visitday",text="visitday",anchor="w")
        distributor1_tree.heading("gst",text="gstno",anchor="w")
        distributor1_tree.heading("email",text="email",anchor="w")
        distributor1_tree.tag_configure('oddrow',background="white")
        distributor1_tree.tag_configure('evenrow',background="lightblue")
        distributor1_tree.bind("<ButtonRelease-1>",select_rcord)
        
                                     
            
        enter_en=ctk.CTkEntry(side_fr,width=210,height=28,font=("Cascadia",15),)
        search_button = ctk.CTkButton(side_fr, text="Search",width=60,corner_radius=50)
        search_button.bind("<ButtonRelease-1>",search)
        search_button.place(x=320, y=40)
        enter_nm.place(x=4,y=40)
        enter_en.place(x=100,y=40)
        enter_en.bind("<KeyRelease>", on_entry_change)
        data_query_d()
        
        
        
            
            
         
        
        
        
        supplier_save=ctk.CTkButton(supplier_fr,text="Save",width=150,height=34,text_color="navyblue",corner_radius=40,bg_color="#E2DFD0",fg_color="#D6EFD8",border_width=1,hover_color="#E1F7F5",command=add_1)
        
        supplier_edit=ctk.CTkButton(supplier_fr,text="Edit",width=150,height=34,text_color="navyblue",corner_radius=40,bg_color="#E2DFD0",fg_color="#FFD3B6",border_width=1,hover_color="#FF7F3E")
        supplier_edit.bind("<Button-1>",update_11)
        
        supplier_delete=ctk.CTkButton(supplier_fr,text="Delete",width=150,height=34,text_color="navyblue",corner_radius=40,bg_color="#E2DFD0",fg_color="#E2BBE9",border_width=1,hover_color="#FF0000",)
        supplier_delete.bind("<Button-1>",delete_dis)
      
        name_en.place(x=210,y=60)
        name_label.place(x=16,y=60)
        addres_label.place(x=16,y=100)
        addres_en.place(x=210,y=100)
        mobile_label.place(x=16,y=140)
        mobile_en.place(x=210,y=140)
        credit_label.place(x=16,y=180)
        credit_en.place(x=210,y=180)
        contact_per_label.place(x=16,y=220)
        contact_per_en.place(x=210,y=220)
        visit_dy_label.place(x=16,y=260)
        visit_dy_en.place(x=210,y=260)
        gst_dy_label.place(x=16,y=300)
        gst_dy_en.place(x=210,y=300)
        email_dy_label.place(x=16,y=340)
        email_dy_en.place(x=210,y=340)
        
        supplier_save.place(x=20,y=420)
        supplier_edit.place(x=180,y=420)
        supplier_delete.place(x=348,y=420)
        
        supplier_fr.place(x=3,y=180) 
            
       
class Doctor(ctk.CTkToplevel):
     def __init__(self):
        super().__init__()
        self.title("Doctor")
        self.width=self.winfo_screenwidth()
        self.height=self.winfo_screenheight()
        self.geometry(f"{self.width}x{self.height}+0+0")
        self.iconbitmap("38_113706.ico")
        self.grab_set()
        f1=tk.Frame(self,width=1905,height=175,relief="ridge",borderwidth=7,border=4,background="#E1F7F5", highlightcolor="navyblue")
       
        customer_label=ctk.CTkLabel(f1,text="license no:",font=("Cascadia Mono SemiBold",18),text_color="#1C1678")
        customer_label.place(x=520,y=26)
        
        lic_h=ctk.CTkLabel(f1,text="123456",font=("Cascadia Mono SemiBold",18),text_color="#1C1678")
        lic_h.place(x=650,y=26)
        
        medn_h=ctk.CTkLabel(f1,text="Health Care Chemist and Druggist ",font=("Cascadia Mono SemiBold",18),text_color="#1C1678")
        medn_h.place(x=270,y=75)
      
        
                
                
        medical_logo=ctk.CTkImage(light_image=Image.open("pharmacy.png"),dark_image=Image.open("pharmacy.png"),size=(140,130))
        
        med_label_image1=ctk.CTkLabel(f1,text="",image=medical_logo)
        
        med_label_image1.place(x=1350,y=3)
        
        
        mediine=ctk.CTkImage(light_image=Image.open("home2-removebg-preview.png"),dark_image=Image.open("home2-removebg-preview.png"),size=(200,90))
        
        med_label_image2=ctk.CTkLabel(f1,text="",image=mediine)
        
        med_label_image2.place(x=3,y=40)
        
        
        mediine1=ctk.CTkImage(light_image=Image.open("home2-removebg-preview222.png"),dark_image=Image.open("home2-removebg-preview222.png"),size=(200,90))
        
        med_label_image3=ctk.CTkLabel(f1,text="",image=mediine1)
        
        med_label_image3.place(x=3,y=1)
           
        logo_nm=ctk.CTkLabel(med_label_image3,text="Med Connect",font=("Cascadia Mono SemiBold",22),text_color="#1C1678")
        logo_nm.place(x=27,y=45)
        
       
        
        customer_en=ctk.CTkLabel(f1,text="",font=("Cascadia Mono SemiBold",18),text_color="#1C1678")
        customer_en.place(x=650,y=26)
        
        medical_name12=ctk.CTkLabel(f1,text="",font=("Cascadia Mono SemiBold",18),text_color="#1C1678")
        medical_name12.place(x=300,y=90)
        f1.place(x=2,y=3)
        
        supplier_fr=tk.Frame(self,height=600,width=700,bd=4,relief="raised",background="#DDDDDD")
      
        
        
        
        supplier_create=ctk.CTkLabel(supplier_fr,text="Create(Doctor)",width=550,font=("helvetica",30),text_color="#121481",bg_color="#EEF5FF",fg_color="#EEF7FF",anchor="center")
        supplier_create.place(x=2,y=3)
      
        def select_rcord(e):
            global doctor_tree
            clear_doc()
            
            
            selected = doctor_tree.focus()
            
            
            values = doctor_tree.item(selected, 'values')
            
            degree_en.insert(0,values[1])
            speciality_en.insert(0,values[2])
            reg_en.insert(0,values[3])
            clinic_per_en.insert(0,values[4])
            caddr_en.insert(0,values[5])
            phone_en.insert(0,values[6])
           
        def clear_doc():
            degree_en.delete(0,tk.END)
            speciality_en.delete(0,tk.END)
            reg_en.delete(0,tk.END)
            clinic_per_en.delete(0,tk.END)
            caddr_en.delete(0,tk.END)
            phone_en.delete(0,tk.END)
            
        def data_query_doc():
            global doctor_tree
            global doctor_en
            conn = mysql.connect(host="localhost", user="root", password="dharm", charset="utf8", database="pharmacy", port=3307)

            cur = conn.cursor()
            cur.execute("SELECT *FROM doctor")
            records = cur.fetchall()
            for record in doctor_tree.get_children():
                doctor_tree.delete(record)
            for count, record in enumerate(records):
                if count % 2 == 0:
                    doctor_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3],record[4],record[5],record[6]), tags=("evenrow",))
                else:
                     doctor_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3],record[4],record[5],record[6]), tags=("oddrow",))
            conn.commit()
            conn.close()
        def on_entry_change(event):
            
            global doctor_tree_tree
            global doctor_en

            if not doctor_en.get():  
                data_query_doc() 
        def search(event):
               
            global doctor_tree
            global doctor_en
            
            search_item =doctor_en.get()
            for record in doctor_tree.get_children():
                doctor_tree.delete(record)
                
            connd = mysql.connect(host="localhost", user="root", password="dharm", charset="utf8", database="pharmacy", port=3307)

            cur = connd.cursor()
            cur.execute("SELECT * FROM doctor where doctorname=%s",(search_item,))
            
            records = cur.fetchall()

            count = 0
            for record in records:
                if count%2 == 0:
                    doctor_tree.insert(parent = "", index=tk.END,  iid=None, values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6]), tags=("evenrow",))
                else:
                    doctor_tree.insert(parent = "", index=tk.END,  iid=None, values = (record[0],record[1],record[2],record[3],record[4],record[5],record[6]),  tags=("oddrow",)) 

                count += 1

            #commit the changes
            connd.commit()

                
            connd.close()
      
        def doctor_add(event):
            
            doctorname=degree_en.get()
            speciality=speciality_en.get()
            clinic=reg_en.get()
            clinic_name=clinic_per_en.get()
            clinic_addr=caddr_en.get()
            phone1=phone_en.get()
            if doctorname=="" or speciality=="" or clinic=="" or clinic_name=="" or clinic_addr==""or phone1=="":
                m.showerror("Empty Box","One or more box are empty")
            if not doctorname.isalpha():
                m.showerror("Invalid Name", "The Doctor name must contain only alphabetic characters")
                return
            if  speciality.isdigit():
                m.showerror("Invalid Name", "The Doctor Speciality must contain only alphabetic characters ")
                return
            if  not clinic.isdigit():
                m.showerror("Invalid Registration", "The registration contain number only")
                return
            if not clinic_name.isalpha():
                m.showerror("Invalid Name", "The Clinic name must contain only alphabetic characters")
                return
            if not phone1.isdigit():
                  m.showerror("Invalid Contact", "The Contact contain number only")
                  return
                
                
                
            
            conn=mysql.connect(host="localhost",user="root",password="dharm",charset="utf8",database="pharmacy",port=3307)

            cur=conn.cursor() 
            ins1=f"insert into doctor(doctorname,speciality,clinicreg,clinicname,clinicadd,phone) values('{doctorname}','{speciality}','{clinic}','{clinic_name}','{clinic_addr}','{phone1}')"
            cur.execute(ins1)
            m.showinfo("success","succesfully")
            conn.commit()
            conn.close()  
            data_query_doc()
            clear_doc()
        def doctor_edit(event):
            doctorname1 = degree_en.get()
            speciality1 = speciality_en.get()
            clinic1 = reg_en.get()
            clinic_name1 = clinic_per_en.get()
            clinic_addr1 = caddr_en.get()
            phone1 = phone_en.get()
    
            selected_items = doctor_tree.selection()
    
            if selected_items:
                conn = mysql.connect(host="localhost", user="root", password="dharm", charset="utf8", database="pharmacy", port=3307)
                cur = conn.cursor()
                
                for item in selected_items:
                    # Get the values from the selected row
                    values = doctor_tree.item(item, "values")
                    # Extract the srno from the values tuple
                    srno = values[0]

                    cur.execute("UPDATE doctor SET doctorname=%s, speciality=%s,clinicreg=%s, clinicname=%s, clinicadd=%s, phone=%s WHERE d_id=%s",(doctorname1,speciality1,clinic1,clinic_name1,clinic_addr1,phone1,srno))

        
           
              
                    conn.commit()
                    m.showinfo("Success", "Doctor information updated successfully")
                    data_query_doc()
                    conn.close()
                    clear_doc()
        
            else:
              m.showinfo("Error", "Please select records to update")

    # Close database connection
        def doctor_delete(e):
            selected_items = doctor_tree.selection()
    
            if selected_items:
                
                confirm = m.askyesno("Confirm Deletion", "Are you sure you want to delete the selected records?")
                
                if confirm:
                   
                    conn = mysql.connect(host="localhost", user="root", password="dharm", charset="utf8", database="pharmacy", port=3307)
                    cur = conn.cursor()
                    
                    for item in selected_items:
                        values = doctor_tree.item(item, "values")
                        sr_no = values[0]
                        cur.execute("DELETE FROM doctor WHERE srno=%s", (sr_no,))
                        doctor_tree.delete(item)
                        
                    conn.commit()
                    conn.close()
                    
                    m.showinfo("Success", "Selected records deleted successfully")
                    clear_doc()
            else:
                m.showinfo("Error", "Please select records to delete")   
           
           
        global doctor_tree
        global doctor_en   
        side_fr=tk.Frame(self,height=370,width=870,relief="raised",borderwidth=5)
        
        header_1=ctk.CTkFrame(side_fr,height=35,width=680,border_width=2,corner_radius=0,bg_color="#EEF5FF",fg_color="#EEF7FF",border_color="navyblue")
        header_1.place(x=0,y=1)
        
        find_h=ctk.CTkLabel(header_1,text="Find(Doctor)",width=0,font=("'helvetica",18),text_color="#121481",anchor="center")
        find_h.place(x=2,y=2)
        side_fr.place(x=800,y=230)            
        doc_style=ttk.Style()
        doc_style.theme_use('default')

        doc_style.configure("Treeview", 
                        background = "#68D2E8",
                        rowheight = 25,
                        foreground="black",
                        fieldbackground = "white", font = ("Consolas", 12))
        doc_style.configure("Treeview",background=[('selected',"#347083")])
        doc_style.configure("Treeview.Heading", background="#CDE8E5",font = ("Consolas", 12))
            # tree_frame=tk.Frame(root,width=100)
            # tree_frame.place(x=10,y=50)
        tree_fr=tk.Frame(side_fr,borderwidth=3,height=250,width=850)
        tree_fr.pack_propagate(False)
        tree_fr.place(x=10,y=100)
        tree_scroll=tk.Scrollbar(tree_fr)
        tree_scroll.pack(side=tk.RIGHT,fill=tk.Y)
        tree_scrolx=tk.Scrollbar(tree_fr,orient=tk.HORIZONTAL)
        tree_scrolx.pack(side=tk.BOTTOM ,fill=tk.X)
            
        doctor_tree=ttk.Treeview(tree_fr,yscrollcommand=tree_scroll.set,selectmode="extended",xscrollcommand=tree_scrolx.set)
        doctor_tree.pack(fill="both",expand=True)
        tree_scroll.config(command=doctor_tree.yview)
        tree_scrolx.config(command=doctor_tree.xview)
        enter_nm=ctk.CTkLabel(side_fr,text="Enter Name",font=("helvetica",15))
        doctor_tree['columns']=('Sr no','DoctorName','speciality','regclinic','clinicname','clinicaddr','phone')
        doctor_tree.column("#0",width=0,stretch=tk.NO)
        doctor_tree.column('Sr no',anchor=tk.W,width=80)
        doctor_tree.column('DoctorName',anchor=tk.W,width=160)
        doctor_tree.column('speciality',anchor=tk.W,width=120)
        doctor_tree.column('regclinic',anchor=tk.CENTER,width=120)
        doctor_tree.column('clinicname',anchor=tk.CENTER,width=120)
        doctor_tree.column('clinicaddr',anchor=tk.W,width=120)
        doctor_tree.column('phone',anchor=tk.W,width=120)
           
            
            
        doctor_tree.heading("#0",text="",anchor="w")
        doctor_tree.heading("Sr no",text="Sr no",anchor="w")
        doctor_tree.heading("DoctorName",text="DoctorName",anchor="w")
        doctor_tree.heading("speciality",text="Speciality",anchor="w")
           
        doctor_tree.heading("regclinic",text="Regclinic",anchor="w")
        doctor_tree.heading("clinicname",text="Clinicname",anchor="w",)
        doctor_tree.heading("clinicaddr",text="Clinicaddr",anchor="w")
        doctor_tree.heading("phone",text="phone",anchor="w")
           
        doctor_tree.tag_configure('oddrow',background="white")
        doctor_tree.tag_configure('evenrow',background="lightblue")
        doctor_tree.bind("<ButtonRelease-1>",select_rcord)
                                     
            
        doctor_en=ctk.CTkEntry(side_fr,width=210,height=28,font=("Cascadia",15))
        search_button = ctk.CTkButton(side_fr, text="Search",width=60,corner_radius=50,fg_color="#29ADB2",hover_color="#0766AD")
        search_button.bind("<ButtonRelease-1>",search)
       
        search_button.place(x=320, y=40)
        enter_nm.place(x=4,y=40)
        doctor_en.place(x=100,y=40)
        doctor_en.bind("<KeyRelease>",on_entry_change)
        data_query_doc()
            
        
        
        




        
        
        
        degree_label=ctk.CTkLabel(supplier_fr,text="Doctor Name",font=("'helvetica",25))
        
        degree_en=ctk.CTkEntry(supplier_fr,width=280,height=32,font=("Cascadia",15),corner_radius=0)
        
        speciality_label=ctk.CTkLabel(supplier_fr,text="Speciality",font=("'helvetica",24))
        
        speciality_en=ctk.CTkEntry(supplier_fr,width=280,height=32,font=("Cascadia",15),corner_radius=0)
        
        reg_label=ctk.CTkLabel(supplier_fr,text="Reg clinic",font=("'helvetica",24))
        
        reg_en=ctk.CTkEntry(supplier_fr,width=280,height=32,font=("Cascadia",15),corner_radius=0)
        
        clinic_per_label=ctk.CTkLabel(supplier_fr,text="Clinic Name",font=("'helvetica",25))
        
        clinic_per_en=ctk.CTkEntry(supplier_fr,width=280,height=32,font=("Cascadia",15),corner_radius=0)
        
        caddr_label=ctk.CTkLabel(supplier_fr,text="Clinic Address",font=("'helvetica",25))
        
        caddr_en=ctk.CTkEntry(supplier_fr,width=280,height=32,font=("Cascadia",15),corner_radius=0)
        
        phone_label=ctk.CTkLabel(supplier_fr,text="Phone",font=("'helvetica",25))
        
        phone_en=ctk.CTkEntry(supplier_fr,width=280,height=32,font=("Cascadia",15),corner_radius=0)
        
        
       
        product_save=ctk.CTkButton(supplier_fr,text="Save",width=150,height=34,text_color="navyblue",corner_radius=40,bg_color="#E2DFD0",fg_color="#D6EFD8",border_width=1,hover_color="#E1F7F5")
        product_save.bind("<Button-1>",doctor_add)
        product_edit=ctk.CTkButton(supplier_fr,text="Edit",width=150,height=34,text_color="navyblue",corner_radius=40,bg_color="#E2DFD0",fg_color="#FFD3B6",border_width=1,hover_color="#FF7F3E")
        product_edit.bind("<Button-1>",doctor_edit)
        
        product_delete=ctk.CTkButton(supplier_fr,text="Delete",width=150,height=34,text_color="navyblue",corner_radius=40,bg_color="#E2DFD0",fg_color="#E2BBE9",border_width=1,hover_color="#FF0000",)
        product_delete.bind("<Button-1>",doctor_delete)
        
        
        # name_en.place(x=210,y=60)
        # name_label.place(x=16,y=60)
        degree_label.place(x=16,y=50)
        degree_en.place(x=210,y=50)
        speciality_label.place(x=16,y=90)
        speciality_en.place(x=210,y=90)
        reg_label.place(x=16,y=130)
        reg_en.place(x=210,y=130)
        clinic_per_label.place(x=16,y=170)
        clinic_per_en.place(x=210,y=170)
        caddr_label.place(x=16,y=210)
        caddr_en.place(x=210,y=210)
        
        phone_label.place(x=16,y=250)
        phone_en.place(x=210,y=250)
        
        
        
        product_save.place(x=20,y=320)
        product_edit.place(x=180,y=320)
        product_delete.place(x=348,y=320)
        
        
        
        supplier_fr.place(x=3,y=180)
    

        

        
        
        def date1():
        
            today_date = datetime.today()
            day = today_date.day
            month = today_date.month
            year = today_date.year
            # day1=datetime.now()
            dayname=today_date.strftime("%A")
            date_label.configure(text = f"{day}/{month}/{year} ({dayname})")
        
        date_label=ctk.CTkLabel(self,text="date",text_color="#1C1678",fg_color="transparent",bg_color="#E1F7F5",font=("Cascadia Mono SemiBold",17))
        
        def time12():
            self.hours = strftime("%I")  #I - for 12 hours clock
            self.minute = strftime("%M")
            self.second = strftime("%S")
            self.am_pm = strftime("%p")

            time_label.configure(text = f"{self.hours}:{self.minute}:{self.second} {self.am_pm}")
            time_label.after(1000,time12)
            
            
            
        time_label=ctk.CTkLabel(self,text="",text_color="#1C1678",fg_color="transparent",bg_color="#E1F7F5",font=("Cascadia Mono SemiBold",17))
        
        date_label.place(x=250,y=30)
       
        time_label.place(x=1200,y=100)
        
        
        
        date1()
        time12()    
class Patient(ctk.CTkToplevel):
     def __init__(self):
        super().__init__()
        self.title("Patient")
        self.width=self.winfo_screenwidth()
        self.height=self.winfo_screenheight()
        self.geometry(f"{self.width}x{self.height}+0+0")
        self.iconbitmap("38_113706.ico")
        self.grab_set()
        f1=tk.Frame(self,width=1905,height=175,relief="ridge",borderwidth=7,border=4,background="#E1F7F5", highlightcolor="navyblue")
       
        customer_label=ctk.CTkLabel(f1,text="license no:",font=("Cascadia Mono SemiBold",18),text_color="#1C1678")
        customer_label.place(x=520,y=26)
        
        lic_h=ctk.CTkLabel(f1,text="123456",font=("Cascadia Mono SemiBold",18),text_color="#1C1678")
        lic_h.place(x=650,y=26)
        
        medn_h=ctk.CTkLabel(f1,text="Health Care Chemist and Druggist",font=("Cascadia Mono SemiBold",18),text_color="#1C1678")
        medn_h.place(x=270,y=75)
      
        
                
                
        medical_logo=ctk.CTkImage(light_image=Image.open("pharmacy.png"),dark_image=Image.open("pharmacy.png"),size=(140,130))
        
        med_label_image1=ctk.CTkLabel(f1,text="",image=medical_logo)
        
        med_label_image1.place(x=1350,y=3)
        
        
        mediine=ctk.CTkImage(light_image=Image.open("home2-removebg-preview.png"),dark_image=Image.open("home2-removebg-preview.png"),size=(200,90))
        
        med_label_image2=ctk.CTkLabel(f1,text="",image=mediine)
        
        med_label_image2.place(x=3,y=40)
        
        
        mediine1=ctk.CTkImage(light_image=Image.open("home2-removebg-preview222.png"),dark_image=Image.open("home2-removebg-preview222.png"),size=(200,90))
        
        med_label_image3=ctk.CTkLabel(f1,text="",image=mediine1)
        
        med_label_image3.place(x=3,y=1)
           
        logo_nm=ctk.CTkLabel(med_label_image3,text="Med Connect",font=("Cascadia Mono SemiBold",22),text_color="#1C1678")
        logo_nm.place(x=27,y=45)
        
       
        
        customer_en=ctk.CTkLabel(f1,text="",font=("Cascadia Mono SemiBold",18),text_color="#1C1678")
        customer_en.place(x=650,y=26)
        
        medical_name12=ctk.CTkLabel(f1,text="",font=("Cascadia Mono SemiBold",18),text_color="#1C1678")
        medical_name12.place(x=300,y=90)
        f1.place(x=2,y=3)
        
        
        supplier_fr=tk.Frame(self,height=550,width=740,bd=4,relief="raised",background="#DDDDDD")
        
        
        supplier_create=ctk.CTkLabel(supplier_fr,text="Create(Patient)",width=578,font=("helvetica",30),text_color="#121481",bg_color="#EEF5FF",fg_color="#EEF7FF",anchor="center")
        supplier_create.place(x=2,y=3)
       
        def data_query_pat():
            global patient_tree
            conn = mysql.connect(host="localhost", user="root", password="dharm", charset="utf8", database="pharmacy", port=3307)

            cur = conn.cursor()
            cur.execute("SELECT *FROM patient")
            records = cur.fetchall()
            for record in patient_tree.get_children():
               patient_tree.delete(record)
            for count, record in enumerate(records):
                if count % 2 == 0:
                    patient_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3],record[4],record[5]), tags=("evenrow",))
                else:
                     patient_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3],record[4],record[5]), tags=("oddrow",))
            conn.commit()
            conn.close()
        def on_entry_leave(e):
            global patient_tree
            global patient_en

            if not patient_en.get():  # Entry field is empty
                data_query_pat()
            
        def search(e):
            
             
            
            global patient_tree
            global patient_en
            
            search_p =patient_en.get()
            for record in patient_tree.get_children():
               patient_tree.delete(record)
                
            conn = mysql.connect(host="localhost", user="root", password="dharm", charset="utf8", database="pharmacy", port=3307)

            cur = conn.cursor()
            cur.execute("SELECT * FROM patient where phone=%s",(search_p,))
            
            records = cur.fetchall()

            count = 0
            for record in records:
                if count%2 == 0:
                    patient_tree.insert(parent = "", index=tk.END, iid = count, values=(record[0],record[1],record[2],record[3],record[4],record[5]), tags=("evenrow",))
                else:
                    patient_tree.insert(parent = "", index=tk.END, iid = count, values = (record[0],record[1],record[2],record[3],record[4],record[5]),  tags=("oddrow",)) 

                count += 1

            #commit the changes
            conn.commit()
        def clear_pat():
            name_en.delete(0,tk.END)
            
            addres_en.delete(0,tk.END)
            phone_en.delete(0,tk.END)
            var1.set("")
            doctor_per_en.delete(0,tk.END)
         
           
            
        def select_rec_pat(e):
            selected = patient_tree.focus()
            clear_pat()
            # Get values from the selected row
            values =patient_tree.item(selected, 'values')
            
           
            name_en.insert(0, values[1])
            
            addres_en.insert(0,values[2])
            phone_en.insert(0,values[3])
            var1.set(values[4])
            doctor_per_en.insert(0,values[5])
            
          
        def patient_add(event):
            name=name_en.get()
            addr=addres_en.get()
            mob=phone_en.get()
            gen=gen_en.get()
            doc=int(doctor_per_en.get())
           
            if not name.isalpha():
                m.showerror("Invalid Name", "The name must contain only alphabetic characters.")
                return
            if not mob.isdigit():
                m.showerror("Invalid Contact", "The contact number must contain only numeric characters.")
                return
            if not doc:
                m.showerror("Missing Doctor ID", "Please write doctor id.")
                return
           
           
            
           
            
           
            conn=mysql.connect(host="localhost",user="root",password="dharm",charset="utf8",database="pharmacy",port=3307)

            cur=conn.cursor() 
            ins1=f"insert into patient(patientname,address,phone,gender,doc_id) values('{name}','{addr}','{mob}','{gen}','{doc}')"
            cur.execute(ins1)
            m.showinfo("success","succesfully")
            clear_pat()
            conn.commit()
            conn.close() 
            data_query_pat()  
        def patient_edit(e):
            name1=name_en.get()
            addr1=addres_en.get()
            mob1=phone_en.get()
            gen1=gen_en.get()
            doc1=doctor_per_en.get()
            
             
            selected_items = patient_tree.selection()
    
            if selected_items:
                # Update each selected row in the database
                conn = mysql.connect(host="localhost", user="root", password="dharm", charset="utf8", database="pharmacy", port=3307)
                cur = conn.cursor()
                
                for item in selected_items:
                    # Get the values from the selected row
                    values = patient_tree.item(item, "values")
                 
                    sr_no = int(values[0])
                 
                    cur.execute("UPDATE patient SET patientname=%s, address=%s, phone=%s, gender=%s, doc_id=%s WHERE patid=%s", (name1, addr1, mob1, gen1, doc1, sr_no))

                    conn.commit()
                    conn.close()
                    m.showinfo("Success", "Records updated successfully")
                    clear_pat()
                    
                    data_query_pat()
            else:
                m.showinfo("Error", "Please select records to update")
                
            
        def patient_delete(e):
            selected_items = patient_tree.selection()
    
            if selected_items:
                
                confirm = m.askyesno("Confirm Deletion", "Are you sure you want to delete the selected records?")
                
                if confirm:
                   
                    conn = mysql.connect(host="localhost", user="root", password="dharm", charset="utf8", database="pharmacy", port=3307)
                    cur = conn.cursor()
                    
                    for item in selected_items:
                        values = patient_tree.item(item, "values")
                        srno = values[0]
                        cur.execute("DELETE FROM patient WHERE srno=%s", (srno,))
                        patient_tree.delete(item)
                        
                    conn.commit()
                    conn.close()
                    
                    m.showinfo("Success", "Selected records deleted successfully")
                    clear_pat()
            else:
                m.showinfo("Error", "Please select records to delete")
            
       
        global patient_tree
        global patient_en  
    
        side_fr=tk.Frame(self,height=370,width=990,relief="raised",borderwidth=5)
        
        header_1=ctk.CTkFrame(side_fr,height=35,width=780,border_width=2,corner_radius=0,bg_color="#EEF5FF",fg_color="#EEF7FF",border_color="navyblue")
        header_1.place(x=0,y=1)
        
        find_h=ctk.CTkLabel(header_1,text="Find(Patient)",width=0,font=("'helvetica",20),text_color="#121481",anchor="center")
        find_h.place(x=2,y=2)
        side_fr.place(x=800,y=230)         
                
        patient_style=ttk.Style()
        patient_style.theme_use('default')

        patient_style.configure("Treeview", 
                        background = "#68D2E8",
                        rowheight = 25,
                        foreground="black",
                        fieldbackground = "white", font = ("Consolas", 12))
        patient_style.configure("Treeview",background=[('selected',"#347083")])
        patient_style.configure("Treeview.Heading", background="#CDE8E5",font = ("Consolas", 12))
            # tree_frame=tk.Frame(root,width=100)
            # tree_frame.place(x=10,y=50)
        tree_fr=tk.Frame(side_fr,borderwidth=3,height=250,width=970)
        tree_fr.pack_propagate(False)
        tree_fr.place(x=10,y=100)
        tree_scroll=tk.Scrollbar(tree_fr)
        tree_scroll.pack(side=tk.RIGHT,fill=tk.Y)
        tree_scrolx=tk.Scrollbar(tree_fr,orient=tk.HORIZONTAL)
        tree_scrolx.pack(side=tk.BOTTOM ,fill=tk.X)
            
        patient_tree=ttk.Treeview(tree_fr,yscrollcommand=tree_scroll.set,selectmode="extended",xscrollcommand=tree_scrolx.set)
        patient_tree.pack(fill="both",expand=True)
        tree_scroll.config(command=patient_tree.yview)
        tree_scrolx.config(command=patient_tree.xview)
        enter_nm=ctk.CTkLabel(side_fr,text="Enter Name",font=("helvetica",15))
        patient_tree['columns']=('Sr no','PatientName','address','phone','gender','doctorname')
        patient_tree.column("#0",width=0,stretch=tk.NO)
        patient_tree.column('Sr no',anchor=tk.W,width=80)
        patient_tree.column('PatientName',anchor=tk.W,width=160)
        patient_tree.column('address',anchor=tk.W,width=120)
        patient_tree.column('phone',anchor=tk.CENTER,width=120)
        patient_tree.column('gender',anchor=tk.CENTER,width=120)
        patient_tree.column('doctorname',anchor=tk.W,width=120)
       
           
            
            
        patient_tree.heading("#0",text="",anchor="w")
        patient_tree.heading("Sr no",text="Sr no",anchor="w")
        patient_tree.heading("PatientName",text="PatientName",anchor="w")
        patient_tree.heading("address",text="Address",anchor="w")
           
        patient_tree.heading("phone",text="Phone",anchor="w")
        patient_tree.heading("gender",text="Gender",anchor="w",)
        patient_tree.heading("doctorname",text="Doctor id",anchor="w")
       
        patient_tree.tag_configure('oddrow',background="white")
        patient_tree.tag_configure('evenrow',background="lightblue")
        patient_tree.bind("<ButtonRelease-1>",select_rec_pat)
                                     
            
        patient_en=ctk.CTkEntry(side_fr,width=210,height=28)
        patient_en.bind("<KeyRelease>",on_entry_leave)
        search_button = ctk.CTkButton(side_fr, text="Search",width=60,corner_radius=50,fg_color="#29ADB2",hover_color="#0766AD")
        search_button.bind("<ButtonRelease-1>",search)
        search_button.place(x=350, y=40)
        enter_nm.place(x=10,y=40)
        patient_en.place(x=100,y=40)
        data_query_pat()
            
            
        
            
        
        
        name_label=ctk.CTkLabel(supplier_fr,text="Patient Name",font=("'helvetica",25))
        
        name_en=ctk.CTkEntry(supplier_fr,width=280,height=32,font=("Cascadia",15),corner_radius=0)
        
        
        addres_label=ctk.CTkLabel(supplier_fr,text="Address",font=("'helvetica",25))
        
        addres_en=ctk.CTkEntry(supplier_fr,width=280,height=32,font=("Cascadia",15),corner_radius=0)
        
        phone_label=ctk.CTkLabel(supplier_fr,text="Mobile no",font=("'helvetica",24))
        
        phone_en=ctk.CTkEntry(supplier_fr,width=280,height=32,font=("Cascadia",15),corner_radius=0)
        
        gen_label=ctk.CTkLabel(supplier_fr,text="Gender",font=("'helvetica",24))
        values=["Male","Female","others"]
        var1=tk.StringVar()
        var1.set("")
        gen_en=ctk.CTkComboBox(supplier_fr,width=280,height=32,font=("Cascadia",15),corner_radius=0,values=values,variable=var1)
        
        doctor_per_label=ctk.CTkLabel(supplier_fr,text="Doctor Id",font=("'helvetica",25))
        
        doctor_per_en=ctk.CTkEntry(supplier_fr,width=280,height=32,font=("Cascadia",15),corner_radius=0)
        
        product_save=ctk.CTkButton(supplier_fr,text="Save",width=150,height=34,text_color="navyblue",corner_radius=40,bg_color="#E2DFD0",fg_color="#D6EFD8",border_width=1,hover_color="#E1F7F5")
       
        product_edit=ctk.CTkButton(supplier_fr,text="Edit",width=150,height=34,text_color="navyblue",corner_radius=40,bg_color="#E2DFD0",fg_color="#FFD3B6",border_width=1,hover_color="#FF7F3E")
       
        
        product_delete=ctk.CTkButton(supplier_fr,text="Delete",width=150,height=34,text_color="navyblue",corner_radius=40,bg_color="#E2DFD0",fg_color="#E2BBE9",border_width=1,hover_color="#FF0000",)
       
     
        product_save.bind("<Button-1>",patient_add)
       
        product_edit.bind("<Button-1>",patient_edit)
       
        product_delete.bind("<Button-1>",patient_delete)
       
        
        name_en.place(x=210,y=60)
        name_label.place(x=16,y=60)
        addres_label.place(x=16,y=100)
        addres_en.place(x=210,y=100)
        phone_label.place(x=16,y=140)
        phone_en.place(x=210,y=140)
        gen_label.place(x=16,y=180)
        gen_en.place(x=210,y=180)
        doctor_per_label.place(x=16,y=220)
        doctor_per_en.place(x=210,y=220)
       
        
      
       
        
        product_save.place(x=20,y=320)
        product_edit.place(x=180,y=320)
        product_delete.place(x=348,y=320)
        
       
        
        
        supplier_fr.place(x=3,y=180)
    

        

        
        
        def date1():
        
            today_date = datetime.today()
            day = today_date.day
            month = today_date.month
            year = today_date.year
            # day1=datetime.now()
            dayname=today_date.strftime("%A")
            date_label.configure(text = f"{day}/{month}/{year} ({dayname})")
        
        date_label=ctk.CTkLabel(self,text="date",text_color="#1C1678",fg_color="transparent",bg_color="#E1F7F5",font=("Cascadia Mono SemiBold",17))
        
        def time12():
            self.hours = strftime("%I")  #I - for 12 hours clock
            self.minute = strftime("%M")
            self.second = strftime("%S")
            self.am_pm = strftime("%p")

            time_label.configure(text = f"{self.hours}:{self.minute}:{self.second} {self.am_pm}")
            time_label.after(1000,time12)
            
            
            
        time_label=ctk.CTkLabel(self,text="",text_color="#1C1678",fg_color="transparent",bg_color="#E1F7F5",font=("Cascadia Mono SemiBold",17))
        
        date_label.place(x=250,y=30)
       
        time_label.place(x=1200,y=100)
        
        
        
        date1()
        time12()  
class Product(ctk.CTkToplevel):
     def __init__(self):
        super().__init__()
        self.title("Medicine")
        self.width=self.winfo_screenwidth()
        self.height=self.winfo_screenheight()
        self.geometry(f"{self.width}x{self.height}+0+0")
        self.iconbitmap("38_113706.ico")
        
        f1=tk.Frame(self,width=1905,height=175,relief="ridge",borderwidth=7,border=4,background="#E1F7F5", highlightcolor="navyblue")
       
        customer_label=ctk.CTkLabel(f1,text="license no:",font=("Cascadia Mono SemiBold",18),text_color="#1C1678")
        customer_label.place(x=520,y=26)
        
        lic_h=ctk.CTkLabel(f1,text="123456",font=("Cascadia Mono SemiBold",18),text_color="#1C1678")
        lic_h.place(x=650,y=26)
        
        medn_h=ctk.CTkLabel(f1,text="Health Care Chemist and Druggist ",font=("Cascadia Mono SemiBold",18),text_color="#1C1678")
        medn_h.place(x=270,y=75)       
        medical_logo=ctk.CTkImage(light_image=Image.open("pharmacy.png"),dark_image=Image.open("pharmacy.png"),size=(140,130))
        
        med_label_image1=ctk.CTkLabel(f1,text="",image=medical_logo)
        
        med_label_image1.place(x=1350,y=3)
        
        
        mediine=ctk.CTkImage(light_image=Image.open("home2-removebg-preview.png"),dark_image=Image.open("home2-removebg-preview.png"),size=(200,90))
        
        med_label_image2=ctk.CTkLabel(f1,text="",image=mediine)
        
        med_label_image2.place(x=3,y=40)
        
        
        mediine1=ctk.CTkImage(light_image=Image.open("home2-removebg-preview222.png"),dark_image=Image.open("home2-removebg-preview222.png"),size=(200,90))
        
        med_label_image3=ctk.CTkLabel(f1,text="",image=mediine1)
        
        med_label_image3.place(x=3,y=1)
           
        logo_nm=ctk.CTkLabel(med_label_image3,text="Med Connect",font=("Cascadia Mono SemiBold",22),text_color="#1C1678")
        logo_nm.place(x=27,y=45)
        
       
        
        customer_en=ctk.CTkLabel(f1,text="",font=("Cascadia Mono SemiBold",18),text_color="#1C1678")
        customer_en.place(x=650,y=26)
        
        medical_name12=ctk.CTkLabel(f1,text="",font=("Cascadia Mono SemiBold",18),text_color="#1C1678")
        medical_name12.place(x=300,y=90)
        f1.place(x=2,y=3)
        
        
        
        
        #-----database connectivity----#
        def data_query_pr():
            global product_tree
            conn = mysql.connect(host="localhost", user="root", password="dharm", charset="utf8", database="pharmacy", port=3307)

            cur = conn.cursor()
            cur.execute("SELECT *FROM medicines")
            records = cur.fetchall()
            for record in product_tree.get_children():
               product_tree.delete(record)
            for count, record in enumerate(records):
                if count % 2 == 0:
                    product_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3],record[4],record[5],record[6],record[7],record[8],record[9],record[10],record[11],record[12],record[13],record[14],record[15],record[16]), tags=("evenrow",))
                else:
                     product_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3],record[4],record[5],record[6],record[7],record[8],record[9],record[10],record[11],record[12],record[13],record[14],record[15],record[16]), tags=("oddrow",))
            conn.commit()
            conn.close()
        def on_entry_leave(e):
            global pr1_en
            global product_tree
            
            if not pr1_en.get():
                data_query_pr()
        def search_pr(e):
            
             
            
            global product_tree
            global pr1_en
            
            search_item =pr1_en.get()
            for record in product_tree.get_children():
               product_tree.delete(record)
                
            conn = mysql.connect(host="localhost", user="root", password="dharm", charset="utf8", database="pharmacy", port=3307)

            cur = conn.cursor()
            
            cur.execute("SELECT * FROM medicines where company=%s",(search_item,))
            
            
            records = cur.fetchall()
        
            count = 0
            for record in records:
                if count%2 == 0:
                    product_tree.insert(parent = "", index=tk.END, iid = count, values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[7],record[8],record[9],record[10],record[11],record[12],record[13],record[14],record[15],record[16]), tags=("evenrow",))
                else:
                    product_tree.insert(parent = "", index=tk.END, iid = count, values = (record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[7],record[8],record[9],record[10],record[11],record[12],record[13],record[14],record[15],record[16]),  tags=("oddrow",)) 

                count += 1

            conn.commit()
        def clear_pr():
            global addres_en,phone_en,mobile_en,doctor_per_en,dis_en,gst_en,sale_en,mg_en,exp_en,rak_en
            addres_en.delete(0,tk.END)
            phone_en.delete(0,tk.END)
            mobile_en.delete(0,tk.END)
            doctor_per_en.delete(0,tk.END)
            dis_en.delete(0,tk.END) 
            gst_en.delete(0,tk.END)  
            sale_en.delete(0,tk.END) 
            mg_en.delete(0,tk.END)      
            exp_en.delete(0,tk.END)      
            rak_en.delete(0,tk.END) 
            comp_en.delete(0,tk.END)
            v1.set("") 
            v2.set("")
            v3.set("")
            v4.set("") 
            v5.set("") 
        def select_pr_rec(e):
            global product_tree
            global tak_en
    
    
            clear_pr()
            selected=product_tree.focus()
   
    
            values=product_tree.item(selected,'values')
            comp_en.insert(0,values[1])
            addres_en.insert(0,values[2])
            phone_en.insert(0,values[3])
            mobile_en.insert(0,values[4])
            doctor_per_en.insert(0,values[5])
            dis_en.insert(0,values[6]) 
            gst_en.insert(0,values[7])  
            sale_en.insert(0,values[8]) 
            mg_en.insert(0,values[9])      
            exp_en.insert(0,values[10])      
            rak_en.insert(0,values[11]) 
            v1.set(values[12]) 
            v2.set(values[13]) 
            v3.set(values[14]) 
            v4.set(values[15]) 
            v5.set(values[16])
        def pr_save(event):
                self.company1=comp_en.get()
                self.company=addres_en.get()
                self.Name=phone_en.get()
                self.categories=mobile_en.get()
                self.packing=doctor_per_en.get()
                self.stock=dis_en.get()
                self.bill=gst_en.get()
                self.sale=sale_en.get()
                self.mfg=mg_en.get()
                self.exp=exp_en.get()
                self.shell=rak_en.get()
                self.tax=tak_en.get()
                self.hs_n=hs_en.get()
                self.igst=igst_en.get()
                self.sgst=sgst_en.get()
                self.cgst=cgst_en.get()
                
                
                if (self.company =="" or  self.Name=="" or self.categories=="" or  self.packing=="" or  self.stock =="" or
                self.bill =="" or self.sale=="" or  self.mfg=="" or  self.exp ==""or  self.shell=="" or
                self.tax=="" or  self.hs_n ==""or  self.igst=="" or  self.sgst=="" or  self.cgst==""):
                
                    m.showerror("Empty Field", "All fields are required. Please fill in all fields.")
                    return
                if not self.company.isalpha():
                    m.showerror("Invalid", "It must contain only alphabetic characters .")
                    return

                if not self.Name.isalpha():
                    m.showerror("Invalid", "It must contain only alphabetic characters .")
                    return
                if not self.categories.isalpha():
                    m.showerror("Invalid", "It must contain only alphabetic characters .")
                    return
                if not self.bill.isdigit() or not self.sale.isdigit() or not self.stock.isdigit():
                    m.showerror("Invalid", "It should contain only numeric characters.")
                    return
                if self.mfg.strip() == "":
                    m.showerror("Input Error", "Manufacturing date cannot be empty. Please provide a valid date.")
                    return

                if self.exp.strip() == "":
                    m.showerror("Input Error", "Expiration date cannot be empty. Please provide a valid date.")
                    return
                        
                
                self.con=mysql.connect(host="localhost",user="root",password="dharm",charset="utf8",database="pharmacy",port=3307)
                
                
               
                self.ins=f"insert into product(company,brand,drug,categories,packing,stock,Billrate,salerate,mfg,exp,shell,tax_category,hsncategory,igst,cgst,sgst) values('{self.company1}'.'{self.company}','{self.Name}','{self.categories}','{self.packing}','{self.stock}','{self.bill}','{self.sale}','{self.mfg}','{self.exp}','{self.shell}','{self.tax}','{self.hs_n}','{self.igst}','{self.sgst}','{self.cgst}')"
                self.cur=self.con.cursor()
                self.cur.execute(self.ins)
                self.con.commit()
                m.showinfo("Success","Sucessfully Save")
                data_query_pr()      
                self.con.close()
        def update_product(e):
            global product_tree
            selected = product_tree.focus()
            company1=comp_en.get()
            company = addres_en.get()
            Name = phone_en.get()
            categories = mobile_en.get()
            packing = doctor_per_en.get()
            stock = dis_en.get()
            bill = gst_en.get()
            sale = sale_en.get()
            mfg = mg_en.get()
            exp = exp_en.get()
            shell = rak_en.get()
            tax = tak_en.get()
            hs_n = hs_en.get()
            igst = igst_en.get()
            sgst = sgst_en.get()
            cgst = cgst_en.get()    
            selected_items=product_tree.selection()
            if selected_items:
                # Update each selected row in the database
                conn = mysql.connect(host="localhost", user="root", password="dharm", charset="utf8", database="pharmacy", port=3307)
                cur = conn.cursor()
                
                for item in selected_items:
                    #
                    values = product_tree.item(item, "values")
                
                    srno = values[0]
                    # Update the record in the database
                    cur.execute("UPDATE medicines SET  company=%s,brand=%s, drug=%s,  categories=%s, packing=%s,  stock=%s, Billrate=%s,  salerate=%s,  mfg=%s, exp=%s, shell=%s, tax_category=%s,hsncategory=%s,igst=%s ,cgst=%s ,sgst=%s WHERE med_id=%s",(company1,company,Name,categories,packing,stock,bill,sale,mfg,exp,shell,tax,hs_n,igst,sgst,cgst, srno))
        
                    conn.commit()
                    conn.close()
                    m.showinfo("Success", "Records updated successfully")
                    data_query_pr()
                    clear_pr()
            else:
                m.showinfo("Error", "Please select records to update")
                clear_pr()
        def delete_product(e):
            selected_items = product_tree.selection()
    
            if selected_items:
                
                confirm = m.askyesno("Confirm Deletion", "Are you sure you want to delete the selected records?")
                
                if confirm:
                   
                    conn = mysql.connect(host="localhost", user="root", password="dharm", charset="utf8", database="pharmacy", port=3307)
                    cur = conn.cursor()
                    
                    for item in selected_items:
                        values = product_tree.item(item, "values")
                        med_id = values[0]
                        cur.execute("DELETE FROM product WHERE sr_no=%s", (med_id,))
                        product_tree.delete(item)
                        
                    conn.commit()
                    conn.close()
                    
                    m.showinfo("Success", "Selected records deleted successfully")
                    clear_pr() 
            else:
                m.showinfo("Error", "Please select records to delete")
                
                

                
       
        global product_tree  
        global pr1_en
        side_fr=tk.Frame(self,height=390,width=870,relief="raised",borderwidth=5)
        
        header_1=ctk.CTkFrame(side_fr,height=35,width=690,border_width=2,corner_radius=0,bg_color="#EEF5FF",fg_color="#EEF7FF",border_color="navyblue")
        header_1.place(x=0,y=1)
        
        find_h=ctk.CTkLabel(header_1,text="Find(Product)",width=0,font=("'helvetica",18),text_color="#121481",anchor="center")
        find_h.place(x=2,y=2)
        side_fr.place(x=870,y=230)               
        product_style=ttk.Style()
        product_style.theme_use('default')

        product_style.configure("Treeview", 
                        background = "#68D2E8",
                        rowheight = 25,
                        foreground="black",
                        fieldbackground = "white", font = ("Consolas", 12))
        product_style.configure("Treeview",background=[('selected',"#347083")])
        product_style.configure("Treeview.Heading", background="#CDE8E5",font = ("Consolas", 12))
            # tree_frame=tk.Frame(root,width=100)
            # tree_frame.place(x=10,y=50)
        tree_fr=tk.Frame(side_fr,borderwidth=3,height=280,width=835)
        tree_fr.pack_propagate(False)
        tree_fr.place(x=10,y=100)
        tree_scroll=tk.Scrollbar(tree_fr)
        tree_scroll.pack(side=tk.RIGHT,fill=tk.Y)
        tree_scrolx=tk.Scrollbar(tree_fr,orient=tk.HORIZONTAL)
        tree_scrolx.pack(side=tk.BOTTOM ,fill=tk.X)
            
        product_tree=ttk.Treeview(tree_fr,yscrollcommand=tree_scroll.set,selectmode="extended",xscrollcommand=tree_scrolx.set)
        product_tree.pack(fill="both",expand=True)
        tree_scroll.config(command=product_tree.yview)
        tree_scrolx.config(command=product_tree.xview)
        enter_nm=ctk.CTkLabel(side_fr,text="Enter Name",font=("helvetica",15))
        product_tree['columns']=('Sr no','company','brand','Drug','categories','packing','stock','billrate','salerate','mfg','exp','shell','taxcategory','hsncategory','igst','cgst','sgst')
        product_tree.column("#0",width=0,stretch=tk.NO)
        product_tree.column('Sr no',anchor=tk.W,width=80)
        product_tree.column('company',anchor=tk.W,width=170)
        product_tree.column('brand',anchor=tk.W,width=100)
        product_tree.column('Drug',anchor=tk.W,width=120)
        product_tree.column('packing',anchor=tk.CENTER,width=120)
        product_tree.column('stock',anchor=tk.W,width=120)
        product_tree.column('billrate',anchor=tk.W,width=120)
        product_tree.column('salerate',anchor=tk.W,width=120)
        product_tree.column('mfg',anchor=tk.W,width=140)
        product_tree.column('exp',anchor=tk.W,width=140)
        product_tree.column('shell',anchor=tk.W,width=120)
        product_tree.column('taxcategory',anchor=tk.W,width=150)
        product_tree.column('hsncategory',anchor=tk.W,width=150)
        product_tree.column('igst',anchor=tk.W,width=120)
        product_tree.column('cgst',anchor=tk.W,width=120)
        product_tree.column('sgst',anchor=tk.W,width=120)
           
            
            
        product_tree.heading("#0",text="",anchor="w")
        product_tree.heading("Sr no",text="Sr no",anchor="w")
        product_tree.heading("company",text="Company",anchor="w")
        product_tree.heading("brand",text="Brand",anchor="w")
        product_tree.heading("Drug",text="Drug",anchor="w")
           
        product_tree.heading("categories",text="Categories",anchor="w")
        product_tree.heading("packing",text="Packing",anchor="w",)
        product_tree.heading("stock",text="Stock",anchor="w")
        product_tree.heading("billrate",text="Billrate",anchor="w")
        product_tree.heading("salerate",text="Salerate",anchor="w")
        product_tree.heading("mfg",text="Mfg",anchor="w")
        product_tree.heading("exp",text="Exp",anchor="w")
        product_tree.heading("shell",text="Shell",anchor="w")
        product_tree.heading("taxcategory",text="Taxcategory",anchor="w")
        product_tree.heading("hsncategory",text="Hsncategory",anchor="w")
        product_tree.heading("igst",text="igst",anchor="w")
        product_tree.heading("cgst",text="cgst",anchor="w")
        product_tree.heading("sgst",text="sgst",anchor="w")
           
        product_tree.tag_configure('oddrow',background="white")
        product_tree.tag_configure('evenrow',background="lightblue")
        product_tree.bind("<ButtonRelease-1>",select_pr_rec)
                                     
            
        pr1_en=ctk.CTkEntry(side_fr,width=210,height=28,font=("Cascadia",15),)
        search_button = ctk.CTkButton(side_fr, text="Search",width=60,corner_radius=50,fg_color="#29ADB2",hover_color="#0766AD")
        search_button.bind("<ButtonRelease-1>",search_pr)
        search_button.place(x=320, y=40)
        enter_nm.place(x=10,y=40)
        pr1_en.place(x=100,y=40)
        pr1_en.bind("<KeyRelease>",on_entry_leave)
        data_query_pr()
           
           
       
                
               
            
              
        
        
                
            
            
        
        global addres_en,phone_en,mobile_en,doctor_per_en,dis_en,gst_en,sale_en,mg_en,exp_en,rak_en
        supplier_fr=tk.Frame(self,height=840,width=820,bd=4,relief="raised",background="#DDDDDD")
        
        
        supplier_create=ctk.CTkLabel(supplier_fr,text="Add New Product",width=640,font=("helvetica",30),text_color="#121481",bg_color="#EEF5FF",fg_color="#EEF7FF",anchor="center")
        supplier_create.place(x=2,y=3)
        
        
        addres_label=ctk.CTkLabel(supplier_fr,text="Brand",font=("'helvetica",25))
        
        addres_en=ctk.CTkEntry(supplier_fr,width=280,height=32,font=("Cascadia",15),corner_radius=0)
        
        comp_label=ctk.CTkLabel(supplier_fr,text="Company",font=("'helvetica",25))
        
        comp_en=ctk.CTkEntry(supplier_fr,width=280,height=32,font=("Cascadia",15),corner_radius=0)
        
        
        phone_label=ctk.CTkLabel(supplier_fr,text="Drug",font=("'helvetica",24))
        
        phone_en=ctk.CTkEntry(supplier_fr,width=280,height=32,font=("Cascadia",15),corner_radius=0)
        
        mobile_label=ctk.CTkLabel(supplier_fr,text="Categories",font=("'helvetica",24))
        
        mobile_en=ctk.CTkEntry(supplier_fr,width=280,height=32,font=("Cascadia",15),corner_radius=0)
        
        doctor_per_label=ctk.CTkLabel(supplier_fr,text="Packing",font=("'helvetica",25))
        
        doctor_per_en=ctk.CTkEntry(supplier_fr,width=280,height=32,font=("Cascadia",15),corner_radius=0)
        
        dis_label=ctk.CTkLabel(supplier_fr,text="Stock",font=("'helvetica",25))
        
        dis_en=ctk.CTkEntry(supplier_fr,width=280,height=32,font=("Cascadia",15),corner_radius=0)
        
        gst_label=ctk.CTkLabel(supplier_fr,text="Bill Rate",font=("'helvetica",25))
        
        gst_en=ctk.CTkEntry(supplier_fr,width=280,height=32,font=("Cascadia",15),corner_radius=0)
        
        sale_label=ctk.CTkLabel(supplier_fr,text="Sale Rate",font=("'helvetica",25))
        
        sale_en=ctk.CTkEntry(supplier_fr,width=280,height=32,font=("Cascadia",15),corner_radius=0)
        
        
        mg_label=ctk.CTkLabel(supplier_fr,text="Mfg Dt",font=("'helvetica",25))
        
        mg_en=ctk.CTkEntry(supplier_fr,width=280,height=32,font=("Cascadia",15),corner_radius=0)
        
        exp_label=ctk.CTkLabel(supplier_fr,text="Exp Dt",font=("'helvetica",25))
        
        exp_en=ctk.CTkEntry(supplier_fr,width=280,height=32,font=("Cascadia",15),corner_radius=0)
        
        rak_label=ctk.CTkLabel(supplier_fr,text="Shell",font=("'helvetica",25))
        
        rak_en=ctk.CTkEntry(supplier_fr,width=280,height=32,font=("Cascadia",15),corner_radius=0)
        
        values=["8% GST","12% GST","28% GST","5% GST"]
        v1=tk.StringVar()
        v1.set("")
        tak_label=ctk.CTkLabel(supplier_fr,text="Tax Category",font=("'helvetica",25))
        
        tak_en=ctk.CTkComboBox(supplier_fr,width=100,height=32,font=("Cascadia",15),corner_radius=0,values=values,variable=v1)
        
        data=["2160","3004","3006","3304"]
        hs_label=ctk.CTkLabel(supplier_fr,text="HSN Category",font=("'helvetica",25))
        v2=tk.IntVar()
        v2.set("")
        hs_en=ctk.CTkComboBox(supplier_fr,width=100,height=32,font=("Cascadia",15),corner_radius=0,values=data,variable=v2)
        
        
        igst_label=ctk.CTkLabel(supplier_fr,text="IGST%",font=("'helvetica",25))
        data12=["5","12","18","28"]
        
        v3=tk.IntVar()
        v3.set("")
        igst_en=ctk.CTkComboBox(supplier_fr,width=100,height=32,font=("Cascadia",15),corner_radius=0,values=data12,variable=v3)
        
        cgst_label=ctk.CTkLabel(supplier_fr,text="CGST%",font=("'helvetica",25))
        data13=["2.5","6","9","14"]
        
        v4=tk.IntVar()
        v4.set("")
        cgst_en=ctk.CTkComboBox(supplier_fr,width=100,height=32,font=("Cascadia",15),corner_radius=0,values=data13,variable=v4)
        
        sgst_label=ctk.CTkLabel(supplier_fr,text="SGST%",font=("'helvetica",25))
        data133=["2.5","6","9","14"]
        
        v5=tk.IntVar()
        v5.set("")
        sgst_en=ctk.CTkComboBox(supplier_fr,width=100,height=32,font=("Cascadia",15),corner_radius=0,values=data133,variable=v5)
        
        
        
        
        
        product_save=ctk.CTkButton(supplier_fr,text="Save",width=250,height=34,text_color="navyblue",corner_radius=40,bg_color="#E2DFD0",fg_color="#D6EFD8",border_width=1,hover_color="#E1F7F5")
        
        product_edit=ctk.CTkButton(supplier_fr,text="Edit",width=120,height=34,text_color="navyblue",corner_radius=40,bg_color="#E2DFD0",fg_color="#FFD3B6",border_width=1,hover_color="#FF7F3E")
        
        
        product_delete=ctk.CTkButton(supplier_fr,text="Delete",width=120,height=34,text_color="navyblue",corner_radius=40,bg_color="#E2DFD0",fg_color="#E2BBE9",border_width=1,hover_color="#FF0000",)
      
        product_delete.bind("<Button-1>",delete_product)
       
        product_edit.bind("<Button-1>",update_product)
        product_save.bind("<Button-1>",pr_save)
        
        
        
        
        
       
        comp_label.place(x=16,y=60)
        comp_en.place(x=210,y=60)
        addres_label.place(x=16,y=100)
        addres_en.place(x=210,y=100)
        phone_label.place(x=16,y=140)
        phone_en.place(x=210,y=140)
        mobile_label.place(x=16,y=180)
        mobile_en.place(x=210,y=180)
        doctor_per_label.place(x=16,y=220)
        doctor_per_en.place(x=210,y=220)
        dis_label.place(x=16,y=260)
        dis_en.place(x=210,y=260)
        
        gst_label.place(x=16,y=300)
        gst_en.place(x=210,y=300)
        sale_label.place(x=16,y=340)
        sale_en.place(x=210,y=340)
        mg_label.place(x=16,y=380)
        mg_en.place(x=210,y=380)
        exp_label.place(x=16,y=420)
        exp_en.place(x=210,y=420)
        rak_label.place(x=16,y=460)
        rak_en.place(x=210,y=460)
        tak_label.place(x=16,y=500)
        tak_en.place(x=210,y=500)
        hs_label.place(x=380,y=500)
        hs_en.place(x=550,y=500)
        
        igst_label.place(x=16,y=540)
        igst_en.place(x=210,y=540)
        cgst_label.place(x=16,y=580)
        cgst_en.place(x=210,y=580)
        sgst_label.place(x=16,y=620)
        sgst_en.place(x=210,y=620)
       
        
        product_save.place(x=360,y=600)
        product_edit.place(x=360,y=560)
        product_delete.place(x=489,y=560)
        
        
        
        supplier_fr.place(x=3,y=180)
    

        

        
        
        def date1():
        
            today_date = datetime.today()
            day = today_date.day
            month = today_date.month
            year = today_date.year
            # day1=datetime.now()
            dayname=today_date.strftime("%A")
            date_label.configure(text = f"{day}/{month}/{year} ({dayname})")
        
        date_label=ctk.CTkLabel(self,text="date",text_color="#1C1678",fg_color="transparent",bg_color="#E1F7F5",font=("Cascadia Mono SemiBold",17))
        
        def time12():
            self.hours = strftime("%I")  #I - for 12 hours clock
            self.minute = strftime("%M")
            self.second = strftime("%S")
            self.am_pm = strftime("%p")

            time_label.configure(text = f"{self.hours}:{self.minute}:{self.second} {self.am_pm}")
            time_label.after(1000,time12)
            
            
            
        time_label=ctk.CTkLabel(self,text="",text_color="#1C1678",fg_color="transparent",bg_color="#E1F7F5",font=("Cascadia Mono SemiBold",17))
        
        date_label.place(x=250,y=30)
       
        time_label.place(x=1200,y=100)
        
        
        
        date1()
        time12()
     
        
        
         
        self.grab_set()
class Sale(ctk.CTkToplevel):
     def __init__(self):
        super().__init__()
        global time
        global counter,product_tree
        self.title("Sale")
        self.width=self.winfo_screenwidth()
        self.height=self.winfo_screenheight()
        self.geometry(f"{self.width}x{self.height}+0+0")
        self.iconbitmap("38_113706.ico")
        self.grab_set()
        item_selected=[]
        
   
        
        def data_querypat():
            global patient_tree
            conn = mysql.connect(host="localhost", user="root", password="dharm", charset="utf8", database="pharmacy", port=3307)

            cur = conn.cursor()
            cur.execute("SELECT *FROM patient")
            records = cur.fetchall()
            for record in patient_tree.get_children():
               patient_tree.delete(record)
            for count, record in enumerate(records):
                if count % 2 == 0:
                    patient_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3],record[4],record[5]), tags=("evenrow",))
                else:
                     patient_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3],record[4],record[5]), tags=("oddrow",))
            conn.commit()
            conn.close()
        def on_entry_leave(e):
            global patient_tree
            global patient_en
            global patient_en

            if not patient_en.get():  # Entry field is empty
                data_querypat()
            
        def search(e):
            
             
            
            global patient_tree
            global patient_en
            global patient_en1
            
            search_item =patient_en.get()
            for record in patient_tree.get_children():
               patient_tree.delete(record)
                
            conn = mysql.connect(host="localhost", user="root", password="dharm", charset="utf8", database="pharmacy", port=3307)

            cur = conn.cursor()
            cur.execute("SELECT * FROM patient where phone=%s",(search_item,))
            
            records = cur.fetchall()

            count = 0
            for record in records:
                if count%2 == 0:
                    patient_tree.insert(parent = "", index=tk.END, iid = count, values=(record[0],record[1],record[2],record[3],record[4],record[5]), tags=("evenrow",))
                else:
                    patient_tree.insert(parent = "", index=tk.END, iid = count, values = (record[0],record[1],record[2],record[3],record[4],record[5]),  tags=("oddrow",)) 

                count += 1

            #commit the changes
            conn.commit()
        def select_patient(e):
            global patient_en1

            selected_item = patient_tree.focus()

            values = patient_tree.item(selected_item, 'values')
            if values:
                patient_en1.delete(0, tk.END)  
                patient_en1.insert(0, values[1])
                patient_id.delete(0, tk.END)  
                patient_id.insert(0, values[0])
                
                patient_no.delete(0, tk.END)  
                patient_no.insert(0, values[3])
                # patient_id.configure(state="disabled")
                
                
        def data_query():
            global doctor_tree
            global doctor_en
            conn = mysql.connect(host="localhost", user="root", password="dharm", charset="utf8", database="pharmacy", port=3307)

            cur = conn.cursor()
            cur.execute("SELECT *FROM doctor")
            records = cur.fetchall()
            for record in doctor_tree.get_children():
                doctor_tree.delete(record)
            for count, record in enumerate(records):
                if count % 2 == 0:
                    doctor_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3],record[4],record[5],record[6]), tags=("evenrow",))
                else:
                     doctor_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3],record[4],record[5],record[6]), tags=("oddrow",))
            conn.commit()
            conn.close()
        def on_entry_change(event):
            
            global doctor_tree_tree
            global doctor_en

            if not doctor_en.get():  # Entry field is empty
                data_query() 
        def search_doc(event):
               
            global doctor_tree
            global doctor_en
            
            search_item =doctor_en.get()
            for record in doctor_tree.get_children():
                doctor_tree.delete(record)
                
            conn = mysql.connect(host="localhost", user="root", password="dharm", charset="utf8", database="pharmacy", port=3307)

            cur = conn.cursor()
            cur.execute("SELECT * FROM doctor where doctorname=%s",(search_item,))
            
            records = cur.fetchall()

            count = 0
            for record in records:
                if count%2 == 0:
                        doctor_tree.insert(parent = "", index=tk.END, iid = count, values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6]), tags=("evenrow",))
                else:
                    doctor_tree.insert(parent = "", index=tk.END, iid = count, values = (record[0],record[1],record[2],record[3],record[4],record[5],record[6]),  tags=("oddrow",)) 

                count += 1

            #commit the changes
            conn.commit()

            #close the connection
            conn.close()
        def select_doctor(e):
            global doctor_place

            selected_item = doctor_tree.focus()

            values = doctor_tree.item(selected_item, 'values')
            if values:
               doctor_place.delete(0, tk.END)  
               doctor_place.insert(0, values[1])
        def doctor_name(event):
            global doctor_tree
            global doctor_en
            global doctor_place           
            root=ctk.CTkToplevel()
            root.geometry("420x230+900+80")
            #root.resizable(False,False)
            
                
            doc_style=ttk.Style()
            doc_style.theme_use('default')

            doc_style.configure("Treeview", 
                        background = "#68D2E8",
                        rowheight = 25,
                        foreground="black",
                        fieldbackground = "white", font = ("Consolas", 12))
            doc_style.configure("Treeview",background=[('selected',"#347083")])
            doc_style.configure("Treeview.Heading", background="#CDE8E5",font = ("Consolas", 12))
            # tree_frame=tk.Frame(root,width=100)
            # tree_frame.place(x=10,y=50)
            tree_fr=tk.Frame(root,borderwidth=3,height=200,width=500)
            tree_fr.pack_propagate(False)
            tree_fr.place(x=10,y=50)
            tree_scroll=tk.Scrollbar(tree_fr)
            tree_scroll.pack(side=tk.RIGHT,fill=tk.Y)
            tree_scrolx=tk.Scrollbar(tree_fr,orient=tk.HORIZONTAL)
            tree_scrolx.pack(side=tk.BOTTOM ,fill=tk.X)
            
            doctor_tree=ttk.Treeview(tree_fr,yscrollcommand=tree_scroll.set,selectmode="extended",xscrollcommand=tree_scrolx.set)
            doctor_tree.pack(fill="both",expand=True)
            tree_scroll.config(command=doctor_tree.yview)
            tree_scrolx.config(command=doctor_tree.xview)
            enter_nm=ctk.CTkLabel(root,text="Enter Name",font=("helvetica",15))
            doctor_tree['columns']=('Sr no','DoctorName','speciality','regclinic','clinicname','clinicaddr','phone')
            doctor_tree.column("#0",width=0,stretch=tk.NO)
            doctor_tree.column('Sr no',anchor=tk.W,width=80)
            doctor_tree.column('DoctorName',anchor=tk.W,width=160)
            doctor_tree.column('speciality',anchor=tk.W,width=120)
            doctor_tree.column('regclinic',anchor=tk.CENTER,width=120)
            doctor_tree.column('clinicname',anchor=tk.CENTER,width=120)
            doctor_tree.column('clinicaddr',anchor=tk.W,width=120)
            doctor_tree.column('phone',anchor=tk.W,width=120)
           
            
            
            doctor_tree.heading("#0",text="",anchor="w")
            doctor_tree.heading("Sr no",text="Sr no",anchor="w")
            doctor_tree.heading("DoctorName",text="DoctorName",anchor="w")
            doctor_tree.heading("speciality",text="Speciality",anchor="w")
           
            doctor_tree.heading("regclinic",text="Regclinic",anchor="w")
            doctor_tree.heading("clinicname",text="Clinicname",anchor="w",)
            doctor_tree.heading("clinicaddr",text="Clinicaddr",anchor="w")
            doctor_tree.heading("phone",text="phone",anchor="w")
           
            doctor_tree.tag_configure('oddrow',background="white")
            doctor_tree.tag_configure('evenrow',background="lightblue")
            doctor_tree.bind("<ButtonRelease-1>", select_doctor)
                                     
            doctor_var1=tk.StringVar()
            doctor_en=ctk.CTkEntry(root,width=210,height=28,font=("Cascadia",12),textvariable=doctor_var1)
            search_button = ctk.CTkButton(root, text="Search",width=60,corner_radius=50,fg_color="#29ADB2",hover_color="#0766AD")
            search_button.bind("<ButtonRelease-1>",search_doc)
            search_button.place(x=320, y=4)
            enter_nm.place(x=4,y=4)
            doctor_en.place(x=100,y=4)
            doctor_en.bind("<KeyRelease>",on_entry_change)
            data_query()
            root.grab_set()
            root.mainloop()
        def data_queryitem():
            global product_tree
            conn = mysql.connect(host="localhost", user="root", password="dharm", charset="utf8", database="pharmacy", port=3307)
            
            cur = conn.cursor()
            cur.execute("SELECT *FROM medicines")
            records = cur.fetchall()
            for record in product_tree.get_children():
               product_tree.delete(record)
               
               
            for count, record in enumerate(records):
                if count % 2 == 0:
                    product_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3],record[4],record[5],record[6],record[7],record[8],record[9],record[10],record[11],record[12],record[13],record[14],record[15],record[16]), tags=("evenrow",))
                else:
                     product_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3],record[4],record[5],record[6],record[7],record[8],record[9],record[10],record[11],record[12],record[13],record[14],record[15],record[16]), tags=("oddrow",))
            conn.commit()
            conn.close()
        def on_entry_leave_item(event):
            global item1_en
            global product_tree
            
            if not item1_en.get():
                data_queryitem()
        def search_item(e):
            
             
            
            global product_tree
            global item1_en
            search_item =item1_en.get()
            for record in product_tree.get_children():
               product_tree.delete(record)
                
            conn = mysql.connect(host="localhost", user="root", password="dharm", charset="utf8", database="pharmacy", port=3307)

            cur = conn.cursor()
            
          
            cur.execute("SELECT * FROM medicines where med_id=%s",(search_item,))
            
            records = cur.fetchall()
        
            count = 0
            for record in records:
                if count%2 == 0:
                    product_tree.insert(parent = "", index=tk.END, iid = count, values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[7],record[8],record[9],record[10],record[11],record[12],record[13],record[14],record[15],record[16]), tags=("evenrow",))
                else:
                    product_tree.insert(parent = "", index=tk.END, iid = count, values = (record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[7],record[8],record[9],record[10],record[11],record[12],record[13],record[14],record[15],record[16]),  tags=("oddrow",)) 

                count += 1

          
            conn.commit()
     

            
        def item_search(e):
            
            global product_tree
            global item_entry,item1_en
            global bill_no
           
            root=ctk.CTkToplevel()
            root.geometry("420x270+100+400")
            #root.resizable(False,False)
            
            def insert_into_sale():
                global product_tree
                global sale_tree
                global qt_en
                global val
                global bill_no
                selected_items = product_tree.focus()
                quantity_text = qt1_en.get().strip() 
                if not quantity_text:
                    m.showerror("Error", "The qty field is empty")
                    return

                try:
                    quantity = int(quantity_text)
                except ValueError:
                    m.showerror("Error", "The qty field is not a valid number")
                    return

                if quantity <= 0:
                    m.showerror("Error", "The qty field must be a positive number")
                    return 
                for item in selected_items:
                    values = product_tree.item(item, 'values') 
                    
                  
                    if values:
                        quantity = int(qt1_en.get())
                        amount = float(values[7])
                        total_amount = amount * quantity
                        stock=int(values[6])
                      
                        exp_date = datetime.strptime(values[10], '%Y-%m-%d')
                        if quantity=="":
                            m.showerror("Error", "The qty field is empty")
                            return
                        
                           
                        if exp_date <= datetime.now() + timedelta(days=30):
                            
                            m.showerror("Error", "The selected item is near its expiration date")
                            return
                        if quantity > stock:
                            m.showerror("Error", "The quantity exceeds available stock")
                            return
                        if stock==0:
                            m.showwarning("Stock", "The selected item is Out of Stock better order it ")
                            return
                      
                        sale_tree.insert('', 'end', values=(values[0], values[1], values[2], values[3], values[4], values[5], values[8], values[10], values[11], values[12], values[13],values[14],values[15],values[16],quantity,total_amount))
                        item_selected.append((values[0], values[1], values[2], values[3], values[4], values[5], values[8], values[10], values[11], values[12], values[13],values[14],values[15],values[16],quantity,total_amount))
                        sale_tree.update()
                        
                        
                        count_rows()
                fetch_sale_tree_values()
                
               
                
            product_style=ttk.Style()
            product_style.theme_use('default')

            product_style.configure("Treeview", 
                        background = "#68D2E8",
                        rowheight = 25,
                        foreground="black",
                        fieldbackground = "white", font = ("Consolas", 12))
            product_style.configure("Treeview",background=[('selected',"#347083")])
            product_style.configure("Treeview.Heading", background="#CDE8E5",font = ("Consolas", 12))
            # tree_frame=tk.Frame(root,width=100)
            # tree_frame.place(x=10,y=50)
            tree_fr=tk.Frame(root,borderwidth=3,height=200,width=500)
            tree_fr.pack_propagate(False)
            tree_fr.place(x=10,y=50)
            tree_scroll=tk.Scrollbar(tree_fr)
            tree_scroll.pack(side=tk.RIGHT,fill=tk.Y)
            tree_scrolx=tk.Scrollbar(tree_fr,orient=tk.HORIZONTAL)
            tree_scrolx.pack(side=tk.BOTTOM ,fill=tk.X)
            
            product_tree=ttk.Treeview(tree_fr,yscrollcommand=tree_scroll.set,selectmode="extended",xscrollcommand=tree_scrolx.set)
            product_tree.pack(fill="both",expand=True)
            tree_scroll.config(command=product_tree.yview)
            tree_scrolx.config(command=product_tree.xview)
            enter_nm=ctk.CTkLabel(root,text="Enter Name",font=("helvetica",15))
            product_tree['columns']=('Sr no','company','name','drug','categories','packing','stock','billrate','salerate','mfg','exp','shell','taxcategory','hsncategory','igst','cgst','sgst')
            product_tree.column("#0",width=0,stretch=tk.NO)
            product_tree.column('Sr no',anchor=tk.W,width=80)
            product_tree.column('company',anchor=tk.W,width=170)
            product_tree.column('name',anchor=tk.W,width=120)
            product_tree.column('drug',anchor=tk.W,width=120)
            product_tree.column('categories',anchor=tk.CENTER,width=120)
            product_tree.column('packing',anchor=tk.CENTER,width=120)
            product_tree.column('stock',anchor=tk.W,width=120)
            product_tree.column('billrate',anchor=tk.W,width=120)
            product_tree.column('salerate',anchor=tk.W,width=120)
            product_tree.column('mfg',anchor=tk.W,width=140)
            product_tree.column('exp',anchor=tk.W,width=140)
            product_tree.column('shell',anchor=tk.W,width=120)
            product_tree.column('taxcategory',anchor=tk.W,width=150)
            product_tree.column('hsncategory',anchor=tk.W,width=150)
            product_tree.column('igst',anchor=tk.W,width=120)
            product_tree.column('cgst',anchor=tk.W,width=120)
            product_tree.column('sgst',anchor=tk.W,width=120)
           
            
            
            product_tree.heading("#0",text="",anchor="w")
            product_tree.heading("Sr no",text="Sr no",anchor="w")
            product_tree.heading("company",text="Company",anchor="w")
            product_tree.heading("name",text="Brand",anchor="w")
            product_tree.heading("drug",text="Drug",anchor="w")
            product_tree.heading("categories",text="Categories",anchor="w")
            product_tree.heading("packing",text="Packing",anchor="w",)
            product_tree.heading("stock",text="Stock",anchor="w")
            product_tree.heading("billrate",text="Billrate",anchor="w")
            product_tree.heading("salerate",text="Salerate",anchor="w")
            product_tree.heading("mfg",text="Mfg",anchor="w")
            product_tree.heading("exp",text="Exp",anchor="w")
            product_tree.heading("shell",text="Shell",anchor="w")
            product_tree.heading("taxcategory",text="Taxcategory",anchor="w")
            product_tree.heading("hsncategory",text="Hsncategory",anchor="w")
            product_tree.heading("igst",text="igst",anchor="w")
            product_tree.heading("cgst",text="cgst",anchor="w")
            product_tree.heading("sgst",text="sgst",anchor="w")
           
            product_tree.tag_configure('oddrow',background="white")
            product_tree.tag_configure('evenrow',background="lightblue")
            
           
                                     
            
            item1_en=ctk.CTkEntry(root,width=210,height=28,font=("Cascadia",15))
            search_button = ctk.CTkButton(root, text="Search",width=60,corner_radius=50,fg_color="#29ADB2",hover_color="#0766AD")
            
            pick_bt = ctk.CTkButton(root, text="Pick",width=80,height=30,fg_color="#29ADB2",hover_color="#0766AD",corner_radius=50,command=insert_into_sale)
            pick_bt.place(x=180,y=220)
            search_button.bind("<ButtonRelease-1>",search_item)
            search_button.place(x=320, y=4)
            enter_nm.place(x=4,y=4)
            item1_en.place(x=100,y=4)
            item1_en.bind("<KeyRelease>",on_entry_leave_item)
            data_queryitem()
           
                 
            root.grab_set()
            root.mainloop()
                    
        def patient_name(e):
            global patient_en
            global patient_en1
            global patient_tree
           
            root=ctk.CTkToplevel()
            root.geometry("420x230+400+80")
            root.resizable(False,False)
            
                
            patient_style=ttk.Style()
            patient_style.theme_use('default')

            patient_style.configure("Treeview", 
                        background = "#68D2E8",
                        rowheight = 25,
                        foreground="black",
                        fieldbackground = "white", font = ("Consolas", 12))
            patient_style.configure("Treeview",background=[('selected',"#347083")])
            patient_style.configure("Treeview.Heading", background="#CDE8E5",font = ("Consolas", 12))
            # tree_frame=tk.Frame(root,width=100)
            # tree_frame.place(x=10,y=50)
            tree_fr=tk.Frame(root,borderwidth=3,height=200,width=500)
            tree_fr.pack_propagate(False)
            tree_fr.place(x=10,y=50)
            tree_scroll=tk.Scrollbar(tree_fr)
            tree_scroll.pack(side=tk.RIGHT,fill=tk.Y)
            tree_scrolx=tk.Scrollbar(tree_fr,orient=tk.HORIZONTAL)
            tree_scrolx.pack(side=tk.BOTTOM ,fill=tk.X)
            
            patient_tree=ttk.Treeview(tree_fr,yscrollcommand=tree_scroll.set,selectmode="extended",xscrollcommand=tree_scrolx.set)
            patient_tree.pack(fill="both",expand=True)
            tree_scroll.config(command=patient_tree.yview)
            tree_scrolx.config(command=patient_tree.xview)
            enter_nm=ctk.CTkLabel(root,text="Enter Name",font=("helvetica",15))
            patient_tree['columns']=('Sr no','PatientName','address','phone','gender','doctorname')
            patient_tree.column("#0",width=0,stretch=tk.NO)
            patient_tree.column('Sr no',anchor=tk.W,width=80)
            patient_tree.column('PatientName',anchor=tk.W,width=160)
            patient_tree.column('address',anchor=tk.W,width=120)
            patient_tree.column('phone',anchor=tk.CENTER,width=120)
            patient_tree.column('gender',anchor=tk.CENTER,width=120)
            patient_tree.column('doctorname',anchor=tk.W,width=120)
         
           
            
            
            patient_tree.heading("#0",text="",anchor="w")
            patient_tree.heading("Sr no",text="Sr no",anchor="w")
            patient_tree.heading("PatientName",text="PatientName",anchor="w")
            patient_tree.heading("address",text="Address",anchor="w")
           
            patient_tree.heading("phone",text="Phone",anchor="w")
            patient_tree.heading("gender",text="Gender",anchor="w",)
            patient_tree.heading("doctorname",text="Doctor_id",anchor="w")
         
           
            patient_tree.tag_configure('oddrow',background="white")
            patient_tree.tag_configure('evenrow',background="lightblue")
            #patient_tree.bind("<KeyRelease>")
            
            patient_tree.bind("<ButtonRelease-1>", select_patient)                        
            
            patient_en=ctk.CTkEntry(root,width=210,height=28,font=("Cascadia",12))
            patient_en.bind("<KeyRelease>",on_entry_leave)
            search_button = ctk.CTkButton(root, text="Search",width=60,corner_radius=50,fg_color="#29ADB2",hover_color="#0766AD")
            search_button.bind("<ButtonRelease-1>",search)
            search_button.place(x=320, y=4)
            enter_nm.place(x=4,y=4)
            patient_en.place(x=100,y=4)
            selected=patient_tree.focus()
        

    
            data_querypat()
            root.grab_set()
            root.mainloop()
         
        global patient_en1
        global item_entry
        global doctor_place
        global sale_tree
        global qt_en
        global igst_en
        global sgst_en
        global cgst_en
        global dis_en
        global pay_en
        

        def count_rows():
            
            total_qty = 0
            total_amt=0
          
            
            for child in sale_tree.get_children():
                
                values = sale_tree.item(child, 'values')
                if values:
                   
                    qty_22 = int(values[14])
                    total=float(values[15])
            
                    total_qty += qty_22
                    total_amt+=total
         
            qt_en.delete(0, tk.END)
            qt_en.insert(0, total_qty)
            pay_en.delete(0, tk.END)
            pay_en.insert(0, total_amt)
        
        def fetch_sale_tree_values():
            global val
            global bill_no
            
            igst_en.delete(0, tk.END)
            sgst_en.delete(0, tk.END)
            cgst_en.delete(0, tk.END)
            
            dis_en.delete(0, tk.END)
            pay_en.delete(0, tk.END)

            children = sale_tree.get_children()

            total_qty = 0
            total_amount_all = 0

            for child in children:
                values = sale_tree.item(child, 'values')
                if values:
                    q_11 = int(values[14])
                  
                    mid = int(values[0])

                    shell = values[8]
                    igst = values[11]
                    cgst = values[12]
                    sgst = values[13]
                    amount = float(values[6])
                    total_amount11 = amount * q_11

                 
                    
                    sale_tree.item(child, values=(values[0], values[1], values[2], values[3], values[4], values[5], values[6], values[7], values[8],values[9] ,values[10],igst,cgst,sgst,q_11,total_amount11))
                    total_qty += q_11
                    total_amount_all += total_amount11

            igst_en.insert(tk.END, igst)
          
            cgst_en.insert(tk.END,cgst)
      
            sgst_en.insert(tk.END,sgst)
          
            pay_en.insert(0, total_amount_all)
            
            bill_fetch.configure(text=float(pay_en.get()),fg_color="#FF5F00")
                
        def update_net_amt(event):
            
               
                discount_percentage = float(dis_en.get() or 0)
                
                
                total_amount = float(pay_en.get() or 0) 
                net_amount = total_amount - (total_amount * discount_percentage / 100)
                
                gross_en.delete(0, tk.END)
                gross_en.insert(0, net_amount) 
                bill_fetch.configure(text=float(net_amount),fg_color="#FF5F00")
            
        
        
        
        def sale_date():
            global date_label_fetch
            today_date = datetime.today()
            day = today_date.day
            month = today_date.month
            year = today_date.year
            # day1=datetime.now()
            dayname=today_date.strftime("%Y-%m-%d")
            date_label_fetch.configure(text = dayname)
        global date_label_fetch
        
        def print_recipt_24():
            ord_img = Image.open("billinvoice24.png").resize((900, 900))                
            draw = ImageDraw.Draw(ord_img)
            text_font = ImageFont.truetype("tahomabd.ttf", 18)
            text_font1 = ImageFont.truetype("tahomabd.ttf", 15)
            header_font1 = ImageFont.truetype("tahomabd.ttf", 26)
             
              

            y_pos = 410
            x_positions = [15,80,300,360, 480,520, 600,660,730,800]

            for index, child in enumerate(sale_tree.get_children()[:10], start=1):
                values = sale_tree.item(child, 'values')
                if values:
                    draw.text((x_positions[0], y_pos + index * 20), str(index), fill="black", font=text_font1)
                    draw.text((x_positions[1], y_pos + index * 20), str(values[3]), fill="black", font=text_font1)
                    draw.text((x_positions[2], y_pos + index * 20), str(values[10]), fill="black", font=text_font1)
                    draw.text((x_positions[3], y_pos + index * 20), str(values[7]), fill="black", font=text_font1)
                    draw.text((x_positions[4], y_pos + index * 20), str(values[14]), fill="black", font=text_font1)
                    draw.text((x_positions[5], y_pos + index * 20), str(values[6]), fill="black", font=text_font1)
                    draw.text((x_positions[6], y_pos + index * 20), str(dis_en.get()), fill="black", font=text_font1)
                    draw.text((x_positions[7], y_pos + index * 20), str(sgst_en.get()), fill="black", font=text_font1)
                    draw.text((x_positions[8], y_pos + index * 20), str(cgst_en.get()), fill="black", font=text_font1)
                    draw.text((x_positions[9], y_pos + index * 20), str(values[15]), fill="black", font=text_font1)
                
            draw.text(xy=(70,225), text=f"{date_label_fetch.cget('text')}", fill=(0, 0, 0), font=text_font)
            draw.text(xy=(550,315), text=f"{bill_fetch_no.cget('text')}", fill=(0, 0, 0), font=text_font)
            draw.text(xy=(690,225), text=f"{patient_no.get()}", fill=(0, 0, 0), font=text_font)
            draw.text(xy=(675,270), text=f"{doctor_place.get()}", fill=(0, 0, 0), font=text_font)
            draw.text(xy=(690,845), text=f"{bill_fetch.cget('text')}", fill=(0, 0, 0), font=text_font)
            draw.text(xy=(150,270), text=f"{patient_en1.get()}", fill=(0, 0, 0), font=text_font)
                


            f2 = tk.Frame(self, relief="raised", borderwidth=4, height=700, width=700,)
            f2.place(x=900, y=200)
            f1 = ctk.CTkFrame(f2, height=645, width=550, border_width=3)
            f1.pack()
            def back_to_sale():
                f1.destroy()
                f2.destroy()
            def print_rec():
                ord_img.save("invoice.png")
                file_path = os.path.abspath("invoice.png")

       
                if os.name == 'nt':
                    os.startfile(file_path, "print")
                else: 
                    subprocess.run(["lp", file_path])
     
                    
            backs_1=ctk.CTkButton(f2,height=40,width=100,text="Back",fg_color="#FFC7ED",text_color="navyblue",hover_color="#FF4191",corner_radius=20,anchor="right",bg_color="#DDDDDD",command=back_to_sale)
            print_1=ctk.CTkButton(f2,height=40,width=100,text="Print",fg_color="#D6EFD8",text_color="navyblue",bg_color="#DDDDDD",hover_color="#80AF81",corner_radius=20,anchor="right",command=print_rec)
            print_1.place(x=340,y=600)
            backs_1.place(x=100,y=600)

            image_place = ctk.CTkImage(ord_img, size=(550, 600))
            label1 = ctk.CTkLabel(f1, text="", image=image_place)
            label1.place(x=0,y=0)
        counter=0
        def Cash():

            global counter
            global billno_formatted            
            global bill_fetch_no
            global sale_tree
            global product_tree
            global bill_no
            global counter1_mini
            global counter1_mini
            global counter1_mini2
          
            pay_m=str(cash.cget("text"))
            bill=int(bill_fetch.cget("text"))
            date_presnt=str(date_label_fetch.cget("text"))
            qty=float(qt_en.get() or 0)
            gross_value = float(gross_en.get() or 0)  
            dis_percentage = float(dis_en.get() or 0)
            net_amount = float(pay_en.get() or 0)
            
            patientid=patient_id.get()
            patientname=patient_en1.get()
            product_stock = {}
            
            conn = mysql.connect(host="localhost", user="root", password="dharm", charset="utf8", database="pharmacy", port=3307)
           

            
            

            cur = conn.cursor()
            cur.execute("SELECT *FROM sale")
            sale_records = cur.fetchall()
                
             
          
            if not patientid:
                m.showerror("Empty", "Please enter patient ID")
                return

            if not patientname:
                m.showerror("Empty", "Please select patient")
                return

            
            for row in sale_tree.get_children():
                values = sale_tree.item(row, 'values')
                sale_id = values[0]
                qty_sold = int(values[14])
                
                cur.execute("SELECT med_id, stock FROM medicines WHERE med_id = %s", (sale_id,))
                result = cur.fetchone()
                
                if result:
                    medid, stock = result
                    new_stock = stock - qty_sold
                    
                    cur.execute("UPDATE medicines SET stock = %s WHERE med_id = %s", (new_stock, medid))
                    conn.commit()

                
               

                
                
                combined_values = values + (pay_m, dis_percentage,gross_value, net_amount,date_presnt,patientid,patientname)
        
                cur.execute(
                    "INSERT INTO sale (med_id,company, brand, drug, categories, packing, salerate, exp, shell, tax_category,hsncategory,igst,cgst,sgst,qty,amt, payment_mode,dis,gross,Net_amt,date,pat_id,patient_name) VALUES (%s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s)", combined_values
        )
                conn.commit()
                
                
                
                
            

                    
            item = []
            cur.execute("select pat_id, count(*) from sale group by pat_id")
            result = cur.fetchall()
            for rec in result:
                item.append(rec)
                
           
            billno = 10001
            for rec in item:
                pat_id = rec[0]
                cur.execute(f"update sale set billno={billno} where pat_id={pat_id}")
                bill_fetch_no.configure(text=str(billno),fg_color="#FF5F00")
                billno += 1
            conn.commit()
            
            for row in sale_tree.get_children():
                values = sale_tree.item(row, 'values')
                sr = values[0]
               
                ins1 = "INSERT INTO patient_medicine (patid, medid) VALUES (%s, %s)"
            
                
                values = (patient_id.get() ,sr, )
                    
                    # Execute the query
                cur.execute(ins1, values)
            conn.commit()
                
            conn.close()
            
            if counter == 0:
       
                counter_1_bt.configure(fg_color="navyblue", text_color="white")
                counter1_mini.configure(text=str(qt_en.get()), fg_color="navyblue", text_color="white")
                counter1_mini2.configure(text=str(gross_en.get() or pay_en.get()), fg_color="navyblue", text_color="white")
                
                counter_2_bt.configure(fg_color="#D6EFD8", text_color="black")
                counter2_mini.configure(fg_color="#D6EFD8", text_color="white")
                counter2_mini2.configure(fg_color="#D6EFD8", text_color="white")
                counter = 1  
            elif counter == 1:
                counter_2_bt.configure(fg_color="navyblue", text_color="white")
                counter2_mini.configure(text=str(qt_en.get()), fg_color="navyblue", text_color="white")
                counter2_mini2.configure(text=str(gross_en.get() or pay_en.get()), fg_color="navyblue", text_color="white")
                counter = 0
            if m.askyesno("Receipt", "Do you want receipt?"):
                print_recipt_24()
            item_selected.clear()
            reset_tree()
            

           
            
       
            
        def reset_tree():
            global sale_tree
           
           
            gross_en.delete(0, tk.END)
            dis_en.delete(0, tk.END)
            pay_en.delete(0, tk.END)
            qt_en.delete(0, tk.END)
            qt1_en.delete(0, tk.END)
           
            credit_en.delete(0, tk.END)
            igst_en.delete(0, tk.END)
            sgst_en.delete(0, tk.END)
            cgst_en.delete(0, tk.END)
            # patient_en1.delete(0, tk.END)
            # patient_id.delete(0, tk.END)
            
        def return_product():
            global ret_tree
           
            side_frame=tk.Frame(self,width=970,height=700,background="#DDDDDD",relief="groove",borderwidth=4)
            
            
            order_heading=tk.Frame(side_frame,width=960,height=50,relief="flat",borderwidth=2,bg="#E1F7F5")
            order_heading.place(x=2,y=0)
            
            headinglabel=tk.Label(order_heading,text="Return Medicine",font=('times new roman',25),fg='navyblue',bg="#E1F7F5",anchor="center")
            headinglabel.place(x=20,y=0)
            
            bill_no=ctk.CTkLabel(side_frame,text="Bill No:",font=("Cascadia Mono SemiBold",17),fg_color="#DDDDDD",bg_color="#E2DFD0")
            
            bill_ren=ctk.CTkEntry(side_frame,width=80,height=30,font=("Cascadia",15),corner_radius=0)
            
            
            med_no=ctk.CTkLabel(side_frame,text="Med Id:",font=("Cascadia Mono SemiBold",17),fg_color="#DDDDDD",bg_color="#E2DFD0")
            global med_ren,qty_ren
            med_ren=ctk.CTkEntry(side_frame,width=80,height=30,font=("Cascadia",15),corner_radius=0)
           
            pat_id_no=ctk.CTkLabel(side_frame,text="Patient Id:",font=("Cascadia Mono SemiBold",17),fg_color="#DDDDDD",bg_color="#E2DFD0")
            
            pat_id_ren=ctk.CTkEntry(side_frame,width=80,height=30,font=("Cascadia",15),corner_radius=0)
            
            pat_nm_no=ctk.CTkLabel(side_frame,text="Patient Name:",font=("Cascadia Mono SemiBold",17),fg_color="#DDDDDD",bg_color="#E2DFD0")
            
            pat_nm_ren=ctk.CTkEntry(side_frame,width=150,height=30,font=("Cascadia",15),corner_radius=0)
            
            
            qty_no=ctk.CTkLabel(side_frame,text="Qty:",font=("Cascadia Mono SemiBold",17),fg_color="#DDDDDD",bg_color="#E2DFD0")
            
            qty_ren=ctk.CTkEntry(side_frame,width=50,height=30,font=("Cascadia",15),corner_radius=0)
            
           
           
          
            def ret_tree_select(event):
                selected=ret_tree.focus()
                values = ret_tree.item(selected, 'values')
                if values:
                    pat_id_ren.delete(0,tk.END)
                    pat_id_ren.insert(0,values[0])
                    pat_nm_ren.delete(0,tk.END)
                    pat_nm_ren.insert(0,values[1])
                    qty_ren.delete(0,tk.END)
                    qty_ren.insert(0,values[2])
                    bill_ren.delete(0,tk.END)
                    bill_ren.insert(0,values[9])
                    med_ren.delete(0,tk.END)
                    med_ren.insert(0,values[3])
                   
            def restock():
                global med_ren,qty_ren
                selected=ret_tree.focus()
               
                med_id = med_ren.get()
                new_qty=int(qty_ren.get())
                    
                conn = mysql.connect(host="localhost", user="root", password="dharm", charset="utf8", database="pharmacy", port=3307)  
                cur=conn.cursor()
                cur.execute("SELECT stock FROM medicines WHERE med_id = %s", (med_id,))
                records = cur.fetchone()
                current_stock = records[0]
                updated_stock = current_stock + new_qty
                cur.execute(f"update medicines set stock={updated_stock} where med_id={med_id}")
                
                cur.execute("SELECT * FROM sale WHERE med_id = %s", (med_id,))
                result=cur.fetchall()
                query = "delete from sale where med_id=%s"
                cur.execute(query, (med_id,))
                
                conn.close()
                m.showinfo("Restock","Successfully restock")
                
             
                ret_tree.delete(selected)
             
              

            style=ttk.Style()

            style.theme_use('default')

            style.configure("Treeview",
                background="#D3D3D3",
                foreground="black",
                rowheight=26,  # Adjust the row height
                fieldbackground="white",
                font=("Consolas", 12)) 
            style.configure("Treeview.Heading", background="#CDE8E5",font = ("Consolas", 12))

            style.map("Treeview",background=[('selected',"#347083")])

            tree_frame=ctk.CTkFrame(side_frame,width=750,height=200)
            tree_frame.pack_propagate(False)
            tree_frame.place(x=10,y=150)
            
            tree_scroll=tk.Scrollbar(tree_frame)
            tree_scroll.pack(side=tk.RIGHT,fill=tk.Y)
            tree_scrolx=tk.Scrollbar(tree_frame,orient=tk.HORIZONTAL)
            tree_scrolx.pack(side=tk.BOTTOM ,fill=tk.X)

        


            ret_tree=ttk.Treeview(tree_frame,yscrollcommand=tree_scroll.set,selectmode="extended",height=13,xscrollcommand=tree_scrolx.set)
            ret_tree.pack(fill="both",expand=True)
            
            tree_scroll.config(command=ret_tree.yview)
            tree_scrolx.config(command=ret_tree.xview)
            ret_tree['columns']=('patid','patname','qty','medid','brand','company','salerate','dis','amount','bill')
            ret_tree.column("#0",width=0,stretch=tk.NO)
           
            ret_tree.column('patid',anchor=tk.W,width=80)
            ret_tree.column('patname',anchor=tk.W,width=150)
            ret_tree.column('qty',anchor=tk.CENTER,width=80)
            ret_tree.column('medid',anchor=tk.CENTER,width=80)
            ret_tree.column('brand',anchor=tk.CENTER,width=110)
            ret_tree.column('company',anchor=tk.W,width=140)
            #sale_tree.column('billrate',anchor=tk.W,width=120)
            ret_tree.column('salerate',anchor=tk.W,width=80)
            ret_tree.column('dis',anchor=tk.W,width=80)
            ret_tree.column('amount',anchor=tk.W,width=100)
            ret_tree.column('bill',anchor=tk.W,width=80)
           
                
                
            ret_tree.heading("#0",text="",anchor="w")
            
            ret_tree.heading("patid",text="patid",anchor="w")
            ret_tree.heading("patname",text="patient name",anchor="w")
            
            ret_tree.heading("qty",text="Qty",anchor="w")
            ret_tree.heading("medid",text="Medid",anchor="w")
            ret_tree.heading("brand",text="Brand",anchor="w",)
            ret_tree.heading("company",text="Drug",anchor="w")
           
            ret_tree.heading("salerate",text="Salerate",anchor="w")
            ret_tree.heading("dis",text="Dis %",anchor="w")
            ret_tree.heading("amount",text="Amt",anchor="w")
            ret_tree.heading("bill",text="Billno",anchor="w")
            ret_tree.tag_configure('oddrow',background="white")
            ret_tree.tag_configure('evenrow',background="lightblue")
            ret_tree.tag_configure('redrow', background='red')
            ret_tree.bind("<ButtonRelease-1>",ret_tree_select)
            
          
            def fetch_and_display_records(event=None):
                bill_number = bill_ren.get()
                conn = mysql.connect(host="localhost", user="root", password="dharm", charset="utf8", database="pharmacy", port=3307)
                cur = conn.cursor()
                if bill_number:
                    query = "SELECT pat_id, patient_name, qty, med_id, brand, drug, salerate, dis, gross, billno FROM sale WHERE billno LIKE %s"
                    cur.execute(query, (bill_number + '%',))
                else:
                    query = "SELECT pat_id, patient_name, qty, med_id, brand, drug, salerate, dis, gross, billno FROM sale"
                    cur.execute(query)
                records = cur.fetchall()
                conn.close()
                
              
                for item in ret_tree.get_children():
                    ret_tree.delete(item)
                
               
                for count, record in enumerate(records):
                    tag = 'evenrow' if count % 2 == 0 else 'oddrow'
                    ret_tree.insert('', 'end', values=record, tags=(tag,))
            
           
           
           
          
            qty_no.place(x=540,y=110)
            qty_ren.place(x=580,y=110)
            
            
            pat_nm_no.place(x=230,y=110)
            pat_nm_ren.place(x=360,y=110)
            
            pat_id_no.place(x=10,y=110)
            pat_id_ren.place(x=120,y=110)
            bill_ren.place(x=90,y=60)
            bill_no.place(x=10,y=60)
            bill_ren.bind("<KeyRelease>", fetch_and_display_records)

            med_no.place(x=200,y=60)
            med_ren.place(x=270,y=60)
            fetch_and_display_records()
            
           
                    
           
            
            def back_frame():
                side_frame.destroy()
            
                
            bt_1=ctk.CTkButton(order_heading,height=30,width=40,text="X",fg_color="#E4003A",hover="disabled",command=back_frame)
            bt_1.place(x=715,y=2)
            ret_1=ctk.CTkButton(side_frame,height=40,width=90,text="Restock",fg_color="#C8ACD6",text_color="navyblue",hover_color="#C8ACD6",corner_radius=20,command=restock)
            ret_1.place(x=600,y=400)
            side_frame.place(x=935,y=280)
            
            
           
       
       
        def credit():
            global sale_tree
            global counter
            global bill_no
            
            conn = mysql.connect(host="localhost", user="root", password="dharm", charset="utf8", database="pharmacy", port=3307)

            cur = conn.cursor()
            cur.execute("SELECT *FROM sale")
            records = cur.fetchall()
   
            
            
            pay_m=str(online.cget("text"))
            bill=int(bill_fetch.cget("text"))
            date_presnt=str(date_label_fetch.cget("text"))
            qty=float(qt_en.get() or 0)
            gross_value = float(gross_en.get() or 0) 
            dis_percentage = float(dis_en.get() or 0)
            net_amount = float(pay_en.get() or 0)
            credit=credit_en.get()
            patientid=patient_id.get()
            patientname=patient_en1.get()
            if not patientid:
                m.showerror("Empty", "Please enter patient ID")
                return

            if not patientname:
                m.showerror("Empty", "Please select patient")
                return
         
            credit = credit_en.get()
            if not credit:
                m.showerror("Empty", "Please enter credit Days")
                return
            try:
                credit = int(credit)
            except ValueError:
                m.showerror("Invalid", "Credit must be an integer")
                return

            for row in sale_tree.get_children():
                values = sale_tree.item(row, 'values')
                sale_id = values[0]
                qty_sold = int(values[14])
                
                cur.execute("SELECT med_id, stock FROM medicines WHERE med_id = %s", (sale_id,))
                result = cur.fetchone()
                
                if result:
                    medid, stock = result
                    new_stock = stock - qty_sold
                    
                    cur.execute("UPDATE medicines SET stock = %s WHERE med_id = %s", (new_stock, medid))
                    conn.commit()

                
               

                
        
                combined_values = values + (pay_m, dis_percentage,gross_value, net_amount,credit,date_presnt,patientid,patientname)
        
                cur.execute(
                    "INSERT INTO sale (med_id,company, brand, drug, categories, packing, salerate, exp, shell, tax_category, hsncategory, igst, cgst, sgst, qty,amt, payment_mode, dis, gross, Net_amt,credit,date,pat_id,patient_name) VALUES (%s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s,%s)", combined_values
        )
            conn.commit()
    
            
            item = []
            cur.execute("select pat_id, count(*) from sale group by pat_id")
            result = cur.fetchall()
            for rec in result:
                item.append(rec)
                
           
            billno = 10001
            for rec in item:
                pat_id = rec[0]
                cur.execute(f"update sale set billno={billno} where pat_id={pat_id}")
                bill_fetch_no.configure(text=str(billno),fg_color="#FF5F00")
                billno += 1
            conn.commit()
            
            for row in sale_tree.get_children():
                values = sale_tree.item(row, 'values')
                sr = values[0]
             
                ins1 = "INSERT INTO patient_medicine (patid, medid) VALUES (%s, %s)"
            
                
                values = (patient_id.get() ,sr,)
                    
                    # Execute the query
                cur.execute(ins1, values)
            conn.commit()
                
            conn.close()
            
            if counter == 0:
       
                counter_1_bt.configure(fg_color="navyblue", text_color="white")
                counter1_mini.configure(text=str(qt_en.get()), fg_color="navyblue", text_color="white")
                counter1_mini2.configure(text=str(credit_en.get() or pay_en.get()), fg_color="navyblue", text_color="white")
                
                counter_2_bt.configure(fg_color="#D6EFD8", text_color="black")
                counter2_mini.configure(fg_color="#D6EFD8", text_color="white")
                counter2_mini2.configure(fg_color="#D6EFD8", text_color="white")
                counter = 1  
            elif counter == 1:
                counter_2_bt.configure(fg_color="navyblue", text_color="white")
                counter2_mini.configure(text=str(qt_en.get()), fg_color="navyblue", text_color="white")
                counter2_mini2.configure(text=str(credit_en.get() or pay_en.get()), fg_color="navyblue", text_color="white")
                counter = 0
            if m.askyesno("Receipt", "Do you want receipt?"):
                print_recipt_24()
            #---

            
        def counter_change_1():
            gross_en.delete(0, tk.END)
            dis_en.delete(0, tk.END)
            pay_en.delete(0, tk.END)
            qt_en.delete(0, tk.END)
            qt1_en.delete(0, tk.END)

            credit_en.delete(0, tk.END)
            igst_en.delete(0, tk.END)
            sgst_en.delete(0, tk.END)
            cgst_en.delete(0, tk.END)
            for row in sale_tree.get_children():
                sale_tree.delete(row)
            sale_tree.tag_configure('highlight_orange', background='#FF7F3E')
            sale_tree.tag_configure('highlight_red', background='red')

           
            for index, item in enumerate(item_selected):
                item_list = list(item)
                
                if item_list[14] == 1:
                   
                    if index == 0: 
                        sale_tree.insert('', 'end', values=item_list, tags=('highlight_red',))
                    else:
                        sale_tree.insert('', 'end', values=item_list, tags=('highlight_orange',))
                
            def cash_11():
                global counter
                global billno_formatted
                global bill_fetch_no
                global sale_tree
                global bill_no
                global counter1_mini
                global counter1_mini
                global counter1_mini2
                conn = mysql.connect(host="localhost", user="root", password="dharm", charset="utf8", database="pharmacy", port=3307)

                cur = conn.cursor()
                cur.execute("SELECT *FROM sale")
                records = cur.fetchall()
               
                
                pay_m=str(cash.cget("text"))
                bill=int(bill_fetch.cget("text"))
                date_presnt=str(date_label_fetch.cget("text"))
                qty=float(qt_en.get() or 0)
                gross_value = float(gross_en.get() or 0)  # Ensure numeric conversion or default to 0
                dis_percentage = float(dis_en.get() or 0)
                net_amount = float(pay_en.get() or 0)


                patientid=patient_id.get()
                patientname=patient_en1.get()
                if not patientid:
                    m.showerror("Empty", "Please enter patient ID")
                    return

                if not patientname:
                    m.showerror("Empty", "Please select patient")
                    return

            
                for row in sale_tree.get_children():
                    values = sale_tree.item(row, 'values')
                    sale_id = values[0]
                    qty_sold = int(values[14])
                    
                    cur.execute("SELECT med_id, stock FROM medicines WHERE med_id = %s", (sale_id,))
                    result = cur.fetchone()
                
                if result:
                    medid, stock = result
                    new_stock = stock - qty_sold
                    
                    cur.execute("UPDATE medicines SET stock = %s WHERE med_id = %s", (new_stock, medid))
                    conn.commit()

                
               

                
        
                combined_values = values + (pay_m, dis_percentage,gross_value, net_amount,date_presnt,patientid,patientname)
        
                cur.execute(
                    "INSERT INTO sale (med_id,company, brand, drug, categories, packing, salerate, exp, shell, tax_category, hsncategory, igst, cgst, sgst, qty,amt, payment_mode, dis, gross, Net_amt,date,pat_id,patient_name) VALUES (%s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s)", combined_values
        )
        
        
    
            
                item = []
                cur.execute("select pat_id, count(*) from sale group by pat_id")
                result = cur.fetchall()
                for rec in result:
                    item.append(rec)
                    
            
                billno = 10001
                for rec in item:
                    pat_id = rec[0]
                    cur.execute(f"update sale set billno={billno} where pat_id={pat_id}")
                    bill_fetch_no.configure(text=str(billno),fg_color="#FF5F00")
                    billno += 1
                conn.commit()
                for row in sale_tree.get_children():
                    values = sale_tree.item(row, 'values')
                    sr = values[0]
                   
                    ins1 = "INSERT INTO patient_medicine (patid, medid) VALUES (%s, %s)"
                
                    
                    values = (patient_id.get() ,sr, )
                        
                        # Execute the query
                    cur.execute(ins1, values)
                conn.commit()
                    
                conn.close()
                
                counter_1_bt.configure(fg_color="navyblue", text_color="white")
                counter1_mini.configure(text=str(qt1_en.get()), fg_color="navyblue", text_color="white")
                counter1_mini2.configure(text=str(gross_en.get() or pay_en.get()), fg_color="navyblue", text_color="white")
                if m.askyesno("Receipt", "Do you want receipt?"):
                    print_recipt_24()
                reset_tree()
                    
                item_selected.clear()
                    

       
        
                
           
                
                
            def count1_credit():
                global sale_tree
                global counter
                global bill_no
                
                conn = mysql.connect(host="localhost", user="root", password="dharm", charset="utf8", database="pharmacy", port=3307)

                cur = conn.cursor()
                cur.execute("SELECT *FROM sale")
                records = cur.fetchall()
    
                
                
                pay_m=str(online.cget("text"))
                bill=int(bill_fetch.cget("text"))
                date_presnt=str(date_label_fetch.cget("text"))
                qty=float(qt_en.get() or 0)
                gross_value = float(gross_en.get() or 0) 
                dis_percentage = float(dis_en.get() or 0)
                net_amount = float(pay_en.get() or 0)
                credit=credit_en.get()
                patientid=patient_id.get()
                patientname=patient_en1.get()
                if not patientid:
                    m.showerror("Empty", "Please enter patient ID")
                    return

                if not patientname:
                    m.showerror("Empty", "Please select patient")
                    return
                credit = credit_en.get()
               
                if not credit:
                    m.showerror("Empty", "Please enter credit Days")
                    return
                try:
                    credit = int(credit)
                except ValueError:
                    m.showerror("Invalid", "Credit must be an integer")
                    return

            

                for row in sale_tree.get_children():
                    values = sale_tree.item(row, 'values')
                    sale_id = values[0]
                    qty_sold = int(values[14])
                    
                    cur.execute("SELECT med_id, stock FROM medicines WHERE med_id = %s", (sale_id,))
                    result = cur.fetchone()
                    
                    if result:
                        medid, stock = result
                        new_stock = stock - qty_sold
                        
                        cur.execute("UPDATE medicines SET stock = %s WHERE med_id = %s", (new_stock, medid))
                        conn.commit()

                    
                

                    
            
                    combined_values = values + (pay_m, dis_percentage,gross_value, net_amount,credit,date_presnt,patientid,patientname)
            
                    cur.execute(
                    "INSERT INTO sale (med_id,company, brand, drug, categories, packing, salerate, exp, shell, tax_category, hsncategory, igst, cgst, sgst, qty,amt, payment_mode, dis, gross, Net_amt,credit,date,pat_id,patient_name) VALUES (%s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s,%s)", combined_values
        )
        
                conn.commit()
        
                
                item = []
                cur.execute("select pat_id, count(*) from sale group by pat_id")
                result = cur.fetchall()
                for rec in result:
                    item.append(rec)
                    
            
                billno = 10001
                for rec in item:
                    pat_id = rec[0]
                    cur.execute(f"update sale set billno={billno} where pat_id={pat_id}")
                    bill_fetch_no.configure(text=str(billno),fg_color="#FF5F00")
                    billno += 1
                conn.commit()
                
                for row in sale_tree.get_children():
                    values = sale_tree.item(row, 'values')
                    sr = values[0]
                  
                    ins1 = "INSERT INTO patient_medicine (patid, medid) VALUES (%s, %s)"
                
                    
                    values = (patient_id.get() ,sr)
                        
                        # Execute the query
                    cur.execute(ins1, values)
                conn.commit()
                    
                conn.close()
                
              
                counter_1_bt.configure(fg_color="navyblue", text_color="white")
                counter1_mini.configure(text=str(qt_en.get()), fg_color="navyblue", text_color="white")
                counter1_mini2.configure(text=str(credit_en.get() or pay_en.get()), fg_color="navyblue", text_color="white")
                if m.askyesno("Receipt", "Do you want receipt?"):
                    print_recipt_24()
            
        
               
                

            
            def coun1_return():
               return_product()
        
                
            
                
                
            bt_frame=ctk.CTkFrame(patient_fr,width=404,height=75,border_color="#1C1678",border_width=2,fg_color="#DDDDDD",bg_color="#E2DFD0",corner_radius=0)
            
            counter_1_bt=ctk.CTkButton(bt_frame,text="1",width=200,height=34,text_color="navyblue",corner_radius=0,bg_color="#E2DFD0",fg_color="#D6EFD8",border_width=1,background_corner_colors=("black","black","black","black"),hover_color="#E1F7F5")
         
                
            counter_2_bt=ctk.CTkButton(bt_frame,text="2",width=200,height=34,text_color="navyblue",corner_radius=0,bg_color="#E2DFD0",fg_color="#DDDDDD",border_width=1,background_corner_colors=("black","black","black","black"),hover_color="#E1F7F5")
                
            
            global counter1_mini
            global counter1_mini2
                    
            counter1_mini=ctk.CTkButton(bt_frame,text="",width=70,height=34,text_color="navyblue",corner_radius=0,bg_color="#E2DFD0",fg_color="#D6EFD8",border_width=1,background_corner_colors=("black","black","black","black"),hover_color="#E1F7F5")
                    
            counter1_mini2=ctk.CTkButton(bt_frame,text="",width=130,height=34,text_color="navyblue",corner_radius=0,bg_color="#E2DFD0",fg_color="#D6EFD8",border_width=1,background_corner_colors=("black","black","black","black"),hover_color="#E1F7F5")
                    
                    
            counter2_mini=ctk.CTkButton(bt_frame,text="",width=70,height=34,text_color="navyblue",corner_radius=0,bg_color="#E2DFD0",fg_color="#DDDDDD",border_width=1,background_corner_colors=("black","black","black","black"),hover_color="#E1F7F5")
                    
                    
            counter2_mini2=ctk.CTkButton(bt_frame,text="",width=130,height=34,text_color="navyblue",corner_radius=0,bg_color="#E2DFD0",fg_color="#DDDDDD",border_width=1,background_corner_colors=("black","black","black","black"),hover_color="#E1F7F5")
            
           
                
            pay_method1=tk.LabelFrame(self,text="Payment Type",font=("Cascadia Mono SemiBold",17),fg="blue",bg="#DDDDDD",height=250,width=570,foreground="black")
            cash_12=ctk.CTkButton(pay_method1,text="Cash",width=200,height=38,text_color="navyblue",corner_radius=0,fg_color="#D6EFD8",border_width=1,hover_color="#80AF81",command=cash_11)
        
            online=ctk.CTkButton(pay_method1,text="Credit",width=200,height=38,text_color="navyblue",corner_radius=0,fg_color="#FFD3B6",border_width=1,hover_color="#FF7F3E",command=count1_credit)
            
            return1=ctk.CTkButton(pay_method1,text="Return",width=300,height=38,text_color="navyblue",corner_radius=0,bg_color="#E2DFD0",fg_color="#E2BBE9",border_width=1,hover_color="#AF47D2",command=coun1_return)
        
         
            counter_1_bt.place(x=1,y=2)
            counter_2_bt.place(x=200,y=2)
            
            counter1_mini.place(x=1,y=37)
            counter1_mini2.place(x=70,y=37)
            counter2_mini.place(x=201,y=37)
            counter2_mini2.place(x=270,y=37)
            bt_frame.place(x=70,y=90)
            pay_method1.place(x=1020,y=700)
            cash_12.place(x=10,y=5)
            online.place(x=240,y=5)
            return1.place(x=70,y=55)
                   
        def counter_change_2():
            
            
         
            for row in sale_tree.get_children():
                sale_tree.delete(row)
            
            bt_frame=ctk.CTkFrame(patient_fr,width=404,height=75,border_color="#1C1678",border_width=2,fg_color="#DDDDDD",bg_color="#E2DFD0",corner_radius=0)
            
            counter_1_bt=ctk.CTkButton(bt_frame,text="1",width=200,height=34,text_color="navyblue",corner_radius=0,bg_color="#E2DFD0",fg_color="#DDDDDD",border_width=1,background_corner_colors=("black","black","black","black"),hover_color="#E1F7F5")
         
                
            counter_2_bt=ctk.CTkButton(bt_frame,text="2",width=200,height=34,text_color="navyblue",corner_radius=0,bg_color="#E2DFD0",fg_color="#D6EFD8",border_width=1,background_corner_colors=("black","black","black","black"),hover_color="#E1F7F5")
                
            
            global counter1_mini
            global counter1_mini2
                    
            counter1_mini=ctk.CTkButton(bt_frame,text="",width=70,height=34,text_color="navyblue",corner_radius=0,bg_color="#E2DFD0",fg_color="#DDDDDD",border_width=1,background_corner_colors=("black","black","black","black"),hover_color="#E1F7F5")
                    
            counter1_mini2=ctk.CTkButton(bt_frame,text="",width=130,height=34,text_color="navyblue",corner_radius=0,bg_color="#E2DFD0",fg_color="#DDDDDD",border_width=1,background_corner_colors=("black","black","black","black"),hover_color="#E1F7F5")
                    
                    
            counter2_mini=ctk.CTkButton(bt_frame,text="",width=70,height=34,text_color="navyblue",corner_radius=0,bg_color="#E2DFD0",fg_color="#D6EFD8",border_width=1,background_corner_colors=("black","black","black","black"),hover_color="#E1F7F5")
                    
                    
            counter2_mini2=ctk.CTkButton(bt_frame,text="",width=130,height=34,text_color="navyblue",corner_radius=0,bg_color="#E2DFD0",fg_color="#D6EFD8",border_width=1,background_corner_colors=("black","black","black","black"),hover_color="#E1F7F5")
            
            pay_method=tk.LabelFrame(self,text="Payment Type",font=("Cascadia Mono SemiBold",17),fg="#DDDDDD",bg="#DDDDDD",height=250,width=570,foreground="black")
           
            def cash_2():
                global bill_fetch_no
                global sale_tree
                global bill_no
                global counter1_mini
                global counter1_mini
                global counter1_mini2
                
                conn = mysql.connect(host="localhost", user="root", password="dharm", charset="utf8", database="pharmacy", port=3307)

                cur = conn.cursor()
                cur.execute("SELECT *FROM sale")
                records = cur.fetchall()
                print(records)
                
                
                pay_m=str(cash.cget("text"))
                bill=int(bill_fetch.cget("text"))
                date_presnt=str(date_label_fetch.cget("text"))
                qty=float(qt_en.get() or 0)
                gross_value = float(gross_en.get() or 0)  # Ensure numeric conversion or default to 0
                dis_percentage = float(dis_en.get() or 0)
                net_amount = float(pay_en.get() or 0)


                patientid=patient_id.get()
                patientname=patient_en1.get()
                if not patientid:
                    m.showerror("Empty", "Please enter patient ID")
                    return

                if not patientname:
                    m.showerror("Empty", "Please select patient")
                    return

            
                for row in sale_tree.get_children():
                    values = sale_tree.item(row, 'values')
                    sale_id = values[0]
                    qty_sold = int(values[14])
                    
                    cur.execute("SELECT med_id, stock FROM medicines WHERE med_id = %s", (sale_id,))
                    result = cur.fetchone()
                
                if result:
                    medid, stock = result
                    new_stock = stock - qty_sold
                    
                    cur.execute("UPDATE medicines SET stock = %s WHERE med_id = %s", (new_stock, medid))
                    conn.commit()

                
               

                
        
                combined_values = values + (pay_m, dis_percentage,gross_value, net_amount,date_presnt,patientid,patientname)
        
                cur.execute(
                    "INSERT INTO sale (med_id,company, brand, drug, categories, packing, salerate, exp, shell, tax_category, hsncategory, igst, cgst, sgst, qty,amt, payment_mode, dis, gross, Net_amt,date,pat_id,patient_name) VALUES (%s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s)", combined_values
        )
        
        
    
            
                item = []
                cur.execute("select pat_id, count(*) from sale group by pat_id")
                result = cur.fetchall()
                for rec in result:
                    item.append(rec)
                    
            
                billno = 10001
                for rec in item:
                    pat_id = rec[0]
                    cur.execute(f"update sale set billno={billno} where pat_id={pat_id}")
                    bill_fetch_no.configure(text=str(billno),fg_color="#FF5F00")
                    billno += 1
                conn.commit()
                for row in sale_tree.get_children():
                    values = sale_tree.item(row, 'values')
                    sr = values[0]
                   
                    ins1 = "INSERT INTO patient_medicine (patid, medid) VALUES (%s, %s)"
                
                    
                    values = (patient_id.get(),sr)
                        
                        # Execute the query
                    cur.execute(ins1, values)
                conn.commit()
                    
                conn.close()
                
                counter_2_bt.configure(fg_color="navyblue", text_color="white")
                counter2_mini.configure(text=str(qt_en.get()), fg_color="navyblue", text_color="white")
                counter2_mini2.configure(text=str(gross_en.get() or pay_en.get()), fg_color="navyblue", text_color="white")
                
                if m.askyesno("Receipt", "Do you want receipt?"):
                    print_recipt_24()
                reset_tree2()

            def reset_tree2():
                global sale_tree
                gross_en.delete(0, tk.END)
                dis_en.delete(0, tk.END)
                pay_en.delete(0, tk.END)
                qt_en.delete(0, tk.END)
                qt1_en.delete(0, tk.END)
              
                credit_en.delete(0, tk.END)
                igst_en.delete(0, tk.END)
                sgst_en.delete(0, tk.END)
                cgst_en.delete(0, tk.END)
                
            def count_credit2():
                global sale_tree
                # global counter
                global bill_no
                
                conn = mysql.connect(host="localhost", user="root", password="dharm", charset="utf8", database="pharmacy", port=3307)

                cur = conn.cursor()
                cur.execute("SELECT *FROM sale")
                records = cur.fetchall()
    
                
                
                pay_m=str(online.cget("text"))
                bill=int(bill_fetch.cget("text"))
                date_presnt=str(date_label_fetch.cget("text"))
                qty=float(qt_en.get() or 0)
                gross_value = float(gross_en.get() or 0) 
                dis_percentage = float(dis_en.get() or 0)
                net_amount = float(pay_en.get() or 0)
                credit=credit_en.get()
                patientid=patient_id.get()
                patientname=patient_en1.get()
                if not patientid:
                    m.showerror("Empty", "Please enter patient ID")
                    return

                if not patientname:
                    m.showerror("Empty", "Please select patient")
                    return
                credit = credit_en.get()
                if not credit:
                    m.showerror("Empty", "Please enter credit Days")
                    return
                try:
                    credit = int(credit)
                except ValueError:
                    m.showerror("Invalid", "Credit must be an integer")
                    return

                for row in sale_tree.get_children():
                    values = sale_tree.item(row, 'values')
                    sale_id = values[0]
                    qty_sold = int(values[14])
                    
                    cur.execute("SELECT med_id, stock FROM medicines WHERE med_id = %s", (sale_id,))
                    result = cur.fetchone()
                    
                    if result:
                        medid, stock = result
                        new_stock = stock - qty_sold
                        
                        cur.execute("UPDATE medicines SET stock = %s WHERE med_id = %s", (new_stock, medid))
                        conn.commit()

                    
                

                    
            
                    combined_values = values + (pay_m, dis_percentage,gross_value, net_amount,credit,date_presnt,patientid,patientname)
            
                    cur.execute(
                    "INSERT INTO sale (med_id,company, brand, drug, categories, packing, salerate, exp, shell, tax_category, hsncategory, igst, cgst, sgst, qty,amt, payment_mode, dis, gross, Net_amt,credit,date,pat_id,patient_name) VALUES (%s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s,%s)", combined_values
        )
                conn.commit()
        
                
                item = []
                cur.execute("select pat_id, count(*) from sale group by pat_id")
                result = cur.fetchall()
                for rec in result:
                    item.append(rec)
                    
            
                billno = 10001
                for rec in item:
                    pat_id = rec[0]
                    cur.execute(f"update sale set billno={billno} where pat_id={pat_id}")
                    bill_fetch_no.configure(text=str(billno),fg_color="#FF5F00")
                    billno += 1
                conn.commit()
                for row in sale_tree.get_children():
                    values = sale_tree.item(row, 'values')
                    sr = values[0]
                  
                    ins1 = "INSERT INTO patient_medicine (patid, medid) VALUES (%s, %s)"
                
                    
                    values = (patient_id.get() ,sr,)
                        
                        # Execute the query
                    cur.execute(ins1, values)
                conn.commit()
                
                conn.close()
                
              
                counter_2_bt.configure(fg_color="navyblue", text_color="white")
                counter2_mini.configure(text=str(qt_en.get()), fg_color="navyblue", text_color="white")
                counter2_mini2.configure(text=str(credit_en.get() or pay_en.get()), fg_color="navyblue", text_color="white")
                if m.askyesno("Receipt", "Do you want receipt?"):
                    print_recipt_24()
            
            def counter2_ret():
                return_product()
            
            cash=ctk.CTkButton(pay_method,text="Cash",width=200,height=38,text_color="navyblue",corner_radius=0,fg_color="#D6EFD8",border_width=1,hover_color="#80AF81",command=cash_2)
            
            online=ctk.CTkButton(pay_method,text="Credit",width=200,height=38,text_color="navyblue",corner_radius=0,bg_color="#E2DFD0",fg_color="#FFD3B6",border_width=1,hover_color="#FF7F3E",command=count_credit2)
            
            return1=ctk.CTkButton(pay_method,text="Return",width=300,height=38,text_color="navyblue",corner_radius=0,bg_color="#E2DFD0",fg_color="#E2BBE9",border_width=1,hover_color="#AF47D2",command=counter2_ret)
           
            pay_method.place(x=1020,y=700)
            cash.place(x=10,y=5)
            online.place(x=240,y=5)
            return1.place(x=70,y=55)
            def reset_c1():
                global reset_c1
                gross_en.delete(0, tk.END)
                dis_en.delete(0, tk.END)
                pay_en.delete(0, tk.END)
                qt_en.delete(0, tk.END)
                qt1_en.delete(0, tk.END)
              
                credit_en.delete(0, tk.END)
                igst_en.delete(0, tk.END)
                sgst_en.delete(0, tk.END)
                cgst_en.delete(0, tk.END)
            counter_1_bt.place(x=1,y=2)
            counter_2_bt.place(x=200,y=2)
            
            counter1_mini.place(x=1,y=37)
            counter1_mini2.place(x=70,y=37)
            counter2_mini.place(x=201,y=37)
            counter2_mini2.place(x=270,y=37)
            bt_frame.place(x=70,y=90)
            reset_c1()
       
        patient_fr=ctk.CTkFrame(self,width=1527,height=830,border_color="#1C1678",border_width=2,fg_color="#DDDDDD",bg_color="#E2DFD0",corner_radius=4)
              
        Vocher_label=ctk.CTkLabel(self,text="Patient ID:",font=("Cascadia Mono SemiBold",17),fg_color="#DDDDDD",bg_color="#E2DFD0")
        
        patient_id=ctk.CTkEntry(self,width=60,height=32,font=("Cascadia",15),corner_radius=0)
        patient_id.place(x=123,y=3)
        
               
        Date_label1=ctk.CTkLabel(self,text="Date:",font=("Cascadia Mono SemiBold",17),fg_color="#DDDDDD",bg_color="#E2DFD0")
        
        date_label_fetch=ctk.CTkLabel(self,text="Date:",font=("Cascadia Mono SemiBold",17),fg_color="#DDDDDD",bg_color="#E2DFD0")       
        Vocher_label.place(x=10,y=2)
        Date_label1.place(x=1200,y=2)
        sale_date()
        date_label_fetch.place(x=1250,y=2)
                
        bt_frame=ctk.CTkFrame(patient_fr,width=404,height=75,border_color="#1C1678",border_width=2,fg_color="#DDDDDD",bg_color="#E2DFD0",corner_radius=0)
        global counter_1_bt
        global counter1_mini2       
        counter_1_bt=ctk.CTkButton(bt_frame,text="1",width=200,height=34,text_color="navyblue",corner_radius=0,bg_color="#E2DFD0",fg_color="#D6EFD8",border_width=1,background_corner_colors=("black","black","black","black"),hover_color="#E1F7F5",command=counter_change_1)
        keyboard.add_hotkey('left',counter_change_1)
         
                
        counter_2_bt=ctk.CTkButton(bt_frame,text="2",width=200,height=34,text_color="navyblue",corner_radius=0,bg_color="#E2DFD0",fg_color="#DDDDDD",border_width=1,background_corner_colors=("black","black","black","black"),hover_color="#E1F7F5",command=counter_change_2)
        keyboard.add_hotkey('right',counter_change_2)
            
        
        global counter1_mini
        global counter1_mini2
                
        counter1_mini=ctk.CTkButton(bt_frame,text="",width=70,height=34,text_color="navyblue",corner_radius=0,bg_color="#E2DFD0",fg_color="#D6EFD8",border_width=1,background_corner_colors=("black","black","black","black"),hover_color="#E1F7F5")
                
        counter1_mini2=ctk.CTkButton(bt_frame,text="",width=130,height=34,text_color="navyblue",corner_radius=0,bg_color="#E2DFD0",fg_color="#D6EFD8",border_width=1,background_corner_colors=("black","black","black","black"),hover_color="#E1F7F5")
                
                
        counter2_mini=ctk.CTkButton(bt_frame,text="",width=70,height=34,text_color="navyblue",corner_radius=0,bg_color="#E2DFD0",fg_color="#DDDDDD",border_width=1,background_corner_colors=("black","black","black","black"),hover_color="#E1F7F5")
                
                
        counter2_mini2=ctk.CTkButton(bt_frame,text="",width=130,height=34,text_color="navyblue",corner_radius=0,bg_color="#E2DFD0",fg_color="#DDDDDD",border_width=1,background_corner_colors=("black","black","black","black"),hover_color="#E1F7F5")
                
        
                
                
                
        
                
                
      
         
         
        global bill_fetch
        global bill_fetch_no
        self.bill_no=ctk.CTkLabel(self,text="Bill No :",font=("Cascadia Mono SemiBold",17),fg_color="#DDDDDD",bg_color="#E2DFD0")
        bill_fetch_no=ctk.CTkLabel(self,text="",font=("Cascadia Mono SemiBold",17),fg_color="#DDDDDD",bg_color="#E2DFD0")
        
        
        
        def remove():
            selected=sale_tree.selection()
            for item in selected:
                values = sale_tree.item(item, "values")
                      
                sale_tree.delete(item) 
                gross_en.delete(0, tk.END)
                dis_en.delete(0, tk.END)
                pay_en.delete(0, tk.END)
                qt_en.delete(0, tk.END)
                qt1_en.delete(0, tk.END)
             
                credit_en.delete(0, tk.END)
                igst_en.delete(0, tk.END)
                sgst_en.delete(0, tk.END)
                cgst_en.delete(0, tk.END)
                item_selected.clear()
        def add():
            selected = sale_tree.focus()
            
            
            values = sale_tree.item(selected, 'values')
            
            igst_en.insert(0,values[11])
            sgst_en.insert(0,values[12])
            cgst_en.insert(0,values[13])
            qt1_en.insert(0,values[14])
            qt_en.insert(0,values[14])
            pay_en.insert(0,values[15])
                         
        reest=ctk.CTkButton(self,text="remove",width=90,height=34,text_color="navyblue",corner_radius=0,bg_color="#E2DFD0",fg_color="#DDDDDD",border_width=1,background_corner_colors=("black","black","black","black"),hover_color="#E1F7F5",command=remove)
        reest.place(x=550,y=220)
        
        add1=ctk.CTkButton(self,text="Add",width=90,height=34,text_color="navyblue",corner_radius=0,bg_color="#E2DFD0",fg_color="#DDDDDD",border_width=1,background_corner_colors=("black","black","black","black"),hover_color="#E1F7F5",command=add)
        add1.place(x=700,y=220)
        
                
        bill_fetch_no.place(x=1008,y=80)
        
        self.bill_amt=ctk.CTkLabel(self,text="Bill Amt :",font=("Cascadia Mono SemiBold",17),fg_color="#DDDDDD",bg_color="#E2DFD0")
        
        bill_fetch=ctk.CTkLabel(self,text="",font=("Cascadia Mono SemiBold",17),fg_color="#DDDDDD",bg_color="#E2DFD0")
        
        bill_fetch.place(x=1008,y=140)
        
        
        patient_label=ctk.CTkLabel(self,text="Patient Name:",font=("Cascadia Mono SemiBold",17),fg_color="#DDDDDD",bg_color="#E2DFD0")
        
        patient_sal_nm=tk.StringVar()
        patient_en1=ctk.CTkEntry(self,width=230,height=32,font=("Cascadia",15),corner_radius=0,textvariable=patient_sal_nm)
        patient_no=ctk.CTkEntry(self,width=230,height=32,font=("Cascadia",15),corner_radius=0)
        
       
        patient_en1.bind("<ButtonRelease-1>",patient_name)
        doctor_place=ctk.CTkEntry(self,width=230,height=32,corner_radius=0,font=("Cascadia",15),)
        doctor_place.bind("<ButtonRelease-1>",doctor_name)
        
        
        dr_label=ctk.CTkLabel(self,text="Doctor Name:",font=("Cascadia Mono SemiBold",17),fg_color="#DDDDDD",bg_color="#E2DFD0")
        
        item_label=ctk.CTkLabel(self,text="Item:",font=("Cascadia Mono SemiBold",17),fg_color="#DDDDDD",bg_color="#E2DFD0")
        item_label.place(x=13,y=220)
        item_entry=ctk.CTkEntry(self,width=260,height=32,font=("Cascadia",15),corner_radius=0)
        item_entry.place(x=80,y=220)
        item_entry.bind("<Enter>",item_search)
      
        
            
        
        
      
            
     
        
        
        style=ttk.Style()

        style.theme_use('default')

        style.configure("Treeview",
                        background="#D3D3D3",
                        foreground="white",rowheight=25,fieldbackground="white")
        style.configure("Treeview.Heading", background="#CDE8E5",font = ("Consolas", 12))

        style.map("Treeview",background=[('selected',"#347083")])

        tree_frame=ctk.CTkFrame(patient_fr,width=1400,height=300)
        tree_frame.pack_propagate(False)
        tree_frame.place(x=10,y=255)
        
        tree_scroll=tk.Scrollbar(tree_frame)
        tree_scroll.pack(side=tk.RIGHT,fill=tk.Y)
        tree_scrolx=tk.Scrollbar(tree_frame,orient=tk.HORIZONTAL)
        tree_scrolx.pack(side=tk.BOTTOM ,fill=tk.X)

       


        sale_tree=ttk.Treeview(tree_frame,yscrollcommand=tree_scroll.set,selectmode="extended",height=13,xscrollcommand=tree_scrolx.set)
        sale_tree.pack(fill="both",expand=True)
        
        tree_scroll.config(command=sale_tree.yview)
        tree_scrolx.config(command=sale_tree.xview)
        sale_tree['columns']=('Sr no','company','brand','drug','categories','packing','salerate','exp','shell','taxcategory','hsncategory','igst','cgst','sgst','qty','amt')
        sale_tree.column("#0",width=0,stretch=tk.NO)
        sale_tree.column('Sr no',anchor=tk.W,width=80)
        sale_tree.column('company',anchor=tk.W,width=200)
        sale_tree.column('brand',anchor=tk.W,width=220)
        sale_tree.column('drug',anchor=tk.W,width=220)
        
        
        sale_tree.column('categories',anchor=tk.CENTER,width=120)
        sale_tree.column('packing',anchor=tk.CENTER,width=120)
        
       
        sale_tree.column('salerate',anchor=tk.W,width=120)
     
        sale_tree.column('exp',anchor=tk.W,width=120)
        sale_tree.column('shell',anchor=tk.W,width=120)
        sale_tree.column('taxcategory',anchor=tk.W,width=150)
        sale_tree.column('hsncategory',anchor=tk.W,width=150)
        sale_tree.column('igst',anchor=tk.W,width=120)
        sale_tree.column('cgst',anchor=tk.W,width=120)
        sale_tree.column('sgst',anchor=tk.W,width=120)
        sale_tree.column('qty',anchor=tk.W,width=120)
        sale_tree.column('amt',anchor=tk.W,width=120)
           
            
            
        sale_tree.heading("#0",text="",anchor="w")
        sale_tree.heading("Sr no",text="Medid",anchor="w")
        sale_tree.heading("company",text="Company",anchor="w")
        sale_tree.heading("brand",text="Brand",anchor="w")
        sale_tree.heading("drug",text="Drug",anchor="w")
           
        sale_tree.heading("categories",text="Categories",anchor="w")
        sale_tree.heading("packing",text="Packing",anchor="w",)
       
        #sale_tree.heading("billrate",text="Billrate",anchor="w")
        sale_tree.heading("salerate",text="Salerate",anchor="w")
      
        sale_tree.heading("exp",text="Exp",anchor="w")
        sale_tree.heading("shell",text="Shell",anchor="w")
        sale_tree.heading("taxcategory",text="Taxcategory",anchor="w")
        sale_tree.heading("hsncategory",text="Hsncategory",anchor="w")
        sale_tree.heading("igst",text="igst",anchor="w")
        sale_tree.heading("cgst",text="cgst",anchor="w")
        sale_tree.heading("sgst",text="sgst",anchor="w")
        sale_tree.heading("qty",text="qty",anchor="w")
        sale_tree.heading("amt",text="Amount",anchor="w")
        
       
#data


#striped row tag

        sale_tree.tag_configure('oddrow',background="white")
        sale_tree.tag_configure('evenrow',background="lightblue")
       
       
        
        
        credit_label=ctk.CTkLabel(self,text="Credit:",font=("Cascadia Mono SemiBold",17),fg_color="#DDDDDD",bg_color="#E2DFD0")
        credit_en=ctk.CTkEntry(self,width=50,height=32,font=("Cascadia",15),corner_radius=0)
        
        igst_label=ctk.CTkLabel(self,text="IGST:",font=("Cascadia Mono SemiBold",17),fg_color="#DDDDDD",bg_color="#E2DFD0")
        igst_en=ctk.CTkEntry(self,width=50,height=32,font=("Cascadia",15),corner_radius=0)
        
        sgst_label=ctk.CTkLabel(self,text="SGST:",font=("Cascadia Mono SemiBold",17),fg_color="#DDDDDD",bg_color="#E2DFD0")
        sgst_en=ctk.CTkEntry(self,width=50,height=32,font=("Cascadia",15),corner_radius=0)
        cgst_label=ctk.CTkLabel(self,text="CGST:",font=("Cascadia Mono SemiBold",17),fg_color="#DDDDDD",bg_color="#E2DFD0")
        cgst_en=ctk.CTkEntry(self,width=50,height=32,font=("Cascadia",15),corner_radius=0)
        Qty_label=ctk.CTkLabel(self,text=" Total Qty:",font=("Cascadia Mono SemiBold",17),fg_color="#DDDDDD",bg_color="#E2DFD0")
        qt_en=ctk.CTkEntry(self,width=50,height=32,font=("Cascadia",15),corner_radius=0)
        
        
        qty1_label=ctk.CTkLabel(self,text="Qty:",font=("Cascadia Mono SemiBold",17),fg_color="#DDDDDD",bg_color="#E2DFD0")
        
        
        qt1_en=ctk.CTkEntry(self,width=50,height=32,font=("Cascadia",15),corner_radius=0)
        qty1_label.place(x=380,y=220)
        qt1_en.place(x=430,y=220)
        
        gross_label=ctk.CTkLabel(self,text="Gross Value:",font=("Cascadia Mono SemiBold",17),fg_color="#DDDDDD",bg_color="#E2DFD0")
        gross_en=ctk.CTkEntry(self,width=53,height=32,font=("Cascadia",15),corner_radius=0,)
        
        dis_label=ctk.CTkLabel(self,text="Disc %:",font=("Cascadia Mono SemiBold",17),fg_color="#DDDDDD",bg_color="#E2DFD0")
        dis_en=ctk.CTkEntry(self,width=50,font=("Cascadia",15),height=32,corner_radius=0)
        
        
        pay_label=ctk.CTkLabel(self,text="Net Amt:",font=("Cascadia Mono SemiBold",17),fg_color="#DDDDDD",bg_color="#E2DFD0")
        pay_en=ctk.CTkEntry(self,width=50,font=("Cascadia",15),height=32,corner_radius=0)
        
        pay_method=tk.LabelFrame(self,text="Payment Type",font=("Cascadia Mono SemiBold",17),fg="#DDDDDD",bg="#DDDDDD",height=250,width=570,foreground="black")
       
        cash=ctk.CTkButton(pay_method,text="Cash",width=200,height=38,text_color="navyblue",corner_radius=0,fg_color="#D6EFD8",border_width=1,hover_color="#80AF81",command=Cash)
        
        online=ctk.CTkButton(pay_method,text="Credit",width=200,height=38,text_color="navyblue",corner_radius=0,fg_color="#FFD3B6",border_width=1,hover_color="#FF7F3E",command=credit)
        
        return1=ctk.CTkButton(pay_method,text="Return",width=300,height=38,text_color="navyblue",corner_radius=0,bg_color="#E2DFD0",fg_color="#E2BBE9",border_width=1,hover_color="#AF47D2",command=return_product)
        def scroll_text():
            global display_text, label1, x_position
            x_position -= 2  
            if x_position < -label1.winfo_width():  
                x_position  = 1900
            label1.place_configure(x=x_position)
            label1.after(40, scroll_text) 
        noti_fr=ctk.CTkFrame(patient_fr,width=1523,height=35,border_color="#1C1678",border_width=2,fg_color="navyblue",bg_color="#E2DFD0",corner_radius=4)
        
        conn = mysql.connect(host="localhost", user="root", password="dharm", charset="utf8", database="pharmacy", port=3307)  
        cur=conn.cursor()
        cur.execute("select drug ,exp from medicines")
        result=cur.fetchone()
        current_date = datetime.now().date()
        date_30_days_from_now = current_date + timedelta(days=30)

     
        
        results = cur.fetchall()

       
        filtered_drugs_exp_text = ""

       
        for result in results:
            drug = result[0]
            exp = result[1]
            if exp is not None:
                
                if isinstance(exp, str):
                    try:
                        exp = datetime.strptime(exp, "%Y-%m-%d").date()
                    except ValueError:
                        continue
                if current_date <= exp <= date_30_days_from_now:
                    filtered_drugs_exp_text += f"{drug} is near Expiry {exp}{' ' * 10}  "

     
        if filtered_drugs_exp_text:
            global display_text,label1,x_position
            display_text = filtered_drugs_exp_text.strip() + ' ' * 10
            label1 = ctk.CTkLabel(noti_fr, text=filtered_drugs_exp_text, fg_color="navyblue", text_color="white", bg_color="navyblue",corner_radius=0)
            x_position = 1900  
            label1.place(x=x_position, y=2)
            scroll_text()


            
        conn.commit()
        conn.close()
        noti_fr.place(x=1,y=795) 
       
        counter_1_bt.place(x=1,y=2)
        counter_2_bt.place(x=200,y=2)
        
        counter1_mini.place(x=1,y=37)
        counter1_mini2.place(x=70,y=37)
        counter2_mini.place(x=201,y=37)
        counter2_mini2.place(x=270,y=37)
       
        self.bill_no.place(x=900,y=80)
        self.bill_amt.place(x=900,y=140)
        
        patient_label.place(x=190,y=2)
        patient_en1.place(x=320,y=2)
        patient_no.place(x=320,y=35)
        doctor_place.place(x=700,y=2)
        dr_label.place(x=570,y=2)
        
       
        
        igst_label.place(x=25,y=600)
        igst_en.place(x=100,y=600) 
        sgst_label.place(x=25,y=650)
        sgst_en.place(x=100,y=650)
        cgst_label.place(x=25,y=700)
        cgst_en.place(x=100,y=700)
        Qty_label.place(x=200,y=600)  
        qt_en.place(x=330,y=600)   
        
        credit_label.place(x=210,y=650)
        credit_en.place(x=330,y=650)
        gross_label.place(x=580,y=600)
        gross_en.place(x=710,y=600)
        dis_label.place(x=580,y=650)
        dis_en.place(x=710,y=650)
        dis_en.bind("<KeyRelease>", update_net_amt)
        pay_label.place(x=580,y=700)
        pay_en.place(x=710,y=700)
        pay_method.place(x=1020,y=700)
        cash.place(x=10,y=5)
        online.place(x=240,y=5)
        return1.place(x=70,y=55)
        bt_frame.place(x=70,y=90)
        patient_fr.place(x=1,y=0)

class Order(ctk.CTkToplevel):
     def __init__(self):
        super().__init__()
        global time
        self.title("Order")
        self.width=self.winfo_screenwidth()
        self.height=self.winfo_screenheight()
        self.geometry(f"{self.width}x{self.height}+0+0")
        self.iconbitmap("38_113706.ico")
        self.grab_set()
        global pd_tree,my_tree,cod_en,packing_en,amt_en,rate_en,item_en,ordr_en
        
        order_fr=ctk.CTkFrame(self,width=1524,height=150,border_color="#1C1678",border_width=2,fg_color="#D8EFD3",bg_color="#DEF9C4",corner_radius=0) 
        order_heading=tk.Frame(self,width=1910,height=70,relief="raised",borderwidth=4,bg="#E1F7F5")
        order_heading.place(x=2,y=0)
        headinglabel=tk.Label(order_heading,text="Order to Supplier",font=('times new roman',29),fg='navyblue',bg="#E1F7F5",anchor="center")
        headinglabel.place(x=700,y=1)
        orderlabel=ctk.CTkLabel(order_fr,text="Medid:",font=("Cascadia Mono SemiBold",17))
        orderlabel.place(x=20,y=5)
        ordr_en=ctk.CTkEntry(order_fr,width=90,font=("Cascadia",15),height=30,corner_radius=0)
        ordr_en.place(x=120,y=5)
        def ord_date():
            
            today_date = datetime.today()
            dayname=today_date.strftime("%Y-%m-%d")
            date_fetch.configure(text = dayname)
        datelabel=ctk.CTkLabel(order_fr,text="Date:",font=("Cascadia Mono SemiBold",17))
        datelabel.place(x=20,y=40)
        global date_fetch
        date_fetch=ctk.CTkLabel(order_fr,text="Date:",font=("Cascadia Mono SemiBold",17))
        date_fetch.place(x=90,y=40)

        ord_date()
        def update_amount(event):
            
            try:
                rate = rate_en.get()
                quantity = qty_en.get()
                
                
                if rate == "" or quantity == "":
                    amt_en.delete(0, tk.END)
                    amt_en.insert(0, "")
                else:
                    rate = int(rate)
                    quantity = float(quantity)
                    amt = rate * quantity
                    amt_en.delete(0, tk.END)
                    amt_en.insert(0, f"{amt:.2f}")
                
        
            except ValueError:
                pass
        def select_ord_tree(event):
            global ord_tree
            selected=ord_tree.focus()
            values=ord_tree.item(selected, 'values')
            sup_id.delete(0,tk.END)
            sup_id.insert(0,values[0])
            sup_nm.delete(0,tk.END)
            sup_nm.insert(0,values[1])
            sup_no1.delete(0,tk.END)
            sup_no1.insert(0,values[3])
            sup_nm2.delete(0,tk.END)
            sup_nm2.insert(0,values[2])
            company=values[1]
         
            refresh_pd_tree(company)
        def refresh_pd_tree(company):
            global pd_tree

        
            for item in pd_tree.get_children():
                pd_tree.delete(item)

            conn = mysql.connect(host="localhost", user="root", password="dharm", charset="utf8", database="pharmacy", port=3307)
            cur = conn.cursor()
            if not company:
                cur.execute("SELECT * FROM medicines")
            else:
                cur.execute("SELECT * FROM medicines WHERE company = %s", (company,))
            
            records = cur.fetchall()

            for count, record in enumerate(records):
                stock = record[6]
                if stock in [0, 1, 2, 3, 4, 5]:
                    pd_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[10], record[11], record[12], record[13], record[14], record[15], record[16]), tags=("redrow",))
                elif count % 2 == 0:
                    pd_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[10], record[11], record[12], record[13], record[14], record[15], record[16]), tags=("evenrow",))
                else:
                    pd_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[10], record[11], record[12], record[13], record[14], record[15], record[16]), tags=("oddrow",))
            
            conn.commit()
            conn.close()
            pd_tree.update()
        def on_sup_nm_change(event):
            company = sup_nm.get()
            refresh_pd_tree(company)
                    
        def supplier_ser(event):
            root=ctk.CTkToplevel()
            root.geometry("420x230+400+80")
            root.resizable(False,False)
            
            global ord_tree
               
            patient_style=ttk.Style()
            patient_style.theme_use('default')

            patient_style.configure("Treeview", 
                        background = "#68D2E8",
                        rowheight = 25,
                        foreground="black",
                        fieldbackground = "white", font = ("Consolas", 12))
            patient_style.configure("Treeview",background=[('selected',"#347083")])
            patient_style.configure("Treeview.Heading", background="#CDE8E5",font = ("Consolas", 12))
           
            tree_fr=tk.Frame(root,borderwidth=3,height=200,width=500)
            tree_fr.pack_propagate(False)
            tree_fr.place(x=10,y=50)
            tree_scroll=tk.Scrollbar(tree_fr)
            tree_scroll.pack(side=tk.RIGHT,fill=tk.Y)
            tree_scrolx=tk.Scrollbar(tree_fr,orient=tk.HORIZONTAL)
            tree_scrolx.pack(side=tk.BOTTOM ,fill=tk.X)
            
            ord_tree=ttk.Treeview(tree_fr,yscrollcommand=tree_scroll.set,selectmode="extended",xscrollcommand=tree_scrolx.set)
            ord_tree.pack(fill="both",expand=True)
            tree_scroll.config(command=ord_tree.yview)
            tree_scrolx.config(command=ord_tree.xview)
            enter_nm=ctk.CTkLabel(root,text="Enter Name",font=("helvetica",15))
            enter_nm.place(x=20,y=4)
            ord_tree['columns']=('Sr no','suppliernm','Contact','phone','credit','email')
            ord_tree.column("#0",width=0,stretch=tk.NO)
            ord_tree.column('Sr no',anchor=tk.W,width=80)
            ord_tree.column('suppliernm',anchor=tk.W,width=160)
            ord_tree.column('Contact',anchor=tk.W,width=120)
            ord_tree.column('phone',anchor=tk.W,width=120)
            ord_tree.column('credit',anchor=tk.CENTER,width=120)
            ord_tree.column('email',anchor=tk.CENTER,width=120)
            ord_tree.heading("#0",text="",anchor="w")
            ord_tree.heading("Sr no",text="Sr no",anchor="w")
            ord_tree.heading("suppliernm",text="Company",anchor="w")
            ord_tree.heading("Contact",text="Contactperson",anchor="w")
            ord_tree.heading("phone",text="Phone",anchor="w")
           
            ord_tree.heading("credit",text="Credit",anchor="w")
            ord_tree.heading("email",text="Email",anchor="w",)
          
           
            ord_tree.tag_configure('oddrow',background="white")
            ord_tree.tag_configure('evenrow',background="lightblue")
            #patient_tree.bind("<KeyRelease>")
            ord_tree.bind("<ButtonRelease-1>", select_ord_tree) 
            enter_en=ctk.CTkEntry(root,width=150,height=28,font=("Cascadia",12))
            search_button = ctk.CTkButton(root, text="Search",width=20,corner_radius=20)
            enter_en.place(x=120,y=5)
            search_button.place(x=275, y=5)
            #search_button.bind("<ButtonRelease-1>",search) 
           
            conn = mysql.connect(host="localhost", user="root", password="dharm", charset="utf8", database="pharmacy", port=3307)

            cur = conn.cursor()
            cur.execute("SELECT supid ,name,contactperson,telephone,credit,email FROM supplier")
            records = cur.fetchall()
            for record in records:
                ord_tree.insert('','end',values=record)
              
                
            root.grab_set()
            root.mainloop()                 
        sup_label=ctk.CTkLabel(order_fr,text="Supplier:",font=("Cascadia Mono SemiBold",17))
        
        sup_label.place(x=240,y=5)
        
        sup_id=ctk.CTkEntry(order_fr,width=50,height=30,corner_radius=0,font=("Cascadia",15),)
        sup_id.place(x=330,y=5)
        sup_id.bind("<ButtonRelease-1>",supplier_ser)
        
        sup_nm=ctk.CTkEntry(order_fr,width= 150,height=30,corner_radius=0,font=("Cascadia",15),)
        sup_nm.place(x=380,y=5)
        sup_nm.bind("<KeyRelease>", on_sup_nm_change)
        sup_nm2=ctk.CTkEntry(order_fr,width=130,height=30,corner_radius=0,font=("Cascadia",15),)
        sup_nm2.place(x=530,y=5)
        sup_no1=ctk.CTkEntry(order_fr,width=200,height=30,corner_radius=0,font=("Cascadia",15),)
        sup_no1.place(x=330,y=34)
        global total_fetch,code_en
        
        Total_label=ctk.CTkLabel(order_fr,text="Total:",font=("Cascadia Mono SemiBold",24))
        Total_label.place(x=1200,y=90)
        
        total_fetch=ctk.CTkLabel(order_fr,text="",font=("Cascadia Mono SemiBold",24),fg_color="#E76F51",)
        total_fetch.place(x=1290,y=90)
        code_label=ctk.CTkLabel(order_fr,text="Comp.",font=("Cascadia Mono SemiBold",17))
        code_label.place(x=30,y=90)

        cod_en=ctk.CTkEntry(order_fr,width=80,height=30,corner_radius=0,font=("Cascadia",15),)
        cod_en.place(x=20,y=115)

        item_label=ctk.CTkLabel(order_fr,text="Item Description.",font=("Cascadia Mono SemiBold",17))
        item_label.place(x=160,y=90)
        
       
        item_en=ctk.CTkEntry(order_fr,width=350,height=30,corner_radius=0,font=("Cascadia",15),)
        item_en.place(x=100,y=115)
        
        packing_label=ctk.CTkLabel(order_fr,text="Packing.",font=("Cascadia Mono SemiBold",17))
        packing_label.place(x=453,y=90)
      
        packing_en=ctk.CTkEntry(order_fr,width=100,height=30,corner_radius=0,font=("Cascadia",15),)
        packing_en.place(x=448,y=115)
        
        rate_label=ctk.CTkLabel(order_fr,text="Qty.",font=("Cascadia Mono SemiBold",17))
        rate_label.place(x=570,y=90)
       
      
        rate_en=ctk.CTkEntry(order_fr,width=100,height=30,corner_radius=0,font=("Cascadia",15),)
        rate_en.place(x=545,y=115)
       
       
        qty_label=ctk.CTkLabel(order_fr,text="Rate.",font=("Cascadia Mono SemiBold",17))
        qty_label.place(x=670,y=90)
       
        global qty_en,value_en_1
     
        qty_en=ctk.CTkEntry(order_fr,width=100,height=30,corner_radius=0,font=("Cascadia",15),)
        qty_en.place(x=643,y=115)
        
        value_label=ctk.CTkLabel(order_fr,text="Value.",font=("Cascadia Mono SemiBold",17))
        value_label.place(x=770,y=90)
        
        
        
       
        value_en_1=ctk.CTkEntry(order_fr,width=100,height=30,corner_radius=0,font=("Cascadia",15),)
        value_en_1.place(x=740,y=115)
        
        amt_label=ctk.CTkLabel(order_fr,text="Amt.",font=("Cascadia Mono SemiBold",17))
        amt_label.place(x=860,y=90)
       
        amt_en=ctk.CTkEntry(order_fr,width=100,height=30,corner_radius=0,font=("Cascadia",15),)
        
        amt_en.place(x=830,y=115)
        
        rate_en.bind('<KeyRelease>', update_amount)
        qty_en.bind('<KeyRelease>', update_amount)
        side_frame=ctk.CTkFrame(self,width=470,height=470,border_width=2,border_color="navyblue",corner_radius=0)
        
        
        list_header=ctk.CTkFrame(side_frame,width=462,height=35,border_width=0,fg_color="#EEF5FF",bg_color="#EEF5FF",corner_radius=0)
        list_header.place(x=3,y=3)
        list_label=ctk.CTkLabel(list_header,text="List of Product",width=0,font=("'helvetica",20),text_color="#121481",anchor="center")
        list_label.place(x=3,y=2)
        def data_query():
            global pd_tree
            conn = mysql.connect(host="localhost", user="root", password="dharm", charset="utf8", database="pharmacy", port=3307)

            cur = conn.cursor()
            cur.execute("SELECT *FROM medicines")
            records = cur.fetchall()
            
            for count, record in enumerate(records):
                stock = record[6]  
                if stock == 0 or stock==1 or stock==2 or stock==3 or stock==4 or stock == 5:
                    pd_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[10], record[11], record[12], record[13], record[14],record[15],record[16]), tags=("redrow",))
                elif count % 2 == 0:
                    pd_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3],record[4],record[5],record[6],record[7],record[8],record[9],record[10],record[11],record[12],record[13],record[14],record[15],record[16]), tags=("evenrow",))
                else:
                    pd_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3],record[4],record[5],record[6],record[7],record[8],record[9],record[10],record[11],record[12],record[13],record[14],record[15],record[16]), tags=("oddrow",))
            conn.commit()
            conn.close()
       
        def confirm():
            global sql
            global total_fetch,total_item_amount,my_tree
            total_amt=0
            for child in my_tree.get_children():
                total_amt += float(my_tree.item(child, 'values')[9])
        
         
            total_fetch.configure(text=f"{total_amt:.2f}")
            
            conn = mysql.connect(host="localhost", user="root", password="dharm",charset="utf8", database="pharmacy", port=3307)
            
            cur = conn.cursor()
            for child in my_tree.get_children():
                values = my_tree.item(child, 'values')
                code=values[1]
                company = values[2]  
                item_des = values[3]  
                packing = values[4]  
                stock = values[5]  
                bill_rate = values[6] 
                sale_rate = values[7] 
                date = values[8] 
                amt=values[9]
                tot=total_fetch.cget("text")
                supp_id=sup_id.get()
                supp_nm=sup_nm.get()
                sup_no=sup_no1.get()
                sql = "INSERT INTO ord_to_supplier (med_id,company, item_des, packing, stock, bill_rate, sale_rate, date,amt,Total,suppliername,supplierphone,supid) VALUES (%s, %s, %s, %s, %s, %s, %s,%s,%s,%s,%s,%s,%s)"
                cur.execute(sql, (code,company, item_des, packing, stock, bill_rate, sale_rate, date,amt,tot,supp_nm,sup_no,supp_id))
            conn.commit()
            conn.close()
            m.showinfo("Order","Your Order is Genrated!")
            
            ord_img=Image.open("dyadavlastord.png").resize((900,900))                
                
            draw=ImageDraw.Draw(ord_img)
            text_font=ImageFont.truetype("tahomabd.ttf",18)
            text_font1=ImageFont.truetype("tahomabd.ttf",22)
           
           
            y_pos = 350
           
            x_positions = [10, 70, 365, 500, 620, 700,820]

  
            for index, child in enumerate(my_tree.get_children()[:10], start=1):
                values = my_tree.item(child, 'values')
                if values:
                  
                    draw.text((x_positions[0], y_pos + index * 20), str(values[0]), fill="black", font=text_font)
                    draw.text((x_positions[1], y_pos + index * 20), str(values[3]), fill="black", font=text_font)
                    draw.text((x_positions[2], y_pos + index * 20), str(values[4]), fill="black", font=text_font)
                    draw.text((x_positions[3], y_pos + index * 20), str(values[1]), fill="black", font=text_font)
                    draw.text((x_positions[4], y_pos + index * 20), str(values[5]), fill="black", font=text_font)
                    draw.text((x_positions[5], y_pos + index * 20), str(values[6]), fill="black", font=text_font)
                    draw.text((x_positions[6], y_pos + index * 20), str(values[9]), fill="black", font=text_font)

         
                        
          
            draw.text(xy=(85,145),text="HealthCare Chemist and Druggist",fill=(0,0,0),font=text_font)          
            draw.text(xy=(130,248),text=f"{sup_nm2.get()}",fill=(0,0,0),font=text_font)
                       
            draw.text(xy=(680,248),text=f"{sup_no1.get()}",fill=(0,0,0),font=text_font)
            draw.text(xy=(660,214),text=f"{date_fetch.cget('text')}",fill=(0,0,0),font=text_font)
            draw.text(xy=(810,845),text=f"{total_fetch.cget('text')}",fill=(0, 0, 0),font=text_font1)
            
         
            
            f2=tk.Frame(self,relief="raised",borderwidth=4,height=510,width=790)
            f2.place(x=900,y=200)
            f1=ctk.CTkFrame(f2,height=500,width=600,border_width=3)
            f1.pack()
            image_place=ctk.CTkImage(ord_img,size=(550,600))
            label1=ctk.CTkLabel(f1,text="",image=image_place)
            
            label1.pack()
            def send():
                ord_img.save("order_image.png")
                pywhatkit.sendwhats_image(sup_no1.get(), "order_image.png", "Here is your order", wait_time=20)
            def back_frame():
                f1.destroy()
                f2.destroy()  
            bt_1=ctk.CTkButton(f1,height=30,width=40,text="X",fg_color="#E4003A",hover="disabled",command=back_frame)
            bt_1.place(x=510,y=2)
            send_bt=ctk.CTkButton(f2,text="Send",width=200,height=38,text_color="navyblue",corner_radius=0,bg_color="#E2DFD0",fg_color="#FFC7ED",border_width=1,background_corner_colors=("black","black","black","black"),hover_color="#FF7F3E",command=send)
            send_bt.pack(side="bottom")    
        def Add_to_order():
            global pd_tree
            global qty_en, rate_en, pd_tree, date_fetch,ordr_en
            try:
                selected_item = pd_tree.focus()
                values = pd_tree.item(selected_item, 'values') 
                if values:
                    date_1 = date_fetch.cget("text")
                    
                    ordr_en.delete(0, tk.END)
                    ordr_en.insert(0, values[0])
                   
                    cod_en.delete(0, tk.END)
                    cod_en.insert(0, values[1])
                    
                    item_en.delete(0, tk.END)
                    item_en.insert(0, values[3])
                    
                    packing_en.delete(0, tk.END)
                    packing_en.insert(0, values[5])
                    
                    rate_en.delete(0, tk.END)
                    rate_en.insert(0, values[6])
                
                    qty_en.delete(0, tk.END)
                    qty_en.insert(0, values[7])
                    
                    value_en_1.delete(0, tk.END)
                    value_en_1.insert(0, values[8])
                    
                    amt_en.delete(0, tk.END)
                    
            except Exception as e:
                print("insert into order")

        def update_ord():
            global my_tree,cod_en, item_en, packing_en, rate_en, qty_en, value_en_1, amt_en, date_fetch
            try:
                selected=my_tree.focus()
                
                values = [
                    len(my_tree.get_children()) + 1,
                    ordr_en.get(),
                    cod_en.get(),
                    item_en.get(),
                    packing_en.get(),
                    rate_en.get(),
                    qty_en.get(),
                    value_en_1.get(),
                    date_fetch.cget("text"),
                    amt_en.get(),
                    
                ]
            
                my_tree.insert(selected, 'end', values=values)
            except Exception as e:
                print("frtch")
           
      
        style=ttk.Style()
        style.theme_use('default')

        style.configure("Treeview", 
                        background = "#68D2E8",
                        rowheight = 20,
                        foreground="black",
                        fieldbackground = "white", font = ("Consolas", 12))
        style.configure("Treeview",background=[('selected',"#347083")])
        style.configure("Treeview.Heading", background="#CDE8E5",font = ("Consolas", 12))
            # tree_frame=tk.Frame(root,width=100)
            # tree_frame.place(x=10,y=50)
        tree_fr=tk.Frame(side_frame,borderwidth=3,height=550,width=570)
        tree_fr.pack_propagate(False)
        tree_fr.place(x=3,y=47)
        tree_scroll=tk.Scrollbar(tree_fr)
        tree_scroll.pack(side=tk.RIGHT,fill=tk.Y)
        tree_scrolx=tk.Scrollbar(tree_fr,orient=tk.HORIZONTAL)
        tree_scrolx.pack(side=tk.BOTTOM ,fill=tk.X)
            
        pd_tree=ttk.Treeview(tree_fr,yscrollcommand=tree_scroll.set,selectmode="extended",xscrollcommand=tree_scrolx.set)
        pd_tree.pack(fill="both",expand=True)
        tree_scroll.config(command=pd_tree.yview)
        tree_scrolx.config(command=pd_tree.xview)
            
        pd_tree.column("#0",width=0,stretch=tk.NO)
        pd_tree['columns']=('Sr no','company','name','drug','categories','packing','stock','billrate','salerate','mfg','exp','shell','taxcategory','hsncategory','igst','cgst','sgst')
        pd_tree.column('Sr no',anchor=tk.W,width=80)
        pd_tree.column('company',anchor=tk.W,width=170)
        pd_tree.column('name',anchor=tk.W,width=120)
        pd_tree.column('drug',anchor=tk.W,width=120)
        pd_tree.column('categories',anchor=tk.CENTER,width=120)
        pd_tree.column('packing',anchor=tk.CENTER,width=120)
        pd_tree.column('stock',anchor=tk.W,width=120)
        pd_tree.column('billrate',anchor=tk.W,width=120)
        pd_tree.column('salerate',anchor=tk.W,width=120)
        pd_tree.column('mfg',anchor=tk.W,width=140)
        pd_tree.column('exp',anchor=tk.W,width=140)
        pd_tree.column('shell',anchor=tk.W,width=120)
        pd_tree.column('taxcategory',anchor=tk.W,width=150)
        pd_tree.column('hsncategory',anchor=tk.W,width=150)
        pd_tree.column('igst',anchor=tk.W,width=120)
        pd_tree.column('cgst',anchor=tk.W,width=120)
        pd_tree.column('sgst',anchor=tk.W,width=120)   
        pd_tree.heading("#0",text="",anchor="w")
        pd_tree.heading("Sr no",text="Sr no",anchor="w")
        pd_tree.heading("company",text="Company",anchor="w")
        pd_tree.heading("name",text="Brand",anchor="w")
        pd_tree.heading("drug",text="Drug",anchor="w")  
        pd_tree.heading("categories",text="Categories",anchor="w")
        pd_tree.heading("packing",text="Packing",anchor="w",)
        pd_tree.heading("stock",text="Stock",anchor="w")
        pd_tree.heading("billrate",text="Billrate",anchor="w")
        pd_tree.heading("salerate",text="Salerate",anchor="w")
        pd_tree.heading("mfg",text="Mfg",anchor="w")
        pd_tree.heading("exp",text="Exp",anchor="w")
        pd_tree.heading("shell",text="Shell",anchor="w")
        pd_tree.heading("taxcategory",text="Taxcategory",anchor="w")
        pd_tree.heading("hsncategory",text="Hsncategory",anchor="w")
        pd_tree.heading("igst",text="igst",anchor="w")
        pd_tree.heading("cgst",text="cgst",anchor="w")
        pd_tree.heading("sgst",text="sgst",anchor="w")
           
        pd_tree.tag_configure('oddrow',background="white")
        pd_tree.tag_configure('evenrow',background="lightblue")
        pd_tree.tag_configure('redrow', background="red")
        data_query()
        
        def remove_ord_tree():
            global my_tree
            selected_items = my_tree.selection()
    
  
            for item in selected_items:
                my_tree.delete(item)
                
      
        remove_bt=ctk.CTkButton(order_fr,text="Remove",width=100,height=34,text_color="navyblue",corner_radius=0,bg_color="#E2DFD0",fg_color="#E2BBE9",border_width=1,background_corner_colors=("black","black","black","black"),hover_color="#FF0000",command=remove_ord_tree)
        
        remove_bt.place(x=1000,y=50)
        
        add_bt=ctk.CTkButton(order_fr,text="Add",width=100,height=34,text_color="navyblue",corner_radius=0,bg_color="#E2DFD0",fg_color="#FFCBCB",border_width=1,background_corner_colors=("black","black","black","black"),hover_color="#FFB1B1",command=Add_to_order)
        
        add_bt.place(x=1000,y=10)
        
        
        confirf_bt=ctk.CTkButton(order_fr,text="Confirm",width=100,height=34,text_color="navyblue",corner_radius=0,bg_color="#E2DFD0",fg_color="#FCF8F3",border_width=1,background_corner_colors=("black","black","black","black"),hover_color="#FFD3B6",command=confirm)
        
        confirf_bt.place(x=1000,y=90)
        
        
        update_bt=ctk.CTkButton(order_fr,text="Update",width=100,height=34,text_color="navyblue",corner_radius=0,bg_color="#E2DFD0",fg_color="#FFD3B6",border_width=1,background_corner_colors=("black","black","black","black"),hover_color="#FF7F3E",command=update_ord)
        
        update_bt.place(x=1200,y=10)
       
        side_frame1=ctk.CTkFrame(self,width=950,height=450,border_width=2,border_color="navyblue",corner_radius=0)
        style=ttk.Style()
        style.theme_use('default')

        style.configure("Treeview", 
                        background = "#68D2E8",
                        rowheight = 20,
                        foreground="black",
                        fieldbackground = "white", font = ("Consolas", 12))
        style.configure("Treeview",background=[('selected',"#347083")])
        style.configure("Treeview.Heading", background="#CDE8E5",font = ("Consolas", 12))
            # tree_frame=tk.Frame(root,width=100)
            # tree_frame.place(x=10,y=50)
        tree_fr=tk.Frame(side_frame1,borderwidth=3,height=550,width=1170)
        tree_fr.pack_propagate(False)
        tree_fr.place(x=3,y=2)
        tree_scroll=tk.Scrollbar(tree_fr)
        tree_scroll.pack(side=tk.RIGHT,fill=tk.Y)
        tree_scrolx=tk.Scrollbar(tree_fr,orient=tk.HORIZONTAL)
        tree_scrolx.pack(side=tk.BOTTOM ,fill=tk.X)
            
        my_tree=ttk.Treeview(tree_fr,yscrollcommand=tree_scroll.set,selectmode="extended",xscrollcommand=tree_scrolx.set)
        my_tree.pack(fill="both",expand=True)
        tree_scroll.config(command=my_tree.yview)
        tree_scrolx.config(command=my_tree.xview)
            
        my_tree['columns']=('Sr no','med','name','categories','packing','stock','billrate','salerate','Date','amt',)
        my_tree.column("#0",width=0,stretch=tk.NO)
        my_tree.column('Sr no',anchor=tk.W,width=50)
        my_tree.column('med',anchor=tk.W,width=70)
        
        my_tree.column('name',anchor=tk.W,width=120)
        my_tree.column('categories',anchor=tk.CENTER,width=220)
        my_tree.column('packing',anchor=tk.CENTER,width=80)
        my_tree.column('stock',anchor=tk.W,width=90)
        my_tree.column('billrate',anchor=tk.W,width=100)
        my_tree.column('salerate',anchor=tk.W,width=100)
        my_tree.column('Date',anchor=tk.W,width=110)
        my_tree.column('amt',anchor=tk.W,width=90)
       
       
         
            
            
        my_tree.heading("#0",text="",anchor="w")
        my_tree.heading("Sr no",text="Sr no",anchor="w")
        my_tree.heading("med",text="Code",anchor="w")
       
        my_tree.heading("name",text="Company",anchor="w")
           
        my_tree.heading("categories",text="Item Description",anchor="w")
        my_tree.heading("packing",text="Packing",anchor="w",)
        my_tree.heading("stock",text="Stock",anchor="w")
        my_tree.heading("billrate",text="Billrate",anchor="w")
        my_tree.heading("salerate",text="Salerate",anchor="w")
        my_tree.heading("Date",text="Date",anchor="w")
        my_tree.heading("amt",text="Amt",anchor="w")
       
        
           
        my_tree.tag_configure('oddrow',background="white")
        my_tree.tag_configure('evenrow',background="lightblue")
        my_tree.tag_configure('redrow', background="red")
        

        
        
      
        side_frame.place(x=1050,y=207)
        side_frame1.place(x=5,y=207)
       
        order_fr.place(x=2,y=56)
class Purchase(ctk.CTkToplevel):
     def __init__(self):
        super().__init__()
        global time,my_tree,purchase_en,Bill_en,supplier_en,credit_en,billrate_en,salerate_en,mfg_en,exp_en,pack_en,qty_en,item_en,shell_en,igst_en,cgst_en,sgst_en
        self.title("Purchase")
        self.width=self.winfo_screenwidth()
        self.height=self.winfo_screenheight()
        self.geometry(f"{self.width}x{self.height}+0+0")
        self.iconbitmap("38_113706.ico")
        self.grab_set()
        order_heading=tk.Frame(self,width=1910,height=70,relief="raised",borderwidth=5,bg="#E1F7F5")
        order_heading.place(x=2,y=0)
        headinglabel=tk.Label(order_heading,text="Purchase",font=('times new roman',29),fg='navyblue',bg="#E1F7F5",anchor="center")
        headinglabel.place(x=760,y=0)
        patient_fr=ctk.CTkFrame(self,width=1527,height=210,border_color="#1C1678",border_width=2,fg_color="#D6EFD8",bg_color="#E2DFD0",corner_radius=0)
        Purchase_label=ctk.CTkLabel(patient_fr,text="Purchase Type:",font=("Cascadia Mono SemiBold",17))
        values=["Cash Purchase","Credit Purchase"]
        v1=tk.StringVar()
        v1.set("")
        purchase_en=ctk.CTkComboBox(patient_fr,width=150,height=30,font=("Cascadia",15),variable=v1,values=values,corner_radius=0)
        
        def pur_date():
            
            today_date = datetime.today()
            dayname=today_date.strftime("%Y-%m-%d")
            date_fetch.configure(text = dayname)
        
        date_fetch=ctk.CTkLabel(patient_fr,text="Date:",font=("Cascadia Mono SemiBold",17))      
        Date_label1=ctk.CTkLabel(patient_fr,text="Date:",font=("Cascadia Mono SemiBold",17))
        bill_label1=ctk.CTkLabel(patient_fr,text="Company:",font=("Cascadia Mono SemiBold",17))
        supplier_label1=ctk.CTkLabel(patient_fr,text="Supplier:",font=("Cascadia Mono SemiBold",17))
        
        Bill_en=ctk.CTkEntry(patient_fr,width=80,font=("Cascadia",15),height=30,corner_radius=0)   
        supplier_enid=ctk.CTkEntry(patient_fr,font=("Cascadia",15),width=200,height=30,corner_radius=0)
        supplier_ennm=ctk.CTkEntry(patient_fr,font=("Cascadia",15),width=200,height=30,corner_radius=0)
        credit_label1=ctk.CTkLabel(patient_fr,text="Credit:",font=("Cascadia Mono SemiBold",17))
        credit_en=ctk.CTkEntry(patient_fr,width=80,height=30,corner_radius=0)
        item_label1=ctk.CTkLabel(patient_fr,text="Item:",font=("Cascadia Mono SemiBold",17))
        billrate_label1=ctk.CTkLabel(patient_fr,text="Bill Rate:",font=("Cascadia Mono SemiBold",17))
        billrate_en=ctk.CTkEntry(patient_fr,width=80,font=("Cascadia",15),height=30,corner_radius=0)
        salerate_label1=ctk.CTkLabel(patient_fr,text="Sale Rate:",font=("Cascadia Mono SemiBold",17))
        salerate_en=ctk.CTkEntry(patient_fr,width=80,font=("Cascadia",15),height=30,corner_radius=0)
        mfg_label1=ctk.CTkLabel(patient_fr,text="Mfg Dt:",font=("Cascadia Mono SemiBold",17)) 
        exp_label1=ctk.CTkLabel(patient_fr,text="Exp Dt:",font=("Cascadia Mono SemiBold",17))
        mfg_en=ctk.CTkEntry(patient_fr,width=80,font=("Cascadia",15),height=30,corner_radius=0)
        exp_en=ctk.CTkEntry(patient_fr,width=80,font=("Cascadia",15),height=30,corner_radius=0)
        
        packing_label1=ctk.CTkLabel(patient_fr,text="Packing:",font=("Cascadia Mono SemiBold",17))
        pack_en=ctk.CTkEntry(patient_fr,width=100,font=("Cascadia",15),height=30,corner_radius=0)
        
        qty_label1=ctk.CTkLabel(patient_fr,text="Qty:",font=("Cascadia Mono SemiBold",17))
        qty_en=ctk.CTkEntry(patient_fr,width=80,font=("Cascadia",15),height=30,corner_radius=0)
        
        hsn_label1=ctk.CTkLabel(patient_fr,text="HSN No:",font=("Cascadia Mono SemiBold",17),)
        hsn_en=ctk.CTkEntry(patient_fr,width=80,font=("Cascadia",15),height=30,corner_radius=0)
        
        batch_label1=ctk.CTkLabel(patient_fr,text="Total:",font=("Cascadia Mono SemiBold",17))
        
        batch_en=ctk.CTkEntry(patient_fr,width=80,font=("Cascadia",15),height=30,corner_radius=0)
        
        med_label1=ctk.CTkLabel(patient_fr,text="Med id:",font=("Cascadia Mono SemiBold",17))
        
        med_en=ctk.CTkEntry(patient_fr,width=80,font=("Cascadia",15),height=30,corner_radius=0)
        shell_label1=ctk.CTkLabel(patient_fr,text="Shell:",font=("Cascadia Mono SemiBold",17))
        
        
        
        
        shell_en=ctk.CTkEntry(patient_fr,width=80,height=30,font=("Cascadia",15),corner_radius=0)
        
       
        item_en=ctk.CTkEntry(patient_fr,width=280,font=("Cascadia",15),height=30,corner_radius=0)
        
        
        
        def data_query():
            global my_tree
        
            conn = mysql.connect(host="localhost", user="root", password="dharm", charset="utf8", database="pharmacy", port=3307)

            cur = conn.cursor()
            cur.execute("SELECT *FROM  ord_to_supplier")
            records = cur.fetchall()
            
            for count, record in enumerate(records):
                if count %2==0:
                    my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[13], record[11], record[1], record[2], record[3],record[4],record[5],record[6],record[7],record[8],record[9]), tags=("evenrow",))
                else:
                    my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[13], record[11], record[1], record[2], record[3],record[4],record[5],record[6],record[7],record[8],record[9]), tags=("oddrow",))
            conn.commit()
            conn.close()
            
        def Add_to_purchase():
            global my_tree
            try:
        
                selected_item = my_tree.focus()
                values = my_tree.item(selected_item, 'values') 

                if values:
                    med_en.delete(0, tk.END)
                    med_en.insert(0, values[3])
                    Bill_en.delete(0, tk.END)
                    Bill_en.insert(0, values[4])
                    
                    item_en.delete(0, tk.END)
                    item_en.insert(0, values[5])
                  
                    pack_en.delete(0, tk.END)
                    pack_en.insert(0, values[6])
                    
                    qty_en.delete(0, tk.END)
                    qty_en.insert(0, values[7])
                    
                    billrate_en.delete(0, tk.END)
                    billrate_en.insert(0, values[8])
                
                    salerate_en.delete(0, tk.END)
                    salerate_en.insert(0, values[9])
                    supplier_enid.delete(0, tk.END)
                    supplier_enid.insert(0, values[1])
                    supplier_ennm.delete(0, tk.END)
                    supplier_ennm.insert(0, values[2])
                    batch_en.delete(0, tk.END)
                    batch_en.insert(0, values[11])
                    
                    
                  
            except Exception as e:
                print(e)
        
        def update_to_product():
            
           
            bill_pur=billrate_en.get()
            sale_pur=salerate_en.get()
            mfg=str(mfg_en.get())
            exp=str(exp_en.get())
            supp_id=supplier_enid.get()
            med=med_en.get()
            credit=credit_en.get()if credit_en.get() != '' else None
            Dat_pur=date_fetch.cget('text')
            Total=batch_en.get()
            purchase_type=purchase_en.get()
            shell1=shell_en.get()
            if mfg=="" or exp=="":
                m.showerror("Empty","Manufacture or Expiry are empty please check")
                return
                
            if bill_pur=="" or sale_pur=="":
                m.showerror("Empty","billrate or salerate are empty please check")
                return
             

            try:
                bill_pur = float(bill_pur)
            except ValueError:
                m.showerror("Invalid", "Billrate field must contain a valid number")
                return

            try:
                sale_pur = float(sale_pur)
            except ValueError:
                m.showerror("Invalid", "Salerate field must contain a valid number")
                return
            if mfg.strip() == "":
                m.showerror("Invalid", "Manufacturing date cannot be empty. Please provide a valid date.")
                return

            if exp.strip() == "":
                m.showerror("Invalid", "Expiration date cannot be empty. Please provide a valid date.")
                return
          
                
            conn = mysql.connect(host="localhost", user="root", password="dharm", charset="utf8", database="pharmacy", port=3307)

            cur = conn.cursor()
            
            bill_up=f" update medicines set Billrate='{bill_pur}',salerate='{sale_pur}' where med_id={med}"
            exp1=f" update medicines set exp='{exp}' where med_id={med}"
            mg1=f" update medicines set mfg='{mfg}' where med_id={med}"
            shell=f" update medicines set shell='{shell1}' where med_id={med}"
            
            
            cur.execute(exp1)
            cur.execute(mg1)
            cur.execute(shell)
            conn.commit()
            cur.execute(bill_up)
            cur.execute(f"SELECT stock FROM medicines WHERE med_id='{med}'")
            result=cur.fetchone()
            if result:
               stock = result[0]
               newstock = int(stock) + int(qty_en.get())
               ins=f" update medicines set stock='{newstock}' where med_id={med}"
               cur.execute(ins)
                
            conn.commit()
            
            cur.execute("INSERT INTO purchase (medid,supid,qty,credit,Date,amt,purchasetype) VALUES (%s, %s, %s,%s,%s,%s,%s)",(med,supp_id,qty_en.get(),credit,Dat_pur,Total,purchase_type))
            
            delete_query = f"DELETE FROM ord_to_supplier WHERE med_id={med}"
            cur.execute(delete_query)
            conn.commit()
            
            m.showinfo("updated","stock is updated")
            mfg_en.delete(0,tk.END)
            exp_en.delete(0,tk.END)
            shell_en.delete(0,tk.END)
            selected_item = my_tree.focus()
            
            my_tree.delete(selected_item) 
            conn.close()
        side_frame1=ctk.CTkFrame(self,width=940,height=280,border_width=2,border_color="navyblue",corner_radius=0)
        
        list_header=ctk.CTkFrame(side_frame1,width=930,height=35,border_width=0,fg_color="#EEF5FF",bg_color="#EEF5FF",corner_radius=0)
        list_header.place(x=3,y=3)
        list_label=ctk.CTkLabel(list_header,text="You Ordered ",width=0,font=("'helvetica",24),text_color="#121481",anchor="center")
        list_label.place(x=3,y=2)
        
        style=ttk.Style()
        style.theme_use('default')

        style.configure("Treeview", 
                        background = "#68D2E8",
                        rowheight = 20,
                        foreground="black",
                        fieldbackground = "white", font = ("Consolas", 12))
        style.configure("Treeview",background=[('selected',"#347083")])
        style.configure("Treeview.Heading", background="#CDE8E5",font = ("Consolas", 12))
         
        tree_fr=tk.Frame(side_frame1,borderwidth=3,height=300,width=1160)
        tree_fr.pack_propagate(False)
        tree_fr.place(x=3,y=47)
        tree_scroll=tk.Scrollbar(tree_fr)
        tree_scroll.pack(side=tk.RIGHT,fill=tk.Y)
        tree_scrolx=tk.Scrollbar(tree_fr,orient=tk.HORIZONTAL)
        tree_scrolx.pack(side=tk.BOTTOM ,fill=tk.X)
            
        my_tree=ttk.Treeview(tree_fr,yscrollcommand=tree_scroll.set,selectmode="extended",xscrollcommand=tree_scrolx.set)
        my_tree.pack(fill="both",expand=True)
        tree_scroll.config(command=my_tree.yview)
        tree_scrolx.config(command=my_tree.xview)
            
        my_tree['columns']=('Sr no','supno','supnm','medid','name','categories','packing','stock','billrate','salerate','Date','amt',)
        my_tree.column("#0",width=0,stretch=tk.NO)
        my_tree.column('Sr no',anchor=tk.W,width=80)
        my_tree.column('supno',anchor=tk.W,width=110)
        my_tree.column('supnm',anchor=tk.W,width=120)
        my_tree.column('medid',anchor=tk.W,width=80)
        
        my_tree.column('name',anchor=tk.W,width=120)
        my_tree.column('categories',anchor=tk.CENTER,width=220)
        my_tree.column('packing',anchor=tk.CENTER,width=80)
        my_tree.column('stock',anchor=tk.W,width=90)
        my_tree.column('billrate',anchor=tk.W,width=100)
        my_tree.column('salerate',anchor=tk.W,width=100)
        my_tree.column('Date',anchor=tk.W,width=110)
        my_tree.column('amt',anchor=tk.W,width=90)
       
       
         
            
            
        my_tree.heading("#0",text="",anchor="w")
        my_tree.heading("Sr no",text="Sr no",anchor="w")
        my_tree.heading("supno",text="Supp Id",anchor="w")
        my_tree.heading("supnm",text="Supp Name",anchor="w")
        my_tree.heading("medid",text="Medid",anchor="w")
       
        my_tree.heading("name",text="Company",anchor="w")
           
        my_tree.heading("categories",text="Item Description",anchor="w")
        my_tree.heading("packing",text="Packing",anchor="w",)
        my_tree.heading("stock",text="Stock",anchor="w")
        my_tree.heading("billrate",text="Billrate",anchor="w")
        my_tree.heading("salerate",text="Salerate",anchor="w")
        my_tree.heading("Date",text="Date",anchor="w")
        my_tree.heading("amt",text="Amt",anchor="w")
       
        
           
        my_tree.tag_configure('oddrow',background="white")
        my_tree.tag_configure('evenrow',background="lightblue")
        data_query()

        add_bt=ctk.CTkButton(patient_fr,text="Add",width=100,height=34,text_color="navyblue",corner_radius=0,bg_color="#E2DFD0",fg_color="#FF6969",border_width=1,background_corner_colors=("black","black","black","black"),hover_color="#C80036",command=Add_to_purchase)
        
        add_bt.place(x=1000,y=150)
       
        
    
        
        
        update_bt=ctk.CTkButton(patient_fr,text="Update",width=100,height=34,text_color="navyblue",corner_radius=0,bg_color="#E2DFD0",fg_color="#FFE6E6",border_width=1,background_corner_colors=("black","black","black","black"),hover_color="#AD88C6",command=update_to_product)
        
        update_bt.place(x=1100,y=150)
        pur_date()
        Purchase_label.place(x=10,y=2)
        Date_label1.place(x=1200,y=2)
        date_fetch.place(x=1250,y=2)
        purchase_en.place(x=170,y=3)
        bill_label1.place(x=10,y=50)
        Bill_en.place(x=100,y=50)
        med_label1.place(x=200,y=50)
        med_en.place(x=290,y=50)
        supplier_label1.place(x=340,y=3)
        supplier_enid.place(x=430,y=3)
        supplier_ennm.place(x=430,y=30)
        credit_label1.place(x=700,y=50)
        credit_en.place(x=780,y=50)
        item_label1.place(x=10,y=100)
        item_en.place(x=100,y=100)
        billrate_label1.place(x=400,y=100)
        billrate_en.place(x=500,y=100)
        salerate_label1.place(x=400,y=130)
        salerate_en.place(x=500,y=130)
        mfg_label1.place(x=630,y=100)
        exp_label1.place(x=630,y=130)
        mfg_en.place(x=700,y=100)
        exp_en.place(x=700,y=130)
        packing_label1.place(x=10,y=160)
        pack_en.place(x=100,y=160)
        qty_label1.place(x=250,y=160)
        qty_en.place(x=300,y=160)
        hsn_label1.place(x=400,y=160)
        hsn_en.place(x=500,y=160)
        batch_label1.place(x=900,y=50)
        batch_en.place(x=1000,y=50)
       
        
        shell_label1.place(x=630,y=160)
        shell_en.place(x=700,y=160)
        
       
        patient_fr.place(x=1,y=57)
        side_frame1.place(x=1,y=261)  
class Purchase_report(ctk.CTkToplevel):
     def __init__(self):
        super().__init__()
        global time
        self.title("Purchase report")
        self.width=self.winfo_screenwidth()
        self.height=self.winfo_screenheight()
        self.geometry(f"{self.width}x{self.height}+0+0")
        self.iconbitmap("38_113706.ico")
        self.grab_set()
        f1=tk.Frame(self,width=1905,height=175,relief="ridge",borderwidth=7,border=4,background="#E1F7F5", highlightcolor="navyblue")
       
        customer_label=ctk.CTkLabel(f1,text="license no:",font=("Cascadia Mono SemiBold",18),text_color="#1C1678")
        customer_label.place(x=520,y=26)
        
        lic_h=ctk.CTkLabel(f1,text="123456",font=("Cascadia Mono SemiBold",18),text_color="#1C1678")
        lic_h.place(x=650,y=26)
        
        medn_h=ctk.CTkLabel(f1,text="Health Care Chemist and Druggist ",font=("Cascadia Mono SemiBold",18),text_color="#1C1678")
        medn_h.place(x=270,y=75)     
        medical_logo=ctk.CTkImage(light_image=Image.open("pharmacy.png"),dark_image=Image.open("pharmacy.png"),size=(140,130))
        med_label_image1=ctk.CTkLabel(f1,text="",image=medical_logo)
        med_label_image1.place(x=1350,y=3)
        mediine=ctk.CTkImage(light_image=Image.open("home2-removebg-preview.png"),dark_image=Image.open("home2-removebg-preview.png"),size=(200,90))
        med_label_image2=ctk.CTkLabel(f1,text="",image=mediine)
        med_label_image2.place(x=3,y=40)
        mediine1=ctk.CTkImage(light_image=Image.open("home2-removebg-preview222.png"),dark_image=Image.open("home2-removebg-preview222.png"),size=(200,90))
        med_label_image3=ctk.CTkLabel(f1,text="",image=mediine1)
        med_label_image3.place(x=3,y=1)  
        logo_nm=ctk.CTkLabel(med_label_image3,text="Med Connect",font=("Cascadia Mono SemiBold",22),text_color="#1C1678")
        logo_nm.place(x=27,y=45)
        customer_en=ctk.CTkLabel(f1,text="",font=("Cascadia Mono SemiBold",18),text_color="#1C1678")
        customer_en.place(x=650,y=26)
        medical_name12=ctk.CTkLabel(f1,text="",font=("Cascadia Mono SemiBold",18),text_color="#1C1678")
        medical_name12.place(x=300,y=90)
        f1.place(x=2,y=3)
        
        
        def date1():
        
            today_date = datetime.today()
            day = today_date.day
            month = today_date.month
            year = today_date.year
            # day1=datetime.now()
            dayname=today_date.strftime("%A")
            date_label.configure(text = f"{day}/{month}/{year} ({dayname})")
        
        date_label=ctk.CTkLabel(self,text="date",text_color="#1C1678",fg_color="transparent",bg_color="#E1F7F5",font=("Cascadia Mono SemiBold",17))
        
        def time12():
            self.hours = strftime("%I")  #I - for 12 hours clock
            self.minute = strftime("%M")
            self.second = strftime("%S")
            self.am_pm = strftime("%p")

            time_label.configure(text = f"{self.hours}:{self.minute}:{self.second} {self.am_pm}")
            time_label.after(1000,time12)
            
            
            
        time_label=ctk.CTkLabel(self,text="",text_color="#1C1678",fg_color="transparent",bg_color="#E1F7F5",font=("Cascadia Mono SemiBold",17))
        
        date_label.place(x=250,y=30)
       
        time_label.place(x=1200,y=100)
        
        
      
        date1()
        time12()
       
        side_frame=tk.Frame(self,width=885,height=750,relief="raised",borderwidth=4)
        list_header=ctk.CTkFrame(side_frame,width=700,height=35,border_width=0,fg_color="#EEF5FF",bg_color="#EEF5FF",corner_radius=0)
        list_label=ctk.CTkLabel(list_header,text="Purchase product",width=0,font=("'helvetica",30),text_color="#121481",anchor="center")
        def purchase_rep_data():
            global my_tree
            conn = mysql.connect(host="localhost", user="root", password="dharm", charset="utf8", database="pharmacy", port=3307)

            cur = conn.cursor()
            cur.execute("SELECT p.srno,s.name,p.medid,m.drug,p.qty,m.Billrate,m.salerate,m.mfg,m.exp,p.credit,p.purchasetype,p.amt,p.Date from purchase p join supplier s on p.supid = s.supid join medicines m ON p.medid = m.med_id" )
            records = cur.fetchall()
            
            for count, record in enumerate(records):
                if count%2==0:
                    my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[10], record[11],record[12]), tags=("evenrow",))
                else:
                    my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3],record[4],record[5],record[6],record[7],record[8],record[9],record[10],record[11],record[12]), tags=("oddrow",))
        global my_tree       
        style=ttk.Style()
        style.theme_use('default')

        style.configure("Treeview", 
                        background = "#68D2E8",
                        rowheight = 25,
                        foreground="black",
                        fieldbackground = "white", font = ("Consolas", 12))
        style.configure("Treeview",background=[('selected',"#347083")])
        style.configure("Treeview.Heading", background="#CDE8E5",font = ("Consolas", 12))
        tree_fr=tk.Frame(side_frame,borderwidth=3,height=690,width=860)
        tree_fr.pack_propagate(False)
        tree_fr.place(x=3,y=47)
        tree_scroll=tk.Scrollbar(tree_fr)
        tree_scroll.pack(side=tk.RIGHT,fill=tk.Y)
        tree_scrolx=tk.Scrollbar(tree_fr,orient=tk.HORIZONTAL)
        tree_scrolx.pack(side=tk.BOTTOM ,fill=tk.X)   
        my_tree=ttk.Treeview(tree_fr,yscrollcommand=tree_scroll.set,selectmode="extended",xscrollcommand=tree_scrolx.set)
        my_tree.pack(fill="both",expand=True)
        tree_scroll.config(command=my_tree.yview)
        tree_scrolx.config(command=my_tree.xview)     
        my_tree['columns']=('Sr no','suppname','medid','item','stock','bill','sale','mfg','exp','credit','purchasetype','amt','date')
        my_tree.column("#0",width=0,stretch=tk.NO)
        my_tree.column('Sr no',anchor=tk.W,width=90)
        my_tree.column('suppname',anchor=tk.W,width=120)
        my_tree.column('medid',anchor=tk.W,width=120)
        my_tree.column('item',anchor=tk.CENTER,width=150)
        my_tree.column('stock',anchor=tk.CENTER,width=120)
        my_tree.column('bill',anchor=tk.W,width=120)
        my_tree.column('sale',anchor=tk.W,width=120)
        my_tree.column('mfg',anchor=tk.W,width=140)
        my_tree.column('exp',anchor=tk.W,width=140)
        my_tree.column('credit',anchor=tk.W,width=120)
        my_tree.column('purchasetype',anchor=tk.W,width=140)
        my_tree.column('amt',anchor=tk.W,width=120)
        my_tree.column('date',anchor=tk.W,width=120)    
        my_tree.heading("#0",text="",anchor="w")
        my_tree.heading("Sr no",text="Sr no",anchor="w")
        my_tree.heading("suppname",text="Suppliername",anchor="w")
        my_tree.heading("medid",text="Medid",anchor="w") 
        my_tree.heading("item",text="item",anchor="w")
        my_tree.heading("stock",text="Qty",anchor="w",)
        my_tree.heading("bill",text="Billrate",anchor="w")
        my_tree.heading("sale",text="Salerate",anchor="w")
        my_tree.heading("mfg",text="Mfg",anchor="w")
        my_tree.heading("exp",text="Exp",anchor="w")
        my_tree.heading("credit",text="Credit Days",anchor="w")
        my_tree.heading("purchasetype",text="Purchasetype",anchor="w")
        my_tree.heading("amt",text="Amount",anchor="w")
        my_tree.heading("date",text="Date",anchor="w") 
        my_tree.tag_configure('oddrow',background="white")
        my_tree.tag_configure('evenrow',background="lightblue")
        purchase_rep_data()
        grp_fr=tk.Frame(self,width=644,height=400,relief="groove",borderwidth=4)
        mon_fr=tk.Frame(self,width=642,height=50,relief="groove",borderwidth=4)
        def update_graph(month=None):
            month = month_en.get()
            if not month:
                print("Month is empty")
                return
            conn = mysql.connect(host="localhost", user="root", password="dharm", charset="utf8", database="pharmacy", port=3307)

            cur = conn.cursor()
            query = """
            SELECT m.drug, SUM(p.qty), p.Date
            FROM purchase p
            JOIN medicines m ON p.medid = m.med_id
            WHERE MONTH(p.Date) = %s
            GROUP BY m.drug
        """
            cur.execute(query, (month,))
            drug_1=[]
            qty1=[]
            while True:
                result = cur.fetchone()
                if result is None:
                    break
                drug = str(result[0])
                drug_1.append(drug)
                qty = str(result[1])
                qty1.append(qty)
            qty1 = [int(qty) for qty in qty1]
          
            for widget in grp_fr.winfo_children():
                widget.destroy()

            if not drug_1:
           
                no_data_label = ctk.CTkLabel(grp_fr, text="No data available for the selected month", font=("Cascadia", 15))
                no_data_label.place(x=2,y=2)
                return
            
            bar_width = 0.07 
            max_value = max(qty1)
            min_value = min(qty1)

            spacing = 0.1   
            x = range(len(drug_1))
            x_pos = [i * (bar_width + spacing) for i in x]

            colors = ['green' if qty == max_value else 'red' if qty == min_value else 'red' for qty in qty1]
            fig, ax = plt.subplots(figsize=(5, 4))
            ax.bar(x_pos, qty1, color=colors, width=bar_width, align='center')
            ax.set_xlabel('Drug')
            ax.set_ylabel('Quantity')
            ax.set_title('Purchase Report')
            ax.set_xticks(x_pos)
            ax.set_xticklabels(drug_1)
            yticks = list(range(2, max(qty1) + 5, 5))
            ax.set_yticks(yticks)
            handles = [plt.Line2D([0], [0], color='red', lw=4), plt.Line2D([0], [0], color='green', lw=4)]
            labels = ['Max Quantity', 'Min Quantity']
            ax.legend(handles, labels, loc='best',fontsize=6, handlelength=2, handletextpad=1)
            ax.set_ylim(bottom=0)
            for widget in grp_fr.winfo_children():
                widget.destroy()
            canvas = FigureCanvasTkAgg(fig, master=grp_fr)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=tk.BOTH,expand=True)
            plt.close('all') 
        def initialize_graph():
            current_month = datetime.now().month
            month_en.insert(0, str(current_month))
            update_graph(current_month)           
        month_en=ctk.CTkEntry(mon_fr,width=40,font=("Cascadia",15),height=15,corner_radius=0) 
        month_en.place(x=100,y=2)
        mon_label=ctk.CTkLabel(mon_fr,text="Enter Month:",width=0,font=("'helvetica",15),text_color="#121481",anchor="center")
        mon_label.place(x=10,y=2)
        update_btn = ctk.CTkButton(mon_fr, text="Search",width=20, command=update_graph)
        update_btn.place(x=180, y=2)
        grp_fr.place(x=16,y=230)
        mon_fr.place(x=16,y=180)
        initialize_graph()
        side_frame.place(x=900,y=180)
        list_header.place(x=2,y=2)
        list_label.place(x=2,y=3)
        list_header.place(x=2,y=2)
        list_label.place(x=2,y=3)     
class product_report(ctk.CTkToplevel):
     def __init__(self):
        super().__init__()
        global time
        global my_tree
        self.title("Stock Report")
        self.width=self.winfo_screenwidth()
        self.height=self.winfo_screenheight()
        self.geometry(f"{self.width}x{self.height}+0+0")
        self.iconbitmap("38_113706.ico")
        self.grab_set()
        f1=tk.Frame(self,width=1905,height=175,relief="ridge",borderwidth=7,border=4,background="#E1F7F5", highlightcolor="navyblue")
        customer_label=ctk.CTkLabel(f1,text="license no:",font=("Cascadia Mono SemiBold",18),text_color="#1C1678")
        customer_label.place(x=520,y=26)
        lic_h=ctk.CTkLabel(f1,text="123456",font=("Cascadia Mono SemiBold",18),text_color="#1C1678")
        lic_h.place(x=650,y=26)
        medn_h=ctk.CTkLabel(f1,text="Health Care Chemist and Druggist ",font=("Cascadia Mono SemiBold",18),text_color="#1C1678")
        medn_h.place(x=270,y=75)         
        medical_logo=ctk.CTkImage(light_image=Image.open("pharmacy.png"),dark_image=Image.open("pharmacy.png"),size=(140,130))
        med_label_image1=ctk.CTkLabel(f1,text="",image=medical_logo)
        med_label_image1.place(x=1350,y=3)
        mediine=ctk.CTkImage(light_image=Image.open("home2-removebg-preview.png"),dark_image=Image.open("home2-removebg-preview.png"),size=(200,90))
        med_label_image2=ctk.CTkLabel(f1,text="",image=mediine)
        med_label_image2.place(x=3,y=40)
        mediine1=ctk.CTkImage(light_image=Image.open("home2-removebg-preview222.png"),dark_image=Image.open("home2-removebg-preview222.png"),size=(200,90))
        med_label_image3=ctk.CTkLabel(f1,text="",image=mediine1)
        med_label_image3.place(x=3,y=1)   
        logo_nm=ctk.CTkLabel(med_label_image3,text="Med Connect",font=("Cascadia Mono SemiBold",22),text_color="#1C1678")
        logo_nm.place(x=27,y=45)
        customer_en=ctk.CTkLabel(f1,text="",font=("Cascadia Mono SemiBold",18),text_color="#1C1678")
        customer_en.place(x=650,y=26)
        medical_name12=ctk.CTkLabel(f1,text="",font=("Cascadia Mono SemiBold",18),text_color="#1C1678")
        medical_name12.place(x=300,y=90)
        f1.place(x=2,y=3)
        def date1():
        
            today_date = datetime.today()
            day = today_date.day
            month = today_date.month
            year = today_date.year
            # day1=datetime.now()
            dayname=today_date.strftime("%A")
            date_label.configure(text = f"{day}/{month}/{year} ({dayname})")
        
        date_label=ctk.CTkLabel(self,text="date",text_color="#1C1678",fg_color="transparent",bg_color="#E1F7F5",font=("Cascadia Mono SemiBold",17))
        
        def time12():
            self.hours = strftime("%I") 
            self.minute = strftime("%M")
            self.second = strftime("%S")
            self.am_pm = strftime("%p")
            time_label.configure(text = f"{self.hours}:{self.minute}:{self.second} {self.am_pm}")
            time_label.after(1000,time12)  
        time_label=ctk.CTkLabel(self,text="",text_color="#1C1678",fg_color="transparent",bg_color="#E1F7F5",font=("Cascadia Mono SemiBold",17))
        date_label.place(x=250,y=30)
        time_label.place(x=1200,y=100)
        date1()
        time12()
        def check_stock():
            name = name_en.get()
            conn = mysql.connect(host="localhost", user="root", password="dharm", charset="utf8", database="pharmacy", port=3307)
            cur = conn.cursor()
            if name:
               
                cur.execute("select *from medicines where company=%s", ( name,))
            else:
                query = "select*from medicines"
                cur.execute(query)
            records = cur.fetchall()
            conn.close()
            for item in my_tree.get_children():
                    my_tree.delete(item)
                
               
            for count, record in enumerate(records):
                stock = record[6]  
                if stock == 0 or stock==4 or stock == 5 or stock==3 or stock==2 or stock==1 :
                    my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[10], record[11], record[12], record[13], record[14], record[15], record[16]), tags=("redrow",))
                elif count % 2 == 0:
                    my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3],record[4],record[5],record[6],record[7],record[8],record[9],record[10],record[11],record[12],record[13],record[14],record[15], record[16]), tags=("evenrow",))
                else:
                     my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3],record[4],record[5],record[6],record[7],record[8],record[9],record[10],record[11],record[12],record[13],record[14],record[15], record[16]), tags=("oddrow",))
      
        search_fr = tk.Frame(self,borderwidth=6, background="#DDDDDD", height=200,width=650,relief="raised")

        hd_frame=tk.Frame(search_fr,width=630,height=38,bg="#EEF5FF")
        header_create=ctk.CTkLabel(hd_frame,text="Find Stock(Companywise)",width=0,font=("'helvetica",26),text_color="#121481",anchor="center")
        header_create.place(x=2,y=2)
        name_label=ctk.CTkLabel(search_fr,text="Company:",font=("Cascadia Mono SemiBold",25))
        name_en=ctk.CTkEntry(search_fr,width=280,font=("Cascadia",15),height=32,corner_radius=0)       
     
        
        ser_bt=ctk.CTkButton(search_fr,text="Search",width=100,height=34,text_color="navyblue",corner_radius=20,bg_color="#E2DFD0",fg_color="#D8EFD3",border_width=1,hover_color="#FF7D29",command=check_stock)
        #------------
        def brand_wise():
            name = name_en1.get()
            conn = mysql.connect(host="localhost", user="root", password="dharm", charset="utf8", database="pharmacy", port=3307)
            cur = conn.cursor()
            if name:
               
                cur.execute("select *from medicines where brand=%s", ( name,))
            else:
                query = "select*from medicines"
                cur.execute(query)
            records = cur.fetchall()
            conn.close()
           
   
            for item in my_tree.get_children():
                    my_tree.delete(item)
                
               
            for count, record in enumerate(records):
                stock = record[6]  
                if stock == 0 or stock==4 or stock == 5 or stock==3 or stock==2 or stock==1 :
                    my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[10], record[11], record[12], record[13], record[14], record[15], record[16]), tags=("redrow",))
                elif count % 2 == 0:
                    my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3],record[4],record[5],record[6],record[7],record[8],record[9],record[10],record[11],record[12],record[13],record[14],record[15], record[16]), tags=("evenrow",))
                else:
                     my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3],record[4],record[5],record[6],record[7],record[8],record[9],record[10],record[11],record[12],record[13],record[14],record[15], record[16]), tags=("oddrow",))
           
        search_fr2 = tk.Frame(self,borderwidth=6, background="#DDDDDD", height=200,width=650,relief="raised")

        hd_frame1=tk.Frame(search_fr2,width=630,height=38,bg="#EEF5FF")
        header_create1=ctk.CTkLabel(hd_frame1,text="Find Stock(Brandwise)",width=0,font=("'helvetica",26),text_color="#121481",anchor="center")
        header_create1.place(x=2,y=2)
        name_label1=ctk.CTkLabel(search_fr2,text="Brand:",font=("Cascadia Mono SemiBold",25))
        name_en1=ctk.CTkEntry(search_fr2,width=280,font=("Cascadia",15),height=32,corner_radius=0)       
        
        ser_bt1=ctk.CTkButton(search_fr2,text="Search",width=100,height=34,text_color="navyblue",corner_radius=20,bg_color="#E2DFD0",fg_color="#D8EFD3",border_width=1,hover_color="#FF7D29",command=brand_wise)
        #-----------
        def drug_wise():
            name = name_en2.get()
            conn = mysql.connect(host="localhost", user="root", password="dharm", charset="utf8", database="pharmacy", port=3307)
            cur = conn.cursor()
            if name:
               
                cur.execute("select *from medicines where drug=%s", ( name,))
            else:
                query = "select*from medicines"
                cur.execute(query)
            records = cur.fetchall()
            conn.close()
           
   
            for item in my_tree.get_children():
                    my_tree.delete(item)
            for count, record in enumerate(records):
                stock = record[6]  
                if stock == 0 or stock==4 or stock == 5 or stock==3 or stock==2 or stock==1 :
                    my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[10], record[11], record[12], record[13], record[14], record[15], record[16]), tags=("redrow",))
                elif count % 2 == 0:
                    my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3],record[4],record[5],record[6],record[7],record[8],record[9],record[10],record[11],record[12],record[13],record[14],record[15], record[16]), tags=("evenrow",))
                else:
                     my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3],record[4],record[5],record[6],record[7],record[8],record[9],record[10],record[11],record[12],record[13],record[14],record[15], record[16]), tags=("oddrow",))
               
            
            
            
        search_fr3 = tk.Frame(self,borderwidth=6, background="#DDDDDD", height=200,width=650,relief="raised")

        hd_frame2=tk.Frame(search_fr3,width=630,height=38,bg="#EEF5FF")
        header_create2=ctk.CTkLabel(hd_frame2,text="Find Stock(Drugwise)",width=0,font=("'helvetica",26),text_color="#121481",anchor="center")
        header_create2.place(x=2,y=2)
        name_label2=ctk.CTkLabel(search_fr3,text="Drug:",font=("Cascadia Mono SemiBold",25))
        name_en2=ctk.CTkEntry(search_fr3,width=280,font=("Cascadia",15),height=32,corner_radius=0)       
        
        ser_bt2=ctk.CTkButton(search_fr3,text="Search",width=100,height=34,text_color="navyblue",corner_radius=20,bg_color="#E2DFD0",fg_color="#D8EFD3",border_width=1,hover_color="#FF7D29",command=drug_wise)
      
        
        side_frame=tk.Frame(self,width=885,height=750,relief="raised",borderwidth=4)
        
        
        list_header=ctk.CTkFrame(side_frame,width=700,height=35,border_width=0,fg_color="#EEF5FF",bg_color="#EEF5FF",corner_radius=0)
        
        list_label=ctk.CTkLabel(list_header,text="List of Product",width=0,font=("'helvetica",30),text_color="#121481",anchor="center")
        def data_query():
            global my_tree
            conn = mysql.connect(host="localhost", user="root", password="dharm", charset="utf8", database="pharmacy", port=3307)

            cur = conn.cursor()
            cur.execute("SELECT *FROM medicines")
            records = cur.fetchall()
            
            for count, record in enumerate(records):
                stock = record[6]  
                if stock == 0 or stock==4 or stock == 5 or stock==3 or stock==2 or stock==1 :
                    my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[10], record[11], record[12], record[13], record[14], record[15], record[16]), tags=("redrow",))
                elif count % 2 == 0:
                    my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3],record[4],record[5],record[6],record[7],record[8],record[9],record[10],record[11],record[12],record[13],record[14],record[15], record[16]), tags=("evenrow",))
                else:
                     my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3],record[4],record[5],record[6],record[7],record[8],record[9],record[10],record[11],record[12],record[13],record[14],record[15], record[16]), tags=("oddrow",))
            conn.commit()
            conn.close()
        global my_tree
        style=ttk.Style()
        style.theme_use('default')

        style.configure("Treeview", 
                        background = "#68D2E8",
                        rowheight = 25,
                        foreground="black",
                        fieldbackground = "white", font = ("Consolas", 12))
        style.configure("Treeview",background=[('selected',"#347083")])
        style.configure("Treeview.Heading", background="#CDE8E5",font = ("Consolas", 12))
            
        tree_fr=tk.Frame(side_frame,borderwidth=3,height=690,width=860)
        tree_fr.pack_propagate(False)
        tree_fr.place(x=3,y=47)
        tree_scroll=tk.Scrollbar(tree_fr)
        tree_scroll.pack(side=tk.RIGHT,fill=tk.Y)
        tree_scrolx=tk.Scrollbar(tree_fr,orient=tk.HORIZONTAL)
        tree_scrolx.pack(side=tk.BOTTOM ,fill=tk.X)
            
        my_tree=ttk.Treeview(tree_fr,yscrollcommand=tree_scroll.set,selectmode="extended",xscrollcommand=tree_scrolx.set)
        my_tree.pack(fill="both",expand=True)
        tree_scroll.config(command=my_tree.yview)
        tree_scrolx.config(command=my_tree.xview)
            
        my_tree['columns']=('Sr no','company','name','drug','categories','packing','stock','billrate','salerate','mfg','exp','shell','taxcategory','hsncategory','igst','cgst','sgst')
        my_tree.column("#0",width=0,stretch=tk.NO)
        my_tree.column('Sr no',anchor=tk.W,width=80)
        my_tree.column('company',anchor=tk.W,width=170)
        my_tree.column('name',anchor=tk.W,width=120)
        my_tree.column('drug',anchor=tk.W,width=120)
        my_tree.column('categories',anchor=tk.CENTER,width=120)
        my_tree.column('packing',anchor=tk.CENTER,width=120)
        my_tree.column('stock',anchor=tk.W,width=120)
        my_tree.column('billrate',anchor=tk.W,width=120)
        my_tree.column('salerate',anchor=tk.W,width=120)
        my_tree.column('mfg',anchor=tk.W,width=140)
        my_tree.column('exp',anchor=tk.W,width=140)
        my_tree.column('shell',anchor=tk.W,width=120)
        my_tree.column('taxcategory',anchor=tk.W,width=150)
        my_tree.column('hsncategory',anchor=tk.W,width=150)
        my_tree.column('igst',anchor=tk.W,width=120)
        my_tree.column('cgst',anchor=tk.W,width=120)
        my_tree.column('sgst',anchor=tk.W,width=120)   
        my_tree.heading("#0",text="",anchor="w")
        my_tree.heading("Sr no",text="Sr no",anchor="w")
        my_tree.heading("company",text="Company",anchor="w")
        my_tree.heading("name",text="Brand",anchor="w")
        my_tree.heading("drug",text="Drug",anchor="w")    
        my_tree.heading("categories",text="Categories",anchor="w")
        my_tree.heading("packing",text="Packing",anchor="w",)
        my_tree.heading("stock",text="Stock",anchor="w")
        my_tree.heading("billrate",text="Billrate",anchor="w")
        my_tree.heading("salerate",text="Salerate",anchor="w")
        my_tree.heading("mfg",text="Mfg",anchor="w")
        my_tree.heading("exp",text="Exp",anchor="w")
        my_tree.heading("shell",text="Shell",anchor="w")
        my_tree.heading("taxcategory",text="Taxcategory",anchor="w")
        my_tree.heading("hsncategory",text="Hsncategory",anchor="w")
        my_tree.heading("igst",text="igst",anchor="w")
        my_tree.heading("cgst",text="cgst",anchor="w")
        my_tree.heading("sgst",text="sgst",anchor="w") 
        my_tree.tag_configure('oddrow',background="white")
        my_tree.tag_configure('evenrow',background="lightblue")
        my_tree.tag_configure('redrow', background="red")
        data_query()
        ser_bt.place(x=350,y=100)
        ser_bt1.place(x=350,y=100)
        ser_bt2.place(x=350,y=100)
        name_label.place(x=10,y=60)
        name_en.place(x=140,y=60)
        name_label1.place(x=10,y=60)
        name_en1.place(x=100,y=60)
        name_label2.place(x=10,y=60)
        name_en2.place(x=100,y=60)
        hd_frame.place(x=3,y=3)
        hd_frame1.place(x=3,y=3)
        hd_frame2.place(x=3,y=3)
        side_frame.place(x=800,y=180)
        list_header.place(x=2,y=2)
        list_label.place(x=2,y=3)
        search_fr.place(x=10,y=180)
        search_fr2.place(x=10,y=380)
        search_fr3.place(x=10,y=580)
class sale_report(ctk.CTkToplevel):
     def __init__(self):
        super().__init__()
        global time
        self.title("Sale Report")
        self.width=self.winfo_screenwidth()
        self.height=self.winfo_screenheight()
        self.geometry(f"{self.width}x{self.height}+0+0")
        self.iconbitmap("38_113706.ico")
        self.grab_set()
        f1=tk.Frame(self,width=1905,height=175,relief="ridge",borderwidth=7,border=4,background="#E1F7F5", highlightcolor="navyblue")
        customer_label=ctk.CTkLabel(f1,text="license no:",font=("Cascadia Mono SemiBold",18),text_color="#1C1678")
        customer_label.place(x=520,y=26)
        lic_h=ctk.CTkLabel(f1,text="123456",font=("Cascadia Mono SemiBold",18),text_color="#1C1678")
        lic_h.place(x=650,y=26)
        medn_h=ctk.CTkLabel(f1,text="Health Care Chemist and Druggist ",font=("Cascadia Mono SemiBold",18),text_color="#1C1678")
        medn_h.place(x=270,y=75)      
        medical_logo=ctk.CTkImage(light_image=Image.open("pharmacy.png"),dark_image=Image.open("pharmacy.png"),size=(140,130))
        med_label_image1=ctk.CTkLabel(f1,text="",image=medical_logo)
        med_label_image1.place(x=1350,y=3)
        mediine=ctk.CTkImage(light_image=Image.open("home2-removebg-preview.png"),dark_image=Image.open("home2-removebg-preview.png"),size=(200,90))
        med_label_image2=ctk.CTkLabel(f1,text="",image=mediine)
        med_label_image2.place(x=3,y=40)
        mediine1=ctk.CTkImage(light_image=Image.open("home2-removebg-preview222.png"),dark_image=Image.open("home2-removebg-preview222.png"),size=(200,90))
        med_label_image3=ctk.CTkLabel(f1,text="",image=mediine1)
        med_label_image3.place(x=3,y=1)  
        logo_nm=ctk.CTkLabel(med_label_image3,text="Med Connect",font=("Cascadia Mono SemiBold",22),text_color="#1C1678")
        logo_nm.place(x=27,y=45)
        customer_en=ctk.CTkLabel(f1,text="",font=("Cascadia Mono SemiBold",18),text_color="#1C1678")
        customer_en.place(x=650,y=26)
        medical_name12=ctk.CTkLabel(f1,text="",font=("Cascadia Mono SemiBold",18),text_color="#1C1678")
        medical_name12.place(x=300,y=90)
        f1.place(x=2,y=3)
        def date1():
        
            today_date = datetime.today()
            day = today_date.day
            month = today_date.month
            year = today_date.year
            # day1=datetime.now()
            dayname=today_date.strftime("%A")
            date_label.configure(text = f"{day}/{month}/{year} ({dayname})")
        
        date_label=ctk.CTkLabel(self,text="date",text_color="#1C1678",fg_color="transparent",bg_color="#E1F7F5",font=("Cascadia Mono SemiBold",17))
        
        def time12():
            self.hours = strftime("%I")  #I - for 12 hours clock
            self.minute = strftime("%M")
            self.second = strftime("%S")
            self.am_pm = strftime("%p")

            time_label.configure(text = f"{self.hours}:{self.minute}:{self.second} {self.am_pm}")
            time_label.after(1000,time12)
               
        time_label=ctk.CTkLabel(self,text="",text_color="#1C1678",fg_color="transparent",bg_color="#E1F7F5",font=("Cascadia Mono SemiBold",17))
        
        date_label.place(x=250,y=30)
       
        time_label.place(x=1200,y=100)
        date1()
        time12() 
        search_fr = tk.Frame(self,borderwidth=6, background="#DDDDDD", height=300,width=650,relief="raised")
        hd_frame=tk.Frame(search_fr,width=630,height=38,bg="#EEF5FF")
        header_create=ctk.CTkLabel(hd_frame,text="Search Sale",width=0,font=("'helvetica",30),text_color="#121481",anchor="center")
        header_create.place(x=2,y=3)
        side_frame=tk.Frame(self,width=1170,height=760,borderwidth=3,relief="raised")
        list_header=ctk.CTkFrame(side_frame,width=915,height=35,border_width=0,fg_color="#EEF5FF",bg_color="#EEF5FF",corner_radius=0)
        list_label=ctk.CTkLabel(list_header,text="List of Sale Product ",width=0,font=("'helvetica",30),text_color="#121481",anchor="center")
        def data_query1():
            for item in my_tree.get_children():
                my_tree.delete(item)
            conn = mysql.connect(host="localhost", user="root", password="dharm", charset="utf8", database="pharmacy", port=3307)
            cur = conn.cursor()
            cur.execute("SELECT billno,pat_id,med_id,brand, qty,date,Net_amt,payment_mode FROM sale")
        
            records=cur.fetchall()
            for count, record in enumerate(records):
                if count % 2 == 0:
                    my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1],record[2],record[3],record[4],record[5],record[6],record[7]), tags=("evenrow",))
                else:
                    my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2],record[3],record[4],record[5],record[6],record[7]), tags=("oddrow",))
            conn.commit()
            conn.close()
        global my_tree
        style=ttk.Style()
        style.theme_use('default')

        style.configure("Treeview", 
                        background = "#68D2E8",
                        rowheight = 25,
                        foreground="black",
                        fieldbackground = "white", font = ("Consolas", 12))
        style.configure("Treeview",background=[('selected',"#347083")])
        style.configure("Treeview.Heading", background="#CDE8E5",font = ("Consolas", 12))
        tree_fr=tk.Frame(side_frame,borderwidth=3,height=690,width=1148)
        tree_fr.pack_propagate(False)
        tree_fr.place(x=3,y=47)
        tree_scroll=tk.Scrollbar(tree_fr)
        tree_scroll.pack(side=tk.RIGHT,fill=tk.Y)
        tree_scrolx=tk.Scrollbar(tree_fr,orient=tk.HORIZONTAL)
        tree_scrolx.pack(side=tk.BOTTOM ,fill=tk.X)  
        my_tree=ttk.Treeview(tree_fr,yscrollcommand=tree_scroll.set,selectmode="extended",xscrollcommand=tree_scrolx.set)
        my_tree.pack(fill="both",expand=True)
        tree_scroll.config(command=my_tree.yview)
        tree_scrolx.config(command=my_tree.xview)  
        my_tree['columns']=('Bill No',"Patid","Medid",'Product','Qty','Date','amt','method')
        my_tree.column("#0",width=0,stretch=tk.NO)
        my_tree.column('Bill No',anchor=tk.W,width=100)
        my_tree.column('Patid',anchor=tk.W,width=100)
        my_tree.column('Medid',anchor=tk.W,width=100)
        my_tree.column('Product',anchor=tk.W,width=120)
        my_tree.column('Qty',anchor=tk.CENTER,width=120)
        my_tree.column('Date',anchor=tk.CENTER,width=120)
        my_tree.column('amt',anchor=tk.CENTER,width=120)
        my_tree.column('method',anchor=tk.CENTER,width=120)
        my_tree.heading("#0",text="",anchor="w")
        my_tree.heading("Bill No",text="Bill No",anchor="w")
        my_tree.heading("Patid",text="Patid",anchor="w")
        my_tree.heading("Medid",text="Medid",anchor="w")
        my_tree.heading("Product",text="Product",anchor="w") 
        my_tree.heading("Qty",text="Qty",anchor="w")
        my_tree.heading("Date",text="Date",anchor="w",)
        my_tree.heading("amt",text="Amount",anchor="w",)
        my_tree.heading("method",text="Paymentmode",anchor="w",)
        my_tree.tag_configure('oddrow',background="white")
        my_tree.tag_configure('evenrow',background="lightblue")
        data_query1()
        grp_fr=tk.Frame(self,width=644,height=400,relief="groove",borderwidth=4)
        mon_fr=tk.Frame(self,width=650,height=50,relief="groove",borderwidth=4)
        def update_graph(month=None):
            if month is None:
                month = month_en.get()
            
            if not month:
                print("Month is empty")
                return
            
            conn = mysql.connect(host="localhost", user="root", password="dharm", charset="utf8", database="pharmacy", port=3307)
            cur = conn.cursor()
            query = """
            SELECT Date, SUM(Net_amt) AS total_net_amt
            FROM sale
            WHERE MONTH(Date) = %s
            GROUP BY Date
            """
            cur.execute(query, (month,))
            
            dates = []
            net_amounts = []
            while True:
                result = cur.fetchone()
                if result is None:
                    break
                date = result[0].strftime("%Y-%m-%d")  
                total_net_amt = int(result[1])
                dates.append(date)
                net_amounts.append(total_net_amt)
            
            print(dates)
            print(net_amounts)
            
            for widget in grp_fr.winfo_children():
                widget.destroy()
            
            if not dates:
                no_data_label = ctk.CTkLabel(grp_fr, text="No data available for the selected month", font=("Cascadia", 15))
                no_data_label.place(x=2, y=2)
                return
            
            fig, ax = plt.subplots(figsize=(5.2, 4))
    
            bar_width = 0.3
            
            max_value = max(net_amounts)
            min_value = min(net_amounts)
            colors = ['green' if amt == max_value else 'red' if amt == min_value else 'red' for amt in net_amounts]
            
            ax.bar(dates, net_amounts, color=colors, width=bar_width, align='center')
            ax.set_xlabel('Date')
            ax.set_ylabel('Total Net Amount')
            ax.set_title('Sales Report')
            ax.set_xticks(dates)
            ax.set_xticklabels(dates,)
            handles = [plt.Line2D([0], [0], color='red', lw=4), plt.Line2D([0], [0], color='green', lw=4)]
            labels = ['Max Sale', 'Min Sale']
            ax.legend(handles, labels, loc='best',fontsize=7, handlelength=2, handletextpad=1)
            yticks = list(range(0, max(net_amounts) + 500, 500))
            ax.set_yticks(yticks)
            canvas = FigureCanvasTkAgg(fig, master=grp_fr)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
            plt.close('all')

        def initialize_graph():
            current_month = datetime.now().month
            month_en.insert(0, str(current_month))
            update_graph(current_month)
        month_en=ctk.CTkEntry(mon_fr,width=40,font=("Cascadia",15),height=15,corner_radius=0) 
        month_en.place(x=100,y=2)
        mon_label=ctk.CTkLabel(mon_fr,text="Enter Month:",width=0,font=("'helvetica",15),text_color="#121481",anchor="center")
        mon_label.place(x=10,y=2)
        initialize_graph()
        update_btn = ctk.CTkButton(mon_fr, text="Search",width=20, command=update_graph)
        update_btn.place(x=180, y=2)
        grp_fr.place(x=16,y=250)
        mon_fr.place(x=16,y=200)
        side_frame.place(x=732,y=180)
        list_header.place(x=2,y=2)
        list_label.place(x=2,y=3)
if __name__=="__main__":
    app=App()
    app.mainloop()