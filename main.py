"""
You will be going through the following practice problems, we will
be breaking these problems down into smaller pieces. This will help
you get a better idea on how to solve coding problems.
"""

"""
PROBLEM 1:
The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.

sleep_in(False, False) → True
sleep_in(True, False) → False
sleep_in(False, True) → True
"""
def sleep_in(weekday, vacation):
    print("hello")

"""
PROBLEM 2
We have a loud talking parrot. 
The "hour" parameter is the current hour time in the range 0..23.
We are in trouble if the parrot is talking and the hour is before 
7 or after 20. Return True if we are in trouble.
"""
def parrot_trouble(talking, hour):
    print("hello")
    
    
"""
Problem 3
We have two monkeys, a and b, and the parameters a_smile and 
b_smile indicate if each is smiling. We are in trouble if 
they are both smiling or if neither of them is smiling. 
Return True if we are in trouble
"""

def monkey_trouble(a_smile, b_smile):
    print("hello")
    
"""
PROBLEM 4
Given a string, return a new string where "not " has been 
added to the front. However, if the string already begins with "not",
return the string unchanged.

not_string('candy') → 'not candy'
not_string('x') → 'not x'
not_string('not bad') → 'not bad'
"""

def not_string(str):
    print("hello")
    
    
"""
PROBLEM 5:
Given two strings, a and b, return the result of putting them 
together in the order abba, e.g. "Hi" and "Bye" returns "HiByeByeHi".

make_abba('Hi', 'Bye') → 'HiByeByeHi'
make_abba('Yo', 'Alice') → 'YoAliceAliceYo'
make_abba('What', 'Up') → 'WhatUpUpWhat'
"""
def make_abba(a,b):
    print("hello")
    

"""
PROBLEM 6:
Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".

hello_name('Bob') → 'Hello Bob!'
hello_name('Alice') → 'Hello Alice!'
hello_name('X') → 'Hello X!'
"""

def hello_name(name):
    print("hello")
    
    

"""
PROBLEM 7:
Given a string, return the string made of its first two chars, 
so the String "Hello" yields "He". 
If the string is shorter than length 2,
return whatever there is, so "X" yields "X", 
and the empty string "" yields the empty string "".

first_two('Hello') → 'He'
first_two('abcdefg') → 'ab'
first_two('ab') → 'ab'
"""
def first_two(str):
    print("hello")
    

"""
PROBLEM 8:
When squirrels get together for a party, 
they like to have cigars.
A squirrel party is successful when the number of cigars is 
between 40 and 60, inclusive. Unless it is the weekend, 
in which case there is no upper bound on the number of cigars. 
Return True if the party with the given values is successful, 
or False otherwise.

cigar_party(30, False) → False
cigar_party(50, False) → True
cigar_party(70, True) → True

"""
def cigar_party(cigar, is_weekend):
    print("hello")