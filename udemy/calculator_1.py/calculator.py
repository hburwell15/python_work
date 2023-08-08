def add(n1, n2):
  return n1 + n2


def exponent(n1, n2):
  return n1 ** n2


def subtract(n1, n2):
  return n1 - n2


def multiply(n1, n2):
  return n1 * n2


def divide(n1, n2):
  return n1 / n2


from calculator_art import logo

operations = {
  '+': add, 
  '-': subtract, 
  '*': multiply, 
  '/': divide,
  '**': exponent, 
}

def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))
    
    for symbol in operations:
      print(symbol)
      
    should_continue = True
    while should_continue:
      operation_symbol = input("Please pick an operation: ")
        
      num2 = float(input("What's the next number?: "))
      
      calculation_function = operations[operation_symbol]
      answer = calculation_function(num1, num2)
          
      print(f"{num1} {operation_symbol} {num2} = {answer}")
      var = input(f"Type 'y' to continue calculating with {answer}, to start a new calculaton, type 'c', to exit, type 'n': ")

      if var == 'y':
        num1 = answer
        continue
      elif var == 'c':
        should_continue = False
        calculator()
      elif var == 'n':
        return "Thank you for using my calculator program!"
        

      
calculator() 