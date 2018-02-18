import random

word_list = ['автострада', "бензин", "инопланетянин", "самолет", "библиотека",\
             "шайба", "олимпиада"]
secret_word = random.sample(word_list, 1)[0]
# secret_word = word_list[0]

# users_word = '*' * len(secret_word)
users_word = ['*'] * len(secret_word)


def show_user_word(arg):
    print(''.join(arg))


print(secret_word)
show_user_word(users_word)




















