#TO-DO LIST PROJECT
def print_menu():
    print('\nTo-Do List Menu')
    print('1. View Tasks')
    print('2. Add Task')
    print('3. Remove Task')
    print('4. Exit')
    

def get_choice():
    while True:
        choice = input('Enter your choice (1-4): ')
        valid_choices = ['1', '2', '3', '4']
        if choice not in valid_choices:
            print('Invalid choice. Please try again.')
            continue
        else:
            return choice


def view_tasks(tasks):
    if not tasks:
        print('No tasks in the list.')
        return
    
    for index, task in enumerate(tasks, start=1):
        print(f'{index}. {task}')


def add_task(tasks):
    while True:        
        task = input('Enter the task: ').strip()
        if len(task) != 0:
            tasks.append(task)
            break
        else:
            print('Invalid task!')


def remove_task(tasks):
    view_tasks(tasks)
    while True:
        try:
            task_number =  int(input('Enter the task number: '))
            if 1 <= task_number <= len(tasks):
               tasks.pop(task_number - 1)
               break
            else:
                raise ValueError
        except ValueError:
            print('Invalid task number!')


def main():
    tasks = []
    
    while True:
        print_menu()
        
        choice = get_choice()
        
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        else:
            break