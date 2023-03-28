class Student:
    def __init__(self, studNumber,firstName, lastName, birthDate, sex,country):
        self.studNumber = studNumber
        self.firstName = firstName
        self.lastName = lastName
        self.birthDate = birthDate
        self.sex = sex
        self.country = country

    @property
    def studentInfo(self):
        return [self.studNumber,self.firstName, self.lastName, self.birthDate, self.sex, self.country]
    
    
from ast import literal_eval
def addStudent():
    no = int(input("Please enter student no: "))
    firstName = input("First name: ")
    lastName = input("Last name: ")
    sex = input("Male/Female: ")
    date = int(input("Birth year: "))
    country = input("Country that the student was born: ")
    studentsArr = []
    file = open("C:/Users/kurtk/OneDrive/Masaüstü/Yeni klasör/student_data.txt", "r+")

    #creating student object here
    studentClass = Student(no, firstName, lastName, date,sex , country)
    studentObj = {
            "id": studentClass.studNumber,
            "name": studentClass.firstName,
            "surname": studentClass.lastName,
            "gender": studentClass.sex,
            "Birth date": studentClass.birthDate,
            "country": studentClass.country
        }
    # checking if file is empty  
    if file.read() == "":
        file.close()
        file = open("C:/Users/kurtk/OneDrive/Masaüstü/Yeni klasör/student_data.txt","w")
        studentsArr.append(studentObj)
        file.write(str(studentsArr))
        file.close()

    # checking if file is not empty
    else:
        file.close()
        file = open("C:/Users/kurtk/OneDrive/Masaüstü/Yeni klasör/student_data.txt", "r")
        prevStudents = file.read()
        prevStudentsArr = literal_eval(prevStudents)

        if len(prevStudentsArr) != 25:
            # adding previous students to array
            for prevStudent in prevStudentsArr:
                studentsArr.append(prevStudent)
             # adding new student at the end
            file = open("C:/Users/kurtk/OneDrive/Masaüstü/Yeni klasör/student_data.txt", "w")
            studentsArr.append(studentObj)
            file.write(str(studentsArr))
            file.close()
            print("Added new student.")
        else:
            print("you reached the student cap (25 student)!. You can't create new one anymore")

    file.close()

def deleteStudent(studNumber):
    file = open("C:/Users/kurtk/OneDrive/Masaüstü/Yeni klasör/student_data.txt", "r")
    prevStudents = file.read()
    prevStudentsArr = literal_eval(prevStudents) #add all students in the file

    #find student number
    for i in range(len(prevStudentsArr)):
        if prevStudentsArr[i]['id'] == studNumber:
            del prevStudentsArr[i]
            break
    file.close()

    #write the updated array to file
    file = open("C:/Users/kurtk/OneDrive/Masaüstü/Yeni klasör/student_data.txt", "w")
    file.write(str(prevStudentsArr))
    file.close()


def findStudent(studNumber):
    file = open("C:/Users/kurtk/OneDrive/Masaüstü/Yeni klasör/student_data.txt", "r")
    prevStudents = file.read()
    prevStudentsArr = literal_eval(prevStudents)

    # find student number
    for i in range(len(prevStudentsArr)):
        if prevStudentsArr[i]['id'] == studNumber:
            print(f'Id:   {prevStudentsArr[i]["id"]}\n'
                  f'Name:   {prevStudentsArr[i]["name"]}\n'
                  f'Surname: {prevStudentsArr[i]["surname"]}\n'
                  f'Age:   {2021- prevStudentsArr[i]["Birth date"]}\n'
                  f'Gender:   {prevStudentsArr[i]["sex"]}\n'
                  f'Date of Birth: {prevStudentsArr[i]["Birth date"]}\n'
                  f'Country :  {prevStudentsArr[i]["country"]}')
            break
    file.close()

def findStudentWithDate(date):
    file = open("C:/Users/kurtk/OneDrive/Masaüstü/Yeni klasör/student_data.txt", "r")
    prevStudents = file.read()
    prevStudentsArr = literal_eval(prevStudents)

    # find student number
    for i in range(len(prevStudentsArr)):
        if prevStudentsArr[i]['Birth date'] == date:
            print(f'Id:   {prevStudentsArr[i]["id"]}\n'
                  f'Name:   {prevStudentsArr[i]["name"]}\n'
                  f'Surname: {prevStudentsArr[i]["surname"]}\n'
                  f'Age:   {2021- prevStudentsArr[i]["Birth date"]}\n'
                  f'Gender:   {prevStudentsArr[i]["sex"]}\n'
                  f'Date of Birth: {prevStudentsArr[i]["Birth date"]}\n'
                  f'Country :  {prevStudentsArr[i]["country"]}')
    file.close()

def modifyStudent():
    studNumber = int(input("Enter student no to be modified: "))
    print("1. Student No")
    print("2. First Name")
    print("3. Last Name")
    print("4. Gender")
    print("5. Date of Birth")
    print("6. Country Borned In")
    userInpt = int(input("Enter the field digit you want to modify: "))

    file = open("C:/Users/kurtk/OneDrive/Masaüstü/Yeni klasör/student_data.txt", "r")
    prevStudents = file.read()
    prevStudentsArr = literal_eval(prevStudents)

    for i in range(len(prevStudentsArr)):
        if prevStudentsArr[i]['id'] == studNumber:
            if userInpt == 1:
                newValue = int(input("Enter new student no: "))
                prevStudentsArr[i]['id'] = newValue
            elif userInpt == 2:
                newValue = input("Enter student's first name: ")
                prevStudentsArr[i]['name'] = newValue
            elif userInpt == 3:
                newValue = input("Enter student's last name: ")
                prevStudentsArr[i]['surname'] = newValue
            elif userInpt == 4:
                newValue = input("Enter student's gender: ")
                prevStudentsArr[i]['sex'] = newValue
            elif userInpt == 5:
                newValue = int(input("Enter student's date of birth: "))
                prevStudentsArr[i]['Birth date'] = newValue
            elif userInpt == 6:
                newValue = input("Enter student's country: ")
                prevStudentsArr[i]['country'] = newValue
            break
    print("Student info has been modified.")
    file.close()

    file = open("C:/Users/kurtk/OneDrive/Masaüstü/Yeni klasör/student_data.txt", "w")
    file.write(str(prevStudentsArr))
    file.close()


def showAllStudents():
    print("1. Show all students")
    print("2. Show stundets that born in a specific year")
    usrInpt = int(input("Please enter your option: "))

    #get all students from file
    if usrInpt == 1:
        try:
            file = open("C:/Users/kurtk/OneDrive/Masaüstü/Yeni klasör/student_data.txt", "r")
            prevStudents = file.read()
            prevStudentsArr = literal_eval(prevStudents)
            print(f'     Std No.     Name    Surname     Age    Gender     Date of Birth     Country  ')
            print("   ------------------------------------------------------------------------------")
            # find student no
            for i in range(len(prevStudentsArr)):
                print(f'    {prevStudentsArr[i]["id"]}     '
                      f'{prevStudentsArr[i]["name"]}     '
                      f'{prevStudentsArr[i]["surname"]}      '
                      f'{2021 - prevStudentsArr[i]["Birth date"]}     '
                      f'{prevStudentsArr[i]["sex"]}      '
                      f'{prevStudentsArr[i]["Birth date"]}            '
                      f'{prevStudentsArr[i]["country"]} ')
            file.close()
        except:
            print("There is no student!")

    #get all students with a specified year from the file
    elif usrInpt == 2:
        try:
            file = open("C:/Users/kurtk/OneDrive/Masaüstü/Yeni klasör/student_data.txt", "r")
            prevStudents = file.read()
            prevStudentsArr = literal_eval(prevStudents)
            inpt = int(input("Enter year: "))

            print(f'     Std No.     Name    Surname     Age    Gender     Date of Birth     Country  ')
            print("   ------------------------------------------------------------------------------")

            # find student no
            for i in range(len(prevStudentsArr)):
                if prevStudentsArr[i]["Birth date"] == inpt:
                    print(f'    {prevStudentsArr[i]["id"]}     '
                          f'{prevStudentsArr[i]["name"]}     '
                          f'{prevStudentsArr[i]["surname"]}      '
                          f'{2021 - prevStudentsArr[i]["Birth date"]}     '
                          f'{prevStudentsArr[i]["sex"]}      '
                          f'{prevStudentsArr[i]["Birth date"]}            '
                          f'{prevStudentsArr[i]["country"]} ')

            file.close()
        except:
            print("there is no student please add new to proceed")

def showStudents():
    file = open("C:/Users/kurtk/OneDrive/Masaüstü/Yeni klasör/student_data.txt", "r")
    prevStudents = file.read()
    prevStudentsArr = literal_eval(prevStudents)
    print(f'     Std No.     Name    Surname     Age    Gender     Date of Birth     Country  ')
    print("   ------------------------------------------------------------------------------")
    # find student no
    for i in range(len(prevStudentsArr)):
        print(f'    {prevStudentsArr[i]["id"]}     '
              f'{prevStudentsArr[i]["name"]}     '
              f'{prevStudentsArr[i]["surname"]}      '
              f'{2021 - prevStudentsArr[i]["Birth date"]}     '
              f'{prevStudentsArr[i]["sex"]}      '
              f'{prevStudentsArr[i]["Birth date"]}            '
              f'{prevStudentsArr[i]["country"]} ')
    file.close()


from ast import literal_eval
file = open("C:/Users/kurtk/OneDrive/Masaüstü/Yeni klasör/student_data.txt", "r")
studentsDataFile = file.read()

print("welcome")
print("please enter the number of the option:")

flag = True

def checkIfUserWantToExit():
    select = input("do you want to continue?(y/n): ")
    if select.lower() != "y":
        global flag
        flag = False
        print("quitting..")
        return ""

while(flag):
    print(" MAIN  MENU ")
    print("1. Add a Student")
    print("2. Delete a Student")
    print("3. Find a Student")
    print("4. Find a Student With Date of Birth")
    print("5. Modify a Student")
    print("6. Show All Students on the list")
    print("7. Quit")

    userInpt = int(input("Please enter here :"))

    if userInpt == 1:
        print("-- add new student --")
        addStudent()
        checkIfUserWantToExit()

    elif userInpt == 2:
        print("                         -- delete a student --")
        showStudents()
        inpt = int(input("Enter student number: "))

        deleteStudent(inpt)
        print("Deleting student")
        checkIfUserWantToExit()

    elif userInpt == 3:
        print(" -- find a student --")
        try:
            studentsDataArr = literal_eval(studentsDataFile)
            inpt = int(input("Enter student number: "))
            findStudent(inpt)
            checkIfUserWantToExit()
        except:
            print("there is no data")
            checkIfUserWantToExit()
    elif userInpt == 4:
        print(" -- find a student with date of birth --")
        try:
            studentsDataArr = literal_eval(studentsDataFile)
            inpt = int(input("Enter Date of Birth:"))
            findStudentWithDate(inpt)
            checkIfUserWantToExit()
        except:
            print("there is no data")
            checkIfUserWantToExit()

    elif userInpt == 5:
        print("                         -- modify a student --")
        showStudents()
        modifyStudent()
        showStudents()
        checkIfUserWantToExit()

    elif userInpt == 6:
        print("                        -- all students --")
        showAllStudents()
        print("\n")
        checkIfUserWantToExit()

    elif userInpt == 7:
        flag = False
        print("Quitting..")
        
    else:
        print("Invalid digit! Please try again")