
def write_sentence(sentences,filename):
    try:
        with open(filename,'w') as file:
            for sentence in sentences:
                file.write(sentence.strip()+'\n')
        print("sentence succesfully written")
    except Exception as e:
        print(e)

sentences = [
    "The James The Trademark",
    "i work for jwing academy",
    "james the ghost"
]
filename = "sentence.txt"
write_sentence(sentences,filename)