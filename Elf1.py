#Calorie Counting

elfCalories = [[1000,2000,3000],[4000],[5000,6000],[7000,8000,9000],[10000]]

print(len(elfCalories))


def countCals(elfCalories):
    maxCal = 0
    indElfCal = 0 
    for i in range(len(elfCalories)):
        indElfCal = sum(elfCalories[i])
        if indElfCal > maxCal:
            maxCal = indElfCal
    return maxCal
    



print(countCals(elfCalories))