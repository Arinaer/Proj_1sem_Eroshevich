# Дана строка-предложение на русском языке. Подсчитать количество содержащихся
# в строке гласных букв.

sentence = "В час жаркого весеннего заката на Патриарших прудах появилось двое граждан..."

x = (len([1 for x in list(sentence) if x in ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']]))
print('Кол-во гласных букв: ', x)
