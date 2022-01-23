def encrypt(sequence: bytes, shift: int) -> bytes:
    new_seq = [(x + shift) % 256 for x in sequence]
    return bytes(new_seq)


def decrypt(sequence: bytes, shift: int) -> bytes:
    return encrypt(sequence, -shift)


def encrypt_file(filename, shift, save_path=None):
    with open(filename, 'rb') as f:
        seq = f.read()

    seq = encrypt(seq, shift)

    if save_path is None:
        with open(filename, 'wb') as f:
            f.write(seq)
    else:
        with open(save_path, 'wb') as f:
            f.write(seq)


def decrypt_file(filename, shift, save_path=None):
    encrypt_file(filename, -shift, save_path)


if __name__ == '__main__':
    encrypt_file('3.txt', 3)
