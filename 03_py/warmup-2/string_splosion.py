def string_splosion(str):
    x = ""
    for i in range(len(str)):
        x += str[:i+1]
    return x
