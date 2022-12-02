def main():
    path = "input_1.txt"

    high = 0
    count = 0
    with open(path) as f:
        for line in f.readlines():
            line = line.strip()
            if line:
                count += int(line)
            else:
                if count > high:
                    high = count
                count = 0
        if count > high:
            high = count
    print(high)

if __name__ == "__main__":
    main()
