"""Although you have to be careful using recursion it is one of those concepts you want to at least understand. It's
also commonly used in coding interviews :)

In this beginner Bite we let you rewrite a simple countdown for loop using recursion. See countdown_for below,
it produces the following output:
You will be tested on having the same output, making it work with another start value, and of course if you used
recursion. Have fun!"""
import inspect

def countdown_for(start=10):
    if start != 0:
        print(start)
        countdown_for(start - 1)
    elif start == 0:
        print('time is up')

def countdown_recursive(start=10):
    if start != 0:
        print(start)
        countdown_recursive(start - 1)
    elif start == 0:
        print('time is up')


countdown_for(13)

