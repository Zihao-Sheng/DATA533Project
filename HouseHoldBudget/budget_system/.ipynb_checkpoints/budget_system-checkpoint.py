from .budgetfund import budgetfund, fund_utils
from .member import member_type

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
        return fund_utils.print_log(self.fund)

    def search_fund_log(self, keyword=''):
        return fund_utils.search_log(self.fund, keyword)

    def filter_fund_status(self, status=True):
        return fund_utils.filter_status(self.fund, status)

    def add_fund(self, amount, description='', date=None):
        return self.fund.add(amount, description, date)

    def sub_fund(self, amount, description='', date=None):
        return self.fund.sub(amount, description, date)
        
    def visualize(self,year_month):
        return self.fund.summarize_month(year_month)

    def validate_fund(self, amount=0):
        return self.fund.validate(amount)

    def visualize(self,year_month):
        return self.fund.summarize_month(year_month)

    def validate_fund(self, amount=0):
        return self.fund.validate(amount)

    def visualize(self,year_month):
        return self.fund.summarize_month(year_month)

    def validate_fund(self, amount=0):
        return self.fund.validate(amount)

    def summarize_month(self, month):
        return self.fund.summarize_month(month)

    def get_df(self,start=None,end=None):
        return self.fund.get_df(start,end)
        
