def find_longest(list_of_strings: list) -> str:
    longest = list_of_strings[0]
    for i in range(1, len(list_of_strings)):
        if len(list_of_strings[i]) > len(longest):
            longest = list_of_strings[i]
            # break the code my turn
        return longest


if __name__ == "__main__":
    print(find_longest(["yellow", "red", "blue", "green"]))
