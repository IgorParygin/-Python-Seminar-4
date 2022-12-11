# Задача 1: Напишите программу, удаляющую из текста все слова, содержащие "абв".

text = input('Введите текст через пробел:\n')
print(f'Исходный текст: {text}')
del_text = 'абв'
my_list = [i for i in text.split() if del_text not in i]
print(f'Без абв: {" ".join(my_list)}')

