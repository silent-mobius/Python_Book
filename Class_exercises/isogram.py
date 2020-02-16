def is_isogram(data):
    data = data.lower()

    for ch in data:
        if (ch == ' ') or (ch == '-'):
            continue

        if data.count(ch) > 1:
            return False

    return True