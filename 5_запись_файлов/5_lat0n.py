# Вариант (5) Программа должна спрашивать у пользователя латинские слова до тех пор, пока он не введёт пустое слово. После этого программа должна записать построчно в файл те из введённых слов, которые с большой вероятностью являются формой 3-го лица пассива настоящего времени (каждое слово на отдельной строчке). [Нерегулярными словами можно не заморачиваться.]

list = []
while True:
    word = input("Введите слово \n")
    print(word.upper())
    if word == "":
        break
    else:
        list.append(word)
print("End.")
print(list)

with open("Text.txt", "w") as f:
    for word in list:
        if word[-3:] == "tur":
            f.write(word + "\n")
