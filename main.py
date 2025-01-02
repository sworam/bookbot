def main():
    with open("books/frankenstein.txt") as f:
        word_count = 0
        for line in f:
            word_count += len(line.split())
        print(word_count)

    with open("books/frankenstein.txt") as f:
        character_dict = dict()
        for c in f.read().lower():
            if c not in character_dict:
                character_dict[c] = 0
            character_dict[c] += 1
        
        for key in character_dict.keys():
            print(f"{key}: {character_dict[key]}")

if __name__ == "__main__":
    main()
