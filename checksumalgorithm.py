

"""
add the digits of a number 
"""
def adder(number):
    sum_of_n = 0
    for x in str(number):
        sum_of_n += int(x)
    return sum_of_n

"""
reverse the numbers
"""
def rev_num(number): 
    rev = list(reversed(number))
    join = "".join(rev)
    return join

"""
take the numbers at 1st, 3rd etc... and sum them up
"""
def odd_sum(number_input): 
    sum = 0
    number = number_input[::2]
    for i in number: 
        sum = sum + int(i)
    return sum
    


"""
take the digits at values 2nd, 4th and etc... 
multiply by 2
if 2 digit number add the individual digits together 
Sum all of them up
"""
def even_sum(number_input): 
    arr_single_digits = []
    arr_if_double_digits = []
    number = number_input[1:][::2]

    for i in number: 
        value_by_2 = (int(i) * 2)
        valuestr = str(value_by_2) 
        #print(valuestr)
        if len(valuestr) >= 2: 
            sumvalue = adder(valuestr)
            arr_if_double_digits.append(sumvalue)
        else: 
            arr_single_digits.append(value_by_2)
    final_sum = sum(arr_if_double_digits) + sum(arr_single_digits)
    return final_sum

"""
decide if passed the checksum
"""
def decider(card):
    reversed_num = rev_num(card)
    sum_A = odd_sum(reversed_num)
    sum_B = even_sum(reversed_num)
    final_sum = sum_A + sum_B
    if final_sum % 10 == 0:
        return "Yes"
    else: 
        return "No"
        
#print((odd_sum("9795526789839145")))

"""
Read in input
"""
mystring = input()
no_of_lines = int(mystring)
cards = []
ran = range(1,no_of_lines+1)
for i in ran:
    l = input()
    cards.append(l)

#print(type(cards))

"""
Finally print the results
"""
for x in cards: 
    print(decider(x))




