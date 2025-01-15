                # #  Lab Demonstrating Access Modifiers with empolyee data

# class Employee:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.__salary = 50000

#     def disp(self):
#         print(f"Name: {self.name}, Age: {self.age}, Salary: {self.__salary}")

#     def _calculate_bonus(self):
#         return self.__salary * 0.10
    
#     def get_salary(self):
#         return self.__salary
    
#     def disp_bonus(self):
#         bonus = self._calculate_bonus()
#         print(f'Bonus for {self.name}: {bonus}')

# employee = Employee("Abdul Rasheed", 30)
# print(employee.name)

# employee.disp()


# try:
#     print(employee.__salary)
# except AttributeError as e:
#     print(e)

# print(employee.get_salary())

# employee.disp_bonus()



            # Lab 51 To create a simple transaction system using classes and objects in Python

# class BankAccount:
#     def __init__(self, account_number, holder_name, initial_balance=0):
#         self.account_number = account_number
#         self.holder_name = holder_name
#         self.balance = initial_balance

#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             print(f"Deposited: {amount:.2f}. New balance is {self.balance:.2f}.")
#         else:
#             print("Deposit amount must be positive.")

#     def withdraw(self, amount):
#         if amount > 0 and amount <= self.balance:
#             self.balance -= amount
#             print(f"Withdrew: {amount:.2f}. New balance is {self.balance:.2f}.")
#         else:
#             print("Insufficient balance or invalid withdrawal amount.")

#     def __str__(self):
#         return (f"Account Number: {self.account_number}\n"
#                 f"Holder Name: {self.holder_name}\n"
#                 f"Balance: ₹{self.balance:.2f}")


# if __name__ == "__main__":

#     account = BankAccount("123459786", "Aadil Chauhan", 1000)


#     print(account)

#     account.deposit(500)
#     account.withdraw(200)
#     account.withdraw(1500)  

#     print(f"Final balance: ₹{account.balance:.2f}")


            # Lab 52 . Implementation of encapsulation in a BankAccount transaction
    

# class BankAccount:
#     def __init__(self, account_number, holder_name, initial_balance=0):

#         self.__account_number = account_number  
#         self.__holder_name = holder_name       
#         self.__balance = initial_balance       

#     def deposit(self, amount):

#         if amount > 0:
#             self.__balance += amount
#             print(f"Deposited: {amount:.2f}. New balance is {self.__balance:.2f}.")
#         else:
#             print("Deposit amount must be positive.")

#     def withdraw(self, amount):

#         if 0 < amount <= self.__balance:
#             self.__balance -= amount
#             print(f"Withdrew: {amount:.2f}. New balance is {self.__balance:.2f}.")
#         else:
#             print("Insufficient funds or invalid amount.")

#     def get_balance(self):
#         return self.__balance

#     def __str__(self):
#         return (f"Account Number: {self.__account_number}\n"
#                 f"Holder Name: {self.__holder_name}\n"
#                 f"Balance: ₹{self.__balance:.2f}")
    

# if __name__ == "__main__":

#     account = BankAccount("987654321", "Ayesha", 1500)
#     print(account)


#     account.deposit(300)
#     account.withdraw(200)
#     account.withdraw(2000)  
#     print(f"Final balance:₹{account.get_balance():.2f}")



            # Lab 53. Implementation of data abstraction for a simple medical billing system in Python


from abc import ABC, abstractmethod

class BillingRecord(ABC):
    @abstractmethod
    def get_bill(self):
        pass

    @abstractmethod
    def update_bill(self, amount):
        pass

class PatientBilling(BillingRecord):
    def __init__(self, patient_id, patient_name, billing_amount=0):
        self.__patient_id = patient_id
        self.__patient_name = patient_name
        self.__billing_amount = billing_amount

    def get_bill(self):
        return {
            'Patient ID': self.__patient_id,
            'Patient Name': self.__patient_name,
            'Billing Amount': f'{self.__billing_amount:.2f}'
        }

    def update_bill(self, amount):
        if amount > 0:
            self.__billing_amount += amount
            print(f"Updated billing amount: {self.__billing_amount:.2f}")
        else:
            print("Amount must be positive.")


if __name__ == "__main__":

    patient_bill = PatientBilling(
        patient_id="P001",
        patient_name="Aadil Chauhan",
        billing_amount=1500.00
    )


    print("Initial Bill Details:")
    print(patient_bill.get_bill())

   
    patient_bill.update_bill(500.00) 

    print("\nUpdated Bill Details:")
    print(patient_bill.get_bill())





