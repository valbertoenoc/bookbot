def get_num_words(text: str):
    return len(text.split())


def get_char_count(text: str):
    words = text.split()
    char_count: dict[str, int] = {}

    for word in words:
        for char in word:
            lower_char = char.lower()
            char_count[lower_char] = char_count.get(lower_char, 0) + 1

    return char_count


def get_sorted_char_count(char_count: dict[str, int]):
    sorted_list_char_count: list[dict[str, str | int]] = [
        {"char": char, "count": count} for char, count in char_count.items()
    ]

    sorted_list_char_count.sort(reverse=True, key=lambda x: x["count"])

    return sorted_list_char_count
