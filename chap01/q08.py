def cipher(text):
    result = []
    for char in text:
        code = ord(char)
        if code >= ord("a") and code <= ord("z"):
            code = 219-code
        result.append(chr(code))
    return result

print(cipher(input()))
