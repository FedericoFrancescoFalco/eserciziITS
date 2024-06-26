#1)Safe Square Root: Write a function safe_sqrt(number) that calculates the square root of a number using math.sqrt(). 
# Handle ValueError if the input is negative by returning an informative message.

import math

def safe_sqrt(number):
    try:
       
        result = math.sqrt(number)
        return result
    except ValueError:
        return "non posso calcolare un numero negativo."

#esempi
print(safe_sqrt(9))   
print(safe_sqrt(-1))  


#Password Validation: Write a function validate_password(password) that checks if a password meets certain criteria
#  (i.e., minimum length of 20 characters, at least three uppercase characters, and at least four special characters).  
# Raise a custom exception (e.g., InvalidPasswordError) for invalid passwords.


import re

class InvalidPasswordError(Exception):
    pass

def validate_password(password):
    
    if len(password) < 20:
        raise InvalidPasswordError("La password deve avere almeno 20 caratteri.")
    
    uppercase_count = len(re.findall(r'[A-Z]', password))
    if uppercase_count < 3:
        raise InvalidPasswordError("La password deve avere almeno un carattere maiuscolo.")
    
    
    special_count = len(re.findall(r'[!@#$%^&*(),.?":{}|<>]', password))
    if special_count < 4:
        raise InvalidPasswordError("La password deve avere almeno un carattere speciale.")
    
    return True

# esempio:
try:
    validate_password("A1b2C3!@#d$%^eFgHiJklmnopqrstuv")
    print("Password is valid.")
except InvalidPasswordError as e:
    print(f"Invalid password: {e}")

try:
    validate_password("shortpassword")
    print("Password is valid.")
except InvalidPasswordError as e:
    print(f"Invalid password: {e}")



#Database of dates:  Write a class that manages a database of dates with the format gg.mm.aaaa implementing methods to add a new date,
#  delete a given date, modify a date, and perform a query on a given date is required.  
# A query on a given date allows for retrieving a given new date. Note that a date is an object for your database;
#  it must be instantiated from a string.

import re

class ErroreDataNonValida(Exception):
    pass

class Data:
    def __init__(self, data_str):
        if not self._valida_formato_data(data_str):
            raise ErroreDataNonValida("Formato data non valido. Usa il formato gg.mm.aaaa.")
        self.data_str = data_str

    def __str__(self):
        return self.data_str

    @staticmethod
    def _valida_formato_data(data_str):
        
        pattern = r"^\d{2}\.\d{2}\.\d{4}$"
        return re.match(pattern, data_str) is not None

class DatabaseDate:
    def __init__(self):
        self.date = []

    def aggiungi_data(self, data_str):
        data = Data(data_str)
        self.date.append(data)
        print(f"Data aggiunta: {data}")

    def elimina_data(self, data_str):
        for data in self.date:
            if data.data_str == data_str:
                self.date.remove(data)
                print(f"Data eliminata: {data}")
                return
        print("Data non trovata.")

    def modifica_data(self, vecchia_data_str, nuova_data_str):
        for data in self.date:
            if data.data_str == vecchia_data_str:
                if not Data._valida_formato_data(nuova_data_str):
                    print("Nuova data non valida.")
                    return
                data.data_str = nuova_data_str
                print(f"Data modificata: {vecchia_data_str} in {nuova_data_str}")
                return
        print("Data non trovata.")

    def cerca_data(self, data_str):
        for data in self.date:
            if data.data_str == data_str:
                print(f"Data trovata: {data}")
                return data
        print("Data non trovata.")
        return None

    def __str__(self):
        return ", ".join(str(data) for data in self.date)

# Esempio di utilizzo:
db = DatabaseDate()
db.aggiungi_data("01.01.2020")
db.aggiungi_data("15.06.2021")
print(db)

db.modifica_data("15.06.2021", "16.06.2021")
print(db)

db.cerca_data("01.01.2020")

db.elimina_data("01.01.2020")
print(db)



#Context Managers for File Handling: Use the with statement and context managers to open and close a file. 
# Handle potential IOError within the with block for clean resource management.

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print(content)
    except IOError as e:
        print(f"An IOError occurred: {e}")

def write_file(file_path, content):
    try:
        with open(file_path, 'w') as file:
            file.write(content)
            print("Write operation successful.")
    except IOError as e:
        print(f"An IOError occurred: {e}")

# esempio di utilizzo:
read_file('example.txt')
write_file('example.txt', 'This is an example content.')



#An interactive calculator: It is required to develop an interactive calculator with at least 10 test cases using UnitTest trying to (possibly) cover all execution paths! User input is assumed to be a formula that consists of a number, an operator (at least + and -), and another number, separated by white space (e.g. 1 + 1). Split user input using str.split(), and check whether the resulting list is valid:
#If the input does not consist of 3 elements, raise a FormulaError, which is a custom Exception.
#Try to convert the first and third inputs to a float (like so: float_value = float(str_value)). Catch any ValueError that occurs, and instead raise a FormulaError.
# If the second input is not '+' or '-', again raise a FormulaError
#If the input is valid, perform the calculation and print out the result. The user is then prompted to provide new input, and so on, until the user enters quit.












#Personalized math library: Create a Python library that provides functions for handling fractions, with built-in error handling. The library must include functions for the following operations:
        #Create a fraction from the numerator and denominator.
        #Collect the numerator and denominator of a fraction.
        #Simplify a fraction.
        #Add, subtract, multiply and divide fractions.
        #Check whether one fraction is equivalent to another. 

        #All library functions must use the try-except block to handle potential errors, such as null denominators, unsupported operations, or division by zero. The library must raise custom exceptions to indicate specific errors to the user.
     #Custom Exception for Data Structure Integrity: Define a custom exception class DataStructureIntegrityError.  Define the custom data structure linked list use classes with methods to append, remove and access a given element, and write functions that operate on that (i.e., print the list,  reverse the list, and check whether the list is ordered). Raise this exception if the data structure's integrity is compromised (e.g., empty list access, index error).
