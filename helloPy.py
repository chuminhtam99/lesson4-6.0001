def calculateCubeRoot(input):
    epsilon = 0.000001
    cube = input
    low = 0
    high = cube
    guess = (low+ high)/2
    countNumber = 1

    while(abs(guess**3 - cube) >= epsilon):
        if guess**3 < cube :
            low = guess
        else:
            high = guess
        guess = (low+ high)/2
        countNumber = countNumber +1

    return guess


input = float(input('enter the number that you want to calculate its square cube: '))
output = 0.0
if -1 < input < 0  : 
    output = -1/calculateCubeRoot(-1 /input)
    print(output)
if input <=-1: 
    output = -calculateCubeRoot(-input)
    print(output)
if input == 0 :
    output = 0
    print(output)
if 0 < input < 1  : 
    output = 1/calculateCubeRoot(1 /input)
    print(output)
if input >= 1  : 
    output = calculateCubeRoot(input)
    print(output)


