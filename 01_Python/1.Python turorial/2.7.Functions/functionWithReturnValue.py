# Here we will learn how to get the value in return in the function.

def cel_2_fah(celsius):
    fahrahneit = (celsius * 9/5)+32
    return fahrahneit

temp_f = cel_2_fah(35)
print("The temperature in fahrahneit is:",temp_f)

temp_1 = cel_2_fah(50)
print("The temperature is :",temp_1)