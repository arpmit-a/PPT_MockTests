'''Write a function that takes a list of numbers as input and returns a new list containing only the even numbers from the input list. Use list comprehension to solve this problem.'''
def even_list(list):
    even=[i for i in list if i%2==0]
    return even
  
