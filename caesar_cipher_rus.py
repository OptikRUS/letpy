def encrypt(s, k):
    letters = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    message = s.upper()
    res = ''
    for letter in message:
        idx = letters.find(letter)
        if idx == -1:
            res += letter
        else:
            res += letters[(idx + k) % 33]
    return res