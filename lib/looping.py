#!/usr/bin/env python3

def happy_new_year():
    i = 11
    while i > 0:
        i -= 1
        print(i)
    if i == 0:
        print("Happy New Year!")

def square_integers(int_list):
    new_list = [i ** 2 for i in int_list]
    return new_list
 
    

def fizzbuzz():
    for i in range(1, 101):
        if(i%3==0 and i%5==0):
            print("FizzBuzz")
        elif(i%3==0):
            print("Fizz")
        elif(i%5==0):
            print("Buzz")
        else:
            print(i)
