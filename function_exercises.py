def is_two(string):
    if string == 2 or string == '2':
        return True
    else:
        return False

    
    

def is_two(string):
    if string == 2 or string == '2':
        return True
    else:
        return False




def is_consonant(string):
    if type(string) == str:
        if string.isalpha() == True:
            if not is_vowel(string):
                return True
            else:
                return False
        else:
            return False
    else:
        return False
    



def capital_cons_start(string):
    if is_consonant(string[0]):
        string = string.capitalize()
    return string


def calculate_tip(total_bill, tip = .1):
    return total_bill * tip + total_bill



def apply_discount(orig_price, disc_price):
    return orig_price - orig_price * disc_price



def handle_commas(string_num):
    return int(string_num.replace(',',''))



def get_letter_grade(grade):
    if grade >= 90:
        letter_grade = 'A'
    elif grade >= 80:
        letter_grade = 'B'
    elif grade >= 70:
        letter_grade = 'C'
    else:
        letter_grade = 'F' 
        
    return letter_grade




def remove_vowels(string):
    new_string = ''

    for char in string:
        if not is_vowel(char):
            new_string += char
            
    return new_string







def normalize_name(string):
    string = string.strip().lower().replace(' ','_')
    
    new_string = ''
    
    for char in string:
        if char.isalpha() or char.isdigit() or char == '_':
            new_string += char
    new_string = new_string.strip('_')
    
    return new_string




def cumulative_sum(ls):
    total = 0 
    some_sums = []

    for numb in ls:
        total += numb
        some_sums.append(total)

    return some_sums