# Homework 1. ToDo List Application

# Define Task Class:
    # Create a Task class with attributes such as task title, description, due date, and status.
# Define ToDoList Class:
    # Create a ToDoList class that manages a list of tasks.
    # Include methods to add a task, mark a task as complete, list all tasks, and display incomplete tasks.
# Create Main Program:
    # Develop a simple CLI to interact with the ToDoList.
    # Include options to add tasks, mark tasks as complete, list all tasks, and display only incomplete tasks.
# Test the Application:
    # Create instances of tasks and test the functionality of your ToDoList.



class Task:
    def __init__(self, task_title, description, due_date):
        self.task_title = task_title
        self.description = description
        self.due_date = due_date
        self.status = 'incomplete'

    def __str__(self):
        return f'{self.task_title} | {self.description} | {self.due_date} | {self.status}'

class ToDoList:
    def __init__(self):
        self.todolist = []

    def add_task(self, task: Task):
        self.todolist.append(task)

    def mark_complete(self, task: Task):
        if task.status == 'incomplete':
            task.status = 'complete'
            print(f'{task.task_title} is complete')
        else:
            print(f'Can not complete {task.task_title}.It is already complete ')

    def list_all_tasks(self):
        print('The list of tasks: ')
        for task in self.todolist:
            print(f' - {task}')
    
    def display_incomp_tasks(self):
        print('The list of incomplete tasks: ')
        for task in self.todolist:
            if task.status == 'incomplete':
                print(f' - {task}')

task1 = Task('Workout', '2-hour after work', '2026-01-01')
task2 = Task('Python 2', 'Dont give up', '2025-09-05')
task3 = Task('Power BI', 'Focus', '2025-09-29')

my_todolist = ToDoList()
# my_todolist.add_task(task1)
# my_todolist.add_task(task2)
# my_todolist.add_task(task3)

while True:
    print("1. List all tasks that is present.\n2. List tasks in my toDoList.\n3. Add Tasks.\n4. Mark Tasks as complete.\n5. Display only incomplete tasks.\n6. Exit.")
    option = int(input('please enter ur option: '))
    
    if option == 1:
        print(f'First task: {task1.task_title}, {task1.description}, {task1.due_date}, {task1.status}')
        print(f'Second task: {task2.task_title}, {task2.description}, {task2.due_date}, {task2.status}')
        print(f'Third task: {task3.task_title}, {task3.description}, {task3.due_date}, {task3.status}')
    
    if option == 2:
        my_todolist.list_all_tasks()

    if option == 3:
        choice = int(input('Tell which task to add according to the list.(1/2/3): '))

        if choice == 1:
            my_todolist.add_task(task1)
        if choice == 2:
            my_todolist.add_task(task2)
        if choice == 3:
            my_todolist.add_task(task3)

        print(f'Task{choice} added successfully')
    
    if option == 4:
        choice1 = int(input('Tell which task to mark complete according to the list.(1/2/3): '))

        if choice1 == 1:
            my_todolist.mark_complete(task1)
        if choice1 == 2:
            my_todolist.mark_complete(task2)
        if choice1 == 3:
            my_todolist.mark_complete(task3)

        print(f'Task{choice1} marked complete successfully')

    if option == 5:
        my_todolist.display_incomp_tasks()

    if option == 6:
        break

# Homework 2. Simple Blog System

# Define Post Class:
#   Create a Post class with attributes like title, content, and author.
# Define Blog Class:
#   Create a Blog class that manages a list of posts.
#   Include methods to add a post, list all posts, and display posts by a specific author.
# Create Main Program:
#   Develop a CLI to interact with the Blog system.
#   Include options to add posts, list all posts, and display posts by a specific author.
# Enhance Blog System:
#   Add functionality to delete a post, edit a post, and display the latest posts.
# Test the Application:
#   Create instances of posts and test the functionality of your Blog system.


class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def __str__(self):
        return f'{self.title} | {self.content} | {self.author}'

class Blog:
    def __init__(self):
        self.BlogList = []

    def add_post(self, post: Post):
        self.BlogList.append(post)
        print(f'{post.title} added successfully!')
    
    def list_all_posts(self):
        print('The list of posts: ')
        if not self.BlogList:
            print('no posts..')
        else:
            for post in self.BlogList:
                print(f' - {post}')
    
    def display_auth(self, author):
        print(f'Posts by {author}: ')
        found = False
        for post in self.BlogList:
            if post.author == author:
                print(f' - {post}')
                found = True
        if not found:
            print(f'no posts by {author}')
    
    def __str__(self):
        for i in self.BlogList:
            return f'{i.title} | {i.content} | {i.author}'

        


blog = Blog()
blog.list_all_posts()

## Main
while True:
    print('---Blog Menu---')
    print('1. Add posts')
    print('2. List all posts')
    print('3. Display by an author')
    print('4. Exit...')

    choice = input('Enter your choice (1/4): ')

    if choice == '1':
        title = input('enter post title: ')
        content = input('enter post content: ')
        author = input('enter post author: ')

        post = Post(title, content, author)
        blog.add_post(post)
    
    elif choice == '2':
        blog.list_all_posts()

    elif choice == '3':
        a1 = input('enter author name: ')
        blog.display_auth(a1)
    
    elif choice == '4':
        break

    else:
        print('please try again..')

# functions

def delete_post(title):
    for post1 in blog.BlogList:
        if title == post1.title:
            blog.BlogList.remove(post1)
    print(f'Removed post: {post1}')

def display_latest():
    print(blog.BlogList[-1])




def edit_post(old_post_title, new_title=None, new_content=None, new_author=None):
    for post in blog.BlogList:
        if post.title == old_post_title:
            if new_title:
                post.title = new_title
            if new_content:
                post.content = new_content
            if new_author:
                post.author = new_author
            print(f'Post updated: {post}')
            return
    print('Post not found')

delete_post('Hi')
display_latest()

edit_post('Hello', new_title='Hey',new_author='Bob')

blog.list_all_posts()


