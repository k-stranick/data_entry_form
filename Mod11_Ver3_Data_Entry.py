##########################################################
# Author : Kyle Stranick                                 #
# Class : ITN160                                         #
# Class Section : 401                                    #
# Date : 11/12/2023                                      #
# Assignment 11: Data Entry                              #
# Version : 3.1                                          #
##########################################################

###################
#Syntax References:
###################
# code academy go APP
# Cannon, Jason. (2016). Python Succinctly., Syncfusion Inc.
# Gupta, Anubhav. Slither into Python. (2021?)
# Murach, Mike. (2021). Murach's Python Programming (2nd Ed.), Mike Murach & Associates, Inc.
# https://docs.python.org/3/library/exceptions.html#bltin-exceptions
# https://www.tutorialspoint.com/python/python_if_else.htm
# https://www.tutorialspoint.com/python/python_functions.htm
# https://www.w3schools.com/python/
# https://www.pluralsight.com  I have a subscription
# https://www.w3schools.com/python/python_dictionaries.asp
# https://initialcommit.com/blog/python-isalpha-string-method
# https://stackoverflow.com/questions/29460405/checking-if-string-is-only-letters-and-spaces-python
# https://www.geeksforgeeks.org/python-test-if-string-contains-alphabets-and-spaces/
# https://www.geeksforgeeks.org/find-average-list-python/
# https://code-basics.com/languages/python/lessons/magic-numbers
# https://wiki.python.org/moin/HandlingExceptions
# https://wiki.python.org/moin/ForLoop
# https://wiki.python.org/moin/WhileLoop
# https://docs.python.org/3/tutorial/datastructures.html
# https://guicommits.com/organize-python-code-like-a-pro/
# https://docs.python-guide.org/writing/structure/
# https://www.askpython.com/python/examples/generate-random-colors#:~:text=Using%20the%20random%20module&text=We%20can%20implement%20it%20to%20generate%20random%20colors.&text=Here%20we%20have%20created%20a,returns%20them%20as%20a%20tuple.
# https://stackoverflow.com/questions/16726354/saving-the-highscore-for-a-game <- implement??
# https://stackoverflow.com/questions/63769198/giving-one-hint-for-each-of-the-tries-guessing-number-game
# https://realpython.com/python-raise-exception/
# https://realpython.com/python-raise-exception/#choosing-the-exception-to-raise-built-in-vs-custom
# https://stackoverflow.com/questions/28465779/how-do-i-limit-the-amount-of-letters-in-a-string
# https://dbader.org/blog/meaning-of-underscores-in-python
# https://www.programiz.com/python-programming/csv#google_vignette
# https://www.w3schools.com/python/ref_keyword_del.asp#:~:text=Definition%20and%20Usage,parts%20of%20a%20list%20etc.
# https://docs.python.org/3/library/csv.html
# https://docs.python.org/3/library/functions.html
# https://www.geeksforgeeks.org/file-flush-method-in-python/
# https://docs.python.org/3/library/getpass.html
# https://www.analyticsvidhya.com/blog/2021/08/python-tutorial-working-with-csv-file-for-data-science/
# https://stackoverflow.com/questions/35805078/how-do-i-convert-a-password-into-asterisks-while-it-is-being-entered#:~:text=this%20can%20be%20resolved%20by,link%20to%20python's%20Lib%20folder.&text=this%20will%20add%20*%20to%20your%20password%20inputs.
# https://stackoverflow.com/questions/9202224/getting-a-hidden-password-input
# https://www.youtube.com/watch?v=dR_cDapPWyY
# https://stackoverflow.com/questions/69301274/how-to-make-sign-up-and-login-program-in-python
# https://stackoverflow.com/questions/28465779/how-do-i-limit-the-amount-of-letters-in-a-string
# https://app.pluralsight.com/course-player?clipId=f7a8297c-32e7-4cbf-9463-36f2f6ae25dc
# https://careerkarma.com/blog/python-jsondecodeerror/
# https://www.google.com/search?q=key%3Dlambda+python&rlz=1C1CHBF_enUS1036US1036&oq=key%3D&gs_lcrp=EgZjaHJvbWUqDAgBEAAYFBiHAhiABDIJCAAQRRg5GIAEMgwIARAAGBQYhwIYgAQyBwgCEAAYgAQyBwgDEAAYgAQyBwgEEAAYgAQyBwgFEAAYgAQyBwgGEAAYgAQyBwgHEAAYgAQyBwgIEAAYgAQyBwgJEAAYgATSAQoxMjE0NmowajE1qAIAsAIA&sourceid=chrome&ie=UTF-8#fpstate=ive&vld=cid:9440843d,vid:goPKxNtuxWo,st:0
# https://www.digitalocean.com/community/tutorials/python-static-method
# https://plainenglish.io/blog/build-a-fast-food-order-taker-in-python-87188efcbbdd
# https://www.geeksforgeeks.org/python-grouping-dictionary-keys-by-value/
# https://docs.python.org/3/howto/sorting.html
# https://realpython.com/python-sort/
# https://www.youtube.com/playlist?list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc
# https://pynative.com/python-static-method/
# https://docs.python.org/3/library/exceptions.html
# https://stackoverflow.com/questions/69199893/using-python-guizero-how-to-access-textbox-input-data-from-a-second-window
# https://www.w3schools.com/python/ref_func_getattr.asp
# https://www.geeksforgeeks.org/python-getattr-method/
# https://docs.python.org/3/library/exceptions.html
# https://validators.readthedocs.io/en/latest/
# https://stackoverflow.com/questions/11832400/validate-postal-code
# https://stackoverflow.com/questions/28495822/best-way-to-validate-a-name-in-python
# https://pypi.org/project/validator/
# https://wiki.python.org/moin/GuiProgramming
# https://docs.python.org/3/library/re.html
# https://www.geeksforgeeks.org/check-if-email-address-valid-or-not-in-python/
# https://validators.readthedocs.io/en/latest/
# https://lawsie.github.io/guizero/textbox/
# https://www.w3schools.com/python/python_arrays.asp
# https://lawsie.github.io/guizero/window/
# https://stackoverflow.com/questions/4553129/when-to-use-os-name-sys-platform-or-platform-system
# https://www.simplilearn.com/tutorials/python-tutorial/subprocess-in-python
# https://docs.python.org/3/library/os.path.html
# https://lawsie.github.io/guizero/layout/
# https://lawsie.github.io/guizero/combo/
# https://github.com/lawsie/guizero/blob/master/examples/layout_boxes.py
# https://www.penguintutor.com/programming/guizero
# https://github.com/Sven-Bo/data-entry-form-pysimplegui
# https://www.youtube.com/watch?v=vusUfPBsggw
# https://snyk.io/advisor/python/guizero/functions/guizero.TextBox
# https://lawsie.github.io/guizero/start/
# https://lawsie.github.io/guizero/box/
# https://lawsie.github.io/guizero/menubar/
# https://github.com/lawsie/guizero/blob/master/examples/menu_bar.py
import guizero as gz  # For creating the GUI
import csv            # For handling CSV file operations
import os             # For file and directory operations
import subprocess     # For opening files with default applications
import platform       # For detecting the operating system
import validators     # For validating email addresses
import regex as re    # For regular expression operations
import sys

class Validations:
    # Regular expression patterns for various validations
    NAME_PATTERN = re.compile(r"^\p{L}[\p{L} \'-]*\p{L}$")
    PHONE_PATTERN = re.compile(r"^\+?1?(\(?\d{3}\)?-?\d{3}-?\d{4})$")
    ADDRESS_PATTERN = re.compile(r"^\d+\s\p{L}[\p{L}\s,'-]*")
    CITY_PATTERN = re.compile(r"^\p{L}+(?:[\s-]\p{L}+)*")
    ZIP_CODE_PATTERN = re.compile(r"^\d{5}$")
    """
    A class for validating various input fields of a form.
    """

    def __init__(self, first_name, last_name, email, phone, address, city_input, zip_code):
        """
        Initialize the Validations class with user input values.

        Parameters:
        first_name (str): User's first name.
        last_name (str): User's last name.
        email (str): User's email address.
        phone (str): User's phone number.
        address (str): User's address.
        city_input (str): User's city.
        zip_code (str): User's zip code.
        """
        # Initialize instance variables with the provided arguments
        self.first_name = first_name
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.address = address
        self.city = city_input
        self.zip_code = zip_code

    # Below are the validation methods for each field
    def validate_name(self, name):
        """
        Validate a name using the defined regular expression pattern.

        Parameters:
        name (str): The name to be validated.

        Returns:
        bool: True if the name is valid, False otherwise.
        """
        return name.strip() and self.NAME_PATTERN.match(name)

    def validate_email(self):
        """
        Validate the email using the 'validators' library.

        Returns:
        bool: True if the email is valid, False otherwise.
        """
        return self.email.strip() and validators.email(self.email)

    def validate_phone(self):
        """
        Validate the phone number using the defined regular expression pattern.

        Returns:
        bool: True if the phone number is valid, False otherwise.
        """
        return self.phone.strip() and self.PHONE_PATTERN.match(self.phone)

    def validate_address(self):
        """
        Validate the address using the defined regular expression pattern.

        Returns:
        bool: True if the address is valid, False otherwise.
        """
        return self.address.strip() and self.ADDRESS_PATTERN.match(self.address)

    def validate_city(self):
        """
        Validate the city using the defined regular expression pattern.

        Returns:
        bool: True if the city is valid, False otherwise.
        """
        return self.city.strip() and self.CITY_PATTERN.match(self.city)

    def validate_zip_code(self):
        """
        Validate the zip code using the defined regular expression pattern.

        Returns:
        bool: True if the zip code is valid, False otherwise.
        """
        return self.zip_code.strip() and self.ZIP_CODE_PATTERN.match(self.zip_code)

    @staticmethod
    def validate_state(selected_state, states):
        """
        Validate the selected state against a list of states.

        Parameters:
        selected_state (str): The state selected by the user.
        states (list): List of valid states.

        Returns:
        bool: True if the state is valid, False otherwise.
        """
        return selected_state in states and selected_state != states[0]


class InformationForm:
    """
    A class representing a form for collecting user information.
    This class handles the creation of the GUI elements and their interactions.
    """
    STATES = [
        # List of states for the state dropdown
        "", "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA",
        "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
        "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
        "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
        "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"
    ]

    def __init__(self):
        """
        Initialize the InformationForm class and set up the GUI components.
        """
        # Constructor for the InformationForm class
        self.app = gz.App(title="Information Form", height=640, width=500)
        self.app.tk.resizable(False, False)

        # Define form input attributes
        self.first_name_input = None
        self.last_name_input = None
        self.email_input = None
        self.phone_input = None
        self.address_input = None
        self.city_input = None
        self.state_dropdown = None
        self.zip_input = None
        self.comment_input = None

        # Define button attributes
        self.submit_btn = None
        self.clear_btn = None
        self.open_btn = None
        self.menubar = None

        # Set up the GUI layout
        self.setup_gui()

    def setup_gui(self):
        """Set up the GUI layout for the form."""
        # Menu bar setup
        self.create_menu_bar()
        # Add title, input fields, and buttons
        # Additional code for setting up the GUI components will be provided in the follow-up messages

        # Create a title box at the top of the app
        title_box = gz.Box(self.app, height=30, width=500, align="top", border=True)
        gz.Text(title_box, text="Please Enter Your Information", font="Comic Sans MS")

        # Personal information section
        pers_info = gz.Box(self.app, height=200, width=500, layout="grid", border=True)
        self.add_text_input(pers_info, "First Name:", 'first_name_input', 0)
        self.add_text_input(pers_info, "Last Name:", 'last_name_input', 2)
        self.add_text_input(pers_info, "Email Address:", 'email_input', 4)
        self.add_text_input(pers_info, "Phone Number:", 'phone_input', 6)

        # Address section
        address_box = gz.Box(self.app, height=140, width=500, layout="grid", border=True)
        self.add_text_input(address_box, "Address:", "address_input", 0)
        self.add_text_input(address_box, "City:", "city_input", 2)

        gz.Text(address_box, text="State:", font="Comic Sans MS", grid=[1, 2], align="left")
        self.state_dropdown = gz.Combo(address_box, options=self.STATES, grid=[1, 3], align="left")

        gz.Text(address_box, text="Zip Code:", font="Comic Sans MS", grid=[2, 2], align="left")
        self.zip_input = gz.TextBox(address_box, width=15, grid=[2, 3], align="left")

        # Comment Box
        comment_box = gz.Box(self.app, height=210, width=500, layout="grid", border=True)
        self.add_text_input(comment_box, input_label="Comments:", multiline=True, attribute_name="comment_input",
                            height=11, width=62, grid_y=0)

        # Buttons section
        button_box = gz.Box(self.app, height=30, width=500, align="bottom")
        self.submit_btn = gz.PushButton(button_box, text="Submit", align="left", width=20, command=self.submit_form)
        self.clear_btn = gz.PushButton(button_box, text="Clear", align="left", command=self.clear_form)
        self.open_btn = gz.PushButton(button_box, text="Open File", align="left", command=self.open_file)

        self.first_name_input.focus()

    def create_menu_bar(self):
        """
        Create a menu bar for the application.
        """
        # Define the menu bar and its options

        self.menubar = gz.MenuBar(self.app,
                                  toplevel=["File"],
                                  options=[
                                      [["Open", self.open_file], ["Save", self.submit_form], ["Exit", self.file_exit],
                                       ["Clear", self.clear_form]]
                                  ])

    def add_text_input(self, parent_box, input_label, attribute_name, grid_y, multiline=False, height=3, width=40):
        """
        Add a text input field with a label to the GUI.

        Parameters:
        parent_box (gz.Box): The container box for the input field.
        input_label (str): The label text for the input field.
        attribute_name (str): The attribute name to assign the input field.
        grid_y (int): The y-coordinate in the grid layout for the input field.
        multiline (bool): Determines if the input field is multiline.
        height (int): The height of the input field (used for multiline).
        width (int): The width of the input field.
        """
        # Add a text label and input box to the GUI
        gz.Text(parent_box, text=input_label, font="Comic Sans MS", grid=[0, grid_y], align="left")
        if multiline:
            setattr(self, attribute_name,
                    gz.TextBox(parent_box, height=height, width=width, grid=[0, grid_y + 1], align="left",
                               multiline=True))
        else:
            setattr(self, attribute_name, gz.TextBox(parent_box, width=width, grid=[0, grid_y + 1], align="left"))

    def validate_form(self):
        """
        Validate all input fields in the form and display error messages if any.

        Returns:
        bool: True if all inputs are valid, False otherwise.
        """
        # Collect and validate form data
        error_messages = []
        validator = Validations(
            self.first_name_input.value,
            self.last_name_input.value,
            self.email_input.value,
            self.phone_input.value,
            self.address_input.value,
            self.city_input.value,
            self.zip_input.value
        )

        if not validator.validate_name(validator.first_name):
            error_messages.append("First Name is not valid or empty.")
        if not validator.validate_name(validator.last_name):
            error_messages.append("Last Name is not valid or empty.")
        if not validator.validate_email():
            error_messages.append("Email is not valid or empty.")
        if not validator.validate_phone():
            error_messages.append("Phone Number is not valid or empty.")
        if not validator.validate_address():
            error_messages.append("Address is not valid or empty.")
        if not validator.validate_city():
            error_messages.append("City is not valid or empty.")
        if not validator.validate_state(self.state_dropdown.value, self.STATES):
            error_messages.append("State is not selected.")
        if not validator.validate_zip_code():
            error_messages.append("Zip Code is not valid or empty.")

        if error_messages:
            gz.warn("Input Error", "\n".join(error_messages))
            return False
        return True

    def open_file(self):
        """
        Opens the data file with the default application based on the operating system.

        This method checks if the file exists. If it does not, a warning message is displayed.
        Depending on the user's operating system, different commands are used to open the file:
        - Windows: Uses `os.startfile`.
        - macOS: Uses `subprocess.run` with the `open` command.
        - Linux and other Unix-like systems: Uses `subprocess.run` with the `xdg-open` command.
        Exceptions during the file opening process are handled and logged.
        """
        data_file_path = self.get_data_file_path()
        if not os.path.exists(data_file_path):
            gz.warn("Error", "The data file does not exist.")
            return

        try:
            if platform.system() == "Windows":
                os.startfile(data_file_path)
            elif platform.system() == "Darwin":  # MacOS
                subprocess.run(["open", data_file_path])
            else:  # Linux
                subprocess.run(["xdg-open", data_file_path])
        except Exception as e:
            print(f"Error opening file: {e}")

    def clear_form(self):
        """
        Clears all input fields in the form.

        Iterates through a list of attribute names corresponding to input fields and sets their value to an empty string
        Resets the state dropdown to its default value and sets the focus back to the first name input field.
        """
        for attr in ["first_name_input", "last_name_input", "email_input", "phone_input", "address_input", "city_input",
                     "zip_input",  "comment_input"]:
            getattr(self, attr).value = ""
        self.state_dropdown.value = self.STATES[0]

        self.first_name_input.focus()

    def file_exit(self):
        """
        Handles the exit operation for the application.

        Prints an 'Exit' message to the console and destroys the application window, closing the application.
        """
        print("Exit")
        self.app.destroy()

    def collect_form_data(self):
        """
        Collects and organizes data from the form into a dictionary.

        Retrieves values from each input field and maps them to corresponding keys representing the form field names.
        Returns a dictionary containing all the user-provided information in a structured format.
        """
        return {
            "First Name": self.first_name_input.value,
            "Last Name": self.last_name_input.value,
            "Email": self.email_input.value,
            "Phone": self.phone_input.value,
            "Address": self.address_input.value,
            "City": self.city_input.value,
            "State": self.state_dropdown.value,
            "Zip": self.zip_input.value,
            "Comments": self.comment_input.value
        }

    def submit_form(self):
        """
        Submits form data to a CSV file.

        Validates the form data before submission. If validation fails, submission is aborted.
        On successful validation, collects form data and writes it to a CSV file.
        Handles file I/O errors and other exceptions, displaying appropriate messages in case of failure.
        On successful data writing, displays a success message and clears the form.
        """
        if not self.validate_form():  # Check if form data is valid
            return  # Don't proceed with submission if validation fails

        data = self.collect_form_data()
        try:
            data_file_path = self.get_data_file_path()
            file_exists = os.path.isfile(data_file_path)
            with open(data_file_path, "a", newline='') as file:
                columns = ["First Name", "Last Name", "Email", "Phone", "Address", "City", "State", "Zip", "Comments"]
                writer = csv.DictWriter(file, fieldnames=columns)
                if not file_exists:
                    writer.writeheader()
                writer.writerow(data)
        except IOError as e:
            # Handle file I/O errors
            gz.error("File Error", f"An error occurred while writing to the file: {e}")
        except Exception as e:
            # Handle other potential exceptions
            gz.error("Error", f"An unexpected error occurred: {e}")
        else:
            # This block executes if no exception was raised
            gz.info("Success", "The information has been successfully saved.")
            self.clear_form()


    @staticmethod
    def get_data_file_path():
        if getattr(sys, 'frozen', False):
            # The application is frozen
            base_path = os.path.dirname(sys.executable)
        else:
            # The application is not frozen
            base_path = os.path.dirname(__file__)

        data_dir = os.path.join(base_path, "data")
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)  # Create 'data' directory if it doesn't exist

        return os.path.join(data_dir, "data.csv")
if __name__ == "__main__":
    form = InformationForm()
    form.app.display()
