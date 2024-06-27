import guizero as gz
import os
import subprocess
import platform
import csv
import sys
from Mod11_validations import Validations
from Mod11_config_files import STATES


class InformationForm:

    def __init__(self):
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
        self.setup_gui()

    def setup_gui(self):
        """Set up the GUI layout for the form."""
        self.create_menu_bar()
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
        self.state_dropdown = gz.Combo(address_box, options=STATES, grid=[1, 3], align="left")

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
        self.menubar = gz.MenuBar(self.app,
                                  toplevel=["File"],
                                  options=[
                                      [["Open", self.open_file], ["Save", self.submit_form], ["Exit", self.file_exit],
                                       ["Clear", self.clear_form]]
                                  ])

    def add_text_input(self, parent_box, input_label, attribute_name, grid_y, multiline=False, height=3, width=40):
        """Helper method to add a text label and input box to the GUI."""
        gz.Text(parent_box, text=input_label, font="Comic Sans MS", grid=[0, grid_y], align="left")
        if multiline:
            setattr(self, attribute_name,
                    gz.TextBox(parent_box, height=height, width=width, grid=[0, grid_y + 1], align="left",
                               multiline=True))
        else:
            setattr(self, attribute_name, gz.TextBox(parent_box, width=width, grid=[0, grid_y + 1], align="left"))

    def validate_form(self):
        """
        Validate all input fields in the form and display error messages.
        """
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
        if not validator.validate_state(self.state_dropdown.value, STATES):
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
        """Clear all input fields in the form."""
        for attr in ["first_name_input", "last_name_input", "email_input", "phone_input", "address_input", "city_input",
                     "zip_input",  "comment_input"]:
            getattr(self, attr).value = ""
        self.state_dropdown.value = STATES[0]

        self.first_name_input.focus()

    def file_exit(self):
        print("Exit")
        self.app.destroy()

    def collect_form_data(self):
        """Collect data from the form."""
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
