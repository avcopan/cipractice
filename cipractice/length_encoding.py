def encode(input_string):
    count = 1
    prev = ''
    lst = []
    for character in input_string:
        if character != prev:
            if prev:
                entry = (prev, count)
                lst.append(entry)
            count = 1
            prev = character
        else:
            count += 1
    if not input_string:
        return []
    else:
        entry = (character, count)
        lst.append(entry)
    return lst


def decode(lst):
    q = ''
    for character, count in lst:
        q += character * count
    return q


if __name__ == '__main__':
    s = 'aabbbbccccccdeee'
    e = encode(s)
    d = decode(e)
    print(e)
    print(d)
