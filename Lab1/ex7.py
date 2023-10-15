def ex7(text):
    chars = [*text]
    found = False
    num = 0
    for char in chars:
        if char.isnumeric():
            num = num * 10 + (int(char) - int('0'))
            found = True
        elif found:
            break

    return num

if __name__ == '__main__':
    input_text = input("Enter your text: ")
    print(ex7(input_text))