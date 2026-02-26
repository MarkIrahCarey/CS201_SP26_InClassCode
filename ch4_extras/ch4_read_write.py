"""
with open('story.txt', 'r') as f:
    # read entire file
    # print(f.read())

    # for loop
    for line in f:
        if "Mark" in line:
            sentence = line.split(" ")
            
            print(sentence)
            for index in range(len(sentence)):
                if "Mark" == sentence[index]:
                    sentence[index] = "Stinky"
            print(" ".join(sentence))
        else:
            print(line)


with open("new_file.txt", "w") as f:
    f.write("Hello World!!!!!!\n")
    f.write(" I am in a text file!!!")
    for i in range(1, 101):
        f.write(f"{i} \n")
"""   

# you can next a read and write
with open('story.txt', 'r') as f:
    # read entire file
    # print(f.read())

    new_story = " "
    # for loop
    for line in f:
        new_line = line
        if "Mark" in line:
            sentence = line.split(" ")
            
            print(sentence)
            for index in range(len(sentence)):
                if "Mark" == sentence[index]:
                    sentence[index] = "Stinky"
            new_line = " ".join(sentence)
        
        new_story += f"{new_line} \n"
    
    with open("new_story.txt", "w") as file:
        file.write(new_story)

    
