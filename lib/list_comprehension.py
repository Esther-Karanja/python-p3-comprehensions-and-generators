#!/usr/bin/env python3

def return_evens(num_list):
  new_list =[None if i%2!=0 else i for i in num_list if i%2==0]
  return (new_list)

return_evens([0, 1, 3, 5, 7, 8, 9])


def make_exclamation(sentence_list):
  new_list=[None if i==None else i+'!' for i in sentence_list]
  return (new_list)

make_exclamation(["Hello", "I'm doing great", "Python is fun"])