name = input("what is your name?")

student_ID = input("What is your Student ID?")

score = []
while True:
    input_score = int(input("Please, type your score:"))
    score.append(input_score)
    yn = input("Is that all?")

    if yn == "y":
        avg = sum(score)/len(score)
        print('\n' + name + ', ('+student_ID+'), your average score is '+str(round(avg, 2))+' and the highest score is '+ str(max(score))+'.')
        break
    elif yn != "n":
        print('잘못 입력하셨습니다. 다시 입력해주세요')