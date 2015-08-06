# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 18:51:00 2015

@author: Johannes Lade
"""

from __future__ import division
import numpy as np


class Sudoku(object):
    """
    Sudoku Class. Generates Sudokus to play and corrects them.
    """
    def __init__(self):
        self.map = np.array(9*[9*[0]])
        self.map_test = np.array(9*[9*[range(1,10)]])

    
    def insert_value(self,row,col,value):
        self.map[row,col] = value

    
    #Correction Algorhytmes
    #######################
    
    
    def list_multiples(self, array):
        """
        Lists all numbers of an array in a dictionary, with the numbers as
        keys and the their frequenzy as the values.
        """
        multiples = {}
        for i in array.flat:
            if i in multiples:
                multiples[i] += 1
            else:
                multiples[i] = 1
        return multiples
    
    
    def test_row_correct(self,row):
        """
        Tests if a row contains all digits from 1 to 9.
        """
        multiples = self.list_multiples(self.map[row])
        correct_row = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1}
        if multiples != correct_row:
            return False
        else:
            return True


    def test_col_correct(self, col):
        """
        Tests if a collumn contains all digits from 1 to 9.
        """
        multiples = self.list_multiples(self.map[:,col])
        correct_col = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1}
        if multiples != correct_col:
            return False
        else:
            return True

    
    def test_field_correct(self, a, b):
        """
        Tests if a 3x3 field contains all digits from 1 to 9.
        """
        multiples = self.list_multiples(self.map[3*a:3*a+3, 3*b:3*b+3])
        correct_field = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1}
        if multiples != correct_field:
            return False
        else:
            return True


    def test_sudoku_correct(self):
        """
        Tests if the sudoku is correct.
        """
        for row,i in enumerate(self.map):
            if self.test_row_correct(row) == False:
                return False
        for col,i in enumerate(self.map.transpose()):
            if self.test_col_correct(col) == False:
                return False
        for a in range(3):
            for b in range(3):
                if self.test_field_correct(a,b) == False:
                    return False
        return True

    
    #Reduction Algorhytmes
    ######################
    
    
    def reduce_cell(self,row,col,value):
        """
        Reduces the cell with the given coordinates by the given value.
        """
        
        values = list(self.map_test[row,col])
        if value in values:
            values.remove(value)
            values.append(0)
            self.map_test[row,col] = values


    def reduce_row(self,row,value):
        """
        Reduces all cells of the given row by the given value.
        """
        for col,i in enumerate(self.map[row]):
            self.reduce_cell(row,col,value)


    def reduce_col(self,col,value):
        """
        Recuces all cells of the given collumn by the given value.
        """
        for row, i in enumerate(self.map.transpose()[col]):
            self.reduce_cell(row,col,value)


    def reduce_field(self,a,b,value):
        """
        Reduces all cells of the given 3x3 field by the given value.
        """
        for row in range(3*a,3*a+3):
            for col in range(3*b,3*b+3):
                self.reduce_cell(row,col,value)
    
    
    def reduce_sudoku(self):
        """
        Reduces self.map_test based on the entries in self.map.
        """
        for row,i in enumerate(self.map):
            for col,i in enumerate(self.map.transpose()):
                value = self.map[row,col]
                if value != 0:
                    self.reduce_row(row,value)
                    self.reduce_col(col,value)
                    a = row%3
                    b = col%3
                    self.reduce_field(a,b,value)


    #Completion Algorhytmes
    #######################
    
    
    def complete_cell(self):
        """
        Tests if a cell has a unique solution and enters the solution into
        self.map.
        """
        pass

    def complete_sudoku(self):
        """
        Completes a sudoku with some entries given.
        """
        pass


#    def complete_row(self,row):
#        try:
#            if self.list_multiples(self.map[row])[0] == 1:
#                index = list(self.map[row]).index(0)
#                digit = 45 - self.map[row].sum()
#                self.map[row,index] = digit
#        except(KeyError):
#            pass    
#    
#    def complete_col(self,col):
#        try:
#            if self.list_multiples(self.map.transpose()[col])[0] == 1:
#                index = list(self.map.transpose()[col]).index(0)
#                digit = 45 - self.map.transpose()[col].sum()
#                self.map[index,col] = digit
#        except(KeyError):
#            pass    
#    
#    
#    def complete_field(self,a,b):
#        field = self.map[3*a:3*a+3, 3*b:3*b+3]
#        try:
#            if self.list_multiples(field.flatten())[0] == 1:
#                index = list(field.flatten()).index(0)
#                digit = 45 - self.field.flatten().sum()
##     correct           self.map[index,col] = digit
#        except(KeyError):
#            pass


    #Game Algorhytmes
    #################


    def generate_random_sudoku(self):
        """
        Generates a random correct sudoku.
        """
        l = 0
        k = 0
        self.map = np.array(9*[9*[0]])
        
        while not self.test_sudoku_correct():        
            digits = range(1,10)
            for row,i in enumerate(self.map):
                self.map[row] = np.random.choice(digits,size=9,replace=False)
            l += 1
            if l%1000 == 0:
                k += 1
                print k*1000
            if l > 10000:
                break


    def start_solver(self):
        """
        Asks for manual number input and completes the sudoku.
        """
        pass
        
    def start_game(self):
        """
        Starts an interactive game of sudoku.
        """
        print "Welcome to Johannes' Sudoku Player."
        answer = raw_input("Would you like to play? yes/no \r")
        while answer == "yes":
            print demo.map
            row = raw_input("Select row.\r")
            col = raw_input("Select collumn.\r")
            value = raw_input("Select value to insert.\r")
            self.insert_value(int(row),int(col),int(value))
            if 0 not in self.map:
                if self.test_sudoku_correct():
                    print "Very good. You just solved this sudoku. Game over."
                    return 1
                else:
                    print "Sorry, your solution is wrong."
                    return 0
        print "Have a nice day."
        return 0


if __name__ == "__main__":
    demo = Sudoku()
    demo.map = np.array([
        [4,8,7,3,2,6,1,5,9],
        [6,5,3,9,4,1,2,8,7],
        [1,2,9,8,5,7,4,3,6],
        [3,6,1,7,9,8,5,2,4],
        [5,9,4,2,1,3,7,6,8],
        [2,7,8,5,6,4,3,9,1],
        [7,1,5,6,3,9,8,4,2],
        [8,3,6,4,7,2,9,1,5],
        [9,4,2,1,8,5,6,7,3]
    ])
    demo.reduce_sudoku()
    print demo.map_test