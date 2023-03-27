arithmetic_arrangers = (["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])

def arithmetic_arranger(problems):
    for problem in problems:
        numbers = problem.split()
        first = int(numbers[0])
        operator = numbers[1]
        second = int(numbers[2])

        print("  ",first)
        print(operator,"", second)
        print("-----\n")

arithmetic_arranger(arithmetic_arrangers)