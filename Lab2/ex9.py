import copy


def ex9(spectators):
    cant_see_list = []
    max_spectators = copy.deepcopy(spectators)
    for i in range(1, len(spectators)):
        for j in range(len(spectators[i])):
            if spectators[i][j] > max_spectators[i - 1][j]:
                max_spectators[i][j] = spectators[i][j]
            else:
                max_spectators[i][j] = max_spectators[i - 1][j]

    for i in range(1, len(spectators)):
        for j in range(len(spectators[i])):
            if spectators[i][j] < max_spectators[i][j] or spectators[i][j] == max_spectators[i - 1][j]:
                cant_see_list.append((i, j))

    print(max_spectators)
    return cant_see_list


if __name__ == '__main__':
    spectators = [[1, 2, 3, 2, 1, 1],
                  [2, 4, 4, 3, 7, 2],
                  [5, 5, 2, 5, 6, 4],
                  [6, 6, 7, 6, 7, 5]]
    print(ex9(spectators))
