# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 13:08:08 2018

@author: I34852
"""

s=input("entre string")
l=len(s)
if (l%2)==0:
    if s[:l//2]==s[l:l//2-1:-1]:
        print("correct")
    else:
        print("incorrect")
else:
    print("invalid")