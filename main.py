import fileinput

def main():
    sum = 0
    for line in fileinput.input(encoding="utf-8"):
        for num in line.split(" "):
            sum += int(num)

    print(sum)

if __name__ == '__main__':
    main()
