def is_two(a):
    a = input('Enter the number or letter 2: ')
    if a.isdigit() == True:
        a = int(a)
    if a == 2 or a == 'two':
        return True
    else:
        return False
im_lost = is_two(a)
print(im_lost)




def is_vowel():
    user_input = input('Enter a vowel:  ')

    if user_input.lower() in 'aeiou':
        return True
    elif user_input.upper() in 'AEIOU':
        return True
    else:
        return False
        
im_lost = is_vowel()
print(im_lost)




def is_vowel():
    user_input = input('Enter a vowel:  ')

    if user_input.lower() not in 'aeiou':
        return True
    elif user_input.upper() not in 'AEIOU':
        return True
    else:
        return False
        
im_lost = is_vowel()
print(im_lost)




# while True:
user_input = input('Enter a your first name:  ')

first_letter_lower_case = user_input[0].lower() + user_input[1:]

print('Hi:' + str(first_letter_lower_case))
    
#     if user_input.isdigit() == True:
#         print('Invalid entry, this is a number. Try again!')
#     elif user_input == .lower()
#         print('lower case')

    
    