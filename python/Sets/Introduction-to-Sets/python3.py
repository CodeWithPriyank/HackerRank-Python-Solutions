def average(array):
    # your code goes here
    #A set is a collection which is unordered, unchangeable*, and unindexed.
    my_array = set(array)
    return sum(my_array)/len(my_array)
