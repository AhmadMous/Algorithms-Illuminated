# Recursively find the 2 largest numbers in a list by D&C
# The list is split into 2 sublists and each is processed to get 2 largest elements
# The elements from the 2 lists of 2 elements are then compared to get 2 largest numebrs across all
def find_secondL(list):

    # List of indices that facilitates work, without worrying of index change when slicing
    index_list = [i for i in range(len(list))]

    # Returns a list of indices of 2 biggest numbers
    def two_highest(list_1, list_2):

        # Create an empty list and indices to iterate over input lists
        result = []
        list_1_index = 0
        list_2_index = 0

        # Iterate twice finding largest then second largest element of the bunch
        for i in range(2):
            if ilist[list_1[list_1_index]] > ilist[list_2[list_2_index]]:
                result.append(list_1[list_1_index])
                list_1_index += 1
            else:
                result.append(list_2[list_2_index])
                list_2_index += 1

        # Return the resultant list
        return result


    # Returns list of indexes in decreasing order of their containing numbers
    def highest_pair(number_1, number_2):
        return [number_2, number_1] if list[number_2] > list[number_1] else [number_1, number_2]


    # Recursively finds the  indices of the 2 largest numbers in a list
    def second_largest(index_list):

        # Handles base case of 2 input elements
        if len(index_list) == 2:
            return highest_pair(index_list[1], index_list[0])

        # Split the array into 2, and recursively find 2 highest numbers in those lists
        midpoint = len(index_list) // 2
        left_half = second_largest(index_list[:midpoint])
        right_half = second_largest(index_list[midpoint:])

        # Find two indices of largest numbers across the 2 lists
        return two_highest(right_half, left_half)


    return second_largest(index_list)
        
ilist = [1,14,3,57,5,6,8,9,434,43,13,54,1,2,1,2]
find_secondL(ilist)