import argparse
from pathlib import Path
from .core import someThing
def main():
    parser = argparse.ArgumentParser(description = 'a simple task manager in cli')
    subparser = parser.add_subparsers(dest = 'command')

    add_subparser = subparser.add_parser('add', help = 'to add a task')
    add_subparser.add_argument('task' , help = 'the task you want to add')

    subparser.add_parser('list' , help = 'list all your tasks')

    remove_parser = subparser.add_parser('remove' , help = 'to remove a task')
    remove_parser.add_argument('index' , type = int , help = 'the number of the task you want to remove')

    parser.add_argument('--file' , type = Path ,default = Path(r'C:\Users\Ghost\Desktop\something.json'))

    args = parser.parse_args()
    beast = someThing(args.file)    #TODO:make the user able to choose the default path

    if args.command == 'add':
        added = beast.add_task(args.task)
        print(f'{added} has been added')

    if args.command == 'list':
        List = beast.list_task()
        for i,t in enumerate(List , start = 1):
            print(f'{i}:{t}')

    if args.command == 'remove':
        removed = beast.remove_task(args.index)
        if removed != None:
            print(f'{removed} has been removed')

if __name__ == '__main__':
    main()

