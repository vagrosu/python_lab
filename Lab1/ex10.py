def ex10(text):
    words = text.split(' ')
    return len(words)

if __name__ == '__main__':
    text = input("Enter your text: ")
    print(ex10(text))