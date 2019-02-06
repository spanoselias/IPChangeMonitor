
def write(filename, entry):
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(entry)