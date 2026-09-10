#学生成绩管理程序
#要求：
# 用户输入学生姓名和成绩；
# 用dict保存；
# 能够：
# 1. 添加成绩
# 2. 删除学生
# 3. 查询学生
# 4. 修改成绩
# 5. 计算平均分
# 6. 找最高分
# 7. 保存到文件
# 8. 从文件读取
# 0. 退出
#并尽量拆成函数
class student:#学生
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def write_score(self):
        students_scores[self.name] = self.score
        print(f"写入成功,{self.name}的成绩是{self.score}")
    def delete_student(self):
        if self.name in students_scores:
            del students_scores[self.name]
            print(f"{self.name}已删除")
        else:
            print(f"{self.name}不存在")
    def check_student(self):
        if students_scores.get(self.name):
            print(f"{self.name}的成绩是{students_scores[self.name]}")
        else:
            print(f"{self.name}不存在")
    def edit_score(self, new_score):
        if self.name in students_scores:
            students_scores[self.name] = new_score
def average_score():
     if students_scores:
         avg = sum(students_scores.values()) / len(students_scores)
         print(f"平均分是{avg}")
def highest_score():
     if students_scores:
         max_score = max(students_scores.values())
         print(f"最高分是{max_score}")
def save_to_file():
    with open("students_scores.txt", "w", encoding="utf-8") as f:
        for name, score in students_scores.items():
            f.write(f"{name},{score}\n")
    print("保存成功")
def load_from_file():
    global students_scores
    students_scores = {}
    try:
        with open("students_scores.txt", "r", encoding="utf-8") as f:
            for line in f:
                name, score = line.strip().split(",")
                students_scores[name] = float(score)
                print("读取成功")
    except FileNotFoundError:
        print("文件不存在")
        pass
def exit_program():
    print("退出程序")
    exit()
def show_menu():
    print("学生成绩管理程序")
    print("1. 添加成绩")
    print("2. 删除学生")
    print("3. 查询学生")
    print("4. 修改成绩")
    print("5. 计算平均分")
    print("6. 找最高分")
    print("7. 保存到文件")
    print("8. 从文件读取")
    print("0. 退出")
    print("="* 30)

students_scores = {}  # 用字典保存学生成绩
def main():
    while True:
        show_menu()
        choice = input("请输入操作编号:")
        if choice == "1":
            name = input("请输入学生姓名:")
            score = float(input("请输入学生成绩:"))
            student(name, score).write_score()
        elif choice == "2":
            name = input("请输入要删除的学生姓名:")
            student(name, 0).delete_student()
        elif choice == "3":
            name = input("请输入要查询的学生姓名:")
            student(name, 0).check_student()
        elif choice == "4":
            name = input("请输入要修改成绩的学生姓名:")
            new_score = float(input("请输入新的成绩:"))
            student(name, 0).edit_score(new_score)
        elif choice == "5":
            average_score()
        elif choice == "6":
            highest_score()
        elif choice == "7":
            save_to_file()
        elif choice == "8":
            load_from_file()
        elif choice == "0":
            exit_program()
        else:
            print("输入有误，请重新输入")
if __name__ == "__main__":
    main()

