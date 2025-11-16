from budget_system.budgetfund import *
from budget_system.member import *

class BudgetSystem:
    def __init__(self, members, current_fund, address, household_name=''): #please enter member as a list of dependant and guardian
        self.fund=budgetfund(current_fund,household_name)
        self.address=address
        self.household_name=household_name
        self.members=members
        #self.incomes=income
        #self.expenses=espenses
        
    def add_member(self,new_member):
        if any(m.ID == new_member.ID for m in self.members):
            print(f"Warning: member with ID {new_member.ID} already exists.")
        self.members.append(new_member)
        
    def remove_member(self, ID):
        for person in self.members:
            if person.ID == ID:
                self.members.remove(person)
                return True
        return False
        
    def list_member(self):
        if not self.members:
            print("No members in the system.")
            return
        for person in self.members:
            print(person)
            
    def get_member(self, ID):
        for person in self.members:
            if person.ID == ID:
                return person
        return None
        
    def __str__(self):
        return (f"Budget System for {self.household_name}\n"
                f"Address: {self.address}\n"
                f"Members: {len(self.members)}\n"
                f"Current Fund: {self.fund.get()}")
        
    def print_fund_log(self):
        return print_log(self.fund)

    def search_fund_log(self, keyword=''):
        return search_log(self.fund, keyword)

    def filter_fund_status(self, status=True):
        return filter_status(self.fund, status)
