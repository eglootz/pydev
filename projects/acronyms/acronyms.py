
# getting a phrase
phrase = input("Enter a Phrase: ")

# splitting the phrase into single words and putting them in a list called words
words = phrase.split()

# setting an empty variable for the acronym
acronym = ""

# getting the first letter of each word (in list words), converting it into uppercase and adding it to the acronym
for word in words:
    acronym = acronym + word[0].upper()
print(f"Phrase: {phrase} \nAcronym: {acronym}")
