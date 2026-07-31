correct_answers = 0
print('Welcome To Todays Quiz Game!')

print('Question 1: What is the capital of France?')
print('a) Berlin')
print('b) Madrid')
print('c) Paris')
print('d) Rome')
answer = input('Enter your answer (a, b, c, or d): ').lower()
if answer == 'c':
    print('Correct!')
    correct_answers += 1
else:
    print('Incorrect. The correct answer is c) Paris.')
    
print('Question 2: What is the largest planet in our solar system?')
print('a) Earth')
print('b) Jupiter')
print('c) Saturn')
print('d) Uranus')
answer = input('Enter your answer (a, b, c, or d): ').lower()
if answer == 'b':
    print('Correct!')
    correct_answers += 1
else:
    print('Incorrect. The correct answer is b) Jupiter.')
    
print('Question 3: What is the chemical symbol for gold?')
print('a) Ag')
print('b) Au')
print('c) Fe')
print('d) Pb')
answer = input('Enter your answer (a, b, c, or d): ').lower()
if answer == 'b':
    print('Correct!')
    correct_answers += 1
else:
    print('Incorrect. The correct answer is b) Au.')

print('Question 4: What is the largest ocean on Earth?')
print('a) Atlantic Ocean')
print('b) Indian Ocean')
print('c) Southern Ocean')
print('d) Pacific Ocean')
answer = input('Enter your answer (a, b, c, or d): ').lower()
if answer == 'd':
    print('Correct!')
    correct_answers += 1
else:
    print('Incorrect. The correct answer is d) Pacific Ocean.')
    
print('Question 5: What is the smallest prime number?')
print('a) 1')
print('b) 2')
print('c) 3')
print('d) 5')
answer = input('Enter your answer (a, b, c, or d): ').lower()
if answer == 'b':
    print('Correct!')
    correct_answers += 1
else:
    print('Incorrect. The correct answer is b) 2.')

print('Quiz complete!')
print(f'You got {correct_answers}/5 questions correct.')