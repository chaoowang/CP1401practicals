import os
import shutil

def main():
    extentions_to_category={}
    os.chdir("FilesToSort2")
    for filename in os.listdir("."):
        if os.path.isdir(filename):
            continue
        extension = filename.split(".")[-1]

        if extension not in extentions_to_category:
            category=input("What category would you like to sort {} files into? ".format(extension))
            extentions_to_category[extension]=category

            try:
                os.mkdir(category)
            except FileExistsError:
                pass
        shutil.move(filename, extentions_to_category[extension])


main()