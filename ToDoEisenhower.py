user_tasks = [None] * 25
updated_tasks = []
eishenhower_ranking = [30,29,28,25,24,23,20,19,18,27,22,17,26,21,16,15,14,13,10,9,8,12,11,7,6]

def menu(userChoice):
    while userChoice > 3 or userChoice < 0:
        print("\n")
        print("1) Add a task")
        print("2) Delete a task")
        print("3) View your task list")
        print("4) Quit")
        try:
            userChoice = int(input("-> "))
        except:
            continue
        
        print("")
        if userChoice == 1:
            addTask()
        elif userChoice == 2:
            deleteTask()
        elif userChoice == 3:
            viewTasks("no")
        else:
            break
    return


def addTask():
    userQuit = False
    while not userQuit:
        userTask = input("\nInput your task you would like to enter\n")

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
    viewTasks("yes")
    taskNum = 0
    # updatedList()
    while type(taskNum) is int:
        myRange = range(0,len(updated_tasks))
        try:
            taskNum = int(input("What task number would you like to delete? [press 0 to quit] "))
            if taskNum == 0:
                menu(4)
                return
            taskNum = taskNum - 1
            if taskNum in myRange:
                break
            else:
                continue
        except:
            print("Please write an integer number")
            continue

    #need to delete from user_tasks
    index = user_tasks.index(updated_tasks[taskNum])
    del user_tasks[index]
    del updated_tasks[taskNum]
    
    # print(updated_tasks)
    menu(4)
    return


def viewTasks(fromDelete):
    print("")
    updated_tasks.clear()
    for task in user_tasks:
        if task != None:
            updated_tasks.append(task)
    for i in range(len(updated_tasks)):
        print(str(i + 1) + ". " + updated_tasks[i])
        
    if fromDelete == "yes":
        return
    else:
        menu(4)
        return

# def updatedList():
#     for task in user_tasks:
#         if task != None:
#             updated_tasks.append(task)
#             print(updated_tasks)
#     return



print("Welcome to your todo list!")
userChoice = menu(4)
