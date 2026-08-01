

def mathematics_quiz():
    correct_answers = 0
    
    print('Welcome to the Mathematics Quiz!')
    print('Question 1: Solve for x: 3x + 7 = 25')
    print('a) 5')
    print('b) 6')
    print('c) 7')
    print('d) 8')
    answer = input('Enter your answer (a, b, c, or d): ').lower()
    if answer == 'b':
        print('Correct!')
        correct_answers += 1
    else:
        print('Incorrect')
    
    print('Question 2: What is the value of: 7^2 - 5^2?')
    print('a) 24')
    print('b) 25')
    print('c) 26')
    print('d) 27')
    answer = input('Enter your answer (a, b, c, or d): ').lower()
    if answer == 'a':
        print('Correct!')
        correct_answers += 1
    else:
        print('Incorrect')
        
    print('Question 3: A rectangle has a length of 12 and a width of 8. What is its area?')
    print('a) 20')
    print('b) 48')
    print('c) 96')
    print('d) 120')
    answer = input('Enter your answer (a, b, c, or d): ').lower()
    if answer == 'c':
        print('Correct!')
        correct_answers += 1
    else:
        print('Incorrect')
        
    print('Question 4: Simplify: 5(2x - 3) + 4 ?')
    print('a) 10x - 11')
    print('b) 10x + 1')
    print('c) 10x - 15')
    print('d) 5x - 11')
    answer = input('Enter your answer (a, b, c, or d): ').lower()
    if answer == 'a':
        print('Correct!')
        correct_answers += 1
    else:
        print('Incorrect')
        
    print('Question 5: A shirt originally costs $80 and is discounted by 25\% off, what is the sale price?')
    print('a) $55')
    print('b) $60')
    print('c) $65')
    print('d) $70')
    answer = input('Enter your answer (a, b, c, or d): ').lower()
    if answer == 'b':
        print('Correct!')
        correct_answers += 1
    else:
        print('Incorrect')
    print(f'You got {correct_answers}/5 questions correct.')


def science_quiz():
    correct_answers = 0
    
    print('Welcome to the Science Quiz!')
    
    print('Question 1: What is the chemical symbol for gold?')
    print('a) Ag')
    print('b) Gd')
    print('c) Au')
    print('d) Go')
    answer = input('Enter your answer (a, b, c, or d): ').lower()
    if answer == 'c':
        print('Correct!')
        correct_answers += 1
    else:
        print('Incorrect')
        
    print('Question 2: What planet is known as the "Red Planet"?')
    print('a) Venus')
    print('b) Mars')
    print('c) Jupiter')
    print('d) Mercury')
    answer = input('Enter your answer (a, b, c, or d): ').lower()
    if answer == 'b':
        print('Correct!')
        correct_answers += 1
    else:
        print('Incorrect')
        
    print('Question 3: What process do plants use to make their own food?')
    print('a) Respiration')
    print('b) Fermentation')
    print('c) Photosynthesis')
    print('d) Digestion')
    answer = input('Enter your answer (a, b, c, or d): ').lower()
    if answer == 'c':
        print('Correct!')
        correct_answers += 1
    else:
        print('Incorrect')
        
    print('Question 4: What is the largest organ in the human body?')
    print('a) Liver')
    print('b) Heart')
    print('c) Skin')
    print('d) Brain')
    answer = input('Enter your answer (a, b, c, or d): ').lower()
    if answer == 'c':
        print('Correct!')
        correct_answers + 1
    else:
        print('Incorrect')
        
    print('Question 5: What force keeps planets in orbits around the Sun?')
    print('a) Magnetism')
    print('b) Friction')
    print('c) Gravity')
    print('d) Electricity')
    answer = input('Enter your answer (a, b, c, or d): ').lower()
    if answer == 'c':
        print('Correct!')
        correct_answers += 1
    else:
        print('Incorrect')
        
    print(f'You got {correct_answers}/5 questions correct.')


def history_quiz():
    correct_answers = 0
    
    print('Welcome to the History Quiz!')
    
    print('Question 1: Who was the first President of the United States?')
    print('a) Abraham Lincoln')
    print('b) Thomas Jefferson')
    print('c) George Washington')
    print('d) John Adams')
    answer = input('Enter your answer (a, b, c, or d): ').lower()
    if answer == 'c':
        print('Correct!')
        correct_answers += 1
    else:
        print('Incorrect')
        
    print('Question 2: In which year did World War II end?')
    print('a) 1943')
    print('b) 1945')
    print('c) 1947')
    print('d) 1950')
    answer = input('Enter your answer (a, b, c, or d): ').lower()
    if answer == 'b':
        print('Correct!')
        correct_answers += 1
    else:
        print('Incorrect')
        
    print('Question 3: Which ancient civilization built the pyramids of Giza?')
    print('a) Romans')
    print('b) Greeks')
    print('c) Egyptians')
    print('d) Persians')
    answer = input('Enter your answer (a, b, c, or d): ').lower()
    if answer == 'c':
        print('Correct!')
        correct_answers += 1
    else:
        print('Incorrect')
        
    print('Question 4: What was the name of the ship that carried the Pilgrims to America in 1620?')
    print('a) Santa Maria')
    print('b) Mayflower')
    print('c) Titanic')
    print('d) Endeavour')
    answer = input('Enter your answer (a, b, c, or d): ').lower()
    if answer == 'b':
        print('Correct!')
        correct_answers += 1
    else:
        print('Incorrect')
        
    print('Question 5: Which wall fell in 1989, symbolizing the end of the Cold War?')
    print('a) Great Wall of China')
    print('b) Hadrian\'s Wall')
    print('c) Berlin Wall')
    print('d) Wall of Jericho')
    answer = input('Enter your answer (a, b, c, or d): ').lower()
    if answer == 'c':
        print('Correct!')
        correct_answers += 1
    else:
        print('Incorrect.')
        
    print(f'You got {correct_answers}/5 questions correct.')


def psychology_quiz():
    correct_answers = 0
    
    print('Welcome to the Psychology Quiz!')
    
    print('Question 1: Which psychologist developed the hierarchy of needs?')
    print('a) Sigmund Freud')
    print('b) Carl Jung')
    print('c) Abraham Maslow')
    print('d) Ivan Pavlov')
    answer = input('Enter your answer (a, b, c, or d): ').lower()
    if answer == 'c':
        print('Correct!')
        correct_answers += 1
    else:
        print('Incorrect.')
        
    print('Question 2: What is the term for learning through rewards and punishments?')
    print('a) Classical Conditioning')
    print('b) Operant Conditioning')
    print('c) Observational Learning')
    print('d) Insight Learning')
    answer = input('Enter your answer (a, b, c, or d): ').lower()
    if answer == 'b':
        print('Correct!')
        correct_answers += 1
    else:
        print('Incorrect.')
        
    print('Question 3: Which part of the brains is primarily responsible for memory formation?')
    print('a) Cerebellum')
    print('b) Hippocampus')
    print('c) Medulla Oblongata')
    print('d) Thalamus')
    answer = input('Enter your answer (a, b, c, or d): ').lower()
    if answer == 'b':
        print('Correct!')
        correct_answers += 1
    else:
        print('Incorrect.')
        
    print('Question 4: What is cognitive dissonance?')
    print('a) A type of memory loss')
    print('b) The inability to concentrate')
    print('c) Mental discomfort from holding conflicting beliefs or behaviors')
    print('d) Fear of public speaking')
    answer = input('Enter your answer (a, b, c, or d): ').lower()
    if answer == 'c':
        print('Correct!')
        correct_answers += 1
    else:
        print('Incorrect.')
        
    print('Question 5: In psychology, what does IQ stand for?')
    print('a) Intellectual Quality')
    print('b) Intelligence Quotient')
    print('c) Intelligence Quality')
    print('d) Intellectual Quantity')
    answer = input('Enter your answer (a, b, c, or d): ').lower()
    if answer == 'b':
        print('Correct!')
        correct_answers += 1
    else:
        print('Incorrect.')
        
    print(f'You got {correct_answers}/5 questions correct.')
                   

def geography_quiz():
    correct_answers = 0
    
    print('Welcome to the Geography Quiz!')
    
    print('Question 1: What is the longest river in the world?')
    print('a) Mississippi River')
    print('b) Yangtze River')
    print('c) Nile River')
    print('d) Congo River')
    answer = input('Enter your answer (a, b, c, or d): ').lower()
    if answer == 'c':
        print('Correct!')
        correct_answers += 1
    else:
        print('Incorrect.')
        
    print('Question 2: Which country currently has the largest population in the world?')
    print('a) China')
    print('b) India')
    print('c) United States')
    print('d) Indonesia')
    answer = input('Enter your answer (a, b, c, or d): ').lower()
    if answer == 'b':
        print('Correct!')
        correct_answers += 1
    else:
        print('Incorrect.')
        
    print('Question 3: What is the capital city of Australia?')
    print('a) Sydney')
    print('b) Melbourne')
    print('c) Perth')
    print('d) Canberra')
    answer = input('Enter your answer (a, b, c, or d): ').lower()
    if answer == 'd':
        print('Correct!')
        correct_answers += 1
    else:
        print('Incorrect.')
        
    print('Question 4: Which desert is the largest hot desert in the world?')
    print('a) Gobi Desert')
    print('b) Sahara Desert')
    print('c) Arabian Desert')
    print('d) Kalahari Desert')
    answer = input('Enter your answer (a, b, c, or d): ').lower()
    if answer == 'b':
        print('Correct!')
        correct_answers += 1
    else:
        print('Incorrect.')
        
    print('Question 5: n which continent insthe Amazon Rainforest primarily located?')
    print('a) Africa')
    print('b) Asia')
    print('c) South America')
    print('d) North America')
    answer = input('Enter your answer (a, b, c, or d): ').lower()
    if answer == 'c':
        print('Correct!')
        correct_answers += 1
    else:
        print('Incorrect.')
    
    print(f'You got {correct_answers}/5 questions correct.')



def main():
    print('Welcome to the Quiz Game!')
    print('1. Mathematics')
    print('2. Science')
    print('3. History')
    print('4. Psychology')
    print('5. Geography')
    selection = input('Choose your category: ')
    
    if selection == '1':
        mathematics_quiz()
    elif selection == '2':
        science_quiz()
    elif selection == '3':
        history_quiz()
    elif selection == '4':
        psychology_quiz()
    elif selection == '5':
        geography_quiz()
    else:
        print('Invalid selection.')
    
    
main()