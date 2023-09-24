import os
import time

from task_manager import Note


def main_menu():
    text = """
1- Add new task to the list.
2- Complete a specific Task.
3- View all Tasks.
4- Clear all Tasks form the list.
5- Quit.
"""
    print(text)
  
def clear_terminal():
  return os.system('cls') if os.name == 'nt' else os.system('clear')

def main():
  clear_terminal()
  note = Note()
  
  while True:
    main_menu()
    choice = input("Enter your choice? ")
    
    match choice:
      case "1":
        clear_terminal()
        text = input("\nWrite task: ")
        if text:
          note.add_task(text)
        else:
          print("You cant leave it empty ):")
        time.sleep(3)
        
      case "2":
        clear_terminal()
        note.set_complete()
        time.sleep(4)
        
      case "3":
        clear_terminal()
        note.view_tasks()
        input("\nPress enter to exit --> ")
        
      case "4":
        clear_terminal()
        note.clear_tasks()
        time.sleep(3)
        
      case "5":
        break
        
      case _:
        clear_terminal()
        print("\nPlease enter a valid choice!")
        time.sleep(3)
          
    clear_terminal()


if __name__ == "__main__":
  main()