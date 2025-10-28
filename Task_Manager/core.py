import json
from pathlib import Path

class someThing:
    def __init__(self , file_path:Path):
        self.file_path = Path(file_path)
        if not self.file_path.exists():
            self.file_path.write_text('[]')


    def _read_file(self):
        try:
            return json.loads(self.file_path.read_text())
        except json.JSONDecodeError:
            self.file_path.write_text('[]')
            return []

    def _write_file(self , tasks):
        self.file_path.write_text(json.dumps(tasks , indent = 4))


    def add_task(self,task):
        tasks = self._read_file()
        tasks.append(task)
        self._write_file(tasks)
        return task


    def list_task(self):
        tasks = self._read_file()
        return tasks


    def remove_task(self,index):
        try:
            tasks = self._read_file()
            removed = tasks.pop(index-1)
            self._write_file(tasks)
            return removed
        except IndexError:
            print('the index is not valid')
