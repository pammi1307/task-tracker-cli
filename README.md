# task-tracker-cli

Task Tracker CLI is a command-line interface tool to manage and track your daily tasks. The tool allows you to add, update, delete, and mark tasks as in progress or completed. Tasks are stored persistently in a JSON file.

## Features
- Add new tasks
- Update tasks
- Delete tasks
- Mark tasks as `in progress` or `done`
- List all tasks
- List tasks filtered by status (`todo`, `in progress`, `done`)

## Prerequisites

- Python 3.x

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/pammi1307/task-tracker-cli.git

# Commands on CLI
## Adding a new task
task-cli.py add "Buy groceries"

## Updating and deleting tasks
task-cli.py update 1 "Buy groceries and cook dinner"
task-cli.py delete 1

## Marking a task as in progress or done
task-cli.py mark-in-progress 1
task-cli.py mark-done 1

## Listing all tasks
task-cli.py list

## Listing tasks by status
task-cli.py list done
task-cli.py list todo
task-cli.py list in-progress

# url of project
https://github.com/pammi1307/task-tracker-cli

## License

This project is licensed under the MIT License - see the [LICENSE](./License) file for details.


