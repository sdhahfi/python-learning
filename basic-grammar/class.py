"""class student:
    def __init__(self, name, number, math, Chinese, English):
        self.name = name
        self.number = number
        self.math = math
        self.Chinese = Chinese
        self.English = English
    def printf(self):
        print(self.name, self.number, self.math, self.Chinese)

p1=student("张三", 1, 90, 80, 70)
p1.printf()"""
class staff:
    def __init__(self, name, id, attribute):
        self.name = name
        self.id = id
        self.attribute = attribute
    def print_info(self):
        print(f"员工姓名:{self.name}", f"员工ID:{self.id}", f"员工属性:{self.attribute}")
class  full_time_staff(staff):
    def __init__(self, name, id, attribute, monthly_salary):
        super().__init__(name, id, attribute)
        self.monthly_salary = monthly_salary
    def calculate_salary(self):
        return self.monthly_salary
class  part_time_staff(staff):
    def __init__(self, name, id, attribute, daily_salary, working_days):
        super().__init__(name, id, attribute)
        self.daily_salary = daily_salary
        self.working_days = working_days
    def calculate_salary(self):
        return self.daily_salary * self.working_days
zhangsan = full_time_staff("张三", 1, "全职", 5000)
lisi = part_time_staff("李四", 2, "兼职", 200, 20)
zhangsan.print_info()
lisi.print_info()
print(f"张三的工资为:{zhangsan.calculate_salary()}")
print(f"李四的工资为:{lisi.calculate_salary()}")