import math

def read_input(filename):
    with open(filename) as f:
        return [line.rstrip() for line in f.readlines()]


def partone(lines):
    no_lines = len(lines)
    s = 0
    for line_nr, line in enumerate(lines):
        line_length = len(line)
        k = 0
        while k < line_length:
            m = k
            while m < line_length and line[k:m+1].isdigit():
                m += 1
            digits = line[k:m]
            if digits:
                neighbors = ( (line[k-1] if k >=1 else "") 
                             + (line[m] if m < line_length else "")
                             + (lines[line_nr - 1][max(k-1, 0):min(m+1,line_length)] if line_nr >= 1 else "")
                             + (lines[line_nr + 1][max(k-1, 0):min(m+1,line_length)] if line_nr < len(lines) - 1 else "")
                )

                if not all(x == "." for x in neighbors):
                    s += int(digits)
            k = m + 1
    return s                             

def parttwo(lines):
    no_lines = len(lines)
    s = 0
    for line_nr, line in enumerate(lines):
        line_length = len(line)
        flag = True
        ll = line
        k = -1
        while ll:
            kk = ll.find("*")
            if kk < 0:
                ll = ""
            else:
                k += (1 + kk)
                numbers = []
                if k > 0 and line[k-1].isdigit():
                    m = k - 1
                    while m >= 0 and line[m: k].isdigit():
                        m -= 1
                    numbers.append(int(line[m+1: k]))
                if k < line_length - 1 and line[k+1].isdigit():
                    m = k + 1
                    while m < line_length and line[k+1: m+1].isdigit():
                        m += 1
                    numbers.append(int(line[k+1: m]))
                if line_nr >= 1 :
                    other_line = lines[line_nr - 1]
                    if other_line[k].isdigit():
                        m = k
                        m1 = m
                        m2 = m
                        while m >= 0 and other_line[m:k+1].isdigit():
                            m1 = m 
                            m -= 1
                        m = k
                        while m < line_length and other_line[k:m+1].isdigit():
                            m2 = m
                            m += 1
                        numbers.append(int(other_line[m1:m2+1]))
                    else:
                        if other_line[k-1].isdigit():
                            m = k - 1
                            m1 = m
                            while m >= 0 and other_line[m:k].isdigit():
                                m1 = m 
                                m -= 1
                            numbers.append(int(other_line[m1:k]))
                        if other_line[k+1].isdigit():
                            m = k + 1
                            m2 = m
                            while m <= line_length and other_line[k+1:m+1].isdigit():
                                m2 = m 
                                m += 1
                            numbers.append(int(other_line[k+1:m2+1]))
                if line_nr < no_lines - 1 :
                    other_line = lines[line_nr + 1]
                    if other_line[k].isdigit():
                        m = k
                        m1 = m
                        while m >= 0 and other_line[m:k+1].isdigit():
                            m1 = m 
                            m -= 1
                        m = k
                        m2 = m
                        while m < line_length and other_line[k:m+1].isdigit():
                            m2 = m
                            m += 1
                        numbers.append(int(other_line[m1:m2+1]))
                    else:
                        if other_line[k-1].isdigit():
                            m = k - 1
                            m1 = m
                            while m >= 0 and other_line[m:k].isdigit():
                                m1 = m 
                                m -= 1
                            numbers.append(int(other_line[m1:k]))
                        if other_line[k+1].isdigit():
                            m = k + 1
                            m2 = m
                            while m < line_length and other_line[k+1:m+1].isdigit():
                                m2 = m 
                                m += 1
                            numbers.append(int(other_line[k+1:m2+1]))
                print(line_nr, k, numbers)
                if len(numbers) == 2:
                    s += numbers[0]*numbers[1]
                ll = line[k+1:] if k+1 < line_length else ""
                
    return s


print(partone(read_input("input.txt")))
print(parttwo(read_input("input.txt")))

