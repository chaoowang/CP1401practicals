from prac_06.ProgrammingLanguage import ProgrammingLanguage

def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(python)
    languages=[]
    languages.append(ruby)
    languages.append(python)
    languages.append(visual_basic)

    dynamic_typing_languages=[]
    for language in languages:
        if language.is_dynamic():
            dynamic_typing_languages.append(language.name)
    print("The dynamically typed languages are:")
    for language in dynamic_typing_languages:
        print(language)
if __name__ == '__main__':
       main()