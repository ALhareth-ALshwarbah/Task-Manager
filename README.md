# Task manager in python (my first professional project)

## main logic behind the code 
this is a pyhton package that works inside the terminal as a (CLI)

**so this package have 1 argument and 3 subparsers and 2 of those subparsers have arguments:**
-  **--file** : which enable you to choose where to save your task manager (and it's format is .json) instead of the default:

``` powershell
C:\Users\Ghost\Desktop\something.json
```

- **add** : this subparser enable you to add a task and it's argument is the task that you will add, ex:

``` powershell
python -m Task_Manager.cli add 'learn anything'

learn anything has been added
```

- **list** : this subparser doesn't have an argument and it's function is to list all your tasks, ex:

``` powershell
python -m Task_Manager.cli list

1:learn anything
```

- **remove** : this subparser enable you to delete a task and it's argument is the index, ex:

``` powershell
python -m Task_Manager.cli remove 1

learn anything has been removed
```

## the real action

- clone the repo to your machine

- after this navigate inside the terminal to the repo that you cloned

- type **ls** inside the repo and make sure that **pyproject.toml** exist

- now  type:

``` powershell
pip install .
```

- by the way the cli command is **alhareth** (it's my name, i know i am lazy in term of choosing names)

![alt text](https://github.com/ALhareth-ALshwarbah/Task-Manager/blob/b821195571c9297c85c147aa649f85b27c825994/Screenshot-4-repo.png)

![alt text](https://github.com/ALhareth-ALshwarbah/Task-Manager/blob/0217e4a4415ef84b8a57dea21500b35e6b210c34/Screenshot%20-1-repo.png)

![alt text](https://github.com/ALhareth-ALshwarbah/Task-Manager/blob/9d92347d1fb4ba8d6a0225ab766493c5be04990b/Screenshot%20-2-repo.png)

![alt text](https://github.com/ALhareth-ALshwarbah/Task-Manager/blob/6d8a2b96988d87777eac157c545edb94e3ea6a8f/Screenshot%20-3-repo.png)
