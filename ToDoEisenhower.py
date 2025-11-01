user_tasks = [None] * 25
# task_rankings = []
eishenhower_ranking = [30,29,28,25,24,23,20,19,18,27,22,17,26,21,16,15,14,13,10,9,8,12,11,7,6]                                                                                                                                                       

def menu(userChoice):
    while userChoice > 3 or userChoice < 0:
        print("")
        print("1) Add a task")
        print("2) Delete a task")
        print("3) View your task list")
        print("4) Quit")
        try:
            userChoice = int(input())
        except:
            continue
        
        print("")
        if userChoice == 1: 
            addTask()
        elif userChoice == 2:
            deleteTask()
        elif userChoice == 3: 
            viewTasks()
        else:
            break
    return


def addTask():
    userQuit = False
    while not userQuit:
        userTask = input("Input your task you would like to enter\n")

        importance = -1
        urgent = -1
        while importance > 5 or importance < 1:
            try:
                importance = int(input("How important is your task on a scale from 1-5? "))
            except:
                continue
        while urgent > 5 or urgent < 1:
            try:
                urgent = int(input("How urgent is your task on a scale from 1-5? "))
            except:
                continue

        urgent = urgent * 5
        taskRanking = urgent + importance

        index = eishenhower_ranking.index(taskRanking)
        user_tasks.insert(index, userTask)

        userContinue = input("Would you like to enter another task? [yes/no] ")
        userContinue = userContinue.lower()
        if userContinue == "no":
            menu(4)
            break
        else:
            continue
    return


def deleteTask():
    taskNum = 0
    while int(taskNum):
        try:
            taskNum = int(input("What task number would you like to delete?"))
            if taskNum in range(len(user_tasks)):
                break
            else:
                continue
        except:
            print("Please write an integer number")
            continue
    del user_tasks[taskNum + 1]
    menu(4)
    return


def viewTasks():
    print("")
    updated_tasks = []
    for task in user_tasks:
        if task != None: 
            updated_tasks.append(task)
    
    for i in range(len(updated_tasks)):
        print(str(i + 1) + ". " + updated_tasks[i])
    menu(4)
    return



print("Welcome to your todo list!")
userChoice = menu(4)