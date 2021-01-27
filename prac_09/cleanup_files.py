"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import shutil
import os


def main():
    """Demo os module functions."""
    print("Starting directory is: {}".format(os.getcwd()))

    # Change to desired directory
    os.chdir('Lyrics/Christmas')

    # Print a list of all files in current directory
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    # Make a new directory
    # The next time you run this, it will crash if the directory exists
    try:
        os.mkdir('temp')
    except FileExistsError:
        pass
    # Loop through each file in the (current) directory
    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue

        new_name = get_fixed_filename(filename)
        print("Renaming {} to {}".format(filename, new_name))


def fix_filename_step_one(filename):
    """Return a 'fixed' version of filename."""
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")

    for i, char in enumerate(new_name):
        try:
            if new_name[i].isalpha() and new_name[i].islower():
                if new_name[i + 1].isalpha() and new_name[i + 1].isupper():
                    new_name = new_name[:i + 1] + "_" + new_name[i + 1:]
        except IndexError:
            pass
    return new_name


def fix_filename_step_two(filename):
    new_name = filename
    for i, char in enumerate(new_name):
        try:
            if new_name[i] == "_" and new_name[i + 1].islower():
                new_name = new_name[:i + 1] + new_name[i + 1].upper() + new_name[i + 2:]
        except IndexError:
            pass
    return new_name


def demo_walk():
    """Process all subdirectories using os.walk()."""
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        # print("Directory:", directory_name)
        # print("\tcontains subdirectories:", subdirectories)
        # print("\tand files:", filenames)
        # print("(Current working directory is: {})".format(os.getcwd()))

        for filename in filenames:
            old_name = os.path.join(directory_name, filename)
            fix_name = os.path.join(directory_name, fix_filename_step_one(filename))
            new_name = os.path.join(directory_name, fix_filename_step_two(fix_name))
            os.renames(old_name, new_name)


demo_walk()
