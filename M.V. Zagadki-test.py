first_quest = ' №1 из 5. Тело деревянное, одежда рваная, не ест, не пьет, огород стережет.\nA. Пиноккио. \nБ. Огородник. \nB. Пугало.'
second_quest = ' №2 из 5. морях и реках обитает, но часто по небу летает, а как наскучит ей летать, на землю падает опять. \nА. Пеликан. \nБ. Вода. \nВ. Самолет-амфибия'
therd_quest = ' №3 из 5. Пришла без красок и без кисти и перекрасила все листья. \nA. Девочка, занимающаяся граффити. \nБ. Осень. \nB. Коза'
four_quest = ' №4 из 5. Он пыхтит, как паровоз, важно кверху держит нос, пошумит,остепенится, пригласит чайку напиться. \nA. Шеф. \nБ. Сосед-пенсионер. \nB. Чайник.'
five_quest = ' №5 из 5. Под водой живет народ, ходит задом наперед. \nA. Дайверы. \nБ. Водяной и его слуги. \nB. Раки.'

zagadka_otvet = {first_quest : 'в', second_quest : 'а', therd_quest : 'б', four_quest :'в', five_quest :'в'}

prav_otvet = 0
neprav_otvet = 0

print('Угадайте 5 загадок! Выберите и введите вариант ответа(А,Б,В): ')
print(first_quest)
otvet_user = input().lower()
if otvet_user == 'в':
    print('Угадал!')
    prav_otvet += 1
else:
    print('Не угадал :(')
    neprav_otvet += 1
    
print(second_quest)
otvet_user = input().lower()
if otvet_user == 'а':
    print('Угадал!')
    prav_otvet += 1
else:
    print('Не угадал :(')
    neprav_otvet += 1
    
print(therd_quest)
otvet_user = input().lower()
if otvet_user == 'б':
    print('Угадал!')
    prav_otvet += 1
else:
    print('Не угадал :(')
    neprav_otvet += 1

print(four_quest)
otvet_user = input().lower()
if otvet_user == 'в':
    print('Угадал!')
    prav_otvet += 1
else:
    print('Не угадал :(')
    neprav_otvet += 1
    
print(five_quest)
otvet_user = input().lower()
if otvet_user == 'в':
    print('Угадал!')
    prav_otvet += 1
else:
    print('Не угадал :(')
    neprav_otvet += 1
    
    
    
print('Правильных ответов: ', prav_otvet)
if neprav_otvet > 0:
    print('Неправильных ответов: ', neprav_otvet)
else:
    print('Поздравляю, Вы большая Умница! Не правильных ответов: 0')
input('Чтобы выйти нажмите ENTER')

