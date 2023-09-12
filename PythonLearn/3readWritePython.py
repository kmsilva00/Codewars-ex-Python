import os

current_directory = os.getcwd()


file_path = current_directory+"/PythonLearn/text.txt"
print(file_path)

# with open(file_path, "w") as file:
#     file.write("aaaa")
    

lorem = "Amet proident veniam sit aliquip ipsum enim officia sint excepteur mollit culpa reprehenderit in. In ad cillum nostrud quis dolore sint nulla commodo eiusmod. Incididunt minim duis duis aute Lorem deserunt occaecat sint. Adipisicing ad ullamco veniam elit."

try:
    with open(file_path, "w") as file:
        file.write(lorem)
except(FileNotFoundError):
    print("local file cannot can be found")
except(Exception)as e:
    print(f"{e} error occured")

with open(file_path, "r") as file:
    for line in file:
        print(line)

#This doesn't work, because file.truncate() puts the file pointer at the end.
"""with open(file_path, "r+")as file:
    inicontent = file.read()
    file.seek(10)
    file.truncate()
    content = file.read()
    file.write(inicontent + "\n" + content)
"""
with open(file_path, "r+")as file:
    inicontent = file.read()
    file.seek(10)
    file.truncate()
    file.seek(0)
    content = file.read()
    file.write(inicontent + "\n" + content)
    
    

        
#read
#readline, reads a single line
#readlines, reads all lines from the file and returns it as a list of strings
#read().strip()
#
#write
#writelines
#   lines = ["Line 1", "Line 2", "Line 3"]
#   file.writelines(lines)
#    
#
#with open(file_path, 'r') as file:
#    file.seek(10)  # Moves the pointer to the 11th byte in the file
#    content = file.read()
#
#with open('file.txt', 'r+') as file:
#    file.seek(10)
#    file.truncate() #Truncates the file at the current position, removing content beyond that point.
#
#content = file.read()
#then modify content