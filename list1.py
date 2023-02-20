# shopping_list = []
# print(type(shopping_list))

# shopping_list.append("apple")
# shopping_list.append("banana")
# shopping_list.append("potato")
# shopping_list.append("mashroom")

# print("my list after adding items:", shopping_list)

# لیستی از اعداد یک تا پنج بسازید و تک تک عضوهای لیست را با هم جمع کنید و حاصل را نمایش دهید.

# numbers = []
# numbers.append(1)
# numbers.append(2)
# numbers.append(3)
# numbers.append(4)
# numbers.append(5)

# print(numbers)
# print(numbers[0] + numbers[1] + numbers[2] +
#       numbers[3] + numbers[4])
# print(sum(numbers))

# numbers = [1, 2, 3, 4, 5]
# print(sum(numbers))
# اضافه کردن در لیست
# numbers.append(6)

# حذف کردن از لیست
# del numbers[3]
# print(numbers)


# names = ['nazain', 'behrad', 'farzam', 'heliya', 'some one']
# del names[4]
# یا
# names.remove('some one')

# print(names)


# exercise : برنامه ای بنویسید که اسم چهار نفر را از ورودی دریافت نماید و در لیستی ذخیره کند
# سپس اسم یک نفر از نفرات موجود در لیست را از ورودی بگیرد و او را از لیست حذف نماید.
# در هز مرحله نمایش لیست الزامیست.

names = []
n1 = input('enter a name: ')
n2 = input('enter a name: ')
n3 = input('enter a name: ')
n4 = input('enter a name: ')
names.append(n1)
names.append(n2)
names.append(n3)
names.append(n4)
print(names)
n = input('enter a name: ')
names.remove(n)
print(names)
