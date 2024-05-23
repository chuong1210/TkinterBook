# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 15:02:05 2024

@author: Administrator
"""

import json
import random
import string
import datetime
from datetime import timedelta
#Thông tin phòng ban, nhân viên để khởi tạo random
department_names= ["Kế toán", "Nhân sự", "Marketing", "Kinh doanh", "Phát triển sản phẩm",
"Kỹ thuật", "Tài chính", "Quản lý chất lượng", "Hành chính" , "Dịch vụ khách hàng"]
common_surname = ["Nguyen", "Trần", "Lê", "Phạm", "Hoàng", "Huỳnh"]
name_lot_thong_dung = ["Vân", "Thi", "Hữu", "Hoàng", "Thông", "Minh", "Tân", "Ngọc",
"Tiến", "Gia"]
common_name=["Hải", "Hà", "Hưng", "Linh", "Minh", "Quan", "Thảo", "Trang", "Tuấn",
"Vy", "An", "Bình", "Cường", "Đức", "Giang", "Kiên", "Nam", "Phương", "Sơn", "Thành"]
def generate_random_departmentName():
   # return random.choice(department_name);
    random_departments = random.sample(department_names, 4)
    departments = [{"name": department} for department in random_departments]
    return departments
def generate_random_department():
    department_names = ["Kế toán", "Nhân sự", "Tiếp thị", "Kinh doanh", "Phát triển sản phẩm",
                        "Kỹ thuật", "Tài chính", "Quản lý chất lượng", "Dịch vụ khách hàng"]
    return random.choice(department_names)

def generate_random_commonSurname():
    return random.choice(common_surname);
def generate_random_nameLot():
    return random.choice(name_lot_thong_dung);
def generate_randow_commonName():
    return random.choice(common_name);
def generate_random_employee():
    common_surnames = ["Nguyen", "Trần", "Lê", "Phạm", "Hoàng", "Huỳnh"]
    common_name_lots = ["Vân", "Thi", "Hữu", "Hoàng", "Thông", "Minh", "Tân", "Ngọc", "Tiên", "Gia"]
    common_names = ["Hải", "Hà", "Hưng", "Linh", "Minh", "Quan", "Thảo", "Trang", "Tuấn",
                    "Vy", "An", "Bình", "Cường", "Đức", "Giang", "Kiên", "Nam", "Phương", "Sơn", "Thành"]

    full_name = f"{random.choice(common_surnames)} {random.choice(common_name_lots)} {random.choice(common_names)}"
    date_of_birth = generate_random_date()
    position = random.choice(["Quản lý", "Nhân viên", "Kế toán", "Lập trình viên"])
    department = generate_random_department()
    
    return Employee(full_name, date_of_birth, position, department)

def generate_random_data():
    departments = [Department(name) for name in ["Kế toán", "Nhân sự", "Tiếp thị", "Kinh doanh"]]
    employees = [generate_random_employee() for _ in range(12)]

    for employee in employees:
        for department in departments:
            if department.name == employee.department:
                if not hasattr(department, 'employees'):
                    department.employees = []
                department.employees.append(employee)

    return departments

#hàm khởi tạo mãng nhân viên ngẫu nhiên
def generate_employee():
    departments = generate_random_departmentName()
    employees = []

    for department_name in departments:
        for _ in range(3): 
            full_name = f"{random.choice(['Nguyen', 'Trần', 'Lê', 'Phạm', 'Hoàng', 'Huỳnh'])} {random.choice(['Vân', 'Thi', 'Hữu', 'Hoàng', 'Thông', 'Minh', 'Tân', 'Ngọc', 'Tiên', 'Gia'])} {random.choice(['Hải', 'Hà', 'Hưng', 'Linh', 'Minh', 'Quan', 'Thảo', 'Trang', 'Tuấn', 'Vy', 'An', 'Bình', 'Cường', 'Đức', 'Giang', 'Kiên', 'Nam', 'Phương', 'Sơn', 'Thành'])}"
            birth_date = generate_random_date()
            position = random.choice(["Quản lý", "Nhân viên", "Kế toán", "Lập trình viên"])
            employee = Employee(full_name, birth_date, position, department_name)
            employees.append(employee)

    return employees
#tạo ngày ngẫu nhiên từ 1980 tới 2004
def generate_random_date():
    start_date = datetime.datetime(1980, 1, 1)
    end_date = datetime.datetime(2004, 12, 31)
    random_days = random.randint(0, (end_date - start_date).days)
    random_date = start_date + timedelta(days=random_days)
    return random_date.strftime("%m/%d/%Y")
#menu để chọn ngày
def menu():
    print("\n===== MENU =====")
    print("1. Quản lý nhân viên")
    print("2. Quản lý phòng ban")
    print("3. Thoát")
# Sử dụng hàm nhap_ngay_thang để nhập ngày tháng
def nhap_ngay_thang():
    while True:
        ngay_thang = input("Nhập ngày tháng (dd/mm/yy): ")
        try:
            # Sử dụng strptime để chuyển đổi chuỗi nhập vào thành đối tượng datetime
            ngay_thang_datetime = datetime.strptime(ngay_thang, "%d/%m/%y")
            return ngay_thang_datetime
        except ValueError:
            print("Định dạng ngày tháng không đúng. Vui lòng nhập lại.")


class Employee:
    #khởi tạo đối tượng nhân viên
    def __init__(self, name, dateofbirth, position, department):
        self.name = name
        self.dateofbirth = dateofbirth
        self.position = position
        self.department = department

    #hàm để in thông tin của 1 nhân viên
    def to_dict(self):
        return {
            "name": self.name,
            "dateofbirth": self.dateofbirth,
            "position": self.position,
            "department": self.department
        }

class Department:
    #khởi tạo đối tượng phòng ban
    def __init__(self, name):
        self.name = name


    #hàm để in tên 1 phòng ban
    def to_dict(self):
        return {
            "name": self.name,
        }

#lớp quản lí danh sách phòng ban
class DepartmentManagement:
    def __init__(self, file_path, employee_management=None):
        self.file_path = file_path
        self.departments = self.load_departments()
        self.employee_management = employee_management
    # Load danh sách phòng ban từ file

    def load_departments(self):
        try:# dùng utf8 để đọc được tiếng Việt
            with open(self.file_path, 'r', encoding='utf-8') as file:
                department_data = json.load(file) #json.load để loadfile json
                departments = [Department(dep["name"]) for dep in department_data] #load name department từ đối tượng json
                return departments #trả về danh sách phòng ban
        except FileNotFoundError: #xử lí lỗi khi ko đọc đc file
            print("Không tìm thấy file dữ liệu phòng ban. Tạo danh sách mới.")
            department_data=generate_random_departmentName()
            departments = [Department(dep["name"]) for dep in department_data]
            return departments #tạo 4 trong 10 phòng ban ngẫu nhiên nếu ko tìm được file
    def save_departments(self):     # Lưu danh sách phòng ban vào file
        with open(self.file_path, 'w') as file: 
            json.dump([dep.to_dict() for dep in self.departments], file, indent=4) #json.dump để lưu 1 đối tượng python vào file json 
            #Trong lệnh json.dump, tham số indent được sử dụng để xác định số lượng dấu cách được thêm vào trước mỗi dòng trong tệp JSON đầu ra. Nó giúp làm cho tệp JSON trở nên dễ đọc hơn cho con người bằng cách tạo ra một cấu trúc có cấp độ và thụt vào các đối tượng con.

#thêm phòng ban mới
    def add_department(self, name):
        new_department = Department(name)
        self.departments.append(new_department)
        self.save_departments()
#xóa phòng ban từ tên nhập từ bàn phím
    def remove_department(self, name):
        self.departments = [dep for dep in self.departments if dep.name != name]
        self.save_departments()
#cập nhật phòng ban từ tên nhập từ bàn phím
    def update_department(self, old_name, new_name):
        updated = False
        for department in self.departments:
            if department.name == old_name:
                department.name = new_name
                self.save_departments()
                updated = True
                break
#cập nhật tên nếu cập nhật thành công return true
        if updated:
            for employee in self.employee_management.employees:
                if employee.department == old_name:
                    employee.department = new_name
            self.employee_management.save_employees()
            return True
        else:
            return False
        #in tât cả phòng ban ra màn hình console
    def print_departments(self):
        if not self.departments:
            print("Danh sách phòng ban trống.")
        else:
            print("Danh sách phòng ban:")
            for department in self.departments:
                print(f"- {department.name}")

    #tính toán số lượng nhân viên trong mỗi phòng ban
    def count_employees_by_department(self):
        department_employee_count = {department.name: 0 for department in self.departments}
        for employee in self.employee_management.employees:
            department_employee_count[employee.department] = department_employee_count.get(employee.department, 0) + 1

        print("Thống kê số lượng nhân viên ở từng phòng ban:")
        for department, count in department_employee_count.items():
            print(f"- {department}: {count} nhân viên")

#in thông tin từng nhân viên từ phòng ban nhập từ bàn phím
    def print_employees_by_department(self, department_name):
        print(f"Danh sách nhân viên trong phòng ban '{department_name}':")
        department_employees = [employee for employee in self.employee_management.employees if employee.department == department_name]
        if department_employees:
            for i, employee in enumerate(department_employees, start=1):
                print(f"{i}. Tên: {employee.name}, Ngày sinh: {employee.dateofbirth}, Chức vụ: {employee.position}")
        else:
            print("Không có nhân viên nào trong phòng ban này.")

#lớp quản lí danh sách nhân viên
class EmployeeManagment:

    def __init__(self, file_path,department_management):
        self.file_path = file_path
        self.employees = self.load_employees()
        self.department_management = department_management # đây là sự thay đổi

    def check_department_list(self):
        if not department_management.departments:
            print("Danh sách phòng ban trống. Không thể thêm nhân viên.")
            return False
        return True        
#load employy từ file json
    def load_employees(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                employee_data = json.load(file)
                #print(employee_data)
                employees = [Employee(prod["name"], prod["dateofbirth"], prod["position"], prod["department"]) for prod in  employee_data]
                return employees
        except FileNotFoundError:
            print("Không tìm thấy file dữ liệu. Tạo danh sách mới.")
            return generate_employee()
       
#lưu employy vào file json
    def save_employees(self):
        with open(self.file_path, 'w') as file:
            json.dump([prod.to_dict() for prod in self.employees], file, indent=4)


#thêm employy vào file json
    def add_employee(self, name, date_of_birth, position, department):
        # Kiểm tra nếu danh sách phòng ban trống
        if not self.department_management.departments:
            print("Danh sách phòng ban trống. Không thể thêm nhân viên.")
            return

        # Kiểm tra xem phòng ban được chọn có trong danh sách phòng ban hay không
        department_names = [dep.name for dep in self.department_management.departments]
        if department not in department_names:
            print("Phòng ban không tồn tại. Vui lòng chọn từ danh sách phòng ban.")
            print("Thêm nhân viên không thành công.")
            return

        new_employee = Employee(name, date_of_birth, position, department)
        self.employees.append(new_employee)
        self.save_employees()
        #xóa employee từ file json
    def remove_employee(self, name):
        self.employees = [prod for prod in self.employees if prod.name != name]
        self.save_employees()

#cập nhật thông tin employy từ bàn phím
    def update_employee(self, name, new_name=None, new_dateofbirth=None, new_position=None, new_department=None):
        if not self.check_department_list():
            return False
        for employee in self.employees:
            if employee.name == name:
                if new_name:
                    employee.name = new_name
                if new_dateofbirth:
                    employee.dateofbirth =new_dateofbirth
                if new_position:
                    employee.position = new_position
                if new_department:
                    employee.department = new_department
                self.save_employyee()
                return True
        return False
    #In thông tin tất cả nhân viên
    def print_employees(self, department=None):
        for i, employee in enumerate(self.employees):
            if department is None or employee.department == department:
                print(f"{i+1}. {employee.name}, {employee.dateofbirth}, {employee.position}, {employee.department}.")

        if not self.employees:
            print("Danh sách nhan vien trống.")
        else:
            print("Danh sách nhan vien:")
            for employee in self.employees:
                print(f"-Tên: {employee.name} | ngày sinh: {employee.dateofbirth} | vị trí: {employee.position} | phong ban  {employee.department}")
    def search_employee_by_name(self, name): #tìm kiếm thông tin nhân viên theo tên
        result = []
        for employee in self.employees:
            if name.lower() in employee.name.lower():
                result.append(employee)
        if result:
            print("Kết quả tìm kiếm:")
            for employee in result:
                print(f"- Tên: {employee.name}, Ngày sinh: {employee.dateofbirth}, Chức vụ: {employee.position}, Phòng ban: {employee.department}")
        else:
            print("Không tìm thấy nhân viên nào phù hợp.")
            #sắp xếp thông tin nhân viên theo tên
    def sort_employees_by_name(self):
        sorted_employees = sorted(self.employees, key=lambda x: x.name.lower())
        print("Danh sách nhân viên đã được sắp xếp theo tên:")
        for employee in sorted_employees:
            print(f"- Tên: {employee.name}, Ngày sinh: {employee.dateofbirth}, Chức vụ: {employee.position}, Phòng ban: {employee.department}")
            #sắp xếp thông tin nhân viên theo ngày

    def sort_employees_by_dob(self):
        self.employees = sorted(self.employees, key=lambda x: datetime.datetime.strptime(x.dateofbirth, "%m/%d/%Y"))
        print("Danh sách nhân viên đã được sắp xếp theo ngày sinh:")
        for employee in self.employees:
            print(f"- Tên: {employee.name}, Ngày sinh: {employee.dateofbirth}, Chức vụ: {employee.position}, Phòng ban: {employee.department}")

#Main
if __name__ == "__main__":
    file_employee_path = "employee.json"
    file_department_path = "Department.json"

    employee_management = EmployeeManagment(file_employee_path, None) # Chú ý dòng này
    # Sau đó tạo quản lý phòng ban và truyền employee_management vào
    department_management = DepartmentManagement(file_department_path, employee_management)
    
    # Cấu hình lại phụ thuộc cho employee_management
    employee_management.department_management = department_management

    while True:
        menu()
        choice = input("Chọn chức năng (1-3): ")

        if choice == '1':
            while True:
                #Quản lí nhân viên
                print("\n===== QUẢN LÝ NHÂN VIÊN =====")
                print("1. Xem danh sách nhân viên")
                print("2. Thêm nhân viên mới")
                print("3. Cập nhật thông tin nhân viên")
                print("4. Xóa nhân viên")
                print("5. Tìm thông tin nhân viên theo tên")
                print("6. Sắp xếp theo tên")
                print("7. Sắp xếp theo ngày tháng")
                print("8. Quay lại")
                employee_choice = input("Chọn chức năng (1-8): ")

                if employee_choice == '1':
                    employee_management.print_employees()
                elif employee_choice == '2':
                    name = input("Nhập tên nhân viên: ")
                    date_of_birth = input("Nhập ngày sinh (dd/mm/yyyy): ")
                    position = input("Nhập chức vụ: ")
                    print("Danh sách phòng ban:")
                    department_management.print_departments()
                    department = input("Chọn phòng ban: ")
                    employee_management.add_employee(name, date_of_birth, position, department)
                    print("Thêm nhân viên thành công.")
                elif employee_choice == '3':
                    name = input("Nhập tên nhân viên cần cập nhật: ")
                    print("Nhập thông tin mới (bỏ trống để giữ nguyên):")
                    new_name = input("Tên mới: ")
                    new_date_of_birth = input("Ngày sinh mới (dd/mm/yyyy): ")
                    new_position = input("Chức vụ mới: ")
                    print("Danh sách phòng ban:")
                    department_management.print_departments()
                    new_department = input("Phòng ban mới: ")
                    if employee_management.update_employee(name, new_name, new_date_of_birth, new_position, new_department):
                        print("Cập nhật thông tin nhân viên thành công.")
                    else:
                        print("Không tìm thấy nhân viên.")
                elif employee_choice == '4':
                    name = input("Nhập tên nhân viên muốn xóa: ")
                    employee_names = [dep.name for dep in employee_management.employees]

                    if name not in employee_names:
                        print("Không có tên nhân viên trong danh sách")
                        break
                    employee_management.remove_employee(name)
                    print("Xóa nhân viên thành công.")
                elif employee_choice == '5':
                     name = input("Nhập tên nhân viên muốn tìm: ")
                     employee_management.search_employee_by_name(name)
                elif employee_choice == '6':

                    employee_management.sort_employees_by_name()
                elif employee_choice == '7':
                    employee_management.sort_employees_by_dob()

                elif employee_choice == '8':
                    break
                else:
                    print("Lựa chọn không hợp lệ.")
        elif choice == '2':
            #Quản lí phòng ban
            while True:
                print("\n===== QUẢN LÝ PHÒNG BAN =====")
                print("1. Xem danh sách phòng ban")
                print("2. Thêm phòng ban mới")
                print("3. Cập nhật tên phòng ban")
                print("4. Xóa phòng ban")
                print("5. Thống kê số lượng danh sách nhân viên theo từng phòng ban")
                print("6. Hiển thị danh sách nhân viên theo từng phòng ban")
                print("7. Quay lại")
                department_choice = input("Chọn chức năng (1-7): ")

                if department_choice == '1':
                    department_management.print_departments()
                elif department_choice == '2':
                    name = input("Nhập tên phòng ban: ")
                    department_management.add_department(name)
                    print("Thêm phòng ban thành công.")
                elif department_choice == '3':
                    old_name = input("Nhập tên phòng ban cần cập nhật: ")
                    new_name = input("Nhập tên mới: ")
                    if department_management.update_department(old_name, new_name):
                        print("Cập nhật tên phòng ban thành công.")
                    else:
                        print("Không tìm thấy phòng ban.")
                elif department_choice == '4':
                    name = input("Nhập tên phòng ban muốn xóa: ")
                    department_management.remove_department(name)
                    print("Xóa phòng ban thành công.")
                elif department_choice == '5':
                    department_management.count_employees_by_department()
                elif department_choice == '6':
                    name = input("Nhập tên phòng ban muốn hiển thị: ")
                    department_management.print_employees_by_department(name)
                elif department_choice == '7':
                    break
                else:
                    print("Lựa chọn không hợp lệ.")
        elif choice == '3':
            #Thoát
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ.")