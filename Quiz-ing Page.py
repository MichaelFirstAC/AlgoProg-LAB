'''RAAAAAAAAAAAAHHHHHHHHH'''

class Binusmaya:
    def __init__(self):
        self.Lecturers = []
        self.Classes = []
        self.Schedules = []

    def add_lecturer(self):
        name = input("Enter lecturer name: ")
        subject = input("Enter lecturer subject: ")
        lecturerID = input("Enter lecturer ID: ")
        for lecturer in self.Lecturers:
            if lecturer['subject'] == subject:
                print("Lecturer for subject {} already exists.".format(subject))
                return
        lecturer_data = {'name': name, 'subject': subject, 'lecturerID': lecturerID}
        self.Lecturers.append(lecturer_data)
        print("Lecturer added: {}".format(lecturer_data))

    def remove_lecturer(self):
        lecturerID = input("Enter lecturer ID to remove: ")
        for lecturer in self.Lecturers:
            if lecturer['lecturerID'] == lecturerID:
                self.Lecturers.remove(lecturer)
                print("Lecturer with ID {} removed.".format(lecturerID))
                return
        print("Lecturer with ID {} not found.".format(lecturerID))

    def add_class(self):
        class_code = input("Enter class code: ")
        if class_code in self.Classes:
            print("Class code {} already exists.".format(class_code))
            return
        self.Classes.append(class_code)
        print("Class code {} added.".format(class_code))

    def remove_class(self):
        class_code = input("Enter class code to remove: ")
        if class_code in self.Classes:
            self.Classes.remove(class_code)
            print("Class code {} removed.".format(class_code))
            return
        print("Class code {} not found.".format(class_code))

    def add_schedule(self):
        class_code = input("Enter class code: ")
        time = input("Enter time: ")
        subject = input("Enter subject: ")
        for lecturer in self.Lecturers:
            if lecturer['subject'] == subject:
                lecturer_name = lecturer['name']
                schedule_tuple = (time, class_code, subject, lecturer_name)
                self.Schedules.append(schedule_tuple)
                print("Schedule added: {}".format(schedule_tuple))
                return
        print("No lecturer found for subject {}.".format(subject))

def main():
    binusmaya = Binusmaya()

    while True:
        print("\nOptions:")
        print("1. Add lecturer")
        print("2. Remove lecturer")
        print("3. Add class")
        print("4. Remove class")
        print("5. Add schedule")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            binusmaya.add_lecturer()
        elif choice == "2":
            binusmaya.remove_lecturer()
        elif choice == "3":
            binusmaya.add_class()
        elif choice == "4":
            binusmaya.remove_class()
        elif choice == "5":
            binusmaya.add_schedule()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()