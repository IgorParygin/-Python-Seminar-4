# Задача 3: Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.


def cod(text):
    count = 1
    result = ''
    for i in range(len(text) - 1):
        if text[i] == text[i + 1]:
            count += 1
        else:
            result = result + str(count) + text[i]
            count = 1
    if count > 1 or (text[len(text) - 2] != text[-1]):
        result = result + str(count) + text[-1]
    return result

def decod(text):
    number = ''
    result = ''
    for i in range(len(text)):
        if not text[i].isalpha():
            number += text[i]
        else:
            result = result + text[i] * int(number)
            number = ''
    return result


s = input("Введите текст для сжатия или восстановления: ")
if s[0].isdigit():
    print(f"Текст после дешифровки: {decod(s)}")
else:
    print(f"Текст после кодировки: {cod(s)}")
