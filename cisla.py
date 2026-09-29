
with open("data/cisla.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    numbers = []
    for line in lines:
        if line.strip() !="":
            number = int(line.strip())
            numbers.append(number)

    if numbers:
        print("Max číslo:", max(numbers))