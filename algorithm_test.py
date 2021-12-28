# -*- coding: utf-8 -*-
"""Algorithm_test .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/149tHy8rg05eePiMhw71D-e-Xhxt0GezW
"""

import numpy as np
a_temp = ([[1 ,2 ,3 ,4 ,5],
              [16,17,18,19,6],
              [15,22,21,20,7],
              [14,23,24,25,8],
              [13,12,11,10,9]])

a = np.array([[5 ,18 ,16 ,14 ,6],
              [4,19,23,21,7],
              [3,11,10,9,8],
              [2,12,24,25,22],
              [1,13,15,17,20]])

def input_matrix():
  row = int(input("Enter the number of rows:"))
  col = int(input("Enter the number of columns:"))

  # Initialize matrix
  matrix = []
  print("Enter the entries rowwise:")
    
  # input
  for i in range(row):          
      input_array =[]
      for j in range(col):      
          input_num = int(input())
          while (input_num > row*col) or (input_num <= 0):
            print("Enter the number again ( 1 to ", row*col, ")")
            input_num = int(input())
          input_array.append(input_num)
      matrix.append(input_array)
  matrix = np.array(matrix)
  print("matrix : ")
  print(matrix)
  return matrix, row, col

def find_max_sequence(matrix, row, col):
  start = matrix.min()
  max_value = 1
  #position = np.where(a==start)
  #print("position : ", position)
  #first = int( position[0])
  #second = int( position[1])
  check = False

  for i in range(start,row*col):
      if check == False:
          max_temp = 1
      check = False
      
      position = np.where(matrix==i)

      try:
        first = int(position[0])
        second = int(position[1])

        #check_up
        if (first - 1) < 0:
            pass
        else:
            first_temp = first - 1
            second_temp = second
            if i+1 == matrix[first_temp][second_temp]:
                max_temp = max_temp+1
                check = True
                
        #check_down
        if (first + 1) > (row-1):
            pass
        else:
            first_temp = first + 1
            second_temp = second
            if i+1 == matrix[first_temp][second_temp]:
                max_temp = max_temp+1
                check = True

        #check_right
        if (second + 1) > (col-1):
            pass
        else:
            first_temp = first
            second_temp = second + 1
            if i+1 == matrix[first_temp][second_temp]:
                max_temp = max_temp+1
                check = True

        #check_left
        if (second - 1) < 0:
            pass
        else:
            first_temp = first
            second_temp = second - 1
            if i+1 == matrix[first_temp][second_temp]:
                max_temp = max_temp+1
                check = True

        if max_temp > max_value:
            max_value = max_temp 

      except:
        pass
  return max_value
matrix, row, col = input_matrix()
value = find_max_sequence(matrix, row, col)
print('max_value: ', value)