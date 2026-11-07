####### EVEN ODD #######
# def even_odd(number):
#     if number % 2 == 0:
#         return 'Even'
#     return 'Odd'

# print(even_odd(20))
# print(even_odd(47))


###### LARGEST NUMBER ######

# def max_number(numbers):
#     largest = numbers[0]
    
#     for number in numbers:
#         if number > largest:
#             largest = number    
#     return largest
    
# print(max_number([4, 6, 2, 9]))


####### VOWEL COUNT ######
# def vowel_count(text):
#     vowels = 'aeiou'
#     count = 0
    
#     for letter in text.lower():
#         if letter in vowels:
#             count +=1
#     return f'Total Vowels = {count}'

# print(vowel_count('I am going to work.'))


######## REMOVE DUPLICATE #########
# def duplicate_remove(numbers):
#     return list(dict.fromkeys(numbers))

# print(duplicate_remove([1, 2, 2, 3, 1, 4]))


######### WORD FREQUENCY #########
def word_frequency(sentence):
    frequency = {}
    
    for word in sentence.lower().split():
        frequency[word] = frequency.get(word, 0) + 1
        
    return frequency

print(word_frequency("learn code learn"))


########### SECOND LARGEST NUMBER ##############
def second_largest(numbers):
    unique_numbers = list(set(numbers))
    
    if len(unique_numbers) < 2 :
        return None
    
    sorted_list = sorted(unique_numbers, reverse=True)
    return sorted_list[1]

print(second_largest([1, 2, 2, 3, 1, 4]))
