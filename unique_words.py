import string

def count_unique_words(great_gatsby_plain_text):
    # Reads a text file and counts unique words
    try:
        with open(great_gatsby_plain_text, "r", encoding="utf-8") as file:
            text = file.read().lower()  # Convert to lowercase
            text = text.translate(str.maketrans("", "", string.punctuation))  # Remove punctuation
            words = set(text.split())  # Convert to a set to get unique words
            return len(words)
    except FileNotFoundError:
        print(f"Error: {great_gatsby_plain_text} not found.")
        return 0

# File names for the books
book1 = "great_gatsby_plain_text"
book2 = "tales_of_secret_egypt_plain_text"

# Count unique words
unique_words_book1 = count_unique_words(book1)
unique_words_book2 = count_unique_words(book2)

# Display results
print(f"Unique words in {book1}: {unique_words_book1}")
print(f"Unique words in {book2}: {unique_words_book2}")

# Compare unique word counts
if unique_words_book1 > unique_words_book2:
    print(f"{book1} has more unique words.")
elif unique_words_book1 < unique_words_book2:
    print(f"{book2} has more unique words.")
else:
    print("Both books have the same number of unique words.")