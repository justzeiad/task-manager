import json
import os


class Task:

  def __init__(self, content, completed=False) -> None:
    self.completed = completed
    self.content = content
    self.position = 0


class TaskEncoder(json.JSONEncoder):

  def default(self, obj):
    if isinstance(obj, Task):
      return {
          '_type': 'Task',
          'content': obj.content,
          'completed': obj.completed,
          'position': obj.position
      }
    return super().default(obj)


def task_decoder(obj):
  if '_type' in obj and obj['_type'] == 'Task':
    return Task(obj['content'], obj['completed'])
  return obj


class Note:

  def __init__(self) -> None:
    self.tasks = []
    self.id = 1
    self.load_tasks()

  def add_task(self, text):
    task = Task(text)
    task.position = self.id
    self.tasks.append({"id": self.id, "task": task})
    self.id += 1
    self.save_tasks()
    print("\nTask added successfully!")

  def set_complete(self):
    incompleted_tasks = [
        task['task'] for task in self.tasks if not task['task'].completed
    ]

    for i, task in enumerate(incompleted_tasks):
      print(f"{i+1}- {task.content}")

    task_index = int(input("\nChoose task to complete: ")) - 1

    if 0 <= task_index < len(self.tasks):
      incompleted_tasks[task_index].completed = True
      self.save_tasks()
      print("\nThe selected task marked as completed!")
    else:
      print("Invalid task index!")

  def view_tasks(self):
    if self.tasks:
      for task in self.tasks:
        print(f"\nTask {task['id']}: {task['task'].content}")
        print(
            f"Status: {'Completed' if task['task'].completed else 'Not completed yet'}"
        )
    else:
      print("< There are no tasks yet >")

  def load_tasks(self):
    if os.path.exists('tasks.json'):
      with open('tasks.json', 'r') as file:
        data = json.load(file, object_hook=task_decoder)
        self.tasks = data['tasks']
        self.id = data['id']

  def save_tasks(self):
    with open('tasks.json', 'w') as file:
      data = {'tasks': self.tasks, 'id': self.id}
      json.dump(data, file, cls=TaskEncoder)

  def clear_tasks(self):
    confirm = input("Are you sure you want to clear all tasks? (yes/no): ").strip().lower()
    if confirm == "yes":
      self.tasks = []
      self.id = 1
      self.save_tasks()
      print("All tasks have been cleared.")
    else:
      print("Task clearing canceled.")