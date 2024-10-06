# # Addition of two number

# class Addition:

#     def __init__(self, firstnum,secondnum):
#         self.firstnum= firstnum
#         self.secondnum= secondnum

#     def display_sentence(self):
#      print(f"First number is :{self.firstnum}")  
#      print(f"Second number is : {self.secondnum}")

#     def answers(self):
#         print(f"Addition of two number is : {self.firstnum+self.secondnum}")

# sum1 = Addition(12,22) 
# sum1.display_sentence()
# sum1.answers()

# sum2 = Addition(123123,45646) 
# sum2.display_sentence()
# sum2.answers()

# # Create student class that takes name and marks of three subjects as argument in constructor the create a method to print the average

# class Student:

#     def __init__(self, name, marks1, marks2, marks3):
#         self.name = name
#         self.marks1= marks1
#         self.marks2= marks2
#         self.marks3= marks3

#     def answer(self):
#         print(f" For {self.name} the average marks of three subjects is : {(self.marks1+self.marks2+self.marks3)/3}")


# student_name1= Student('Durgesh',12,23,34)
# student_name1.answer()
# student_name2= Student("Diksha",13,43,54)
# student_name2.answer()

# class Student:

#     def __init__(self, name, marks):
#         self.name = name
#         self.marks= marks

#     def answer(self):
#         sum =0
#         for val in self.marks:
#            sum+=val
#         print(f" For {self.name} the average marks of three subjects is : {sum/3}")


# student_name1= Student('vikas',[12,29,34])
# student_name1.answer()
# student_name2= Student("vinod",[14,43,54])
# student_name2.answer()


# Create account class wtih two attributes balance and account number
# Create method with debit credit and printing the balance amount

# class Account:

#     def __init__(self, balance, account_number):
#         self.balance= balance
#         self.account_number= account_number

#     def debit(self):
#         a=100
#         debited=self.balance-a
#         print(f"From {self.account_number}, '{a}' is debited from the account now total balance is :{debited}")

#     def credit(self):
#         b=1000
#         credited=self.balance+b
#         print(f"From {self.account_number}, '{b}' is credited to the account now total balance is :{credited}")

# a1 = Account(2000, 388701504258)
# a1.debit()
# a1.credit()


class Account:

    def __init__(self, balance, account_number):
        self.balance= balance
        self.account_number= account_number

    def debit(self,amount):
        self.balance -= amount
        print(f"From {self.account_number}, '{amount}' was debited from the account now total balance is :{self.get_balance()}")

    def credit(self,amount):
        self.balance += amount
        print(f"From {self.account_number}, '{amount}' was credited to the account now total balance is :{self.get_balance()}")

    def get_balance(self):
        return self.balance

a1 = Account(2000, 388701504258)
a1.debit(100)
a1.credit(1000)
a1.credit(132313123)



