# Importing required modules
import customtkinter as ctk
from SignIn import Login
from SignUp import Register

# Setting default color theme and appearance mode for customtkinter
ctk.set_default_color_theme("blue")
ctk.set_appearance_mode("Dark")

# Defining fonts
PRIMARY_FONT = ('Verdana', 22)
SECONDARY_FONT = ('Verdana', 16)

# Function to pack widgets into a container with specified padding and expansion properties
def pack_those_widgets(list_of_widgets):
    for widget in list_of_widgets:
        widget.pack(padx=30, pady=15, fill="x", expand=True)

# Container class
class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        ctk.CTk.__init__(self, *args, **kwargs)
        self.title("Login")  # Setting title of the window
        self.geometry("700x500")  # Setting initial window size
        self.home_page()  # Calling the home_page() method to populate the window with widgets

    # Method to create the home page of the app
    def home_page(self):
        main_frame = ctk.CTkFrame(self, width=700, height=700)  # Creating a main frame for the app
        main_frame.place(relx=0.5, rely=0.5, anchor="center")  # Placing the main frame at the center of the window

        # Function to switch to the login page
        def login_page():
            for widget in main_frame.winfo_children():
                widget.destroy()  # Destroying all widgets inside the main frame
            Login(main_frame)  # Creating an instance of the Login class and passing the main frame as its parent

        # Function to switch to the register page
        def register_page():
            for widget in main_frame.winfo_children():
                widget.destroy()  # Destroying all widgets inside the main frame
            Register(main_frame)  # Creating an instance of the Register class and passing the main frame as its parent

        # Adding widgets to the main frame
        ctk.CTkLabel(master=main_frame, text="Welcome To My Login System App!\n\nCreated By vroses / gthnmp",font=PRIMARY_FONT).pack(padx=20, pady=20)
        ctk.CTkButton(master=main_frame, text="Login", command=login_page, font=SECONDARY_FONT).pack(padx=20, pady=20)
        ctk.CTkButton(master=main_frame, text="Register", command=register_page, font=SECONDARY_FONT).pack(padx=20,pady=20)

app = App()  # Creating an instance of the App class
app.mainloop()  # Starting the main event loop to display the window and handle user interactions
