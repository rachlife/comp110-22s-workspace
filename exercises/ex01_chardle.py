"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = 730272790

fiveword: str = input("Enter a 5-character word: ")
if len(fiveword) > 5:
    print("Error: Word must contain 5 characters")
single_chr: str = input("Enter a single character: ")
if len(single_chr) > 1:
    print("Error: Character must be a single character.")
print("Searching for " + single_chr + " in " + fiveword)

instances: int = 0
if single_chr == fiveword[0]:
    print(single_chr + " found at index 0")
    instances = instances + 1
if single_chr == fiveword[1]:
    print(single_chr + " found at index 1")
    instances = instances + 1
if single_chr == fiveword[2]:
    print(single_chr + " found at index 2")
    instances = instances + 1
if single_chr == fiveword[3]:
    print(single_chr + " found at index 3")
    instances = instances + 1
if single_chr == fiveword[4]:
    print(single_chr + " found at index 4")
    instances = instances + 1

if instances == 0:
    print("No instances of " + single_chr + " in " + fiveword)
if instances == 1:
    print("1 instance of " + single_chr + " in " + fiveword)

if instances > 1:
    print(str(instances) + " instances of " + single_chr + " found in " + fiveword)