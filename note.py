# print("hello")





# output = 0
# print(f"1: {output}")

# def help_me_get_the_answer():
    # output = 3 * 2
    # print(f"2: {output}")
    # return output 
# print(f"3: {output}")


# help_me_get_the_answer()
# print(f"4: {output}")


# output = help_me_get_the_answer()
# print(f"5: {output}")


# output = "None"
# print(f"6: {output}")


# output = None
# print(f"7: {output}")






# output = help_me_get_the_answer()
# print(output)








# o = "OXFORD BOOKWORMS LIBRARY".title()
# print(o)



# print("built a ladder notes 21".title())




# vs code could open these hint
# not notepad++

# def help_me_get_a_apple():
    # """This function is going to help a human
    # get a apple.hhhhhhhhhhhhh"""
    # print("apple")

# help_me_get_a_apple()






# http://patorjk.com/software/taag/#p=display&f=Graffiti&t=Ya-Tao%20Zhao

# logo = '''

# _____.___.              ___________               __________.__                   
# \__  |   |____          \__    ___/____    ____   \____    /|  |__ _____    ____  
 # /   |   \__  \    ______ |    |  \__  \  /  _ \    /     / |  |  \\__  \  /  _ \ 
 # \____   |/ __ \_ /_____/ |    |   / __ \(  <_> )  /     /_ |   Y  \/ __ \(  <_> )
 # / ______(____  /         |____|  (____  /\____/  /_______ \|___|  (____  /\____/ 
 # \/           \/                       \/                 \/     \/     \/        
# '''



# logo2 = '''
 # __     __       _______            _______                 
 # \ \   / /      |__   __|          |___  / |                
  # \ \_/ /_ _ ______| | __ _  ___      / /| |__   __ _  ___  
   # \   / _` |______| |/ _` |/ _ \    / / | '_ \ / _` |/ _ \ 
    # | | (_| |      | | (_| | (_) |  / /__| | | | (_| | (_) |
    # |_|\__,_|      |_|\__,_|\___/  /_____|_| |_|\__,_|\___/ 
# '''
 
 
 
# print(logo)
# print(logo2)
 
 
 
 
 



# remover old dict:
# dict1 = {
    # 'value': 11
# }
# dict2 = dict1

# print(dict1)
# print(dict2)
# print("--------------------------")
# dict1['value'] = 22
# print(dict1)
# print(dict2)





# dict = {
    # "value": 11,
    # "next": None
# }

# print(dict)

# dict.pop("value")
# print(dict)
 
 

# 4!
# def factorial(n):
    # if n == 1:
        # return 1
    # return n * factorial(n-1)
 # print(factorial(4))



# def factorial_number(4):
    
    
# for i in range(1,5):
    # print(f"{i}*{i+1}")
    
# print(range(4))



# def factorial(n):    
    # if n == 1:
        # return 1
    # return print(f"4! = {n} * {factorial(n-1)}")

# factorial(4)





# n = input("Enter a number: ")
# factorial = 1
# if int(n) >= 1:
    # for i in range (1,int(n)+1):
        # print(i)
        # factorial = factorial * i
        # print(f"{factorial} * {i}")
# print("Factorail of ",n , " is : ",factorial)



# def factorial(x):
   # n = 1
   # while x > 1:
       # n *= x
       # x -= 1
   # return n

# print (factorial(5))





# def factorial(x):
    # n = 1   # this will store the factorial value
    # while x > 0:
        # n = n*x
        # x -= 1
    # return n






# def factorial(x):

    # while x > 0:

        # print(x)
        
    
# factorial(4)



# def factorial(x):
    # n = x
    # while n >= 0:
        # x = n * (n - 1)
        # n -= 1
    # return x
    
# print(factorial(4))






# def factorial(x):
    # n = 1
    # while x > 0:
        # print(x)
        # print(f"{n} * {x}")
        # n = x * n
        # print(f"{n} * {x}")
        # x -= 1
        # print(x)
        # print("----------------")
    # return print(n)

# factorial(4)





# def factorial(x):
    # while x != 1:
        # print(x)
        # for i in range(1, x+1):
            # n = x * (x - i)
            # print(f"{n} = {x} * {(x-i)}")
        # x -= 1
        # print("-------------------------")
    # return print(n)

# factorial(4)










# def factorial(x):
    # while x != 1:
        # print(x)
        # for i in range(1, x+1):
            # n = (x - i)
            
            # print(f"{n} = {x} * {(x-i)}")
        # x -= 1
        # print("-------------------------")
    # return print(n)

# factorial(4)





# for i in range(1,5):
    # print(i, end = "")
    
    
    
    
# for i in range(4, 0, -1):
    # if i == 1:
        # print(i, end = "")
        # break
    # print(i, end = "*")
    



# print(type(4/2))






# py -m venv env



# from math import log
# import numpy as number_python
# import matplotlib.pyplot









# Fibonacci series:
# the sum of two elements defines the next
# a, b = 0, 1
# while a < 100:
    # print(a)
    # a, b = b, a+b






# a = 1
# b = 2
# c = 0
# while a < 100:
    # print(a)
    # c = a + b
    # a = b
    # b = c
    




# users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
# print(users)
# for user, status in users.copy().items():
    # if status == 'inactive':
        # del users[user]
        # print(users)






# a = [1, 2, 3, 4, 5]
# b = [i*2 for i in a ]
# print(b)
# c = map(lambda x: x*2, a)
# print(list(c))








# print("This will always be run.")

# def main():
    # print(
    # """
    # This will NOT always be run. 
    # This module's name = {}
    # """
    # .format(__name__))
    
    
 # if __name__ == "__main__":
    # main()
# else:
    # print("this note.py module is run from import.")







# def fullname():
    # return print('arthur')
    ## return 'arthur'
# fullname()







# python object-oriented programming

# class employee:
    # pass
    
# emp_1 = employee()
# emp_2 = employee()

# print(emp_1)
# print(emp_2)












# # print('↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓')
# # print("This will always be run.")


# def main():
    # # print(
    # # """
    
    # # This will NOT always be run. 
    # # This module's name = {}
    # # """
    # # .format(__name__))
    
    
        
    
    # # # class employee:
        # # # pass
        
    # # # emp_1 = employee()
    # # # emp_2 = employee()

    # # # print(emp_1)
    # # # print(emp_2)
    
    # # # emp_1.first = 'Corey'
    # # # emp_1.last = 'Schafer'
    # # # emp_1.email = 'Corey.Schafer@company.com'
    # # # emp_1.pay = '50000'
        
    # # # emp_2.first = 'Test'
    # # # emp_2.last = 'User'
    # # # emp_2.email = 'Test.User@company.com'
    # # # emp_2.pay = '40000'
    
    # # # print()
    # # # print(emp_1.email)
    # # # print(emp_2.email)
    
    # raise_amount = 1.05
    # print(raise_amount)


    # class employee:
        
        # # class variable
        # raise_amount = 1.04
        # print(raise_amount)
        # # print(raise_amount)
        
    
    
    
        # def __init__(self, first, last, pay):
            # # first, last, pay are positional arguments
            # self.first = first
            # # self.first: object's atriburion
            # # first: programmer's input
            # # emp_1.first = "corey"
            # # emp_2.first = 'test'
            # # self = employee's object
            
            # self.last = last
            # self.pay = pay
            # self.email = first + '.' + last + "@company.com"
            
        
        # def fullname(self):
            # return '{} {}'.format(self.first, self.last)
            
            
            
        # def apply_raise(self):
            # print(raise_amount)
            # print(employee.raise_amount)
            # print(self.raise_amount)
            
            # self.pay = int(self.pay * self.raise_amount )
            # return self.pay
            
        
    # emp_1 = employee('yatao', 'zhao', 50000)
    # emp_2 = employee('arthur', 'run', 60000)
    
    # # print()
    # # print(emp_1)
    # # print(emp_1.first, emp_1.last, emp_1.pay)
    # # print(emp_2.first)
    
    # # print()
    # # print('{} {}'.format(emp_1.first, emp_1.last))    
    
    # # # fullname()
    
    # # # print(emp_1.fullname)
    # # # fullname(emp_1)
    # # # emp_1.fullname()
    # # print(emp_1.fullname())  # clear code way
    # # print(emp_2.fullname())
    # # print()
    
    
    # # print(employee.fullname(emp_1)) # better understand way
    # # # class.method.arguments
    
    # # print(emp_1.pay)
    # # emp_1.apply_raise()
    # # print(emp_1.pay)
    
    # print(emp_1.pay)
    # print(employee.apply_raise(emp_1))
    
    # print(employee.__name__)
    
    
        


# print(main.__name__)    
# if __name__ == "__main__":
    # main()
# else:
    # print("this note.py module is run from import.")
















# print("This will always be run.")

# def main():
    # print("This will be run when you do not import this.")
    # print('What\'s up?')
    
    
# if __name__ == "__main__":
    # main()
# else:
    # print("this note.py module is run from import.")
    
    
    






# f(x) = x + 10, x belong Z
# f(1) = 11


# def f(x):
    # y = x + 10
    # print(y) 

# f(1)









# turtle.pencolor('blue')
# for line in range(4):
    # turtle.forward(100)
    # turtle.left(90)


# turtle.penup()
# turtle.forward(-20)
# turtle.left(90)
# turtle.forward(-20)
# turtle.pendown()
# turtle.right(90)


# turtle.pencolor('green')
# for line in range(4):
    # turtle.forward(140)
    # turtle.left(90)    


# turtle.penup()
# turtle.forward(-20)
# turtle.left(90)
# turtle.forward(-20)
# turtle.pendown()
# turtle.right(90)



# turtle.pencolor('black')
# for line in range(4):
    # turtle.forward(180)
    # turtle.left(90)  



# import turtle

# for square in range(10):
    # for line in range(4):
        # turtle.forward(100+square*40)
        # turtle.left(90)
        
    # turtle.penup()
    # turtle.forward(-20)
    # turtle.left(90)
    # turtle.forward(-20)
    # turtle.pendown()
    # turtle.right(90)

# turtle.done()









#######################################
# n = 10
# print(str(n) + "! = ", end = '')
# def factorial(n):
    # '''
    # print factorial number in human way
    # '''
    # if n < 0:
        # return 'factorial() not defined for negative values'
    # if n == 0:
        # return 1
    # if n == 1:
        # print('', n, '= ', end = '')
        # return 1
    # else:
        # print('', n, '*', end = '')
        # return n * factorial(n - 1)

# print(factorial(n))










##############
# import math
# print(math.pi)
# print(math.e)
# print(math.tau)










################
# import pandas

# simpsons = pandas.read_html('https://en.wikipedia.org/wiki/List_of_The_Simpsons_episodes_(seasons_1%E2%80%9320)')
# print(len(simpsons))
# print(simpsons[1])


##############
# import pandas
# england = pandas.read_csv('https://www.football-data.co.uk/mmz4281/2122/E0.csv')

# print(england)








############
# # pip install "camelot-py[cv]"
# import camelot

# table = camelot.read_pdf('foo.pdf', page='1')
# print(table)

# # table.export('foo.csv', f = 'csv')
# table.export('foo.csv')
# # table[0].to_csv('foo.csv')







##############


