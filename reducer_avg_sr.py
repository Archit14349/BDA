import sys

def read_input(file):
    for line in file:
        yield line.strip().split("\t")

def main():
    current_player = None
    total_sr = 0
    count = 0

    data = read_input(sys.stdin)

    for fields in data:
        player, strike_rate = fields
        strike_rate = float(strike_rate)

        if current_player == player:
            total_sr += strike_rate
            count += 1
        else:
            if current_player:
                average_sr = total_sr / count
                print(f"{current_player}\t{average_sr}")
            current_player = player
            total_sr = strike_rate
            count = 1

    if current_player == player:
        average_sr = total_sr / count
        print(f"{current_player}\t{average_sr}")

if __name__ == "__main__":
    main()
