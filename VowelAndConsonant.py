text = input("Enter a string: ")

vowel = 0
char = len(text)

vowels = "aeiouAEIOU"

for ch in text:
    if ch in vowels:
        vowel_count += 1

print("Total characters:", char)
print("Total vowels:", vowel)
print("Total consonants", char-vowel)
