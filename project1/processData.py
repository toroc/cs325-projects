

def insertIntoArrays(fileName):
    """
    Description: 
        Reads data from text file
        Converts each line in file into array of integers
        Appends next array to list of arrays
    Input: n/a 
    Output: Returns array of arrays (list of arrays)
    """

    arrayList = []

    with open(fileName) as file:
        for line in file:
            #Get rid of brackets and empty space    
            line = line.replace('[', '').replace(' ', '').replace(']', '')

            #Append each number to list, add comma separator for next list
            arrayList.append([int(num) for num in line.split(',') if num not in '\n'])
    
    return arrayList



#insertIntoArrays()

def writeResults(file, fullArray, subArray, maxSum):
    """

    """

    file.write('{0}\n'.format(fullArray))
    file.write('{0}\n'.format(subArray))
    file.write('{0}\n\n'.format(maxSum))



