#print("hello world")
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_characters = get_num_characters(text)
    char_report = get_char_report(num_characters)
    print(f"{num_words} words found in the document")
    print(char_report)

def get_char_report(num_characters):
    report = []
    for i in num_characters:
        report.append(f"the '{i}' character was found {num_characters[i]} times")
    return "\n".join(report)

def get_num_characters(text):
    chars_dict = {}
    txt = text.lower()
    for char in txt:
        if char in chars_dict and char.isalpha():
            chars_dict[char] += 1
        elif char.isalpha():
            chars_dict[char] = 1
    return chars_dict

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
