def read_text_file(file_path: str) -> str:
    with open(file_path, 'r', encoding='utf-8') as text_file:
        data = text_file.read()

    return data


def write_text_file(file_path: str, a_string: str) -> None:
    with open(file_path, 'w', encoding='utf-8') as text_file:
        text_file.write(a_string)
