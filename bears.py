with open("Python Restart\bears.txt", "r") as myfile:
        content = myfile.read()
       
print(content)

with open("bears2.txt", "a+") as myfile2:
        loop = "aa"
        for a in loop:
            myfile2.write(content + "\n")


