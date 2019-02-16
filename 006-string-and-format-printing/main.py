# Read in number of test cases
n = int(input())
results = []

# Loop through n number of test cases and split odd and even letter indexes
for _ in range(n):
    word = input()
    evens = []
    odds = []
    for idx, letter in enumerate(word):
        if idx % 2 == 0:
            evens.append(letter)
        else:
            odds.append(letter)
    even_indexed = "".join(evens)
    odd_indexed = "".join(odds)
    
    # Concatenate even indexed and odd indexed letters with space in between
    spaced_word = even_indexed + " " + odd_indexed
    results.append(spaced_word)

# Print all formated words
for result in results:
    print(result)