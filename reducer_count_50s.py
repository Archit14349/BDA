import sys

def read_input(file):
    for line in file:
        yield line.strip().split("\t")

def main():
    current_player = None
    total_fifties = 0

    data = read_input(sys.stdin)

    for fields in data:
        player, fifties = fields
        fifties = int(fifties)

        if current_player == player:
            total_fifties += fifties
        else:
            if current_player:
                print(f"{current_player}\t{total_fifties}")
            current_player = player
            total_fifties = fifties

    if current_player == player:
        print(f"{current_player}\t{total_fifties}")

if __name__ == "__main__":
    main()
