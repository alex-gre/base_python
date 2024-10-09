
s = "hello python"
print('variable s = ',s)
print('length s = ',len(s)-1)
print('s[-2:2] = ',s[-2:2])
#string[start:stop:step]
print('s[2:10:2] = ',s[2:10:2])
print('s[:5:3] = ',s[:5:3])
print('s[::2] = ',s[::2])
print('s[::-1] = ',s[::-1])
print('s[::-2] = ',s[::-2])
# строка относится к неизменяемому типу
# если нужно изменить строку нужно завести новую переменную
s2 = 'H'+s[1:]
print("s2 = 'H'+s[1:] => ",s2) 