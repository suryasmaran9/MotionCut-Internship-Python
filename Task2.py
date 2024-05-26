def count_words(text):
    if not text.strip():
        return 0

    words = text.split()

    return len(words)

def main():

    print("Welcome to the Word Counter!")
    print("Enter a sentence or paragraph to count the number of words.")

    input_text = input("Enter your text: ")

    word_count = count_words(input_text)

    print(f"Number of words: {word_count}")

if __name__ == "__main__":
    main()
