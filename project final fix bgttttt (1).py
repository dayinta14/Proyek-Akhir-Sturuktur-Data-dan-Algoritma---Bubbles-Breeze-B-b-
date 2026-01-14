import tkinter as tk
from PIL import Image, ImageDraw, ImageTk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
from customtkinter import*
from tkcalendar import Calendar
import csv
import re
import customtkinter as customtkinter
import pandas as pd
import webbrowser
from geopy.distance import geodesic


class CustomTkinterButton(tk.Button):
    def __init__(self, master=None, **kwargs):
        tk.Button.__init__(self, master, **kwargs)
        self.configure(cursor="hand2", relief=tk.FLAT)
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

class CustomTkinterApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Laundry App")
        screen_width = 360
        screen_height = 540
        window_width = screen_width
        window_height = screen_height
        self.geometry(f"{window_width}x{window_height}")
        self.canvas = tk.Canvas(self, width=window_width, height=window_height)
        self.canvas.pack()
        image_path = "project uas\\projek fix\\Get Started.jpg"
        image = Image.open(image_path)
        image = image.resize((window_width, window_height))
        self.photo = ImageTk.PhotoImage(image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)

    
        buttonguest = CTkButton(self.canvas, text="Guest", command=self.goto_guest_page,
                                          font=("verdana", int(window_height * 0.025)), corner_radius=70,bg_color='#C6DBEA', width=20, height=30)
        buttonguest.place(relx=0.65 , rely=0.76, anchor=tk.CENTER)
        buttonadmin = CTkButton(self.canvas, text="Admin", command=self.goto_admin_page,
                                          font=("verdana", int(window_height * 0.025)), corner_radius=70,bg_color='#C6DBEA', width=20, height=30)
        buttonadmin.place(relx=0.4, rely=0.76, anchor=tk.CENTER)

 


    def goto_guest_page(self):
        self.destroy()
        Guest()
    def goto_admin_page(self):
        self.destroy()
        Admin()

class Admin(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Next Page")
        screen_width = 360
        screen_height = 540
        window_width = screen_width
        window_height = screen_height
        self.geometry(f"{window_width}x{window_height}")
        self.canvas = tk.Canvas(self, width=window_width, height=window_height)
        self.canvas.pack()
        image_path = "project uas\\projek fix\\login admin.png"
        image = Image.open(image_path)
        image = image.resize((window_width, window_height))
        self.photo = ImageTk.PhotoImage(image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)
        self.emailadmin_entry = tk.Entry(self, font=("verdana", 13), border=0, highlightthickness=2, highlightcolor="#0292B7", relief='groove')  # Create emailadmin_entry widget
        self.emailadmin_entry.place(relx=0.35, rely=0.44, anchor=tk.W)  # Place the widget
        self.password_entry = tk.Entry(self, font=("verdana", 13), border=0, highlightthickness=2, highlightcolor="#0292B7", relief='groove',show="*")
        self.password_entry.place(relx=0.35, rely=0.52, anchor=tk.W)
        self.signup_button = CTkButton(self.canvas, text="Sign Up", command=self.goto_next_page_signup,
                                                 font=("verdana", int(window_height * 0.02)),corner_radius=70, bg_color='#C6DBEA', width=20, height=25)
        self.signup_button.place(relx=0.75, rely=0.883, anchor=tk.CENTER)

        self.login_button = CTkButton(self.canvas, text="Log In", command=self.goto_home_page,
                                                 font=("verdana", int(window_height * 0.025)),corner_radius=70, bg_color='#C6DBEA', width=100, height=30)
        self.login_button.place(relx=0.5, rely=0.683, anchor=tk.CENTER)
        self.show_password_var = tk.BooleanVar()
        self.show_password_checkbox = tk.Checkbutton(self, text="Show Password", variable=self.show_password_var,
                                                      command=self.toggle_show_password, bg="#C6DBEA")
                                                      
        self.show_password_checkbox.place(relx=0.5, rely=0.58, anchor=tk.CENTER)

        # Back button
        self.back_button = CTkButton(self.canvas, text="Back", command=self.back_to_main,
                                     font=("verdana", int(window_height * 0.02)), corner_radius=70, bg_color='#C6DBEA', width=20, height=25)
        self.back_button.place(relx=0.1, rely=0.05, anchor=tk.CENTER)

    def toggle_show_password(self):
        show = self.show_password_var.get()
        if show:
            self.password_entry.config(show="")
        else:
            self.password_entry.config(show="*")

    def goto_next_page_signup(self):
        self.destroy()
        AdminSignUp()

    def goto_home_page(self):
        emailadmin = self.emailadmin_entry.get().strip()
        password = self.password_entry.get().strip()
        if emailadmin == "" or password == "":
            messagebox.showinfo("Error", "Please enter email and password.")
        else:
            with open('akunadmin.csv', mode='r') as file:
                reader = csv.reader(file, delimiter=';')
                found = False
                for row in reader:
                    row = [elem.strip() for elem in row]  # Remove extra spaces
                    if len(row) >= 3 and row[0] == emailadmin and row[2] == password:
                        found = True
                        laundry_name = row[1]
                        break
                if found:
                    messagebox.showinfo("Success", "Login successful!")
                    self.destroy()
                    AdminHome(laundry_name)
                else:
                    messagebox.showerror("Error", "Invalid email or password.")

    def back_to_main(self):
        self.destroy()
        CustomTkinterApp()

class Guest(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Next Page")
        screen_width = 360
        screen_height = 540
        window_width = screen_width
        window_height = screen_height
        self.geometry(f"{window_width}x{window_height}")
        self.canvas = tk.Canvas(self, width=window_width, height=window_height)
        self.canvas.pack()
        image_path = "project uas\\projek fix\\login guest.png"
        image = Image.open(image_path)
        image = image.resize((window_width, window_height))
        self.photo = ImageTk.PhotoImage(image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)
        self.email_entry = tk.Entry(self, font=("verdana", 13), border=0, highlightthickness=2, highlightcolor="#0292B7", relief='groove')
        self.email_entry.place(relx=0.35, rely=0.415, anchor=tk.W)
        self.password_entry = tk.Entry(self, font=("verdana", 13), border=0, highlightthickness=2, highlightcolor="#0292B7", relief='groove' ,show="*")
        self.password_entry.place(relx=0.35, rely=0.52, anchor=tk.W)

        self.signup_button = CTkButton(self.canvas, text="Sign Up", command=self.goto_next_page_signup,
                                                 font=("verdana", int(window_height * 0.02)),corner_radius=70, bg_color='#C6DBEA', width=20, height=25)
        self.signup_button.place(relx=0.75, rely=0.883, anchor=tk.CENTER)

        self.login_button = CTkButton(self.canvas, text="Log In", command=self.goto_home_page,
                                                 font=("verdana", int(window_height * 0.025)),corner_radius=70, bg_color='#C6DBEA', width=100, height=30)
        self.login_button.place(relx=0.5, rely=0.683, anchor=tk.CENTER)
        self.show_password_var = tk.BooleanVar()
        self.show_password_checkbox = tk.Checkbutton(self, text="Show Password", variable=self.show_password_var,
                                                      command=self.toggle_show_password, bg="#C6DBEA")
                                                      
        self.show_password_checkbox.place(relx=0.5, rely=0.58, anchor=tk.CENTER)

        # Back button
        self.back_button = CTkButton(self.canvas, text="Back", command=self.back_to_main,
                                     font=("verdana", int(window_height * 0.02)), corner_radius=70, bg_color='#C6DBEA', width=20, height=25)
        self.back_button.place(relx=0.1, rely=0.05, anchor=tk.CENTER)

    def toggle_show_password(self):
        show = self.show_password_var.get()
        if show:
            self.password_entry.config(show="")
        else:
            self.password_entry.config(show="*")

    def goto_next_page_signup(self):
        self.destroy()
        GuestSignUp()

    def goto_home_page(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        if email == "" or password == "":
            messagebox.showinfo("Error", "Please enter email and password.")
        else:
            self.destroy()
            GuestHome()

    def back_to_main(self):
        self.destroy()
        CustomTkinterApp()

class AdminSignUp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Next page")
        screen_width = 360
        screen_height = 540
        window_width = screen_width
        window_height = screen_height
        self.geometry(f"{window_width}x{window_height}")
        self.canvas = tk.Canvas(self, width=window_width, height=window_height)
        self.canvas.pack()
        image_path = "project uas\\projek fix\\sign up admin.png"
        image = Image.open(image_path)
        image = image.resize((window_width, window_height))
        self.photo = ImageTk.PhotoImage(image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)
        self.emailadmin_entry = tk.Entry(self, font=("verdana", 13), border=0, highlightthickness=2, highlightcolor="#0292B7", relief='groove')
        self.emailadmin_entry.place(relx=0.35, rely=0.497, anchor=tk.W)
        self.laundry_name_entry = tk.Entry(self, font=("verdana", 13), border=0, highlightthickness=2, highlightcolor="#0292B7", relief='groove')
        self.laundry_name_entry.place(relx=0.35, rely=0.41, anchor=tk.W)
        self.password_entry = tk.Entry(self, font=("verdana", 13), border=0, highlightthickness=2, highlightcolor="#0292B7", relief='groove')
        self.password_entry.place(relx=0.35, rely=0.565, anchor=tk.W)
        self.address_entry = tk.Entry(self, font=("verdana", 13), border=0, highlightthickness=2, highlightcolor="#0292B7", relief='groove')
        self.address_entry.place(relx=0.35, rely=0.71, anchor=tk.W)
        self.coordinate_entry = tk.Entry(self, font=("verdana", 13), border=0, highlightthickness=2, highlightcolor="#0292B7", relief='groove')
        self.coordinate_entry.place(relx=0.35, rely=0.635, anchor=tk.W)
        self.services_frame = tk.Frame(self, bg="#C6DBEA")  
        self.services_frame.place(relx=0.35, rely=0.81, anchor=tk.W)
        self.selected_options = []
        options = ["Open 24 Hours", "Delivery", "Express"]
        for option in options:
            var = tk.BooleanVar()
            checkbox = tk.Checkbutton(self.services_frame, text=option, variable=var, font=("verdana", 7),bg="#C6DBEA")
            checkbox.pack(anchor=tk.W)
            self.selected_options.append((option, var))

        self.photo_button = CTkButton(self, text="Choose Photo", command=self.choose_photo, font=("verdana", int(window_height * 0.025)),corner_radius=70, bg_color='#C6DBEA', width=50, height=20)
        self.photo_button.place(relx=0.61, rely=0.82, anchor=tk.W)

        self.create_account_button = CTkButton(self.canvas, text="Create Account", command=self.create_account,
                                                          font=("verdana", int(window_height * 0.025)),corner_radius=70, bg_color='#C6DBEA', width=100, height=30)
        self.create_account_button.place(relx=0.5, rely=0.92, anchor=tk.CENTER)

        # Back button
        self.back_button = CTkButton(self.canvas, text="Back", command=self.back_to_main,
                                     font=("verdana", int(window_height * 0.02)), corner_radius=70, bg_color='#C6DBEA', width=20, height=25)
        self.back_button.place(relx=0.1, rely=0.05, anchor=tk.CENTER)
    def choose_photo(self):
        self.filename = filedialog.askopenfilename(initialdir="/", title="Select Photo", filetypes=(("Image files", ".jpg *.png"), ("All files", ".*")))
       

    def create_account(self):
        email = self.emailadmin_entry.get()
        laundryname = self.laundry_name_entry.get()
        password = self.password_entry.get()
        address = self.address_entry.get()
        coordinate = self.coordinate_entry.get()
        if not self.validate_email(email):
            tk.messagebox.showerror("Error", "Invalid email format")
        elif not self.validate_password(password):
            tk.messagebox.showerror("Error", "Invalid password format. Password must have at least 8 characters, including at least one uppercase letter, one lowercase letter, and one digit.")
        else:
            services = [option for option, var in self.selected_options if var.get()]
            self.save_to_csv(email, laundryname, password, address, services, coordinate)
            tk.messagebox.showinfo("Success", "Account successfully created!")
            self.destroy()
            LoginAdminPage()

    def validate_email(self, email):
        if re.match(r'[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}', email):
            return True
        else:
            return False

    def validate_password(self, password):
        if len(password) < 8:
            return False
        elif not any(char.islower() for char in password):
            return False
        elif not any(char.isupper() for char in password):
            return False
        elif not any(char.isdigit() for char in password):
            return False
        else:
            return True

    def save_to_csv(self, email, laundryname, password, address, services,coordinate):
        with open('akunadmin.csv', mode='a', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow([email, laundryname, password, address] + services + [self.filename] + [coordinate])\

    def back_to_main(self):
        self.destroy()
        Admin()

class GuestSignUp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Next page")
        screen_width = 360
        screen_height = 540
        window_width = screen_width
        window_height = screen_height
        self.geometry(f"{window_width}x{window_height}")
        self.canvas = tk.Canvas(self, width=window_width, height=window_height)
        self.canvas.pack()
        image_path = "project uas\\projek fix\\sign up guest.png"
        image = Image.open(image_path)
        image = image.resize((window_width, window_height))
        self.photo = ImageTk.PhotoImage(image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)
        self.email_entry = tk.Entry(self, font=("verdana", 13), border=0, highlightthickness=2, highlightcolor="#0292B7", relief='groove')
        self.email_entry.place(relx=0.35, rely=0.41, anchor=tk.W)
        self.nama_entry = tk.Entry(self, font=("verdana", 13), border=0, highlightthickness=2, highlightcolor="#0292B7", relief='groove')
        self.nama_entry.place(relx=0.35, rely=0.52, anchor=tk.W)
        self.password_entry = tk.Entry(self, font=("verdana", 13), border=0, highlightthickness=2, highlightcolor="#0292B7", relief='groove')
        self.password_entry.place(relx=0.35, rely=0.61, anchor=tk.W)
        self.conpassword_entry = tk.Entry(self, font=("verdana", 13), border=0, highlightthickness=2, highlightcolor="#0292B7", relief='groove')
        self.conpassword_entry.place(relx=0.35, rely=0.71, anchor=tk.W)

        self.create_account_button = CTkButton(self.canvas, text="Create Account", command=self.create_account,
                                                          font=("verdana", int(window_height * 0.025)),corner_radius=70, bg_color='#C6DBEA', width=100, height=30)
        self.create_account_button.place(relx=0.5, rely=0.85, anchor=tk.CENTER)

        # Back button
        self.back_button = CTkButton(self.canvas, text="Back", command=self.back_to_main,
                                     font=("verdana", int(window_height * 0.02)), corner_radius=70, bg_color='#C6DBEA', width=20, height=25)
        self.back_button.place(relx=0.1, rely=0.05, anchor=tk.CENTER)

    def create_account(self):
        email = self.email_entry.get()
        nama = self.nama_entry.get()
        password = self.password_entry.get()
        conpassword = self.conpassword_entry.get()

        if not self.validate_email(email):
            tk.messagebox.showerror("Error", "Invalid email format")
        elif password != conpassword:
            tk.messagebox.showerror("Error", "Passwords do not match")
        elif not self.validate_password(password):
            tk.messagebox.showerror("Error", "Invalid password format. Password must have at least 8 characters, including at least one uppercase letter, one lowercase letter, and one digit.")
        else:
            self.save_to_csv(email, nama, password)
            tk.messagebox.showinfo("Success", "Account successfully created!")
            self.destroy()
            LoginGuestPage()

    def validate_email(self, email):
        if re.match(r'[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}', email):
            return True
        else:
            return False

    def validate_password(self, password):
        if len(password) < 8:
            return False
        elif not any(char.islower() for char in password):
            return False
        elif not any(char.isupper() for char in password):
            return False
        elif not any(char.isdigit() for char in password):
            return False
        else:
            return True

    def save_to_csv(self, email, nama, password):
        with open('akunpengunjung.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([email, nama, password])

    def back_to_main(self):
        self.destroy()
        Guest()

class LoginGuestPage(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Login Page")
        screen_width = 360
        screen_height = 540
        window_width = screen_width
        window_height = screen_height
        self.geometry(f"{window_width}x{window_height}")
        self.canvas = tk.Canvas(self, width=window_width, height=window_height)
        self.canvas.pack()
        image_path = "project uas\\projek fix\\login guest.png"
        image = Image.open(image_path)
        image = image.resize((window_width, window_height))
        self.photo = ImageTk.PhotoImage(image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)
        self.email_entry = tk.Entry(self, font=("verdana", 13), border=0, highlightthickness=2, highlightcolor="#0292B7", relief='groove')
        self.email_entry.place(relx=0.35, rely=0.415, anchor=tk.W)
        self.password_entry = tk.Entry(self, font=("verdana", 13), border=0, highlightthickness=2, highlightcolor="#0292B7", relief='groove' ,show="*")
        self.password_entry.place(relx=0.35, rely=0.52, anchor=tk.W)
        self.login_button = CTkButton(self.canvas, text="Log In", command=self.login,
                                                 font=("verdana", int(window_height * 0.02)),corner_radius=70, bg_color='#C6DBEA', width=100, height=30)
        self.login_button.place(relx=0.5, rely=0.683, anchor=tk.CENTER)
        self.show_password_var = tk.BooleanVar()
        self.show_password_checkbox = tk.Checkbutton(self, text="Show Password", variable=self.show_password_var,
                                                      command=self.toggle_show_password, bg="#C6DBEA")
        self.show_password_checkbox.place(relx=0.5, rely=0.58, anchor=tk.CENTER)

        # Back button
        self.back_button = CTkButton(self.canvas, text="Back", command=self.back_to_main,
                                     font=("verdana", int(window_height * 0.02)), corner_radius=70, bg_color='#C6DBEA', width=20, height=25)
        self.back_button.place(relx=0.1, rely=0.05, anchor=tk.CENTER)

    def toggle_show_password(self):
        show = self.show_password_var.get()
        if show:
            self.password_entry.config(show="")
        else:
            self.password_entry.config(show="*")

    def login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        if email == "" or password == "":
            messagebox.showinfo("Error", "Please enter email and password.")
        else:
            with open('akunpengunjung.csv', mode='r') as file:
                reader = csv.reader(file)
                found = False
                for row in reader:
                    if row[0] == email and row[2] == password:
                        found = True
                        break
                if found:
                    messagebox.showinfo("Success", "Login successful!")
                    self.destroy()
                    GuestHome()
                else:
                    messagebox.showerror("Error", "Invalid email or password.")

    def back_to_main(self):
        self.destroy()
        GuestSignUp()

class LoginAdminPage(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Login Page")
        screen_width = 360
        screen_height = 540
        window_width = screen_width
        window_height = screen_height
        self.geometry(f"{window_width}x{window_height}")
        self.canvas = tk.Canvas(self, width=window_width, height=window_height)
        self.canvas.pack()
        image_path = "project uas\\projek fix\\login admin.png"
        image = Image.open(image_path)
        image = image.resize((window_width, window_height))
        self.photo = ImageTk.PhotoImage(image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)
        self.email_entry = tk.Entry(self, font=("verdana", 13), border=0, highlightthickness=2, highlightcolor="#0292B7", relief='groove')
        self.email_entry.place(relx=0.35, rely=0.415, anchor=tk.W)
        self.password_entry = tk.Entry(self, font=("verdana", 13), border=0, highlightthickness=2, highlightcolor="#0292B7", relief='groove' ,show="*")
        self.password_entry.place(relx=0.35, rely=0.52, anchor=tk.W)
        self.login_button = CTkButton(self.canvas, text="Log In", command=self.login,
                                                 font=("verdana", int(window_height * 0.02)),corner_radius=70, bg_color='#C6DBEA', width=100, height=30)
        self.login_button.place(relx=0.5, rely=0.683, anchor=tk.CENTER)
        self.show_password_var = tk.BooleanVar()
        self.show_password_checkbox = tk.Checkbutton(self, text="Show Password", variable=self.show_password_var,
                                                      command=self.toggle_show_password, bg="#C6DBEA")
        self.show_password_checkbox.place(relx=0.5, rely=0.58, anchor=tk.CENTER)

        # Back button
        self.back_button = CTkButton(self.canvas, text="Back", command=self.back_to_main,
                                     font=("verdana", int(window_height * 0.02)), corner_radius=70, bg_color='#C6DBEA', width=20, height=25)
        self.back_button.place(relx=0.1, rely=0.05, anchor=tk.CENTER)

    def toggle_show_password(self):
        show = self.show_password_var.get()
        if show:
            self.password_entry.config(show="")
        else:
            self.password_entry.config(show="*")

    def login(self):
        emailadmin = self.email_entry.get()
        password = self.password_entry.get()
        if emailadmin == "" or password == "":
            messagebox.showinfo("Error", "Please enter email and password.")
        else:
            with open('akunadmin.csv', mode='r') as file:
                reader = csv.reader(file, delimiter=';')
                found = False
                for row in reader:
                    row = [item.strip() for item in row]
                    if len(row) >= 3 and row[0] == emailadmin and row[2] == password:
                        found = True
                        laundry_name = row[1]
                        break
                if found:
                    messagebox.showinfo("Success", "Login successful!")
                    self.destroy()
                    AdminHome(laundry_name)
                else:
                    messagebox.showerror("Error", "Invalid email or password.")


    def back_to_main(self):
        self.destroy()
        AdminSignUp()

class ScrollableFrame(tk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)

        # Create a canvas
        self.canvas = tk.Canvas(self, bg="#FFFFFF")
        self.scrollbar = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas)

        # Configure canvas
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Pack scrollbar and canvas
        self.scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)

        # Create a window in canvas
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.scrollable_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        # Bind mouse wheel scrolling
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

    # Function to bind mouse wheel scrolling
    def _on_mousewheel(self, event):
         # Calculate the scroll units
        scroll_units = int(-1 * (event.delta / 120))
        
        # Get the current scroll position
        current_scroll = self.canvas.yview()

        # Check if scrolling up and if we are at the top
        if scroll_units < 0 and current_scroll[0] <= 0:
            return

        # Check if scrolling down and if we are at the bottom
        if scroll_units > 0 and current_scroll[1] >= 1:
            return

        # Scroll the canvas
        self.canvas.yview_scroll(scroll_units, "units")

class GuestHome(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Home Page")
        screen_width = 360
        screen_height = 540
        window_width = screen_width
        window_height = screen_height
        self.geometry(f"{window_width}x{window_height}")
        self.canvas = tk.Canvas(self, width=window_width, height=window_height)
        self.canvas.pack()

        # Image path to be replaced with your image
        image_path = "project uas\\projek fix\\home guest.png"
        image = Image.open(image_path)
        image = image.resize((window_width, window_height))
        self.photo = ImageTk.PhotoImage(image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)

        # Create a Listbox for Services
        self.listbox_services = tk.Listbox(self, selectmode=tk.MULTIPLE, width=15, height=4, bg='#FFFFFF', bd=0, highlightthickness=0, relief='flat', exportselection=False)
        self.listbox_services.place(relx=0.05, rely=0.075, width=50, height=100)

        service_options = ['Open 24 hours', 'Delivery', 'Express']

        # Insert service options into the listbox
        for option in service_options:
            self.listbox_services.insert(tk.END, option)

        # Bind the event to listbox selection change
        self.listbox_services.bind('<<ListboxSelect>>', self.on_listbox_services_select)

        # Hide the listbox initially
        self.listbox_services.place_forget()

        # Create a button to show the service listbox
        self.show_button_services = CTkButton(self.canvas, text="Filter", command=self.show_listbox_services, font=("verdana", int(window_height * 0.02)), corner_radius=70, bg_color='#A2C8DF', width=80, height=20)
        self.show_button_services.place(relx=0.05, rely=0.12)

        # Create a new Listbox for Location
        self.listbox_location = tk.Listbox(self, selectmode=tk.MULTIPLE, width=15, height=4, bg='#FFFFFF', bd=0, highlightthickness=0, relief='flat', exportselection=False)
        self.listbox_location.place(relx=0.3, rely=0.2, width=200, height=100)

        location_options = ['Ketintang', 'Wonokromo', 'Jambangan', 'Karah']

        # Insert location options into the listbox
        for option in location_options:
            self.listbox_location.insert(tk.END, option)

        # Bind the event to location listbox selection change
        self.listbox_location.bind('<<ListboxSelect>>', self.on_listbox_location_select)

        # Hide the location listbox initially
        self.listbox_location.place_forget()

        # Create a button to show the location listbox
        self.show_button_location = CTkButton(self.canvas, text="Location", command=self.show_listbox_location, font=("verdana", int(window_height * 0.02)), corner_radius=70, bg_color='#C6DBEA', width=80, height=20)
        self.show_button_location.place(relx=0.35, rely=0.12)

        # Create a search bar
        self.search_entry = tk.Entry(self, font=("verdana", 13), border=2, highlightthickness=2, highlightcolor="#0292B7", relief='groove', bg='#C6DBEA')
        self.search_entry.place(relx=0.1, rely=0.4, anchor=tk.W)

        # Create a button to trigger search
        self.search_button = CTkButton(self.canvas, text="Search", command=self.search_laundry, font=("verdana", int(window_height * 0.02)), corner_radius=70, bg_color='#FFFFFF', width=55, height=20)
        self.search_button.place(relx=0.82, rely=0.4, anchor=tk.CENTER)

        # Create a scrollable frame
        self.scrollable_frame = ScrollableFrame(self)
        self.scrollable_frame.place(relx=0.55, rely=0.45, anchor="n")

        self.back_button = CTkButton(self.canvas, text="Back", command=self.back_to_main, font=("verdana", int(window_height * 0.02)), corner_radius=70, bg_color='#A2C8DF', width=20, height=25)
        self.back_button.place(relx=0.1, rely=0.05, anchor=tk.CENTER)

        # Read data from akunadmin.csv
        with open('akunadmin.csv', mode='r') as file:
            reader = csv.reader(file, delimiter=';')
            self.data = list(reader)

        # Display data initially
        self.display_data(self.data)

        # Dictionary to store starting locations for each area
        self.location_coordinates = {
            'Ketintang': (-7.315078780839132, 112.73006679798846),
            'Wonokromo': (-7.30072575010308, 112.73977971141755),
            'Jambangan': (-7.3227017427858705, 112.71341422564254),
            'Karah': (-7.30913304192813, 112.71955354763628)
        }

    def show_listbox_services(self):
        if self.listbox_services.winfo_ismapped():
            self.listbox_services.place_forget()
        else:
            self.listbox_services.place(relx=0.05, rely=0.16)

    def show_listbox_location(self):
        if self.listbox_location.winfo_ismapped():
            self.listbox_location.place_forget()
        else:
            self.listbox_location.place(relx=0.35, rely=0.16)

    def on_listbox_services_select(self, event):
        self.filter_data()

    def on_listbox_location_select(self, event):
        self.filter_data()

    def filter_data(self):
        selected_services = [self.listbox_services.get(i) for i in self.listbox_services.curselection()]
        selected_locations = [self.listbox_location.get(i) for i in self.listbox_location.curselection()]

        if not selected_services and not selected_locations:
            self.display_data(self.data)
            return

        def filter_row(row):
            service_mapping = {
                'Open 24 hours': 4,  # Adjust column index if needed
                'Delivery': 4,       # Adjust column index if needed
                'Express': 4,        # Adjust column index if needed
            }
            location_mapping = {
                'Ketintang': 5,  # Adjust column index if needed
                'Wonokromo': 5,  # Adjust column index if needed
                'Jambangan': 5,  # Adjust column index if needed
                'Karah': 5       # Adjust column index if needed
            }

            # Check if all selected services are in the services column of the row
            service_match = all(option.lower() in row[service_mapping[option]].lower() for option in selected_services if service_mapping[option] < len(row))
            # Check if the location of the row matches any selected location
            location_match = any(option.lower() in row[location_mapping[option]].lower() for option in selected_locations if location_mapping[option] < len(row))

            return service_match and (location_match or not selected_locations)

        filtered_data = [row for row in self.data if filter_row(row)]
        if selected_locations:
            for location in selected_locations:
                self.sort_by_distance(location)
        else:
            self.display_data(filtered_data)

    def quicksort(self, data, column_index):
        if len(data) <= 1:
            return data
        pivot = data[len(data) // 2]
        left = [x for x in data if x[column_index] < pivot[column_index]]
        middle = [x for x in data if x[column_index] == pivot[column_index]]
        right = [x for x in data if x[column_index] > pivot[column_index]]
        return self.quicksort(left, column_index) + middle + self.quicksort(right, column_index)

    def sort_by_distance(self, location):
        try:
            starting_location = self.location_coordinates.get(location, None)
            if not starting_location:
                print(f"Starting location for {location} not found.")
                return

            # Load location data from CSV
            df = pd.read_csv('akunadmin.csv', delimiter=';', quotechar='"')

            # Split the combined latitude and longitude column into separate columns
            df[['Latitude', 'Longitude']] = df['-7.316384877388277, 112.73038530719742'].str.split(',', expand=True)

            # Convert Latitude and Longitude columns to float
            df['Latitude'] = df['Latitude'].astype(float)
            df['Longitude'] = df['Longitude'].astype(float)

            # Calculate distances
            df['Distance'] = df.apply(lambda row: geodesic(starting_location, (row['Latitude'], row['Longitude'])).kilometers, axis=1)

            # Sort by distance
            sorted_df = df.sort_values('Distance')

            # Convert sorted DataFrame back to list format for display
            sorted_data = sorted_df.values.tolist()
            self.display_data(sorted_data)

        except FileNotFoundError:
            print("File 'akunadmin.csv' not found.")
        except pd.errors.ParserError:
            print("Error parsing CSV file. Check the format.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def search_laundry(self):
        search_query = self.search_entry.get().lower()
        if not self.data:
            print("Data is empty or not initialized.")
            return
        filtered_data = [row for row in self.data if len(row) > 1 and search_query in row[1].lower()]
        self.display_data(filtered_data)

    def display_data(self, data):
        for widget in self.scrollable_frame.scrollable_frame.winfo_children():
            widget.destroy()
        inner_frame = self.scrollable_frame.scrollable_frame
        total_height = 0
        max_frame_width = 340  # Maximum width for the frame, consider some padding
        for i, row in enumerate(data):
            if len(row) >= 6:
                frame = tk.Frame(inner_frame, bg="#FFFFFF", width=max_frame_width)
                frame.pack(fill="x", padx=10, pady=5)

                image_path = row[5]
                image = Image.open(image_path)
                image = image.resize((330, 200))
                photo = ImageTk.PhotoImage(image)

                address = row[3]
                if len(address) > 40:
                    first_line = address[:address.rfind(' ', 0, 40)]
                    second_line = address[address.rfind(' ', 0, 40):]
                    address_text = f"Address: {first_line}\n{second_line}"
                else:
                    address_text = f"Address: {address}"

                button = tk.Button(frame, image=photo, text=f"Email: {row[0]}\nLaundry Name: {row[1]}\n{address_text}", compound="top", command=lambda current_row=row: self.button_click(current_row), font=('helvetica', 9), bg='#A2C8DF', relief='flat')
                button.image = photo  # To prevent garbage collection
                button.pack(anchor="w")

                total_height += frame.winfo_reqheight() + 10  # Add some padding between frames

    def button_click(self, row):
        self.selected_services = row[4].split(',')
        laundry_name = row[1]
        self.destroy()
        next_page = Booking(self.selected_services, laundry_name)
        next_page.mainloop()

    def back_to_main(self):
        self.destroy()
        Guest()

class Booking(tk.Tk):
    def __init__(self, services, laundry_name):
        tk.Tk.__init__(self)
        self.title("Booking")
        screen_width = 360
        screen_height = 540
        window_width = screen_width
        window_height = screen_height
        self.geometry(f"{window_width}x{window_height}")
        self.canvas = tk.Canvas(self, width=window_width, height=window_height)
        self.canvas.pack()
        image_path = "project uas\\projek fix\\booking from.png"
        image = Image.open(image_path)
        image = image.resize((window_width, window_height))
        self.photo = ImageTk.PhotoImage(image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)

        self.name_entry = tk.Entry(self, font=("verdana", 13), border=0, highlightthickness=2, highlightcolor="#0292B7", relief='groove',bg='#FFFFFF', width=25)
        self.name_entry.place(relx=0.11, rely=0.29, anchor=tk.W)
        self.Quantity_entry = tk.Entry(self, font=("verdana", 13), border=0, highlightthickness=2, highlightcolor="#0292B7", relief='groove',bg='#FFFFFF', width=5)
        self.Quantity_entry.place(relx=0.11, rely=0.56, anchor=tk.W)

        self.quantity_label = tk.Label(self, text="kg", font=("verdana", 13), bg='#C6DBEA')
        self.quantity_label.place(relx=0.29, rely=0.56, anchor=tk.W)

        self.booking_button = CTkButton(self.canvas, text="Booking", command=self.recipt,
                                        font=("verdana", int(window_height * 0.02)), corner_radius=70, bg_color='#C6DBEA', width=80, height=30)
        self.booking_button.place(relx=0.4, rely=0.9)

        # Listbox untuk menampilkan layanan yang tersedia
        self.listbox = tk.Listbox(self, selectmode=tk.MULTIPLE, width=20, height=4, bg='#FFFFFF', exportselection=False)
        self.listbox.place(relx=0.11, rely=0.37, width=100, height=55)
        self.listbox.bind('<<ListboxSelect>>', self.check_delivery)

        # Listbox untuk memilih treatment
        self.treatment_listbox = tk.Listbox(self, selectmode=tk.MULTIPLE, width=20, height=4, bg='#FFFFFF', exportselection=False)
        self.treatment_listbox.place(relx=0.55, rely=0.37, width=100, height=55)
 
        self.laundry_name_label = tk.Label(self, text=laundry_name, font=("times new roman", 12), bg="#C6DBEA")
        self.laundry_name_label.place(relx=0.5, rely=0.221, anchor=tk.CENTER)

        # Simpan informasi layanan dari GuestHome
        self.services = services

        # Isi listbox dengan layanan yang tersedia
        self.populate_service_listbox()

        # Isi listbox treatment dengan pilihan treatment
        self.populate_treatment_listbox()

        # Label dan Entry untuk alamat (disembunyikan secara default)
        self.address_label = tk.Label(self, text="Address:", font=("verdana", 13), bg='#C6DBEA')
        self.address_entry = tk.Entry(self, font=("verdana", 13), border=0, highlightthickness=2, highlightcolor="#0292B7", relief='groove',bg='#FFFFFF', width=25)

        # Label dan Calendar untuk tanggal penjemputan (disembunyikan secara default)
        self.date_label = tk.Label(self, text="Pick-up Date:", font=("verdana", 13), bg='#C6DBEA')
        self.date_entry = Calendar(self, font=("verdana", 5), background='#C6DBEA', foreground='black', borderwidth=2)

        # Label dan Combobox untuk waktu penjemputan (disembunyikan secara default)
        self.time_label = tk.Label(self, text="Pick-up Time:", font=("verdana", 13), bg='#C6DBEA')
        self.time_entry = ttk.Combobox(self, font=("verdana", 7), values=["08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00"], state='readonly', width=5)

        self.back_button = CTkButton(self.canvas, text="Back", command=self.back_to_main,
                                     font=("verdana", int(window_height * 0.02)), corner_radius=70, bg_color='#C6DBEA', width=20, height=25)
        self.back_button.place(relx=0.1, rely=0.05, anchor=tk.CENTER)
        
        
    def populate_service_listbox(self):
        # Bersihkan listbox sebelum mengisi kembali
        self.listbox.delete(0, tk.END)

        # Masukkan layanan yang tersedia ke dalam listbox
        for service in self.services:
            self.listbox.insert(tk.END, service)

    def populate_treatment_listbox(self):
        # Bersihkan listbox sebelum mengisi kembali
        treatments = ["Wash & Fold", "Ironing", "Dry Clean", "Delivery"]
        self.treatment_listbox.delete(0, tk.END)

        # Masukkan treatment ke dalam listbox
        for treatment in treatments:
            self.treatment_listbox.insert(tk.END, treatment)

    def check_delivery(self, event):
        selected_service = [self.listbox.get(i) for i in self.listbox.curselection()]
        if "Delivery" in selected_service:
            self.address_label.place(relx=0.11, rely=0.8, anchor=tk.W)
            self.address_entry.place(relx=0.11, rely=0.85, anchor=tk.W)
            self.date_label.place(relx=0.55, rely=0.51, anchor=tk.W)
            self.date_entry.place(relx=0.48, rely=0.67, anchor=tk.W)
            self.time_label.place(relx=0.11, rely=0.65, anchor=tk.W)
            self.time_entry.place(relx=0.11, rely=0.7, anchor=tk.W)
        else:
            self.address_label.place_forget()
            self.address_entry.place_forget()
            self.date_label.place_forget()
            self.date_entry.place_forget()
            self.time_label.place_forget()
            self.time_entry.place_forget()
    def get_next_queue_number(self, laundry_name):
        queue_number= []
        try:
            with open('order.csv', mode='r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[0] == laundry_name:
                        queue_number.append(int(row[-1]))
        except FileNotFoundError:
            return 1
        
        return max(queue_number, default=0) + 1

    def recipt(self):
        selected_services = [self.listbox.get(i) for i in self.listbox.curselection()]
        selected_treatments = [self.treatment_listbox.get(i) for i in self.treatment_listbox.curselection()]

        if not selected_services:
            messagebox.showwarning("Warning", "Please select at least one service.")
            return

        if not selected_treatments:
            messagebox.showwarning("Warning", "Please select at least one treatment.")
            return

        laundry_name = self.laundry_name_label.cget("text")
        name = self.name_entry.get()
        quantity = self.Quantity_entry.get()
        address = self.address_entry.get() if "Delivery" in selected_services else ""
        date = self.date_entry.get_date() if "Delivery" in selected_services else ""
        time = self.time_entry.get() if "Delivery" in selected_services else ""

        if not name or not quantity or ("Delivery" in selected_treatments and (not address or not date or not time)):
            messagebox.showwarning("Warning", "Please fill in all the fields.")
            return

        try:
            quantity = float(quantity)
        except ValueError:
            messagebox.showwarning("Warning", "Quantity must be a number.")
            return    
        queue_number= self.get_next_queue_number(laundry_name)

        with open('order.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([laundry_name, name, quantity, selected_services, selected_treatments, address, date, time,queue_number])
        self.destroy()
        next_page = Recipt(name, quantity, selected_services, selected_treatments, address, date, time,queue_number)
        next_page.mainloop()

    def back_to_main(self):
        self.destroy()
        GuestHome()

class Recipt(tk.Tk):
    def __init__(self, name, quantity, selected_services, selected_treatments, address, date, time, queue_number):
        super().__init__()
        self.title("Recipt")
        screen_width = 360
        screen_height = 540
        window_width = screen_width
        window_height = screen_height
        self.geometry(f"{window_width}x{window_height}")
        self.canvas = tk.Canvas(self, width=window_width, height=window_height)
        self.canvas.pack()
        self.background_image = Image.open("project uas\\projek fix\\recipt.png")
        self.background_image = self.background_image.resize((window_width, window_height))
        self.background_photo = ImageTk.PhotoImage(self.background_image)
        self.background_label = tk.Label(self, image=self.background_photo)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Menampilkan informasi pesanan
        tk.Label(self, text="Name: " + name, font=("verdana", 10), bg='#FFFFFF').place(relx=0.15, rely=0.3, anchor=tk.W)
        tk.Label(self, text="Quantity: " + str(quantity), font=("verdana", 10), bg='#FFFFFF').place(relx=0.15, rely=0.38, anchor=tk.W)
        tk.Label(self, text="Service: " + ', '.join(selected_services), font=("verdana", 10), bg='#FFFFFF').place(relx=0.15, rely=0.46, anchor=tk.W)
        tk.Label(self, text="Treatment: " + ', '.join(selected_treatments), font=("verdana", 10), bg='#FFFFFF').place(relx=0.15, rely=0.54, anchor=tk.W)
        
        if address:
            tk.Label(self, text="Address: " + address, font=("verdana", 10), bg='#FFFFFF').place(relx=0.15, rely=0.62, anchor=tk.W)
            tk.Label(self, text="Pick Up Date: " + date, font=("verdana", 10), bg='#FFFFFF').place(relx=0.15, rely=0.7, anchor=tk.W)
            tk.Label(self, text="Pick Up Time: " + time, font=("verdana", 10), bg='#FFFFFF').place(relx=0.15, rely=0.78, anchor=tk.W)
       
        self.queue_number_label = tk.Label(self, text=f"Queue Number: {queue_number}", font=("verdana", 10), bg='#FFFFFF')
        self.queue_number_label.place(relx=0.15, rely=0.82, anchor=tk.W)
        
        self.next_button = CTkButton(self, text="Next", command=self.go_to_last_page, 
                                     font=("verdana", int(window_height * 0.02)), corner_radius=70, bg_color='#C6DBEA', width=100, height=25)
        self.next_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

    def go_to_last_page(self):
        self.destroy()
        last_page = LastPage()
        last_page.mainloop()

class AdminHome(tk.Tk):
    def __init__(self, laundry_name):
        tk.Tk.__init__(self)
        self.title("Home Page")
        screen_width = 360
        screen_height = 540
        window_width = screen_width
        window_height = screen_height
        self.geometry(f"{window_width}x{window_height}")
        
        # Canvas and background image setup
        self.canvas = tk.Canvas(self, width=window_width, height=window_height)
        self.canvas.pack()
        image_path = "project uas\\projek fix\\adminhomeee.png"
        try:
            image = Image.open(image_path)
            image = image.resize((window_width, window_height))
            self.photo = ImageTk.PhotoImage(image)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)
        except FileNotFoundError:
            messagebox.showerror("Error", "Image file not found.")
        
        # Laundry name label
        self.laundry_name_label = tk.Label(self, text=laundry_name, font=("times new roman", 12), bg="#A2C8DF")
        self.laundry_name_label.place(relx=0.5, rely=0.221, anchor=tk.CENTER)
    
        # Treeview setup
        self.tree_frame = tk.Frame(self)
        self.tree_frame.place(relx=0.01, rely=0.29, relwidth=0.98, relheight=0.7)
 
        self.tree = ttk.Treeview(self.tree_frame, columns=("No", "Name", "Quantity", "Services", "Treatments", "Address", "Date", "Time"), show='headings')
        self.tree.heading("No", text="No", anchor=tk.CENTER)
        self.tree.heading("Name", text="Name", anchor=tk.CENTER)
        self.tree.heading("Quantity", text="Quantity", anchor=tk.CENTER)
        self.tree.heading("Services", text="Services", anchor=tk.CENTER)
        self.tree.heading("Treatments", text="Treatments", anchor=tk.CENTER)
        self.tree.heading("Address", text="Address", anchor=tk.CENTER)
        self.tree.heading("Date", text="Date", anchor=tk.CENTER)
        self.tree.heading("Time", text="Time", anchor=tk.CENTER)
        self.tree.column("#0", width=0, stretch=False)  # Hide the first empty column
        self.tree.column("No", width=30, anchor=tk.CENTER, stretch=True)
        self.tree.column("Name", width=70, anchor=tk.CENTER, stretch=True)
        self.tree.column("Quantity", width=70, anchor=tk.CENTER, stretch=True)
        self.tree.column("Services", width=100, anchor=tk.CENTER, stretch=True)
        self.tree.column("Treatments", width=100, anchor=tk.CENTER, stretch=True)
        self.tree.column("Address", width=150, anchor=tk.CENTER, stretch=True)
        self.tree.column("Date", width=80, anchor=tk.CENTER, stretch=True)
        self.tree.column("Time", width=80, anchor=tk.CENTER, stretch=True)
        
        # Adding vertical and horizontal scrollbars
        self.vsb = ttk.Scrollbar(self.tree_frame, orient="vertical", command=self.tree.yview)
        self.hsb = ttk.Scrollbar(self.tree_frame, orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=self.vsb.set, xscrollcommand=self.hsb.set)
        
        # Grid configuration for treeview and scrollbars
        self.tree.grid(row=0, column=0, sticky="nsew")
        self.vsb.grid(row=0, column=1, sticky="ns")
        self.hsb.grid(row=1, column=0, sticky="ew")

        self.tree_frame.grid_rowconfigure(0, weight=1)
        self.tree_frame.grid_columnconfigure(0, weight=1)
        
        # Load booking data
        self.load_booking_data()

        # Custom Style for Treeview columns and items
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("Treeview.Heading", background="#D9E5EF", foreground="black")
        self.style.map("Treeview.Heading", background=[("active", "#347083")])
        self.style.configure("Treeview", background="#A2C8DF", fieldbackground="#A2C8DF", foreground="black")
        self.style.map("Treeview", background=[("selected", "#347083")])

    def load_booking_data(self):
        admin_laundry_name = self.laundry_name_label.cget("text")
        order_number = 1  # Initialize order number
        try:
            with open('order.csv', mode='r') as file:
                reader = csv.reader(file)
                for row in reader:
                    # Check if the laundry name in the row matches the admin's laundry name
                    if row and row[0].strip() == admin_laundry_name:  
                        # Insert only the necessary values (excluding the laundry name) into the treeview
                        values = [order_number] + row[1:]  # Add order number and exclude the first element (laundry name)
                        self.tree.insert("", tk.END, values=values)
                        self.tree.insert("", tk.END, values=["-" * 200])  # Add separator line between orders
                        order_number += 1  # Increment order number for the next order
        except FileNotFoundError:
            messagebox.showerror("Error", "Order file not found.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

class LastPage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Last Page")
        screen_width = 360
        screen_height = 540
        window_width = screen_width
        window_height = screen_height
        self.geometry(f"{window_width}x{window_height}")
        self.canvas = tk.Canvas(self, width=window_width, height=window_height)
        self.canvas.pack()
        # Image path to be replaced with your image
        image_path = "project uas\\projek fix\\bookingsukses.jpg"
        image = Image.open(image_path)
        image = image.resize((window_width, window_height))
        self.photo = ImageTk.PhotoImage(image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)

        # Menambahkan tombol Admin
        self.admin_button = CTkButton(self, text="Admin", command=self.contact_admin, 
                                      font=("verdana", int(window_height * 0.02)), corner_radius=70, bg_color='#C6DBEA', width=100, height=30)
        self.admin_button.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

    def contact_admin(self):
        # Ganti nomor dengan nomor WhatsApp yang ingin Anda tuju
        phone_number = "6285258309060"
        url = f"https://wa.me/{phone_number}"
        webbrowser.open(url)

if __name__ == "__main__":
    app = CustomTkinterApp()
    app.mainloop()