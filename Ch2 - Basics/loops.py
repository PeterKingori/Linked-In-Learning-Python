#
# Example file for working with loops
# LinkedIn Learning Python course by Joe Marini
#


def main():
    x = 0

    # define a while loop
    while x < 5:
        print(x)
        x += 1

    print()

    # define a for loop
    for x in range(3, 8):
        print(x)

    print()

    # use a for loop over a collection
    days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
    for day in days:
        print(day)

    print()

    # use the break and continue statements
    for x in range(1, 10):
        if x == 4:
            break
        print(x)

    for a in range(1, 10):
        if a % 2 == 0:
            continue
        print(a)

    print()

    # using the enumerate() function to get index
    for i, day in enumerate(days):
        print(i, day)

if __name__ == "__main__":
    main()
