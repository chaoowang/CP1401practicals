def main():
    word_to_count={}
    text=input("Text:")
    words= text.split()
    for word in words:
        times= word_to_count.get(word,0)
        word_to_count[word]=times+1
    words=list(word_to_count.keys())
    words.sort()
    max_len=max(len(word) for word in words)
    for word in words:
        print("{:{}} : {}".format(word, max_len, word_to_count[word]))


if __name__ == '__main__':
    main()