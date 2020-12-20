def get_input():
    data = []
    while True:
        raw = input()
        if raw:
            data.append(raw)
        else:
            break

    return data
