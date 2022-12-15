#!/usr/bin/env python3

def main():
    BOXES = [(20, 12, 4), (40, 20, 10), (80, 40, 40), (150, 75, 60)]
    BOXES_TRAD = ['A', 'B', 'C', 'D', 'E']
    dims = []
    for _ in range(3):
        temp = input()
        dims.append(int(temp))
    dims.sort(reverse=True)
    box_index = 4
    for i in range(len(BOXES)):
        funciona = True
        for j in range(len(dims)):
            if dims[j] > BOXES[i][j]:
                funciona = False
                break
        if funciona:
            box_index = i
            break
    print(BOXES_TRAD[box_index])

if __name__ == "__main__":
    main()