# def search4vowels():
#     """Выводит гласные, найденные во введенном слове"""
#     vowels = set('aeiou')
#     word = input('Provide a word to search for vowels: ')
#     found = vowels.intersection(set(word))
#     for vowel in found:
#         print(vowel)

# def search4vowels(word):
#     """Выводит гласные, найденные во введенном слове"""
#     vowels = set('aeiou')
#     # word = input('Provide a word to search for vowels: ')
#     found = vowels.intersection(set(word))
#     for vowel in found:
#         print(vowel)

# def search4vowels(word):
#     """Возрващает булевое значение в зависимости
# от присутствия любых гласных"""
#     vowels = set('aeiou')
#     found = vowels.intersection(set(word))
#     return bool(found)

# def search4vowels(word):
#     """Возрващает булевое значение в зависимости
# от присутствия любых гласных"""
#     vowels = set('aeiou')
#     return vowels.intersection(set(word))

# def search4vowels(phrase: str) -> set:
#     """Возрващает булевое значение в зависимости
# от присутствия любых гласных"""
#     vowels = set('aeiou')
#     return vowels.intersection(set(phrase))
# print(search4vowels('Conectikut'))

# def search4letters(phrase: str, letters: str) -> set:
#     """Возрващает множество букв из letters,
# найденных в указанной фразе"""
#     return set(letters).intersection(set(phrase))
#
#
# print(search4letters('Galaxy', 'aeiou'))

# def search4letters(phrase: str, letters: str='aeiou') -> set:
#     """Возрващает множество букв из letters,
# найденных в указанной фразе"""
#     return set(letters).intersection(set(phrase))
#
#
# print(search4letters('Connecticut',))


def search4vowels(word: str) -> set:
    """Возвращает булевое значение в зависимости
    от присутствия любых гласных"""
    vowels = set('aeiou')
    return vowels.intersection(set(word))


def search4letters(phrase: str, letters: str='aeiouzcbdrtfg') -> set:
    """Возвращает множество букв из letters,
    найденных в указанной фразе"""
    return set(letters).intersection(set(phrase))


# print(search4letters(phrase = 'Connecticut',
#                      letters='asjfhlesfkbvsdilkvnjk'))
