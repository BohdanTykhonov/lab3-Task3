import string

sentence = input("Введіть речення: ")

words = sentence.split()
cleaned_words = [word.strip(string.punctuation) for word in words]

filtered_words = [word for word in cleaned_words if word.endswith("ий")]

print("Слова, які закінчуються на 'ий':", filtered_words)