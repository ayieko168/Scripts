import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'q', 'y', 'z']


def generate_dummy_word(number_of_letters=None):

    if number_of_letters == None:
        word_lenth = random.randint(3, 9)
    else:
        word_lenth = number_of_letters
    
    chosen_letters = random.sample(letters, word_lenth)
    word = ''.join(chosen_letters)

    # print(word)
    return word


def generate_dummy_sentence():

    sentence_length = random.randint(4, 7)
    words = []
    starts = ["the", 'a', "it", 'they']

    for _ in range(sentence_length):
        words.append(generate_dummy_word())

    words.insert(0, random.choice(starts))

    sentence = " ".join(words).capitalize()
    # print(sentence)
    return sentence


def generate_dummy_paragraph(number_of_sentences=None):

    if number_of_sentences is not None: paragraph_length = number_of_sentences
    else: paragraph_length = random.randint(1, 50)

    sentences = []

    for _ in range(paragraph_length):
        sentences.append(generate_dummy_sentence())

    paragraph = ". ".join(sentences)
    print(paragraph)

x = generate_dummy_word(16)
print(x)
