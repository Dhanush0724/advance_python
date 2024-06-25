def count_words(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            line_count = len(lines)
            word_count = 0
            for line in lines:
                words = line.split()
                print(words)
                word_count +=len(words)
            print(f"number of lines: {line_count}")
            print(f"Number of words :{word_count}")
    except FileNotFoundError:
        print("error")

filename = 'a.txt'
count_words(filename)