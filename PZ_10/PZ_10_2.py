# Из предложенного текстового файла (text18-14.txt) вывести на экран его содержимое,
# количество пробельных символов. Сформировать новый файл, в который поместить текст
# в стихотворной форме предварительно заменив символы третей строки их числовыми
# кодами.

with open('text18-14.txt', 'r', encoding='utf8') as file:
    text = file.read()

print(text)

space_ch = 0
for i in text:
    if i == ' ':
        space_ch += 1

print('Количество пробельных символов: ', space_ch)

with open('text18-14.txt', 'r', encoding='utf8') as file:
    text_lines = file.readlines()

# преобразуем третью строку в кодировку
line3 = text_lines[2]
for i in line3:
    line3 = line3.replace(i, str(ord(i)), 1)
line3 = line3 + '\n'
text_lines[2] = line3

with open('text18-14_2.txt', 'w', encoding='utf8') as file:
    file.writelines(text_lines)
