import random

DICE_ART = {
        1: [
            "┌─────────┐",
            "│         │",
            "│    ●    │",
            "│         │",
            "└─────────┘",
        ],
        2: [
            "┌─────────┐",
            "│  ●      │",
            "│         │",
            "│      ●  │",
            "└─────────┘",
        ],
        3: [
            "┌─────────┐",
            "│  ●      │",
            "│    ●    │",
            "│      ●  │",
            "└─────────┘",
        ],
        4: [
            "┌─────────┐",
            "│  ●   ●  │",
            "│         │",
            "│  ●   ●  │",
            "└─────────┘",
        ],
        5: [
            "┌─────────┐",
            "│  ●   ●  │",
            "│    ●    │",
            "│  ●   ●  │",
            "└─────────┘",
        ],
        6: [
            "┌─────────┐",
            "│  ●   ●  │",
            "│  ●   ●  │",
            "│  ●   ●  │",
            "└─────────┘",
        ],
    }

def roll_dice(possible_moves):

    num_dice = int(input('Enter number of dice you want to roll [1-6] : '))
    dice_faces_lst = [random.choice(possible_moves) for i in range(num_dice)]
    return dice_faces_lst

def generate_dice_diagram(dice_faces):

    for dice_face in dice_faces:
        for line in DICE_ART[dice_face]:
            print(line)

def main():

    # possible moves in a die
    possible_moves = [1, 2, 3, 4, 5, 6]


    # roll dice
    dice_faces = roll_dice(possible_moves)

    # generate dice faces
    generate_dice_diagram(dice_faces)


if __name__ == '__main__':
    main()