# Using function 
import os
import time


def createfile():
    fileName = input("File name : ")
    
    # Checking file if exist or not
    if os.path.exists("{}.txt".format(fileName)):
        print("The file exists and system will remove it!")
        os.remove("{}.txt".format(fileName))
        time.sleep(2)
        print("Removed!")
        fileName = input(" New file name : ")
        print("Creating a new file ")
        f = open(f"{fileName}.txt", "x")
        time.sleep(2)
        print("Done!")
    else:
        f = open(f"{fileName}.txt", "x")

def writecontent():
    fileName = input("File name : ")
    
    # Checking file if exists or not
    if os.path.exists("{}.txt".format(fileName)):
        f = open(f"{fileName}.txt", "w")
        content = input("Enter the content inside the file : \n ")
        f.write(content)
        f.close()
    else:
        # Writing new file
        f = open(f"{fileName}.txt" "w")
        content = input("Enter the content insided the file : \n")
        f.write(content)
        f.close()

def deletecontent():
    for x in os.listdir():
        print(x)
    
    fileName = input("File name : ")
    if os.path.exists("{}.txt".format(fileName)):
        os.remove("{}.txt".format(fileName))
    else:
        print("{}.txt does not exist!".format(fileName))

def readcontent():
    for x in os.listdir():
        print(x)

    fileName = input("File name : ")
    if x.endswith(".txt"):
        f = open(f"{fileName}.txt", "r")
        print(f.read())
    else:
        print(f"{fileName}.txt does not exist!")
    
def listdirectory():
    print("List of directory : ")
    for x in os.listdir():
        print(x)
    
if __name__ == '__main__':
    # Looping menu 
    while True:
        # Banner
        print("---------- MENU ----------")
        print("\t1. Create File ")
        print("\t2. Write File ")
        print("\t3. Delete File ")
        print("\t4. Read File ")
        print("\t5. List Directory ")
        print("\t6. Exit ")
        print("--------------------------")

        userInput = int(input("Choose (1/2/3/4/5/6) : "))
        
        # Checking user input
        if userInput == 1:
            createfile()
        elif userInput == 2:
            writecontent()
        elif userInput == 3:
            deletecontent()
        elif userInput == 4:
            readcontent()
        elif userInput == 5:
            listdirectory()
        elif userInput == 6:
            break
        else:
            print("Error")
