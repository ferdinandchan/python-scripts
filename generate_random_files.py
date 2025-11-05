#!/usr/bin/env python3
"""
Script to generate random text files with variable sizes in a given folder.

Usage: python3 generate_random_files.py <folder_path> <num_files> <max_size_kb>

Arguments:
    folder_path: Directory where files will be created, directory will be created automatically if it does not exist
    num_files: Number of files to generate
    max_size_kb: Maximum size of each file in kilobytes
"""


"""
Belows are a list of libraries/modules that we import to help us.
Think of them as "reusable code" that someone already written and tested.
It is very common to "import" libraries/modules so we don't "reinvent the wheel"
"""
import os
import sys
import random
import string
from pathlib import Path


"""
This function generate a random content with the specified size in bytes. 
The generated content will be a mix of words, sentences, and paragraphs for more realistic text
"""
def generate_random_text(size_bytes):
    
    # The array of "word" that this function will randomly pick when generating the content
    word_library = [
        'lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetur', 'adipiscing', 
        'elit', 'sed', 'do', 'eiusmod', 'tempor', 'incididunt', 'ut', 'labore',
        'et', 'dolore', 'magna', 'aliqua', 'enim', 'ad', 'minim', 'veniam',
        'quis', 'nostrud', 'exercitation', 'ullamco', 'laboris', 'nisi', 'ut',
        'aliquip', 'ex', 'ea', 'commodo', 'consequat', 'duis', 'aute', 'irure',
        'dolor', 'in', 'reprehenderit', 'voluptate', 'velit', 'esse', 'cillum',
        'fugiat', 'nulla', 'pariatur', 'excepteur', 'sint', 'occaecat',
        'cupidatat', 'non', 'proident', 'sunt', 'culpa', 'qui', 'officia',
        'deserunt', 'mollit', 'anim', 'id', 'est', 'laborum'
    ]
    
    # Two local variables that help us keep track of what we have got so far

    # content is an array that stores the word(s) that we picked so far
    content = []
    # current_size keep track of the size of string stored in 'content'
    current_size = 0
    
    # Use a while loop to keep adding words to content while the 'current_size' is still less than our target 'size_bytes'
    while current_size < size_bytes:

        # We start by randoming picking whether we want to 
        # - add a word to the content, or
        # - add a sentence end, or
        # - add a paragraph break
        choice = random.choices(
            ['word', 'sentence_end', 'paragraph_break'], 
            weights=[85, 10, 5] # weights means how likely certain things will get pick
        )[0]
        
        # if the random choice is `word`, randomly pick a word from the word_library
        if choice == 'word':
            word = random.choice(word_library)

            # if content is not "empty" AND NOT ends with one of those special characters, prefix the selected word with a "whitespace"
            if content and not content[-1].endswith(('\n', '. ', '? ', '! ')):
                word = ' ' + word
            
            # Add the word to the existing content and increment the current_size by the length of the word (we are assuming one character is one byte)
            content.append(word)
            current_size += len(word)
            
        # if the random choice is 'sentence_end', add one of the punctuation, followed by a whitespace
        elif choice == 'sentence_end':
            punctuation = random.choice(['.', '!', '?'])
            content.append(punctuation + ' ')
            current_size += 2

        # if the random choice is 'paragraph_break', add a newline special character
        elif choice == 'paragraph_break':
            content.append('\n\n') # just trust me this is newline :) 
            current_size += 2
    
    # Once the while loop is finish, we know that we have a bunch of words stored in "content" array
    # Now we need to "join" them together to make it a single "string" and also trim the size to the target size
    # Join content and trim to exact size
    text = ''.join(content)
    return text[:size_bytes]

"""
This function create a new file with random content. It takes three arguments
- folder_path - where to store this new file
- file_index - a integer that help us avoid duplicate file name issue
- max_size_kb - the maximum size of the file to be generated

Once the file is created, it will return the name of the file and the size of the file
"""
def create_random_file(folder_path, file_index, max_size_kb):
    # Generate random size between 1KB and max_size_kb
    # Ignore the difference between KB and bytes for now :)
    size_kb = random.randint(1, max_size_kb)
    size_bytes = size_kb * 1024
    
    # Generate filename
    # Note for :04d, this is a special formatter that format an integer with a minimum width of 4 digits, e.g. 3 will become 0003
    filename = f"random_file_{file_index:04d}.txt"
    file_path = folder_path / filename
    
    # Generate content using the function we created above
    content = generate_random_text(size_bytes)
    
    # Write file. This is a two step process
    # First, it create the file using the "open" function
    # Then, it write the content into the file and save the file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    # Return the name of the file and the size
    return filename, size_kb


"""
This is the entry point of this python script!
If you want to trace the logic of this script, this is where you should start
"""
def main():

    """
    This script start by making sure user have provided all necessary arguments.
    Arguments are like options or settings that the user can use to modify the behavior of this script.
    For this script we expect three arguments

    - folder_path
    - num_files
    - max_size_kb

    All arguments are mandatory and the script will quit if any is missing
    """
    
    # Check arguments
    # sys.argv contains the arguments that user pass when they call this script via 'python3'
    # The first argument will be the name of the script
    if len(sys.argv) != 4:
        print("Usage: python3 generate_random_files.py <folder_path> <num_files> <max_size_kb>")
        print("\nArguments:")
        print("  folder_path: Directory where files will be created")
        print("  num_files: Number of files to generate")
        print("  max_size_kb: Maximum size of each file in kilobytes")
        sys.exit(1)
    
    # After we count that we have received 3 arguments, we continue to check their "type"
    # folder_path must be a valid path, it should be in the format of "/xxxx"
    # num_files must be an integer
    # max_size_kb must be an integer
    #
    # This script will quit if any argument does not match its type
    try:
        folder_path = Path(sys.argv[1])
        num_files = int(sys.argv[2])
        max_size_kb = int(sys.argv[3])
    except ValueError:
        print("Error: num_files and max_size_kb must be integers")
        sys.exit(1)
    
    # Validate arguments
    #
    # We also want to make sure the value of the int argument make sense, i.e. they must be non-negative 
    if num_files <= 0:
        print("Error: num_files must be positive")
        sys.exit(1)
    
    if max_size_kb <= 0:
        print("Error: max_size_kb must be positive")
        sys.exit(1)
    
    """
    
    After we validate and make sure we have all valid arguments. 
    We start to do the real work.

    First is to make sure the "target folder" exists, if it doesn't we will try to create it
    """
    # Create folder if it doesn't exist
    try:
        folder_path.mkdir(parents=True, exist_ok=True) # mkdir will create the folder if it does not exists
    except Exception as e:
        print(f"Error creating folder {folder_path}: {e}")
        sys.exit(1)
    
    """
    
    Once we have the destination folder, we start to create file that contain randomly generated content
    
    It is a good practice to always give the user informed about what we are doing by printing out some messages like below
    """
    # Generate files
    print(f"Generating {num_files} random text files in '{folder_path}'...")
    print(f"Maximum file size: {max_size_kb} KB")
    print("-" * 50)
    
    
    """
    
    Mini quiz -> can you try figure out what the below logic does and write a short comment? :) 
    """
    total_size = 0
    for i in range(1, num_files + 1):
        try:
            filename, size_kb = create_random_file(folder_path, i, max_size_kb)
            total_size += size_kb
            print(f"Created: {filename} ({size_kb} KB)")
        except Exception as e:
            print(f"Error creating file {i}: {e}")
    
    print("-" * 50)
    print(f"Successfully generated {num_files} files")
    print(f"Total size: {total_size} KB ({total_size / 1024:.2f} MB)")


if __name__ == "__main__":
    main()