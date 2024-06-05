import sys

def read_input(file):
    for line in file:
        yield line.strip().split("\t")

def main():
    current_player = None
    total_runs = 0

    data = read_input(sys.stdin)

    for fields in data:
        player, runs = fields
        runs = int(runs)

        if current_player == player:
            total_runs += runs
        else:
            if current_player:
                print(f"{current_player}\t{total_runs}")
            current_player = player
            total_runs = runs

    if current_player == player:
        print(f"{current_player}\t{total_runs}")

if __name__ == "__main__":
    main()
