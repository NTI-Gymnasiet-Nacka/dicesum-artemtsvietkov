# Dice sum probability calculator
# Författare: Artem Tsvietkov
# Datum: 08.21

from random import randint

def main():
    user_input = [int(x) for x in input("").split(" ")]
    max_value = int(max(user_input))
    min_value = int(min(user_input))

    for x in range(min_value + 1, max_value + 2):
        print(x)
if __name__ == "__main__":
    main()