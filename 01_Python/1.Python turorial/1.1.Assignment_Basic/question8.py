# Slice to get only the middle character for my_string = "Madhav", use slicing to extract the middle characters.

my_string = "Madhav"

def mid_string(word):
    middle = int(len(word)/2)
    if (len(word) % 2 == 0):
        return word[middle-1:middle+1]
    else:
        return word[middle]

mid = mid_string(my_string)

print(mid)