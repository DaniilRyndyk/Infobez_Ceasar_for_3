def text_caesar(text: str, shift: int) -> str:
    alphabet_lower = 'йцукенгшщзхъфывапролджэячсмитьбю'
    alphabet_upper = alphabet_lower.upper()

    ord_first_letter_lower = ord('а')
    ord_first_letter_upper = ord('А')

    new_text = ''

    for i in text:
        if i in alphabet_lower:
            new_text += chr(((ord(i) - ord_first_letter_lower + shift) % 32) + ord_first_letter_lower)
        elif i in alphabet_upper:
            new_text += chr(((ord(i) - ord_first_letter_upper + shift) % 32) + ord_first_letter_upper)
        else:
            new_text += i

    return new_text


def decrypt_text_caesar(text: str, shift: int) -> str:
    return text_caesar(text, -shift)


if __name__ == '__main__':
    print(text_caesar('Привет, это зашифрованное сообщение!', 2))



