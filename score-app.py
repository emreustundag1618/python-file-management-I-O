# compute student score
def computeScore(line):
    line = line[:-1]
    list_ = line.split(':')

    studentName = list_[0]
    scores = list_[1].split(",")

    score1 = int(scores[0])
    score2 = int(scores[1])
    score3 = int(scores[2])

    mean = (score1 + score2 + score3) / 3

    if mean>=90 and mean<=100:
        score = "AA"
    elif mean>=85 and mean<=89:
        score = "BA"
    elif mean>=80 and mean<=84:
        score = "BB"
    elif mean>=75 and mean<=79:
        score = "CB"
    elif mean>=70 and mean<=74:
        score = "CC"
    elif mean>=65 and mean<=69:
        score = "DC"
    elif mean>=60 and mean<=64:
        score = "DD"
    elif mean>=50 and mean<=59:
        score = "FD"
    else:
        score = "FF"

    return studentName + ": " + score + "\n"

def readMeans():
    with open("scores.txt","r",encoding="utf-8") as file:
        for line in file:
            print(computeScore(line))

def addScore():
    name = input("Student's name: ")
    surname = input("Student's lastname: ")
    score1 = input("Score 1: ")
    score2 = input("Score 2: ")
    score3 = input("Score 3: ")

    with open("scores.txt", "a", encoding="utf-8") as file:
        file.write(name + ' ' + surname + ' ' + score1 + ' ' + score2 + ' ' + score3+'\n')

def recordScore():
    with open("scores.txt", "r", encoding = "utf-8") as file:
        list_ = []

        for i in file:
            list_.append(computeScore(i))

        with open("results.txt", "w", encoding = "utf-8") as file2:
            for i in list_:
                file2.write(i)

while True:
    option = input("1- Read scores\n2- Add Score\n3- Record Score\n4- Exit\n")

    if option=="1":
        readMeans()
    elif option=="2":
        addScore()
    elif option=="3":
        recordScore()
    else:
        break