def adjacentElementsProduct(inputArray):
    for i in range(0, len(inputArray)-1):
        lis=(inputArray[i]*inputArray[i+1])
        print(lis)