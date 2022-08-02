# creates a basic file-copy function

def copyFile(fileName, newFileName):
    with open(fileName) as file:
        content = file.read()

    with open(newFileName, "w") as new_file:
        new_file.write(content)

# copyFile("msg.txt","new-msg-txt")

# the function that prints a text file reversely
def reverseText(fileName, newFileName):
    with open(fileName, encoding="utf-8") as file:
        content = file.read()
    
    with open(newFileName, "w", encoding="utf-8") as new_file:
        new_file.write(content[::-1])

reverseText("msg.txt", "reversed-txt")

# info about a text file
def info(fileName):
    with open(fileName) as file:
        lines = file.readlines()

    result = {
        "lineNum": len(lines),
        "wordNum": sum(len(line.split(' ')) for line in lines),
        "charNum": sum(len(line) for line in lines)
    }

    return result

print(info("msg.txt"))