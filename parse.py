my_string = 'Lorem ipsum dolor sit amet, consectetur #adipiscing elit. '

# split the string at ':'
step_0 = my_string.split('#')

# get the first slice of the list
step_1 = step_0[1]

# split the string at ','
step_2 = step_1.split(' ')

# strip leading and trailing edge spaces of each item of the list 
step_3 = step_2[0]


print(step_3)
