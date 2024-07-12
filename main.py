



def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        file_contents = file_contents.lower()
        character_counts = {}

        words = file_contents.split()
        word_count = len(words)

        for char in file_contents:
            if char.isalpha():
                if char in character_counts:
                    character_counts[char] += 1
                else:
                    character_counts[char] = 1

        character_tuples = list(character_counts.items())
        sorted_characters = sorted(character_tuples, key=lambda item: item[1], reverse=True)
    
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{word_count} words found in the document")

        for character, count in sorted_characters:
            print(f"The '{character}' was found {count} times")
        
        print("--- End report ---")

        
main()






