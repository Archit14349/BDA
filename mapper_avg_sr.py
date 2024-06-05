import sys
import csv

def read_input(file):
    for line in csv.reader(file):
        yield line

def main():
    data = read_input(sys.stdin)
    for fields in data:
        try:
            if fields[0] == "Unnamed: 0":
                continue  # Skip the header line
            player = fields[1]
            strike_rate = float(fields[10])
            print(f"{player}\t{strike_rate}")
        except IndexError:
            continue
        except ValueError:
            continue

if __name__ == "__main__":
    main()
