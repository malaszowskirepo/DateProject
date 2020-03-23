import sys


def main():
    with open(sys.argv[1]) as file:
        line = file.read()
        if len(line) > 4:
            interpret(line)
        else:
            print(line + ' is illegal')


def interpret(arg):
    input_line = arg.split('/')
    if len(input_line) != 3:
        print(arg + ' is illegal')

    else:
        input_line.sort()

        year = int(input_line[0])
        month = int(input_line[1])
        day = int(input_line[2])

        found_solution = True

        if not validate_date(year, month, day):
            tmp = month
            month = day
            day = tmp
            if not validate_date(year, month, day):
                tmp = year
                year = month
                month = tmp
                if not validate_date(year, month, day):
                    found_solution = False

        if not found_solution:
            print(arg + ' is illegal')
        else:
            if year <= 99:
                year += 2000
            solution = str(year) + '-' + str(month) + '-' + str(day)
            print(solution)


def validate_date(y, m, d):
    if y <= 99:
        y += 2000
    days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if 2000 <= y <= 2999:
        if 1 <= m <= 12:
            if 1 <= d <= days_in_month[m - 1]:
                if m != 2:
                    return True
                else:
                    if not (y % 400 == 0 or (y % 100 != 0 and y % 4 == 0)):
                        if d <= 28:
                            return True
                    else:
                        return True
    return False


if __name__ == '__main__':
    main()
