f = open ('data.txt','r', encoding = 'utf8')

f1 = f.readlines()

for x in f1:
    print(x.replace('\n','').split('#'))

class Worker():
    __id = str
    __name = str
    __position = str
    __salaryAmount = int

    def init(self, id, name, position, salaryAmount):
        self.__id = id
        self.__name = name
        self.__position = position
        self.__salaryAmount = salaryAmount

    def get_id(self):
        return self.__id

    def setID(self, id = str):
        self.__id = id
        if id:1 == str('S'):
            return id
        elif id:2 == int:
            return id
        elif id:3 == int:
            return id
        elif id:4 == int:
            return id
        elif id:5 == int:
            return id
        elif len(id) = 5:
            return id
        else:
            'wrong format'
        

    def get_name(self):
        return self.__name

    def setName(self, name = str):
        self.__name = name

    def get_position(self):
        return self.__position

    def set_position(self, position = str):
        self.__position = position
        if position == 'Staff':
             return position
        elif position == 'Officer':
             return position
        elif position == 'Manager':
             return position
        else:
             print('Not avaiable Position')
    
    def get_salary(self):
        return self.__salaryAmount

    def setSalary(self, salary):
        self.__salaryAmount = salary

class Staff(Worker):
    __salaryAmount = int

    def __init__(self):
        Worker.__init__(self, salaryAmount = str)
    
    def setSalary(self, salary = int):
        self.__salaryAmount = salary
        if salary >= 3500000:
            return salary
        elif salary <= 7000000:
            return salary
        else:
            'not in range'

class Officer(Worker):
    __salaryAmount = int

    def __init__(self):
        Worker.__init__(self, salaryAmount = str)
    
    def setSalary(self, salary = int):
        self.__salaryAmount = salary
        if salary >= 7000001:
            return salary
        elif salary <= 10000000:
            return salary
        else:
            'not in range'

class Manager(Worker):
    __salaryAmount = int

    def __init__(self):
        Worker.__init__(self, salaryAmount = str)
    
    def setSalary(self, salary = int):
        self.__salaryAmount = salary
        if salary >= 10000000:
            return salary
        else:
            'not in range'

def newStaff():
    print: "New Staff"
    input("Input ID SXXXX ")
    Worker().setID

def delStaff():
    print(input("Delete Staff: "))

def viewSum():
    print('Staff Maximum pay: ')
    print('Staff Minimum pay: ')
    print('Staff Average pay: ')
    print('Officer Maximum pay: ')
    print('Officer Minimum pay: ')
    print('Officer Average pay: ')
    print('Manager Maximum pay: ')
    print('Manager Minimum pay: ')
    print('Manager Average pay: ')

def save():
    f = open ('data.txt', 'a', encoding='utf8')

    exit

print('1. New Staff')
print('2. Delete Staff')
print('3. View Summary')
print('4. Save and Exit')
inputchoice = input('Input Choice: ')

if inputchoice == 1:
    newStaff()

if inputchoice == 2:
    delStaff()

if inputchoice == 3:
    viewSum()

if inputchoice == 4:
    save()