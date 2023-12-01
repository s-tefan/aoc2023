def read_input(filename):
    with open(filename) as f:
        return [line.rstrip() for line in f.readlines()]

digits = "0123456789"


def partone(lines):
    cal_val_sum = 0
    for line in lines:
        rline = reversed(line)
        for c in line:
            if c in digits:
                break
        digs = c
        for c in rline:
            if c in digits:
                break
        digs += c
        cal_val_sum += int(digs)
    return cal_val_sum

print(partone(read_input("input.txt")))
