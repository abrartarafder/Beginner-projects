# Beginner-projects


Some projects I've worked on as a beginner when I first started coding. 


# Calculators in Different Languages

I think that the best way to learn a language is learning how to build a calculator in that language.

# TicTacToe game

Simple TicTacToe game in python made just for fun -- some parts still incomplete.


# Binary-Search-Code-Project-1

A quick explanation of binary search line by line with the code in PYTHON. 

Essentially the function is defined with the parameters values, to find, start index and end index. Values represents the list that will be provided by the user, to find is the value that is to be found, the start index will be the start of values which is 0 β because in code we start from 0 and the index at 0 will be the start of the list. Finally, the end index will be len(values) - 1 which essentially represents the end of the list. Len is a function in Python which counts the number of elements in the list and the -1 accurately represents the index of the last value since we start from 0. So if a list has 5 values its indexes would look like - 01234 where len(values) is equal to 5 and -1 would give us index 4 which is the last index of the list. To begin with, we start with the base case because binary search is a recursive function(function that calls itself) so we must start with a base case (also known as exit condition). The typical base case in this type of problem according to pseudo code would be to return false if the start index is greater than the end index - - essentially in simple terms the way I think about it is that if a list is empty itβs start index will be 0 and len([]) - 1 will return -1 which is obviously less than 0. So basically if a list is empty then it returns false. The next line of code that we see defines a index variable called middle by adding the start and end index and floor division by 2 (floor division, represented by β//β is just a special kind of division which rounds down so essentially 5//2 would result in 2.5 but due to floor division would essentially be rounded to 2. Binary search uses the middle variable specifically because it starts it search from the middle. So the next line refers to the value being searched for being equal to the value at the middle index. If the value that we are searching for equals to the value at the middle index then the search is complete. Ie - looking for 4 list has [1,2,3,4,5,6,7] then we return true right away no need to keep going. Otherwise if the to find value is less than the value at the middle then we only look at the first part of the list which is shown in the next bit of recursive code calling the function from the start index up to the middle-1. In the example if we were looking for 2 then it looks at 123 otherwise the last bit of code is if the value is greater than the middle then it would look at the value greater than the middle value all the way to the end index so 567 in the case of the same list. This way we can find specific values inside of the list. 

# Binary-Search-Tree

Finding the left right index nodes in Python implemented as array

# Insertion Sort Project

Another DSA Algorithm learned in python and trying to implement it. 

# Cardgame

Worked on a cardgame for a lab and uploaded

# Regex 

Basic regular expression checker which checks if a phone number entered by user is valid.

list of valid phone numbers include:

_ _ _ - _ _ _ - _ _ _ _ , _ _ _ _ _ _ _ _ _ _ , ( _ _ _ )_ _ _ _ _ _ _ , ( _ _ _ ) - _ _ _ - _ _ _ _ , ( _ _ _ )_ _ _ - _ _ _ _ , +_ - _ _ _ - _ _ _ - _ _ _ _ , +_ ( _ _ _ )_ _ _ -_ _ _ _ , +_ _ _ _ _ _ _ _ _ _ _ , _ _ _ _ _ _ _ _ _ _ _

this takes into account country codes, area codes, parenthesis --> the code assumes that dashes and parenthesis are consistent

** The python code takes spaces into account as well!


# RockpaperScissors 

Rock paper Scissors game

# Number Guess

Number guessing in python and c++

# Coin Toss Guessing Game 

A simple coin toss game that simulates tossing a coin, if the user guesses heads or tails before the toss correctly, they get a point. The final score is returned after 5 attempts as a percentage and the total number of correct answers.
