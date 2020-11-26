
class Employee:

    def __init__(self,name,emp_id,email_id):
        self.__name = name
        self.__emp_id = emp_id
        self.__email_id = email_id

    def get_name(self):
        return self.__name

    def get_emp_id(self):
        return self.__emp_id

    def get_email_id(self):
        return self.__email_id

class OrgDir:

    def __init__(self,emp_list):
        self.__emp_list = emp_list

    def lookup(self,key_name):
        result_list = []
        for emp in self.__emp_list:
            if(key_name in emp.get_name()):
                result_list.append(emp)

        self.display(result_list)
        return result_list

    def display(self,result_list):
        for emp in result_list:
            print("Name :",emp.get_name())
            print("Employee ID :",emp.get_emp_id())
            print("Email ID :",emp.get_email_id())                



emp1 = Employee("Rupayan",1083187,"rupayan.roy@infosys.com")
emp2 = Employee("lakshya",1083186,"lakhi@infosys.com")
emp3 = Employee("Siddharth",1083189,"sid@infosys.com")

emp_list = [emp1,emp2,emp3]
org_dir = OrgDir(emp_list)
org_dir.lookup("Rupayan")