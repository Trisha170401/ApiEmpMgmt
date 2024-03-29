import json
from user import employee_page
from util.config import config_dict

# file paths
employee_file_path = config_dict.get('file_paths').get('employee')
login_file_path = config_dict.get('file_paths').get('login')

# print statements
printer = config_dict.get("print-stmts")
generic_statements = printer.get("generic")


class Admin:

    def __init__(self, username):
        self.username = username

    @staticmethod
    def access_check(user_name):

        with open(login_file_path, 'r', encoding="utf8") as login_db:
            login_data = json.load(login_db)
        for login in login_data:
            if user_name == login.get("username"):
                if login.get("access_type") == 0:
                    print("You do not have admin access!!")
                    return False
                elif login.get("access_type") == 1:
                    return True

    def display_admin_menu(self):

        while True:

            index = 1
            statements = printer.get('admin-menu')
            print(str(generic_statements.get("welcome")).format("Admin"))

            for statement in statements:
                print(f"{index}. {statement}")
                index = index + 1
            print(f"{index}. {generic_statements.get('exit')}")
            choice = input(f"{generic_statements.get('choice')}")

            match choice:
                case "1":
                    if self.access_check(self.username):
                        self.display_all_emp_details()
                    else:
                        break
                case "2":
                    if self.access_check(self.username):
                        self.add_employee()
                    else:
                        break
                case "3":
                    if self.access_check(self.username):
                        self.remove_employee()
                    else:
                        break
                case "4":
                    if self.access_check(self.username):
                        self.change_access()
                    else:
                        break
                case "5":
                    employee_caller = employee_page.Employee(self.username)
                    employee_caller.employee_menu_display()
                case "6":
                    print(generic_statements.get('thank_you_message'))
                    break
                case _:
                    print(str(generic_statements.get('incorrect_input')).format("choice"))

    def display_all_emp_details(self):
        with open(employee_file_path, 'r', encoding="utf8") as emp_db:
            emp_data = json.load(emp_db)
        return emp_data

    def add_employee(self, new_employee):
        with open(employee_file_path, 'r+', encoding="utf8") as emp_db:
            emp_data = json.load(emp_db)
            emp_list = emp_data.get("employees")
            emp_list.append(new_employee)
            emp_db.seek(0)
            json.dump(emp_data, emp_db, indent=4)


    def remove_employee(self, del_uname):
        # delete employee record.
        new_emp_data = []

        with open(employee_file_path, 'r', encoding="utf8") as emp_db:
            emp_data = json.load(emp_db)

        curr_emp_list = emp_data.get('employees')
        found = False

        for emp in curr_emp_list:
            if emp.get('username').__eq__(del_uname):
                found = True
            else:
                new_emp_data.append(emp)
        with open(employee_file_path, 'r', encoding="utf8") as emp_db:
            emp_data = json.load(emp_db)

        if not found:
            return {"message" : "employee not found"}
        else:
            dict_new = {'employees': new_emp_data}
            with open(employee_file_path, 'w', encoding="utf8") as emp_db:
                json.dump(dict_new, emp_db, indent=4)

        # delete login information
        with open(login_file_path, 'r', encoding="utf8") as login_db:
            curr_login_list = json.load(login_db)

        new_login_data = []
        found = False

        for login in curr_login_list:
            if login.get('username').__eq__(del_uname):
                found = True
            else:
                new_login_data.append(login)

        with open(login_file_path, 'w', encoding="utf8") as login_db:
            json.dump(new_login_data, login_db, indent=4)

        if found:
            return {"message": "Record deleted"}
        else:
            return {"message": "Record not found"}
            


    def change_access(self):

        while True:
            update_id = input(generic_statements.get.format("Username of desired User"))
            confirm = input(generic_statements.get("confirm"))
            if confirm.lower()[0] == 'n':
                return
            updated_login_data = []

            with open(login_file_path, 'r', encoding="utf8") as login_db:
                login_data = json.load(login_db)

            curr_login_list = login_data
            found = False

            for emp in curr_login_list:
                if emp.get('username').__eq__(update_id):
                    found = True
                    emp['access_type'] = 1
                updated_login_data.append(emp)

            if not found:
                print(f"Employee {generic_statements.get('404')}")
            else:
                with open(login_file_path, 'w', encoding="utf8") as emp_db:
                    json.dump(updated_login_data, emp_db, indent=4)
                print(f"Employee {generic_statements.get('update')}")
                break
