import random
from termcolor import cprint

QUESTION = 'question'
OPTIONS = 'options'
ANSWER = 'answer'

quiz = [
    {
        QUESTION: 'What is the capital of France?',
        OPTIONS: ['a) Berlin', 'b) Madrid', 'c) Paris', 'd) Rome'],
        ANSWER: 'c'
    },
    {
        QUESTION: 'Which planet is known as the Red Planet?',
        OPTIONS: ['a) Venus', 'b) Mars', 'c) Jupiter', 'd) Saturn'],
        ANSWER: 'b'
    },
    {
        QUESTION: 'What is the largest ocean in the world?',
        OPTIONS: ['a) Atlantic Ocean', 'b) Indian Ocean', 'c) Arctic Ocean', 'd) Pacific Ocean'],
        ANSWER: 'd'
    },
    {
        QUESTION: 'What is the most dangerous snake in the world?',
        OPTIONS: ['a) King Cobra', 'b) Black Mamba', 'c) Green Anaconda', 'd) Reticulated Python'],
        ANSWER: 'a'
    },
    {
        QUESTION: 'What is the most populated country in the world?',
        OPTIONS: ['a) India', 'b) China', 'c) United States', 'd) Indonesia'],
        ANSWER: 'a'
    }
]


random.shuffle(quiz)

score = 0

for index, item in enumerate(quiz):
    print(f'Question {index + 1}: {item[QUESTION]}')
    for option in item[OPTIONS]:
        print(option)
    
    answer = input('Your answer: ').lower()
    if answer == item[ANSWER]:
        cprint('Correct!', 'green')
        score += 1
    else:
        cprint(f'Incorrect. The correct answer is {item[ANSWER]}.', 'red')
    print()

print(f'Your final score is {score} out of {len(quiz)}.')