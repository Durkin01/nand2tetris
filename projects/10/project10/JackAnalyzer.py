#!/usr/bin/env python3
import sys
import os
import Tokenizer

# Jack Analyzer
class JackAnalyzer():

    @staticmethod
    def use(arg):

        directory = 0

        if arg[-5:] != '.jack':
            files = os.listdir(sys.argv[1])
            file_list = []
            for file in files:
                if file[-5] == '.jack':
                    file_list.append(file)

            file_name = arg
            if arg[:1] == '/':
                file_name = file_name[1:]
            if file_name[-1:] == '/':
                file_name = file_name[:-1]
            
            directory = 1

        else:
            file_name = arg[:-5]
            file_list = [sys.argv[1]]



        for file in file_list:
            with open(file_name + '/'):

            
