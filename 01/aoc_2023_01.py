def read_input(filename):
    with open(filename) as f:
        return [line.rstrip() for line in f.readlines()]

digits = "0123456789"
textdigits = ['zero','one','two','three','four','five','six','seven','eight','nine']


def partone(lines):
    cal_val_sum = 0
    for line in lines:
        line_str = str(line)
        k = float('inf')     
        for n, d in enumerate(digits):
            m = line_str.find(d)
            if m >=0 and m < k:
                dig1 = n
                k = m
        for n, d in enumerate(textdigits):
            m = line_str.find(d)
            if m >=0 and m < k:
                dig1 = n
                k = m

        k = -1     
        for n, d in enumerate(digits):
            m = line_str.rfind(d)
            if m >=0 and m > k:
                dig2 = n
                k = m
        for n, d in enumerate(textdigits):
            m = line_str.rfind(d)
            if m >=0 and m > k:
                dig2 = n
                k = m

        cal_val_sum += 10*dig1+dig2
    return cal_val_sum

print(partone(read_input("input.txt")))
