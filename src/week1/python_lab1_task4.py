"""
Task 4 – Text-based Arithmetic Analyzer
--------------------------------------
Create a text-based analyzer that:
1. Counts non-space characters.
2. Counts words.
3. Extracts numbers and computes their sum and average.
Use helper functions:
- count_characters(text)
- count_words(text)
- extract_numbers(text)
- analyze_text(text)
Print formatted summary in main.
"""


def count_characters(text):
    """Count non-space characters in a string."""
    return len(text.replace(" ", ""))
    # TODO: implement
    pass


def count_words(text):
    """Count number of words in a string."""

    return len(text.split())
    # TODO: implement
    pass


def extract_numbers(text):
    """Return list of integers found in text."""
    words = text.replace(",", " ").replace(".", " ").split()
    numbers = []

    for word in words:
        # Handle negative numbers and normal digits
        if word.lstrip("-").isdigit():
            numbers.append(int(word))
    return numbers
    pass


def analyze_text(text):
    """Perform text-based arithmetic analysis."""

    char_count = count_characters(text)
    word_count = count_words(text)
    numbers = extract_numbers(text)
    if numbers:
        total = sum(numbers)
        average = total / len(numbers)
    else:
        total = 0
        average = 0
    return {
        "characters": char_count,
        "words": word_count,
        "numbers": numbers,
        "sum": total,
        "average": average,
    }

    # TODO: call helper functions and compute total, average, etc.
    pass


if __name__ == "__main__":
    # TODO: read input, call analyze_text(), and print results
    inp = input("Input text with numbers ")

    res = analyze_text(inp)

    print("Total Non space characters - ", res["characters"])
    print("Total Word count - ", res["words"])
    print("Numbers found in text - ", res["numbers"])
    print("Sum of these numbers - ", res["sum"])
    print("Avg of numbers - ", res["average"])

    pass
