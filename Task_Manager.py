import pickle

def Print_Task(task):
    print("\n--------------------------------------")
    print("Title is : ",task[0])
    print("Description is : ",task[1])
    print("Due Date is : ",task[2])

class Task_Manager:
    def __init__(self):
        self.Task_List = []
    
    def Add_Task(self):
        temp = []
        temp.append(input("Enter the       Title : "))
        temp.append(input("Enter the Description : "))
        temp.append(input("Enter the    Due Date : "))
        self.Task_List.append(temp)
        print("Add Task Successful")

    def Search_Task(self):
        temp = input("Enter the Title : ")
        for task in self.Task_List:
            if temp in task:
                Print_Task(task)
                break
        else:
            print("This Title name is not found in the Database")

    def View_All_Task(self):
        for task in self.Task_List:
            Print_Task(task)
        if self.Task_List == [] :
            print("Database Empty")

    def Delete_Task(self):
        title = input("Enter the Title : ")
        for task in self.Task_List:
            if title in task:
                self.Task_List.remove(task)
                print("Deletion is Successful")
                break
        else:
            print("This Title name is not found in the database")

    def Load_Task(self):
        try:
            with open("Task_Manager.txt",'rb') as file:
                self.Task_List.clear()
                for task in pickle.load(file):
                    self.Task_List.append(task)
        except FileNotFoundError :
            print("You open this project first time")
            print("Firstly add new Task")
            self.Add_Task()

    def Unload_Task(self):
        with open("Task_Manager.txt",'wb') as file:
            for task in self.Task_List:
                pickle.dump(task, file)

    def Main_Menu(self):
        self.Load_Task()
        while True:
            print()
            print("Enter 1 For Add       Task")
            print("Enter 2 For Search    Task")
            print("Enter 3 For Print All Task")
            print("Enter 4 For Delete    Task")
            print("Enter 5 For Exit this App ")
            choice = int(input("Enter a Choice : "))
            match choice:
                case 1:
                    self.Add_Task()
                case 2:
                    self.Search_Task()
                case 3:
                    self.View_All_Task()
                case 4:
                    self.Delete_Task()
                case 5:
                    self.Unload_Task()
                    print("Thank you for using this Application")
                    break
                case _:
                    print("Enter valid Choice")


Task_Manager().Main_Menu()
