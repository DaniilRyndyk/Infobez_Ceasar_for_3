from Caesar.Caesar import decrypt_text_caesar


def break_text_caesar(text: str) -> str:
    res = []

    for i in range(32):
        res.append(decrypt_text_caesar(text, i))

    return '\n'.join(res)


print(break_text_caesar('Сткдзф, яфр йвъкцтрдвппрз урргызпкз!'))
