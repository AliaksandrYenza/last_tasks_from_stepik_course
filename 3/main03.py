def input_list():
    n = int(input())
    list_words = []
    for i in range((n)):
        x = input().lower()
        if x not in list_words:
            list_words.append(x)

    print((list_words))
    return (list_words)

def input_phrase(list_words):
    m = int(input())
    list_phrase = []
    for i in range((m)):
        x = input().lower().split()
        for i in x:
            if i not in list_words and i not in list_phrase:
                list_phrase.append(i)

    print(list_phrase)









if __name__ == '__main__':
    list = input_list()
    input_phrase(list)