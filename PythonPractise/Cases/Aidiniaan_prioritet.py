a = ((s >= '0') and (s <= '9')) or (s == '.')#Для сохранения приоритетов операций
notA = not(A)
#Также нужно написать пример в ручную,саму отрицание применить
notA = (not (s >= '0') or not (s <= '9')) and not(a <= '9')
