def reverse_words(string: str):
    word_list = string.split(" ")
    reverse_word_list = []
    for word in word_list:
        reversed_word = word[::-1]
        if not word[len(word)-1].isalnum():
            reversed_word = reversed_word[1::] + reversed_word[0]
        reverse_word_list.append(reversed_word)
    return " ".join(reverse_word_list)


string = input("Enter the string to reverse: ")
reversed_string = reverse_words(string)
print(reversed_string)