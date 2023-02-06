# name = 'reza'
# این علامت برای کامنت گذاری استفاده می شود.
# print(type(name))
# برای نامگذاری متغیرها هر تر کیبی از کاراکترهای الفبایی انگلیسی و اعداد و _می توان گذاشت
# اما اعداد نباید اولین کاراکتر باشند
# print(name[0])
# print(name[1])
# print(name[2])
# print(name[3])
# print(name[5]) # error
# exercise1  کاراکترهای اسم خودتان زا از انتها به ابتدا بنویسید


# string1 = 'abcd'
# string2 = 'efgh'

# چسباندن رشته ها
# string = string1 + string2

# print(string)


# name = 'nikan'
# family = 'nikani'

# output = name + " " + family
# print(output)

# exercise 2 : نام و نام خانوادگی و سن خود را در سه متغیر ذخیره کنید و با فاصله پرینت کنید
#  مثال : nikan nikani 15

name = "behrad"
family = "alavi"
course = "python"

message = "hello %s %s, welcome to our %s class." % (name, family, course)
print(message)

# روش دوم
# fstring
message = f"hello {name} {family} welcome to our {course} class"
print(message)


# exercise 3 : با استفاده از روش بالا پیغام زیر را پرینت نمایید.
#    I am behrad alavi and i have 12 years old.