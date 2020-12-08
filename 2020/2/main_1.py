def read_policy(raw_policy):
    raw_range, _, password_char = raw_policy.partition(" ")
    low, _, high = raw_range.partition("-")
    return (int(low), int(high)), password_char


if __name__ == '__main__':
    with open('input', 'r') as input:
        input_list = [line for line in input]

    count = 0
    for line in input_list:
        policy, _, password = line.partition(": ")
        range_tuple, password_char = read_policy(policy)
        if range_tuple[0] <= password.count(password_char) <= range_tuple[1]:
            print(policy)
            count += 1

    print(count)
