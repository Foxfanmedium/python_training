import random

MAX_ERRORS = 8

word_list = ['автострада', "бензин", "инопланетянин", "самолет", "библиотека",
             "шайба", "олимпиада"]
secret_word = random.sample(word_list, 1)[0]
users_word = ['*'] * len(secret_word)
errors_counter = 0

def show_user_word(arg):
    print(''.join(arg))
    return True

print(secret_word)
# print(users_word)
# print(''.join(users_word))
show_user_word(users_word)    # вызов функции

while True:
    letter = input("введите букву: ").lower() # преобразование букв внижний регистр

    if len(letter) != 1 or not letter.isalpha():
        print("Enter ONE letter, please")
        continue
    # print(ord(letter)) печать только русских букв

    if letter in secret_word:
        for num, char in enumerate(secret_word):
            if char == letter:
                users_word[num] = letter
        if '*' not in users_word:
            print("You are won!!!")
            break

    else:
        errors_counter += 1
        print(f'буквы {letter} в слове нет, ошибок {errors_counter}')
        if errors_counter==MAX_ERRORS:
            print("вы проиграли :(")
            break

    show_user_word(users_word)







