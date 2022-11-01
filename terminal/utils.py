def truncate(text: str, padding_len: int, max_len:int):
    result = ''
    i = 0
    while i+max_len < len(text):
        result += text[i:i+max_len].strip() +'\n' +' ' * padding_len
        i+= max_len

    result += text[i:].strip() +'\n'
    return result