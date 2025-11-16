from .member import member


class dependant(member):
    def __init__(self,name,ID,DOB):
        super().__init__(name,ID,DOB)
        self.type='dependant'
    def __str__(self):
        return f"{self.name} (ID: {self.ID}, Dependant)"


class guardian(member):
    def __init__(self,name,ID,DOB,income,job_title=''):
        super().__init__(name,ID,DOB)
        self.type='guardian'
        self.income=income
        self.job_title=job_title
    def new_job(self,job):
        self.job_title=job
    def new_income(self,income):
        self.income=income
    def get_income(self):
        return self.income
    def __str__(self):
        return f"{self.name} (ID: {self.ID}, Guardian, Income: {self.income}, Job: {self.job_title})"