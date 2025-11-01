"""
Task 3 – Function with Combined Logic
------------------------------------
Write a function `analyze_sentence(text)` that returns:
1. total character count (len)
2. word count (split)
3. whether it contains the word "Python" (case-insensitive)
Return results as a tuple and print summary in main.
"""

def analyze_sentence(text):
    """Return length, word count, and whether 'Python' appears in text."""
    var = "python" in text.lower()
    return len(text), len(text.split()), var
    pass

if __name__ == "__main__":
    # TODO: read sentence from input, call function, and print results
    inp = input("Give input : ")

    leng, word, isPython = analyze_sentence(inp)
    print("Total characters : ",leng)
    print("Total words : ",word)
    print("If Python : ",isPython)
    pass
