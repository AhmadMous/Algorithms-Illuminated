def largest_pair(ilist):

    # Dictionary :Winner -> [losers]
    winners = {}

    # Returns highest of 2 numbers and updates winners dictionary
    def higher_of_2(list):

        # Find highest of the two numbers
        if list[0] > list[1]:
            higher, lower = list[0], list[1]
        else:
            higher, lower = list[1], list[0]

        # Update winners dictionary
        if higher in winners:
            winners[higher].append(lower)
        else:
            winners[higher] = [lower]
        
        return higher


    # Recursively finds highest number in a list
    def find_highest(list):

        # Base case
        if len(list) == 2:
            return higher_of_2(list)
            
        # Find the highest number of each list
        middle = len(list) // 2
        left = find_highest(list[:middle])
        right = find_highest(list[middle:])

        # Returns highest number of the two sublists
        return find_highest([left, right])


    highest = find_highest(ilist)
    second_highest = find_highest(winners[highest])

    return highest, second_highest

list1 = [i for i in range(16)]
ilist = [1,14,3,57,5,6,8,9,434,43,13,54,1,2,1,2]

print(largest_pair(ilist))
print(largest_pair(list1))