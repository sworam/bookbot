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


def main():
    content = read_book("books/frankenstein.txt")    
    word_count = calc_word_count(content)
    print(word_count)

    character_dict = calc_character_dict(content)    
    for key in character_dict:
        print(f"{key}: {character_dict[key]}")

if __name__ == "__main__":
    main()
