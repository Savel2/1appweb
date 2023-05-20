#this file contains all functions from the Udemy2. \
#We transfer all functions to organise the code better and to have them separete frome the main file.
def get_todos(): #in order to optimise the code I have added cutom function. That's helped to reduce repetitive code.
    """now we canwrite discription to our function. If someone will use it and type help(get_todos) one will see these message. """
    with open('/Users/savchik/Desktop/python/1appweb/todos.txt', 'r') as file_local: #also we can chose changable option: def get_todos(filepath):  with open (filepath, r)..... todos = get_todos(filepath)
        todos_local = file_local.readlines()
    return todos_local 

def write_todos(arg_todos, filepath = '/Users/savchik/Desktop/python/1appweb/todos.txt'): #here i mentioned two variables. First variable is the different option to input the value (as I wrote in 2 row). Second var is a variable from 31 line (todos)
    with open(filepath, 'w') as file:
                file.writelines(arg_todos)
#we don't use return since we don't need to return anything cause this function just need to change the file.

if __name__ == '__main__': #with these command we can run the code bellow only with such condition. __name__ == __main__ only when we are inside this code, in other files we will see: __name__ == Udemy2Functions
    print("Hello")
