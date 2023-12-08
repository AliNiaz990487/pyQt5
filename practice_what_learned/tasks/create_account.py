import os
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
import json

ACCOUNTS_JSON = "backup/accounts.json"

class CreateAccountWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.accounts = list()

        uic.loadUi("ui/create_account_window.ui", self)
        self.createAccountBtn.clicked.connect(self.create_account)
        self.read_from_json(ACCOUNTS_JSON)

    
    def create_account(self):
        print(self.accounts)
        if self.validate_input_fields():
            self.accounts.append(self.collect_input())  
            self.clear_text_fields()
            self.write_to_json(ACCOUNTS_JSON) 

            self.close()
    
    def read_from_json(self, filename):
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                data = json.load(file)
                for d in data:
                    self.accounts.append(d)

        
    def write_to_json(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.accounts, file, indent=2)
        print(f'Data written to {filename} successfully.')

    def collect_input(self):
        return {
            "firstName": self.firstNameInput.text(),
            "lastName": self.lastNameInput.text(),
            "username": self.usernameInput.text(),
            "password": self.passwordInput.text()
        }
    def clear_text_fields(self):
        self.firstNameInput.setText("")
        self.lastNameInput.setText("")
        self.usernameInput.setText("")
        self.passwordInput.setText("")

    def validate_input_fields(self):
        fields = [
            self.firstNameInput,
            self.lastNameInput,
            self.usernameInput,
            self.passwordInput
        ]
        for f in fields:
            f.setStyleSheet("border: 1px solid black")

        for f in fields:
            if not len(f.text()):
                f.setStyleSheet("border: 1px solid red")
                return False
        return True