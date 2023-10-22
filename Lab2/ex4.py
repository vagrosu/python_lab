def compose(notes, moves, start_pos):
    result = [notes[start_pos]]
    index = start_pos
    for move in moves:
        index += move
        if index >= len(notes):
            index = index - len(notes)
        elif index < 0:
            index = index + len(notes)
        result.append(notes[index])

    return result


if __name__ == '__main__':
    print(compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2, 1, 1, 1, 1, 2, 4, 5], 2))