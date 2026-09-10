def find_longest(input_list: list) -> object:
    longest = input_list[1]
    for i in range(0, len(input_list)):
        if len(input_list[i]) > len(longest):
            longest = input_list[i]
    return longest


if __name__ == "__main__":
    print(find_longest(["yellow", "red", "blue", "green"]))
