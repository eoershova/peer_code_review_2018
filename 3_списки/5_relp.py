#Вам нужно написать программу, которая спрашивает у пользователя слово и, в зависимости от варианта, печатает тот или иной набор строчек. Вместо текстового описания лучше для каждого варианта приведем примеры того, что должно появиться на экране в результате работы программы, если пользователь введёт слово "abracadabra". (Соответственно, если пользователь введёт другое слово, должна получиться другая, но аналогичная картинка.)
# Вариант (5) 
# a
# ra
# bra
# abra
# dabra
# adabra
# cadabra
# acadabra
# racadabra
# bracadabra
# abracadabra

x = input("Введите слово: ")
letters = []
for j in reversed(x):
    letters.append(j)
    print(*letters[::-1])
    
