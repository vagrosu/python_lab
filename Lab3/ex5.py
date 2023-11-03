import re


def validate_dict(rules, dictionary):
    rules_dict = {rule[0]: rule[1:] for rule in rules}

    for key, val in dictionary.items():
        if key not in rules_dict:
            return False

        prefix, middle, suffix = rules_dict[key]

        if not val.startswith(prefix) or not val.endswith(prefix) or not re.search(f'^.+{middle}.+$', val):
            return False

    return True


if __name__ == '__main__':
    print(validate_dict({("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}, {"key1": "come inside, it's too cold out", "key3": "this is not valid"}))