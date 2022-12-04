import random
import json
import os.path as os

if __name__ == '__main__':

    class FormatError(Exception):
        def __str__(self):
            return 'Incorrect format.'


    operators = ['+', '-', '*']
    task_answer = ''
    difficulty_level = 0
    asked_answers = 0
    correct_answers = 0
    levels = {
        '1': {
            'description': 'simple operations with numbers 2-9',
            'results': ''
        },
        '2': {
            'description': 'integral squares 11-29',
            'results': ''
        }
    }
    
    def random_task(difficulty):
        if difficulty == 1:
            global task_answer
            x = random.randint(2, 9)
            y = random.randint(2, 9)
            oper = operators[random.randint(0, 2)]
            task_answer = f'{x}{oper}{y}'
            print(task_answer)
        elif difficulty == 2:
            x = random.randint(11, 29)
            print(x)
            task_answer = f'{x}**2'


    def loop():
        global asked_answers
        global correct_answers
        while asked_answers < 5:
            random_task(difficulty_level)
            while True:
                try:
                    user = int(input())
                    if user == eval(task_answer):
                        print('Right!')
                        correct_answers += 1
                    else:
                        print('Wrong!')
                except ValueError as fe:
                    print(FormatError)
                    continue
                asked_answers += 1
                break


    def difficulty_check():
        global difficulty_level
        while difficulty_level == 0:
            user = input()
            if user == '1':
                difficulty_level = 1
            elif user == '2':
                difficulty_level = 2
            else:
                print(FormatError)


    def file_handling():
        print('What is your name?')

        username = input()
        level_data = ''
        with open('results.txt', 'a+') as results_file:
            results_file.seek(0)
            lines = results_file.readlines()
            for line in lines:
                try:
                    json.loads(line)
                except ValueError:
                    pass
                else:
                    level_data = json.loads(line)
                    break
            print('dif level' + str(difficulty_level))
            final_message = f'{username}: {correct_answers}/5 in level {difficulty_level} ' \
                            f'({levels[str(difficulty_level)]["description"]})'

            json.dump(final_message, results_file)

        print('The results are saved in "results.txt".')


    def final_results():
        user = input()
        if user.lower() == 'yes' or user.lower() == 'y':
            file_handling()
        else:
            return


    # set_levels()
    print(
        'Which level do you want? Enter a number:\n1 - simple operations with numbers 2-9\n2 - integral squares of 11-29')
    difficulty_check()
    loop()
    print(f'Your mark is {correct_answers}/5.')
    print('Would you like to save your result to the file? Enter yes or no.')
    final_results()
