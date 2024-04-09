#opening a text file and reading its contents

text_file_name=input("Enter the name of the file with .txt extension:")
file2=open(text_file_name,'r')
line=file2.readline()
while(line!=""):
    print(line)
    line=file2.readline()
file2.close()

