from collections import defaultdict


def read_book(book: str) -> str:
    content = None
    with open(book) as f:
        content = f.read()
    return content


def calc_word_count(text: str) -> int:
    return len(text.split())


def calc_character_dict(text: str) -> int:
    character_dict = defaultdict(lambda: 0)
    for c in text.lower():
        if c not in character_dict:
            character_dict[c] = 0
        character_dict[c] += 1
    return character_dict


def print_report(path: str, word_count: int, character_dict: dict):
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document\n")
    sorted_dict = {k: v for k, v in sorted(character_dict.items(), key=lambda item: item[1], reverse=True)}
    for key in sorted_dict:
        print(f"The {repr(key)} character was found {sorted_dict[key]} times")


def main():
    path = "books/frankenstein.txt"
    content = read_book(path)    
    word_count = calc_word_count(content)
    character_dict = calc_character_dict(content)
    print_report(path, word_count, character_dict)


if __name__ == "__main__":
    main()
