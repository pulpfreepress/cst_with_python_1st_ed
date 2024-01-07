from calculator import *

def main():
    print(f'1 + 2 = {calc(1, 2, "+")}')
    print(f'2 - 4 = {calc(2, 4, "-")}')
    print(f'5 * 5 = {calc(5, 5, "*")}')
    print(f'14 / 7 = {calc(14, 7, "/")}')

if __name__ == '__main__':
    main()