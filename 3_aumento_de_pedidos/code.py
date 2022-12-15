#!/usr/bin/env python3

def main():
    data = input().split(',')
    aumentos = 0
    for i in range(1, len(data)):
        if int(data[i-1]) < int(data[i]):
            aumentos = aumentos + 1
    print(aumentos)

if __name__ == "__main__":
    main()