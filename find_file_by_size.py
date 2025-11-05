#!/usr/bin/env python3

"""
Script to find files in a specific folder which are larger than the given size

Usage: python3 find_file_by_size.py <folder_path> <min_size_kb>

Arguments:
    folder_path: Directory where this script should search for the files
    min_size_kb: The minimise size of the file that should be included in the result


The output of this script will be something like

>
> python3 find_file_by_size.py ./someFolder 1000
Searching for file(s) larger than 1000kb in folder 'someFolder'
-----------------------------------------------------------------
-> xxxx.txt (2020 KB)
-> aaa.txt (2133 KB)
-> bbbbbbb.txt (100000 KB)
-> e.txt (2222 KB)
-> ccccc.txt (434323223 KB)
-> xxxsssssssx.txt (3333333 KB)
-----------------------------------------------------------------

Scanned 23 files
File meeting the criteria 6


"""

"""
If you want to import something, put them under this comment
"""



"""
This is the entry point of this python script!
"""
def main():

    """
    TODO:

    Step 1 ---> Can you start by making sure user provided the necessary arguments?
    """



    """
    TODO:

    Step 2 ----> Can you make the arguments are valid? both the type and the value?
    """



    """
    TODO:

    Step 3 -----> Start by writing code that will "open the folder"? 
    """


    """
    TODO:

    Step 4 -----> Once you have the folder, you will need two things

    1) Think about how many things you want to keep track of? and create variable for each things you want to keep track?
    2) A logic to check if the file size is greater than a value, maybe write this as a function?
    3) Have some logic that will loop / iterate through all the files in the folder, and use the function you wrote in 1
       to check if the file meet the criteria?
    """


    print("Searching for file(s). - To be implemented")



if __name__ == "__main__":
    main()