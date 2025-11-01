user_tasks = [None] * 25
# task_rankings = []
eishenhower_ranking = [30,29,28,25,24,23,20,19,18,27,22,17,26,21,16,15,14,13,10,9,8,12,11,7,6]                                                                                                                                                       

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
            viewTasks()
            break
        else:
            continue
    return


def deleteTask():
    viewTasks()
    print("What task would you like to delete?")
    return

def viewTasks():
    updated_tasks = []
    for task in user_tasks:
        if task != None:
            updated_tasks.append(task)
    
    for i in range(len(updated_tasks)):
        print(str(i + 1) + ". " + updated_tasks[i])
    return

print("Welcome to your todo list!")

userChoice = 4
while userChoice > 3 or userChoice < 0:
    print("1) Add a task")
    print("2) Delete a task")
    print("3) View your task list")
    try:
        userChoice = int(input())
    except:
        continue

if userChoice == 1:
    addTask()
elif userChoice == 2:
    deleteTask()
else:
    viewTasks()
