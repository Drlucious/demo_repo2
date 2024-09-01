import unittest
from unittest.mock import patch
import datetime

class Car:
    def __init__(self, make, model, year,price):
        self.make = make
        self.model = model
        self.year = year
        self.price = price

    def start_engine(self):
        return f"The {self.year} {self.make} {self.model} {self.price}."

# Create an instance of the Car class
my_car = Car("Mercedes Benz", "A class", 2024,120000)
print(my_car.start_engine())

class BankAccount:
    def __init__(self, balance=0):
        self._balance = balance  # Encapsulated attribute (protected by convention)

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self._balance

# Create an instance of the BankAccount class
class Employee:
    def __init__(self, first, last, pay):
        self.BankAccount = None
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
    raise_amount = 3.02

class Manager(Employee,BankAccount):
      def __init__(self, first, last, pay, employees=None):
          super().__init__(first, last, pay)
          if employees is None:
              self.employees = []
          else:
              self.employees = employees
      def add_emp(self,emp):
          if emp not in self.employees:
              self.employees.append(emp)
      def remove_emp(self,emp):
          if emp in self.employees:
              self.employees.remove(emp)

      def apply_raise(self):
          self.pay = int(self.pay * self.raise_amount)
      raise_amount = 3.02
      def print_emp(self):
          for emp in self.employees:
              print ('--->',emp.fullname())

emp_1 = Employee('Liam', 'Stash', 46000)
emp_2 = Employee('Maria', 'Gonzalez', 50000)
emp_3 = Employee('Gift', 'Ayo', 70000)

mgr_1= Manager('Saito', 'Hajime',120000, [emp_1])


def setUp(self):
    print('setUp')
    emp_1 = Employee('Liam', 'Stash', 46000)
    emp_2 = Employee('Maria', 'Gonzalez', 50000)
    emp_3 = Employee('Gift', 'Ayo', 700000)
    mgr_1 = Manager('Saito', 'Hajime', 120000, [emp_1])

def tearDown(self):
    print('tearDown\n')

def promotion(self):
    cash = self.pay * 15
    return f"Congratulations, you have been promoted with a bonus of {cash}"

def test_fullname(self):
    print('test_fullname')
    self.assertEqual(self.mgr_1.fullname, '')
    self.assertEqual(self.emp_2.fullname, '')

    self.mgr_1.first = ''
    self.emp_2.first = ''

    self.assertEqual(self.mgr_1.fullname, ' ')
    self.assertEqual(self.emp_2.fullname, ' ')

def End(self):
    Deadline = datetime.date(2024,3,20)
    work = datetime.datetime.now()
    if work < Deadline:
        print("Well dome")
    else:
        none = self.pay / 120
        print(f"Your wage has been reduced to {none}")

def car_deal(self,pay):
    # Assuming these are attributes of 'self' or defined elsewhere
    employees = [emp_1, emp_2, emp_3, mgr_1]

    for employee in employees:
        if self.pay < my_car:
            print("Insufficient funds, please withdraw money")
            employee.withdraw(2500)  # Assuming 'withdraw' modifies 'self.pay'
        else:
            print("You have won the car prize")
            return employee

    # If we exit the loop without winning, print a final message
    print("No employee won the car prize after all checks.")
    return None
