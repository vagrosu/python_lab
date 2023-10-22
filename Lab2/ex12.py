def ex12(words):
    rhymes = {}
    
    for word in words:
        rhyme = word[-2:]

        if rhyme not in rhymes:
            rhymes[rhyme] = []
        rhymes[rhyme].append(word)

    return list(rhymes.values())


if __name__ == '__main__':
    print(ex12(['ana', 'banana', 'carte', 'arme', 'parte']))