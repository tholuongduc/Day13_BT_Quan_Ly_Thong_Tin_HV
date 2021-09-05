student_list = '''001,Huy Hoa,Nam,Da Nang,50,50
002,The Anh,Nam,Vung Tau,60,90
003,Duy Luan,Nam,Vung Tau,80,70'''


def add_student(student_list):
    print("Hay nhap thong tin hoc vien!")
    id = input("Nhap ma so:")
    full_name = input("Nhap ho va ten:")
    gender = input("Nhap gioi tinh:")
    province = input("Nhap vao tinh/tp:")
    theory = input("Nhap vao diem ly thuyet:")
    practice = input("Nhap va diem thuc hanh:")

    student_list += '\n' + f"{id},{full_name},{gender},{province},{theory},{practice}"
    return student_list

def edit_options(option_number):
    if option_number == 1:
        full_name = input("Họ tên:")
        return full_name
    elif option_number == 2:
        gender = input("Giới tính:")
        return gender
    elif option_number == 3:
        province = input("Tỉnh/thành phố:")
        return province
    elif option_number == 4:
        theory = input("Điểm thi lý thuyết:")
        return theory
    elif option_number == 5:
        practice = input("Điểm thi thực hành:")
        return practice


def edit_student(student_list):
    edit_id = input("Hay nhap ma so cua hoc vien can sua doi thong tin:")
    print('''Hay chon thong tin can sua doi:
        1. Họ tên
        2. Giới tính
        3. Tỉnh/thành phố
        4. Điểm thi lý thuyết
        5. Điểm thi thực hành
          ''')
    option_number = int(input("Hay nhap số thứ tự tương ứng (1 đến 5):"))
    lst = student_list.split("\n")
    edit_student_list = ""
    for std in lst:
        if std == "":
            continue
        info = std.split(",")
        id = info[0]
        if id == edit_id:
            info[option_number] = edit_options(option_number)
        full_name = info[1]
        gender = info[2]
        province = info[3]
        theory = info[4]
        practice = info[5]
        edit_student_list += '\n' + f"{id},{full_name},{gender},{province},{theory},{practice}"
    return edit_student_list

def show_header():
    print(f"{'Mã số':<10}{'họ tên':^20}{'giới tính':^10}{'tỉnh/thành phố':<20}{'điểm thi lý thuyết':>20}{'điểm thi thực hành':>20}")

def show_students(condition):
    show_header()
    lst = student_list.split("\n")
    for std in lst:
        if std == "":
            continue
        info = std.split(",")
        id = info[0]
        full_name = info[1]
        gender = info[2]
        province = info[3]
        theory = info[4]
        practice = info[5]
        is_valid = condition(theory, practice)
        if is_valid:
            print(f"{id:<10}{full_name:^20}{gender:^10}{province:<20}{theory:>20}{practice:>20}")

def get_all_condition(theory, practice):
    return True
def get_passed_students(theory, practice):
    return (int(theory) + int(practice)) // 2 >= 75
def get_failed_students(theory, practice):
    return (int(theory) + int(practice)) // 2 < 75

def show_students_list():
    show_students(get_all_condition)

def show_passed_students():
    show_students(get_passed_students)

def show_failed_students():
    show_students(get_failed_students)

def remove_student(student_list):
    remove_id = input("Hay nhap ma so cua hoc vien muon xoa khoi bo nho:")
    lst = student_list.split("\n")
    new_student_list = ""
    for std in lst:
        if std == "":
            continue
        info = std.split(",")
        id = info[0]
        full_name = info[1]
        gender = info[2]
        province = info[3]
        theory = info[4]
        practice = info[5]
        if id != remove_id:
            new_student_list += '\n' + f"{id},{full_name},{gender},{province},{theory},{practice}"
    return new_student_list


def show_menu():
    print('''Hay chon tinh nang muon thuc hien theo danh sach duoi day:
        1) Them thong tin hoc vien vao bo nho
        2) Cap nhat thong tin hoc vien
        3) Hien thi danh sach tat ca hoc vien
        4) Hien thi danh sach hoc vien thi do ( Diem trung binh >=75)
        5) Hien thi danh sach hoc vien thi truot ( Diem trung binh < 75)
        6) Xoa thong tin hoc vien
        7) Thoat chuong trinh
          ''')

def get_choice():
    return input("Lua chon cua ban: ")

while True:
    show_menu()
    user_choice = get_choice()
    print("Ban da chon " + user_choice)

    if user_choice == "7":
        break
    elif user_choice == "1":
        student_list = add_student(student_list)
    elif user_choice == "2":
        student_list = edit_student(student_list)
    elif user_choice == "3":
        show_students_list()
    elif user_choice == "4":
        show_passed_students()
    elif user_choice == "5":
        show_failed_students()
    elif user_choice == "6":
        student_list = remove_student(student_list)

