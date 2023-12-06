import numpy as np

alpha = 0.5  # learning rate
gamma = 0.75  # discount factor
decay = 0.99  # exploration rate

rows, cols = 7, 10
wind = np.array([0, 0, 0, 1, 1, 1, 2, 2, 1, 0])

q_table = np.zeros((rows, cols, 4))

start = (3, 0)
end = (3, 7)

actions = {'up': (-1, 0), 'right': (0, 1), 'down': (1, 0), 'left': (0, -1)}


def compute_next_state(current_state, action):
    next_state = (current_state[0] + actions[action][0], current_state[1] + actions[action][1])

    if 3 <= current_state[1] <= 8:
        next_state = (max(min(next_state[0] - wind[current_state[1]], rows - 1), 0), next_state[1])

    next_state = (max(min(next_state[0], rows - 1), 0), max(min(next_state[1], cols - 1), 0))

    return next_state


def q_learning(episodes=10000):
    epsilon = 1
    for episode in range(episodes):
        current_state = start

        while current_state != end:
            if np.random.random() < epsilon:
                action = np.random.choice(list(actions.keys()))
            else:
                action = list(actions.keys())[np.argmax(q_table[current_state])]

            next_state = compute_next_state(current_state, action)

            action_index = list(actions.keys()).index(action)
            current_q_value = q_table[current_state][action_index]
            max_next_q = np.max(q_table[next_state])
            reward = -1
            updated_q_value = alpha * (reward + gamma * max_next_q - current_q_value)
            q_table[current_state][action_index] += updated_q_value

            current_state = next_state

        epsilon *= decay


def get_policy(table):
    action_arrows = ['↑', '→', '↓', '←']

    policy = np.chararray(table.shape[:2], unicode=True)
    for i in range(table.shape[0]):
        for j in range(table.shape[1]):
            best_action_index = np.argmax(table[i, j])
            policy[i, j] = action_arrows[best_action_index]
    return policy


if __name__ == '__main__':
    q_learning()
    print(q_table)
    print(get_policy(q_table))
