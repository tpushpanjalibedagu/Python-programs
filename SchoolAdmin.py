import csv


def write_into_csv(info_list):
    with open('stu_info.csv', 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)

    if csv_file.tell() == 0:
        writer.writerow(["Name", "Age", "Contact", "Email"])

    writer.writerow(info_list)


if __name__ == '__main__':
    condition = True
    student_num = 1

    while condition:
        stu_info = input("Enter student information for student #{} in the following format (Name Age Contact Email): "
                         .format(student_num))

        stu_info_list = stu_info.split(' ')

        print("\nThe entered information is -\nName: {}\nAge: {}\nContact: {}\nEmail: {}"
              .format(stu_info_list[0], stu_info_list[1], stu_info_list[2], stu_info_list[3]))

        choice_check = input("Is the entered information correct? (yes/no): ")

        if choice_check == "yes":
            write_into_csv(stu_info_list)

            condition_check = input("Enter (yes/no) if you want to enter information for another student: ")
            if condition_check == "yes":
                condition = True
                student_num = student_num + 1
            elif condition_check == "no":
                condition = False
        elif choice_check == "no":
            print("\nPlease re-enter the values!")
