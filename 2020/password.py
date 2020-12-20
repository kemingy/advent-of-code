from utils import get_input


def validate_password(strings, rule):
    count = 0
    for string in strings:
        r, char, password = string.strip().split(" ")
        low, high = [int(x) for x in r.split("-")]
        if rule(password, char[0], low, high):
            count += 1

    return count


def check_range(password, char, x, y):
    return x <= password.count(char) <= y


def check_index(password, char, x, y):
    n = len(password)
    count = 0
    if x <= n and password[x - 1] == char:
        count += 1
    if y <= n and password[y - 1] == char:
        count += 1
    return count == 1


if __name__ == "__main__":
    strings = get_input()
    range_count = validate_password(strings, rule=check_range)
    print(f"valid password (range): {range_count}")

    index_count = validate_password(strings, rule=check_index)
    print(f"valid password (index): {index_count}")
