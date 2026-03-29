def is_duplicate(word):
    """
    inputs strings from the user until the user enters 'quit'
    :return: boolean
    """
words = []
_is_duplicate = False
while True:

    word =  str(input('Enter string [quit to exit]: '))
    if word == 'quit':
        break
    words.append(word)

for word in words:
    if words.count(word) > 1:
        _is_duplicate = True
        break
print(f"Are there duplicated here {words} ? {_is_duplicate}")
