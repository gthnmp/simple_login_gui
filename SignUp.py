import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from Authentication import CreateUser, CheckUser

PRIMARY_FONT = ('Verdana', 22)
SECONDARY_FONT = ('Verdana', 16)

def pack_those_widgets(list_of_widgets):
    """
    Packs a list of tkinter widgets with common padding and filling options.

    Args:
    - list_of_widgets: list of tkinter widgets

    Returns: None
    """
    for widget in list_of_widgets:
        widget.pack(padx=30, pady=15, fill="x", expand=True)

class Register:
    """
    Class representing a registration page in a tkinter application.
    """
    def __init__(self, master_frame):
        """
        Constructor for Register class.

        Args:
        - master_frame: tkinter Frame object representing the main window

        Returns: None
        """
        def go_to_login_page():
            """
            Function to switch to the login page when called.

            Returns: None
            """
            from SignIn import Login
            for widget in master_frame.winfo_children():
                widget.destroy()
            Login(master_frame)

        self.page_title = ctk.CTkLabel(master=master_frame, text="Let's Make You\nBecome one of us👆👆", font=PRIMARY_FONT)
        self.error_label = ctk.CTkLabel(master=master_frame, text="", font=PRIMARY_FONT)
        self.input_username = ctk.CTkEntry(master=master_frame, placeholder_text="Enter your username", font=SECONDARY_FONT)
        self.input_email = ctk.CTkEntry(master=master_frame, placeholder_text="Enter your email", font=SECONDARY_FONT)
        self.input_password1 = ctk.CTkEntry(master=master_frame, placeholder_text="Enter your password", font=SECONDARY_FONT)
        self.input_password2 = ctk.CTkEntry(master=master_frame, placeholder_text="Re-enter your password", font=SECONDARY_FONT)
        self.register_button = ctk.CTkButton(master=master_frame, text="Let's Become A New Member!", font=SECONDARY_FONT, command=self.create_user)
        self.login_button = ctk.CTkButton(master=master_frame, text="Sign In", font=SECONDARY_FONT, command=go_to_login_page)
        widgets = [self.page_title, self.input_username, self.input_email, self.input_password1, self.input_password2, self.register_button, self.login_button]
        pack_those_widgets(widgets)

    def create_user(self):
        """
        Method to create a new user when the register button is clicked.

        Returns: None
        """
        self.USERNAME = self.input_username.get()
        self.EMAIL = self.input_email.get()
        self.PASSWORD = self.input_password1.get() if self.input_password1.get() == self.input_password2.get() else None
        user = CheckUser(self.USERNAME, self.PASSWORD)
        if user.isexist():
            return CTkMessagebox(message="Sorry, user is already exist!", icon="cancel", option_1="Ok :(")
        new_user = CreateUser(self.USERNAME, self.EMAIL, self.PASSWORD)
        new_user.create_user()
