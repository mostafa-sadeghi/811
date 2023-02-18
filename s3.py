# message = "hello every body, welcome to our \"python\" class.\nwe are going to learn everything about python.\npython from zero to hero!!"
# print(message)
# message = """hello every body, welcome to our "python" class.
# we are going to learn everything about "python".
# python from zero to hero!!"""
# print(message)
# message = '''hello every body, welcome to our "python" class.
# we are going to learn everything about python.
# python from zero to hero!!'''
# print(message)


# exercise 1 print this statement :  He said, "Aren't can't shouldn't wouldn't."    عبارت مقابل را به همین صورت پرینت نمائید.

# star = '*' * 10
# print(star)

# name = input('enter your name:> ')
# course = input('enter the name of your favorite course: ')
# message = f'''hello {name}, welcome to our "{course}" class.
# we are going to learn everything about {course}.
# {course} from zero to hero!!'''
# print(message)


# casting or converting    تبدیل نوع - رشته به عدد صحیح
# number1 = int(input('enter first number '))
# number2 = int(input('enter second number '))

# result = number1 + number2

# print(f"sum of {number1} and {number2} is:", result)
# converting to float number تبدیل به عدد اعشاری
# number1 = float(input('enter first number '))
# number2 = float(input('enter second number '))

# result = number1 + number2

# print(f"sum of {number1} and {number2} is:", result)


# exercise 1 : برنامه ای بنویسید که دو عدد را از ورودی دریافت نماید و حاصل جمع آن ها را به صورت زیر نمایش دهد
# 10 + 12 = 22
# number1 = int(input('enter first number:'))
# number2 = int(input('enter second number:'))
# result = number1 + number2
# print(f"{number1} + {number2} = {result}")
# exercise 2 : برنامه ای بنویسید که نام و نام خانوادگی و سن شما را از ورودی بگیرد و به صورت زیر نمایش دهد
# ali ramezani is 13 years old
# name = input('enter your name: ')
# family = input('enter your family: ')
# age = int(input('enter your age: '))
# print(f"{name} {family} is {age} years old.")

# exercise 3 : برنامه ای بسازید که سه عدد از ورودی دریافت نماید و عدد اول و دوم را با هم جمع و از عدد سوم کم نماید.
number1 = float(input('enter first number:'))
number2 = float(input('enter second number:'))
number3 = float(input('enter third number:'))

result = number1 + number2 - number3
print(f"{number1} + {number2} - {number3} = {result}")
