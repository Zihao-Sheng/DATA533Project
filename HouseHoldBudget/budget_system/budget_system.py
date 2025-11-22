from .budgetfund import budgetfund, fund_utils
from .member.member_type import guardian, dependant
from IPython.display import clear_output
import time

def clear_screen():
    clear_output(wait=False)

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
            return False
        self.members.append(new_member)
        return True

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
                return person.
        return None
        
    def __str__(self):
        return (f"Budget System for {self.household_name}\n"
                f"Address: {self.address}\n"
                f"Members: {len(self.members)}\n"
                f"Current Fund: {self.fund.get()}")
        
    def print_fund_log(self,start,end):
        return fund_utils.print_log(self.fund,start,end)

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

    def summarize_month(self, start_month,end_month=''):
        if end_month=='':
            return self.fund.summarize_month(start_month,start_month)
        return self.fund.summarize_month(start_month,end_month)

    def get_df(self,start=None,end=None):
        return self.fund.get_df(start,end)

def initialization(system=None):
    if system==None:
        print('Welcome to the Family Budget System')
        print('Please follow the instruction to Initialize the system')
        house_hold_name=input('Please input your household name:')
        balance=float(input('Please input your available balance:'))
        ini_address=input('Please input your address:')
        system = BudgetSystem(
            members=[],
            current_fund=balance,
            address=ini_address,
            household_name=house_hold_name
        )
        input('First time setup complete, please initialize again with the given system:')
    else:
        main_menu(system)
    return system

def main_menu(system):
    while True:
        clear_screen()
        time.sleep(0.05)
        print("===== Family Budget System =====")
        print(system)
        print("--------------------------------")
        print("1. Member editor")
        print("2. Fund / Expense editor")
        print("3. Transaction log")
        print("4. Property Manager")
        print("5. Quit")
        print("--------------------------------")
        choice = input("Choose an option (1-5): ").strip()
        if choice == "1":
            member_editor(system)
        elif choice == "2":
            fund_editor(system)
        elif choice == "3":
            log_viewer(system)
        elif choice == "4":
            property_manager(system)      # ← 你缺少这个入口，我补上了
        elif choice == "5":
            clear_screen()
            print("Thank you for using the system. Goodbye!")
            break
        else:
            print("Invalid choice.")
            input("Press Enter to try again...")

def member_editor(system):
    while True:
        clear_screen()
        time.sleep(0.05)
        print("=== Member Editor ===")
        print(system)
        print("------------------------------")

        print("Current members:")
        if len(system.members) == 0:
            print("  (No members yet)")
        else:
            for m in system.members:
                print("  " + str(m))
        print("\nOptions:")
        print("1. List members")
        print("2. Add member")
        print("3. Delete member")
        print("4. Find member by ID")
        print("5. Back to main menu")
        print("------------------------------")
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            print("=== Member List ===")
            time.sleep(0.05)
            system.list_member()
            input("\nPress Enter to return...")

        elif choice == "2":
            print("=== Add Member ===")
            time.sleep(0.05)
            name = input("Name: ")
            dob = input("Date of birth (YYYY-MM-DD): ")
            ID = input("Unique ID: ")
            mtype = input("Type (guardian/dependant): ")

            if mtype.lower() == "guardian":
                job = input('Job Title:')
                income = float(input('income:'))
                new_member = guardian(name,ID,dob,income,job)
            else:
                new_member = dependant(name, ID, dob)

            system.add_member(new_member)

            print("\nMember successfully added.")
            input("Press Enter to return...")

        elif choice == "3":
            print("=== Delete Member ===")
            time.sleep(0.05)
            ID = input("Enter ID to delete: ").strip()

            if system.remove_member(ID):
                print(f"Member with ID {ID} removed.")
            else:
                print(f"No member found with ID {ID}.")
            input("\nPress Enter to return...")

        elif choice == "4":
            print("=== Find Member by ID ===")
            time.sleep(0.05)
            ID = input("Enter ID: ").strip()

            person = system.get_member(ID)
            if person:
                print("\nFound member:")
                print(person)
            else:
                print("\nNo member found with that ID.")

            input("\nPress Enter to return...")

        elif choice == "5":
            break

        else:
            print("Invalid choice.")
            input("Press Enter to try again...")

def fund_editor(system):
     while True:
        clear_screen()
        time.sleep(0.05)
        print("=== Fund Editor ===")
        print(system)
        print("------------------------------")
        print("\nOptions:")
        print("1. Add Fund")
        print("2. Sub Fund")
        print("3. Back to main menu")
        print("------------------------------")
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            print("=== Add Fund ===")
            time.sleep(0.05)
            amount=float(input('Please enter amount:'))
            text=input('Please enter description:')
            date=input("Please enter date (YYYY-MM-DD): ")
            system.add_fund(amount,text,date)
            input("\nPress Enter to return...")

        elif choice == "2":
            print("=== Sub Fund ===")
            time.sleep(0.05)
            amount=float(input('Please enter amount:'))
            text=input('Please enter description:')
            date=input("Please enter date (YYYY-MM-DD): ")
            system.sub_fund(amount,text,date)
            input("\nPress Enter to return...")

        elif choice == "3":
            break

        else:
            print("Invalid choice.")
            input("Press Enter to try again...")

def log_viewer(system):
    while True:
        clear_screen()
        time.sleep(0.05)
        print("=== Fund Log Viewer ===")
        print(f"Household: {system.household_name}")
        print("------------------------------")
        print("1. Print full fund log")
        print("2. Search fund log by keyword")
        print("3. Filter fund log by status")
        print("4. Monthly / period summary")
        print("5. Back to main menu")
        print("------------------------------")
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            print("=== Print Fund Log ===")
            time.sleep(0.05)
            print("You can enter a date range to filter the log.")
            print("Leave blank to use full range.")
            start = input("Start date (YYYY-MM-DD, or blank for no limit): ").strip()
            end   = input("End date   (YYYY-MM-DD, or blank for no limit): ").strip()

            start = start or None
            end   = end or None

            system.print_fund_log(start, end)
            input("\nPress Enter to return...")

        elif choice == "2":
            print("=== Search Fund Log ===")
            time.sleep(0.05)
            keyword = input("Enter keyword to search in description: ")
            system.search_fund_log(keyword)
            input("\nPress Enter to return...")

        elif choice == "3":
            print("=== Filter Fund Log by Status ===")
            time.sleep(0.05)
            print("Do you want to see:")
            print("1. Succeeded records")
            print("2. Failed records")
            status_choice = input("Choose (1/2): ").strip()
            if status_choice == "1":
                flag = True   # succeeded
            elif status_choice == "2":
                flag = False  # failed
            else:
                print("Invalid choice.")
                input("Press Enter to return...")
                continue
            system.filter_fund_status(flag)
            input("\nPress Enter to return...")

        elif choice == "4":
            print("=== Fund Summary ===")
            time.sleep(0.05)
            print("Please enter the summary period.")
            print("For monthly summary, you can use year-month format like 2025-05.")
            start = input("Start (e.g., 2025-05 or 2025-05-01): ").strip()
            end   = input("End   (e.g., 2025-05 or 2025-05-31): ").strip()
            system.summarize_month(start, end)
            input("\nPress Enter to return...")

        elif choice == "5":
            break

        else:
            print("Invalid choice.")
            input("Press Enter to try again...")