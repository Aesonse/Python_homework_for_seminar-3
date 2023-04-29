''' Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
В случае с английским алфавитом очки распределяются так:
A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка; 
B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; 
K – 5 очков; J, X – 8 очков; Q, Z – 10 очков. 
А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко;
 Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков;
   Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. 
   Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
   Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

*Пример:*

ноутбук
    12
    '''
price = {}
for letter in 'A, E, I, O, U, L, N, S, T, R, А, В, Е, И, Н, О, Р, С, Т'[::3]:
    price[letter] = 1
for letter in 'D, G, Д, К, Л, М, П, У'[::3]:
    price[letter] = 2
for letter in 'B, C, M, P, Б, Г, Ё, Ь, Я'[::3]:
    price[letter] = 3
for letter in 'F, H, V, W, Y, Й, Ы'[::3]:
    price[letter] = 4
for letter in 'K, Ж, З, Х, Ц, Ч'[::3]:
    price[letter] = 5
for letter in 'J, X, Ш, Э, Ю'[::3]:
    price[letter] = 8
for letter in 'Q, Z, Ф, Щ, Ъ'[::3]:
    price[letter] = 10

word = input('Введите слово: ')
word_cost = 0
for letter in word.upper():
    word_cost += price[letter]
print(f'Слово стоит {word_cost} очков')