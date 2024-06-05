import sys

def read_input(file):
    for line in file:
        yield line.strip().split("\t")

def main():
    current_player = None
    total_fours = 0
    total_sixes = 0

    data = read_input(sys.stdin)

    for fields in data:
        player, fours, sixes = fields
        fours = int(fours)
        sixes = int(sixes)

        if current_player == player:
            total_fours += fours
            total_sixes += sixes
        else:
            if current_player:
                print(f"{current_player}\t{total_fours}\t{total_sixes}")
            current_player = player
            total_fours = fours
            total_sixes = sixes

    if current_player == player:
        print(f"{current_player}\t{total_fours}\t{total_sixes}")

if __name__ == "__main__":
    main()
