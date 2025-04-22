# You have invented a time-machine which has taken you back to ancient
# Rome. Caeser is impressed with your programming skills and has appointed you
# to be the new information security officer.
# Caeser has ordered you to write a Caeser cipher to prevent Asterix and Obelix
# from reading his emails.
# A Caeser cipher shifts the letters in a message by the value dictated by
# the encryption key. Since Caeser's emails are very important, he wants all
# encryptions to have upper-case output, for example:
# If key = 3 "hello" -> KHOOR If key = 7 "hello" -> OLSSV
# Input will consist of the message to be encrypted and the encryption key.
def caesar_encrypt(text, shift):
    encrypted_text = []
    for char in text:
        if char.isalpha():  # Работаем только с буквами
            shift_base = 97 if char.islower() else 65  # Для 'a' или 'A'
            # Сдвиг символа с учётом зацикливания
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_text.append(encrypted_char.upper())
        else:
            encrypted_text.append(char)  # Не буквы оставляем как есть
    return ''.join(encrypted_text)


print(caesar_encrypt('hello', 3))