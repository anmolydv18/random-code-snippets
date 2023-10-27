#kbc
# a list 
#     a list of questions, their options and the correct answer
# a list to store the score

allQuestions = [
    ["1) question 1","option1","option2","option3","option4",1],
    ["2) question 2","option1","option2","option3","option4",1],
    ["3) question 3","option1","option2","option3","option4",1],
    ["4) question 4","option1","option2","option3","option4",1],
    ["5) question 5","option1","option2","option3","option4",1],
    ["6) question 6","option1","option2","option3","option4",1],
    ["7) question 7","option1","option2","option3","option4",1],
    ["8) question 8","option1","option2","option3","option4",1],
    ["9) question 9","option1","option2","option3","option4",1],
    ["10) question 10","option1","option2","option3","option4",1],
    ["11) question 11","option1","option2","option3","option4",1],
    ["12) question 12","option1","option2","option3","option4",1],
    ["13) question 13","option1","option2","option3","option4",1],
    ["14) question 14","option1","option2","option3","option4",1],
    ["15) question 15","option1","option2","option3","option4",1]
]
currentScore=0
score=[10,20,40,80,160,320,640,1280,2560,5120,10240,20480,40960,81920,70000000]

print("welcome to the game \nhere are your questions:\n\n")

for  i in range(0,len(allQuestions)):
    question=allQuestions[i]
    print(f"\n{question[0]}")
    print("enter 1,2,3,4 to select the option or enter 'quit' to quit the game")
    print(f"{allQuestions[i][1]} \t\t {allQuestions[i][2]}" )
    print(f"{allQuestions[i][3]} \t\t {allQuestions[i][4]}" )
    answer=input()
    # if i==6:
    #     currentScore=score[5]
    # if i==11:
    #     currentScore=score[10]
    if answer=="quit":
        print("your current score is: ", currentScore)
        break
    elif int(answer)==allQuestions[i][-1]:
        print("correct answer")
        currentScore=score[i]
        print("your score is: ", currentScore)
    elif not int(answer) == question[-1]:
        print("wrong answer\nthanks for playing")
        if i<5:
            print("your score is: 0  ")
        elif i>=5 and i<=10:
            print("your score is:",score[5])
        elif i>10:
            print("your score is:",score[10])
        break
    
        


        



