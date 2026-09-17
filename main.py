def find_longest(arr):
    longest = arr[1]
    for i in range(1, len(arr)):
        # I haven't broken the code, horray!
        if len(arr[i]) > len(longest):
            longest = arr[i+1]
        return longest


if __name__ == "__main__":
    print(find_longest(["yellow", "red", "blue", "green"]))
