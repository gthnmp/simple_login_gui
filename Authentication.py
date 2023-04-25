import sqlite3 as sqlite
import hashlib 

def passwd_hash(password):
    """
    Hashes the input password using SHA-256 algorithm.
    
    Args:
        password (str): The password to be hashed.
    
    Returns:
        str: The hexadecimal representation of the password hash.
    """
    hash_password = hashlib.sha256()
    hash_password.update(password.encode('utf8'))
    return hash_password.hexdigest()

class CreateUser:
    """
    Class to create a new user and insert the user's information into the users database.
    """
    def __init__(self, username, email, password):
        """
        Initializes a new CreateUser object.
        
        Args:
            username (str): The username of the new user.
            password (str): The password of the new user.
            email (str): The email of the new user. 
        """
        self.definite_username = username
        self.definite_email = email
        self.definite_password = passwd_hash(password)
        self.values = (self.definite_username, self.definite_email, self.definite_password)
  
    def create_user(self): 
        """
        Creates a new user by inserting the user's information into the users database.
        """
        try:
            conn = sqlite.connect("users.db")
            cur = conn.cursor()
            command = "INSERT INTO users (username, email, passwd_hash) VALUES (?, ?, ?);"
            cur.execute(command, self.values)
            conn.commit()
            cur.close()
            conn.close()
            print(self.values)
            print("User registered successfully.")
        except sqlite.Error as e:
            print("Error inserting data into the database:", e)
        except Exception as e:
            print("Error:", e)
    
class CheckUser:
    """
    Class to check the existence of a user in the users database.
    """
    def __init__(self, definite_username, definite_password):
        """
        Initializes a new CheckUser object.
        
        Args:
            definite_username (str): The username of the user to be checked.
            definite_password (str): The password of the user to be checked.
        """
        self.definite_username = definite_username
        self.definite_password = passwd_hash(definite_password)
        self.user_values = (self.definite_username, self.definite_password)
    
    def isexist(self):
        """
        Checks if the user exists in the users database.
        
        Returns:
            bool: True if the user exists, False otherwise.
        """
        self.user_existence = False
        try:
            conn = sqlite.connect("users.db")
            curr = conn.cursor()
            command = f"SELECT username,passwd_hash FROM users WHERE username = '{str(self.definite_username)}'"
            curr.execute(command)
            data = curr.fetchone()
            if self.user_values == data:
                self.user_existence = True
        except sqlite.Error as e:
            print(f"User does not exist : {e}")
        
        return self.user_existence
    
    # def isdouble(self):
    #     """
    #     Checks if the users is already exist in the database.
        
    #     Returns :
    #         bool: True if the user exists, False otherwise.
    #     """
    #     self.user_existence = False
    #     try:
    #         conn = sqlite.connect("users.db")
    #         cursor = conn.cursor()
    #         command = f"SELECT username, passwd_hash FROM users WHERE username = '{self.definite_username}'"
    #         cursor.execute(command)
    #         user_data = cursor.fetchone()
    #         if user_data is not self.user_values:

    #     except sqlite.Error as e:
    #         print("Error :", e)        
