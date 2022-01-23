from Caesar.Caesar_files import decrypt_file


def break_files_caesar(filename: str):
    for i in range(256):
        decrypt_file(filename, i, f'files/{filename}_shift{i}')

break_files_caesar('3.txt')
