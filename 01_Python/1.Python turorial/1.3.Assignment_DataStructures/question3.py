# Find the cummulative sum of the given elements in the list.

number = [1,2,3,4,5,6]

def cumulative_sum (list):
    cum_list = []
    sum = 0
    for item in list:
        sum += item
        cum_list.append(sum)
    return cum_list

print(cumulative_sum(number))