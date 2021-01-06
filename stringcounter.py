text = input("Please enter a string: ")


def diction(x):
    dictionary = {}
    for txt in x:
        dictionary[txt] = 1 + dictionary.get(txt, 0)
    return dictionary


def most_frequent(text):
    txts = [txt.lower() for txt in text if txt.isalpha()]
    dictionary = diction(txts)
    result = []
    for key in dictionary:
        result.append((dictionary[key], key))
    result.sort(reverse=True)
    for count, txt in result:
        print(txt,'=',count, end=' ')

most_frequent(text)