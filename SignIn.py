import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from Authentication import CheckUser

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
        widget.pack(padx = 30, pady = 15, fill = "x", expand = True)

class Login:
    """
    Class representing a login page in a tkinter application.
    """

    def __init__ (self, master_frame):
        """
        Constructor for Login class.

        Args:
        - master_frame: tkinter Frame object representing the main window
        """

        def go_register_page():
            """
            Function to switch to the regsister page when called.

            Returns: None
            """
            from SignUp import Register
            for widget in master_frame.winfo_children():
                widget.destroy()
            Register(master_frame)

        self.page_title         = ctk.CTkLabel(master = master_frame, text = "Please Sign In", font = PRIMARY_FONT)
        self.error_label        = ctk.CTkLabel(master = master_frame, text = "")
        self.input_username     = ctk.CTkEntry(master = master_frame, placeholder_text="Enter your username or email", font = SECONDARY_FONT)
        self.input_password     = ctk.CTkEntry(master = master_frame,placeholder_text="Enter your password", font = SECONDARY_FONT)
        self.login_button       = ctk.CTkButton(master = master_frame, text = "Let's Go!", font = SECONDARY_FONT, command = self.check_user_existence)
        self.register_button    = ctk.CTkButton(master = master_frame, text = "Become A New User!", font = SECONDARY_FONT, command=go_register_page)
        widgets = [self.page_title,self.input_username,self.input_password, self.login_button, self.register_button, self.error_label]
        pack_those_widgets(widgets)
        
    def check_user_existence(self): 
        """
        Method to check whether the inputed data is already exist or not.

        Returns: Success message box is there is no existing data, and Invalid message box otherwise.  
        """
        self.USERNAME = self.input_username.get()
        self.PASSWORD = self.input_password.get()
        check = CheckUser(self.USERNAME, self.PASSWORD)
        print(f"user exist : {check.isexist()}") 
        if check.isexist() is True:
            return CTkMessagebox(message="Login Success!", icon="check", option_1="Thanks!")
        return CTkMessagebox(message = "Invalid User :(", icon = "cancel", option_1 = "Sorry!")
    
