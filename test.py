"""
Creating a 26.02.2023 10:55 code in a file `test`
Author: Igor Nezhivykh
Description: 
"""
import os

os.environ.setdefault('XCV1', 'X<A1')
os.environ.setdefault('XCV2', 'X<A2')
os.environ.setdefault('XCV3', 'X<A3')

print(os.environ['XCV3'])
