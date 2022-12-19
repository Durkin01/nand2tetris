import sys
import os
import Tokenizer
import CompilationEngine

def main():

    path = sys.argv[1]
    directory = False

    # If directory
    if os.path.isdir(path):
        directory = True

        files = os.listdir(path)
        file_list = []
        for file in files:
            if file[-5:] == '.jack':
                file_list.append(file)

        # ???
        file_name = path
        if path[:1] == '/':
            file_name = file_name[1:]
        if file_name[-1:] == '/':
            file_name = file_name[:-1]
        
        os.chdir(path)

    # If file
    else:
        file_name = path[:-5]
        file_list = [sys.argv[1]]

    for file in file_list:
        tokenizer = Tokenizer.JackTokenizer(file)
        CompilationEngine.CompilationEngine(tokenizer, file + "_mine")


if __name__ == "__main__":
    main()         