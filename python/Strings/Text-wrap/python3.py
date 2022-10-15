
def wrap(string, max_width):
    new_str=""
    for i,char in enumerate(string):
        new_str+=char
        if (i+1)% max_width == 0:
            new_str+='\n'
    return new_str
