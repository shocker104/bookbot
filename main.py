from stats import words_count, char_count, sort_character
import sys

def get_book_text (book):
    with open(book) as f:
        book_content = f.read()        
        return book_content

def main():
    if len(sys.argv)!=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        parte=[]
        num_words = words_count(get_book_text(sys.argv[1]))
        char_num = char_count(get_book_text(sys.argv[1]))
        char_list = sort_character(char_num)
        
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for pair in char_list:
            del parte[:]
            for single in pair:
                parte.append(str(pair[single]))
            if parte[0].isalpha():
                line = ": ".join(parte)
                print(f"{line}")

    
        
main()