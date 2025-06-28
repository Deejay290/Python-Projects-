""" Components: The Menu, Input, 
"""
def To_Do_Menu():
  print("----TO DO LIST----")
  print("----1: Add a task")
  print("----2: Show a task")
  print("----3: Delete Task")



def To_Do_Options():
  task_list = []
  while True:
    To_Do_Menu()
    option = input("----Choose an Option: ")
    if option == "exit":
      print("Exiting...")
      break
    if option == "1":
        print("----Please add a task\t")
        task = input("")
        task_list.append(task)
    elif option == "2": # I want to show the list numbered 
      task_number = int(input("----Which task would you like to view?"))# This takes the input from the user for which task they would like to view
      x = task_number - 1 #Because array are zero index based, we want to subtract the number chosen by 1 to match the correct index in the array
      if 0 <= x < len(task_list): #We have this here to check whether the task chosen is within the range of the number of tasks inside of our array
        print(f"Task {task_number}: {task_list[x]}")#If the condition is met, then we will print the task_number, and the task asked for.
    elif option == "3":#After I get the numbered list to show, 
      task_delete = int(input("----Which task would you like to delete?")) 
      y = task_delete - 1
      if 0 <= y < len(task_list):
         print(f"Deleted Task: {task_list[y]}")
         task_list.pop(y)#Deletes the chosen task from the list 
         print(f"----{task_list}")
         
    else:
      print('invalid option... Try again.')
    #if option == "2"
      


To_Do_Options()  