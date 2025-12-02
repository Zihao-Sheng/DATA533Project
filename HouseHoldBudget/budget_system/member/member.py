"""
===========================================================
 Member Class Definition
-----------------------------------------------------------
 This module defines the Member class, which represents an 
 individual registered in the budgeting system. Each member 
 stores basic identifying information including name, unique 
 ID, and date of birth (DOB). Simple update methods are 
 provided to modify individual attributes.

 Attributes:
     name (str): The member's full name.
     ID (str or int): A unique identifier for the member.
     DOB (str): Date of birth in 'YYYY-MM-DD' format.

 Methods:
     new_name(name): Update the member's name.
     new_DOB(DOB): Update the member's date of birth.
     new_ID(ID): Update the member's ID.
     get_age(): Returns the age of the member (approximate).
     __str__(): String representation used for display.

 Notes:
     - DOB should be stored as a string in 'YYYY-MM-DD' format.
     - get_age() safely handles invalid or missing DOB values.
===========================================================
"""

from datetime import datetime

class member:
    def __init__(self,name,ID,DOB):
        self.name=name
        self.DOB=DOB
        self.ID=ID
    def new_name(self,name):
        self.name=name
    def new_DOB(self,DOB):
        self.DOB=DOB
    def new_ID(self,ID):
        self.ID=ID
    def __str__(self):
        return f"{self.name} (ID: {self.ID}, Member)"