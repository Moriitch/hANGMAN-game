import random

def get_list():
    word_list = ["кот", "собака", "мышь", "крокодил", "ящерица", "змея", "заяц", "лягушка", "черепаха", "лиса",
                 "волк", "слон", "тигр", "шиншила", "кролик", "бык", "бизон", "баран", "корова", "медведь", "кабан",
                 "страус", "лев", "зебра", "жираф", "бегемот", "пингвин", "игуана", "ёж", "олень", "лось", "ленивец",
                 "капибара", "цапля", "крыса", "суслик", "ягуар", "леопард", "крот", "енот", "хомяк", "свинья"]
    a = random.choice(word_list)
    word = a.upper()
    return word

def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]

def is_valid(letter):
    low_letters = 'абвгдеёжзиклмнопрстуфхцчшщъыьэюя'
    c = 0
    for i in letter:
        if i.lower() in low_letters:
            c += 1
    if c == len(letter):
        return True
    else:
        return False

def play(word):
    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False  # сигнальная метка
    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов
    tries = 6  # количество попыток
    print("Let's play, HANGMAN!!!!!!! :))")
    print(display_hangman(tries))
    print(word_completion)
    print("В загаданном слове ", len(word_completion), ' букв ')
    while tries != 0:
        letter = input("Введите угадываемую букву ИЛИ слово: ")
        letter = letter.upper()
        if is_valid(letter) == True:
            if len(letter) == 1:
                if letter in guessed_letters:
                    print('Такая буква уже была :(')
                    tries -= 1
                    print("Количество оставшихся попыток: ", tries)
                    if tries == 0:
                        break
                    else:
                        print(display_hangman(tries))
                        continue
                elif letter not in guessed_letters and letter not in word:
                    guessed_letters.append(letter)
                    print("К сожалению, такой буквы нет в загаданном слове :(")
                    tries -= 1
                    print("Количество оставшихся попыток: ", tries)
                    if tries == 0:
                        break
                    else:
                        print(display_hangman(tries))
                        continue
                elif letter not in guessed_letters and letter in word:
                    guessed_letters.append(letter)
                    print("Ура! Эта буква есть в загаданном слове :)")
                    word_completion = ''
                    for i in word:
                        if i != letter and i not in guessed_letters:
                            word_completion += "_"
                        elif i != letter and i in guessed_letters:
                            word_completion += i
                        elif i == letter:
                            word_completion += letter
                    print(word_completion)
                    tries -= 1
                    print("Количество оставшихся попыток: ", tries)
                    if tries == 0:
                        break
                    else:
                        print(display_hangman(tries))
                        continue
            elif len(letter) >= 2:
                if letter in guessed_words:
                    print('Такое слово уже было :(')
                    print(letter)
                    tries -= 1
                    print("Количество оставшихся попыток: ", tries)
                    if tries == 0:
                        break
                    else:
                        print(display_hangman(tries))
                        continue
                elif letter == word:
                    guessed_words.append(letter)
                    break
                else:
                    guessed_words.append(letter)
                    print("К сожалению, это не загаданное слово :(")
                    tries -= 1
                    print("Количество оставшихся попыток: ", tries)
                    if tries == 0:
                        break
                    else:
                        print(display_hangman(tries))
                        continue
        else:
            print("Пожалуйста, введите БУКВУ или СЛОВО")
            continue
    if letter == word:
        print("УРА!! ВЫ УГАДАЛИ СЛОВО!!")
    elif word_completion == word:
        print("УРА!! ВЫ УГАДАЛИ СЛОВО!!")
    elif word_completion != word:
        print(display_hangman(tries))
        print('К сожалению, вы не угадали :(( Слово, которое было загадано: ', word)
    elif letter != word:
        print(display_hangman(tries))
        print('К сожалению, вы не угадали :(( Слово, которое было загадано: ', word)

gaym = True
while gaym == True:
    a = play(get_list())
    print("Wanna PLAY aGAYn??? ;)")
    print('д - да, н - нет')
    answ = input()
    if answ == 'д':
        continue
    else:
        break

# :)