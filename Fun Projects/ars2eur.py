# ARS to EUR / EUR to ARS - 1 ARS = 0.0095200
convertion = 0.00952

# function to convert ARS to EUR
def ars():
    value = float(input("ARS: "))
    return round(value * convertion, 2)


# function to convert EUR to ARS
def eur():
    value = float(input("EUR: "))
    return round(value / convertion, 2)


def run():
    print("""ARS - EUR [1]
EUR - ARS [2]

EXIT      [0]""")
    choice = int(input(">>> "))
    if choice == 1:
        print(f"EUR: {ars()}")
    elif choice == 2:
        print(f"ARS: {eur()}")
    elif choice == 0:
        exit()
    else:
        run()


if __name__ == '__main__':
    run()
