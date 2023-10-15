def ex9(text):
    frequency = {}
    for char in text:
        if char.isalpha():
            if char.lower() in frequency:
                frequency[char.lower()] += 1
            else:
                frequency[char.lower()] = 1

    return max(frequency, key=frequency.get)

if __name__ == '__main__':
    text = input("Enter text: ")
    print(ex9(text))