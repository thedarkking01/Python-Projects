def length_of_last_word(sentence):

    # split sentence into words
    words_list = sentence.split()

    # get the length of the last word
    result = len(words_list[-1])

    # if there is punctuation at the end of the sentence, remove it from the result
    if words_list[-1][-1] in '.,!?;:':
        result = len(words_list[-1].rstrip('.,!?;:'))

    print(result)
length_of_last_word('I love programming')