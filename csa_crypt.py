import itertools


def solve_cryptarithmetic(words, result):
    unique_chars = set("".join(words) + result)
    if len(unique_chars) > 10:
        print("Too many unique letters, cannot solve.")
        return None
    unique_chars = list(unique_chars)


    for perm in itertools.permutations(range(10), len(unique_chars)):
        mapping = dict(zip(unique_chars, perm))
        if any(mapping[word[0]] == 0 for word in words + [result]):
            continue
        words_nums = [sum(mapping[char] * (10 ** i) for i, char in enumerate(word[::-1])) for word in words]
        result_num = sum(mapping[char] * (10 ** i) for i, char in enumerate(result[::-1]))
        if sum(words_nums) == result_num:
            print("\nSolution Found!")
            for char, num in mapping.items():
                print(f"{char} = {num}")
            return mapping
    print("\nNo solution found.")
    return None


if __name__ == "__main__":
    words = input("Enter words (comma-separated): ").split(",")
    result = input("Enter result word: ")
    solve_cryptarithmetic(words, result)

