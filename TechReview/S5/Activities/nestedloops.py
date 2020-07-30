residents_ages = [[14,15,18,50,54], [9,9,39,42], [25,22,55,54], [25,28], [2,1,28,30]]

# Calculates the number of eligible voters per household
def number_of_voters(neighborhood):
    for house in neighborhood: # Outer loop
        print("-----")
        for age in house:
            print(age)

number_of_voters(residents_ages)



residents_ages = [[14,15,18,50,54], [9,9,39,42], [25,22,55,54], [25,28], [2,1,28,30]]

# Calculates the number of eligible voters per household
def number_of_voters(neighborhood):
    # A list to hold the number of eligible voters for each household.
    eligible_voters = []
    
    for house in neighborhood: 
        can_vote = 0
        for age in house:
            if age >= 18:
                can_vote += 1
        eligible_voters.append(can_vote)


           # Write your conditional statement(s) here
    
    return eligible_voters

print(number_of_voters(residents_ages))



def reverseList(l1):
    return l1[::-1]

print(reverseList([1, 2, 3, 4, 5]))

def findMax(data):
    '''Takes an iterable of integers, data, as input and returns the max item, an integer.'''
    max = 0
    for num in data:
        if num > max:
            max = num
    return max

print(findMax.__doc__)