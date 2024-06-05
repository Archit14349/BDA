import sys

def read_input(file):
    for line in file:
        yield line.strip().split("\t")

def main():
    current_player = None
    highest_score = 0

    data = read_input(sys.stdin)

    for fields in data:
        player, score = fields
        score = int(score)

        if current_player == player:
            if score > highest_score:
                highest_score = score
        else:
            if current_player:
                print(f"{current_player}\t{highest_score}")
            current_player = player
            highest_score = score

    if current_player == player:
        print(f"{current_player}\t{highest_score}")

if __name__ == "__main__":
    main()
