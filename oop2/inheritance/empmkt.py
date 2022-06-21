from employee import Employee

class EmpMKT(Employee):
    def __init__(self, id, name, salary) -> None:
        super().__init__(id, name, salary)
        self.location = 'Bangkok'
        self.commision = 30
        self.department = 'Marketing'

    def add_location(self,location):
        self.location = location

    def add_commision(self,commision):
        self.commision = commision

    def emp_detail(self):
        print("===== Employee Marketing Detail =====")
         #เรียกใช้เมธอท emp_detail ของคลาส Employee เพื่อแสดง id, name vvvvv
        super().emp_detail()
        print(f'Location : {self.location}')
        print(f'Commision: {self.commision} %')

    def mkt_salary(self):
        self._emp_salary()