import json
import os
import sys
from datetime import datetime

TASK_FILE = 'tasks.json'

def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE,'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TASK_FILE,'w') as file:
        json.dump(tasks,file,indent=4)    #indent=4 as third parameter 

def add_task(description):
    tasks = load_tasks()
    new_task = {
        'id': len(tasks) + 1,
        'description':description,
        'status':'todo',
        'createdAt':datetime.now().isoformat(),
        'updatedAt':None
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print("Task added successfully")

def update_task(task_id,description):
    tasks = load_tasks()
    for task in tasks:
        if task['id']==task_id:
            task['description']=description
            task['updateaAt'] = datetime.now().isoformat()
            save_tasks(tasks)
            print("Task updated")
            return
    print(f'Task {task_id} not found')

def delete_task(task_id):
    tasks = load_tasks()
    updated_tasks = [task for task in tasks if task['id'] != task_id]
    if len(updated_tasks) < len(tasks):
        # Only save if a task was actually deleted
        save_tasks(updated_tasks)
        print(f'Task {task_id} deleted successfully')
    else:
        print(f'Task {task_id} not found')

def mark_task_status(task_id,status):
    if status not in ['in-progress', 'done']:
        print('Invalid status. Use "in-progress" or "done".')
        return
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = status
            task['updatadAt'] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f'Task {task_id} marked as {status}')
            return
    print(f'Task {task_id} not found')

def list_tasks(status=None):
    tasks = load_tasks()
    if status:
        tasks = [task for task in tasks if task['status'] == status]
    for task in tasks:
        print(f'{task["id"]}: {task["description"]} ({task["status"]})')
def main():
    if len(sys.argv) < 2:
        print('Usage: task-cli <command> [args]')
        sys.exit(1)
    
    command = sys.argv[1]
    if command == 'add':
        if len(sys.argv)<3:
            print('Usage: task-cli add <description>')
            sys.exit(1)
        description = ' '.join(sys.argv[2:])
        add_task(description)
    
    elif command == 'update':
        if len(sys.argv) < 4:
            print("Usage: task-cli update <task_id> <description>")
            sys.exit(1)
        task_id = int(sys.argv[2])
        description = ' '.join(sys.argv[3:])
        update_task(task_id,description)

    elif command == 'delete':
        if len(sys.argv) < 3:
            print('Usage: task-cli delete <task_id>')
            sys.eixt(1)
        task_id = int(sys.argv[2])
        delete_task(task_id)
    
    elif command == 'mark-in-progress':
        if len(sys.argv) < 3:
            print('Usage: task-cli mark-in-progress <task_id>')
            sys.eixt(1)
        task_id = int(sys.argv[2])
        mark_task_status(task_id,'in-progress')
    
    elif command == 'mark-done':
        if len(sys.argv)<3:
            print('Usage: task-cli mark-done <task_id>')
            sys.exit(1)
        task_id = int(sys.argv[2])
        mark_task_status(task_id,'done')
    
    elif command == 'list':
        status = None
        if len(sys.argv) == 3:
            status = sys.argv[2]
        list_tasks(status)
    else:
        print('Invalid command')
        sys.exit(1)

if __name__ == '__main__':
    main()