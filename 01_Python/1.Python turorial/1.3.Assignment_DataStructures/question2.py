# Find the most frequent element in the list.

numbers = [1,2,3,4,4,5,6]

def most_freq (lst):
    max_count = 0
    most_freq = None

    for item in lst:
        count = lst.count(item)
        if count > max_count:
            max_count = count
            most_freq = item
    return most_freq
print(most_freq(numbers))