class User:
    def __init__(self, first_name, last_name, gender, street_address, city, email, cc_number, cc_type, balance,
                 account_no):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.street_address = street_address
        self.city = city
        self.email = email
        self.cc_number = cc_number
        self.cc_type = cc_type
        self.balance = balance
        self.account_no = account_no
        userList.append(self)

    def display_info(self):
        print("##################")
        print("User first name: ", self.first_name)
        print("User last name: ", self.last_name)
        print("User gender: ", self.gender)
        print("User address: ", self.street_address)
        print("User City: ", self.city)
        print("User first name: ", self.first_name)
        print("User cc number: ", self.cc_number)
        print("User cc type: ", self.cc_type)
        print("User balance: ", self.balance)
        print("User account number: ", self.account_no)
        print("##################")


def print_user():
    for user in userList:
        user.display_info()


def generateUsers():
    import csv
    with open('bankUsers.csv', newline='') as csvfile:
        filereader = csv.reader(csvfile, delimiter=',', quotechar="'")
        for line in filereader:
            User(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], float(line[8]), line[9])


def findUser():
    # TO COMPLETE

    True


def overdrafts():
    # TO COMPLETE

    True


def missingEmails():
    # TO COMPLETE

    True


def bankDetails():
    # TO COMPLETE

    True


def transfer():
    # TO COMPLETE

    True


userList = []
generateUsers()

userChoice = ""
print("Welcome")

while userChoice != "Q":
    print("What function would you like to run?")
    print("Type 1 to find a user")
    print("Type 2 to print overdraft information")
    print("Type 3 to print users with missing emails")
    print("Type 4 to print bank details")
    print("Type 5 to transfer money")
    print("Type Q to quit")
    userChoice = input("Enter choice: ").upper()
    print()

    if userChoice == "1":
        findUser()
    elif userChoice == "2":
        overdrafts()
    elif userChoice == "3":
        missingEmails()
    elif userChoice == "4":
        bankDetails()
    elif userChoice == "5":
        transfer()
    elif userChoice == "6":
        print_user()
    print()
