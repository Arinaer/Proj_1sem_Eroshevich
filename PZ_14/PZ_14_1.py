# В исходном текстовом файле (hotline1.txt) найти все номера телефонов,
# соответствующих шаблону 8(000)000-00-00. Посчитать количество полученных
# элементов. После фразы «Горячая линия» добавить фразу «Министерства
# образования Ростовской области», выполнив манипуляции в новом файле.

import re

with open('hotline1.txt', 'r') as file:
    text = file.read()
    add = re.subn(r'«Горячая линия»', '«Горячая линия Министерства образования Ростовской области»', text)
    text = add[0]
with open('hotline1_new.txt', 'w') as out:                  # Добавление текста в новый файл
    out.write(text)

p = re.compile(r'[8][(]\d{3}[)]\d{3}-\d{2}-\d{2}')          # Компилция шаблона.

print('Номера телефонов соответствующих шаблону: ', p.findall(text))
print('Количество полученных элементов: ', len(p.findall(text)))
