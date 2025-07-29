import sys
from stats import get_num_words, get_chars_dict

def get_book_text(path):
    with open(path) as f:
        return f.read()
          
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    #print(f"{num_words} words found in the document")
    report = get_chars_dict(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for entry in report:
        print(f"{entry['char']}: {entry['num']}")
    print("============= END ===============")
 
main()