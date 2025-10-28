import pytest
import subprocess
from pathlib import Path
import json

def test_my_cli(tmp_path):
    temp = tmp_path/'sometime.json'

    adding = subprocess.run(['python','-m','Task_Manager.cli','--file',str(temp),'add','meAgain'],
                        capture_output = True,
                        text = True)

    checking = json.loads(temp.read_text())
    assert adding.returncode == 0
    assert 'meAgain' in adding.stdout
    assert 'meAgain' in checking

    listing = subprocess.run(['python','-m','Task_Manager.cli','--file',str(temp),'list'],
                        capture_output = True,
                        text = True)

    assert listing.returncode == 0
    assert 'meAgain' in listing.stdout

    removing = subprocess.run(['python','-m','Task_Manager.cli','--file',str(temp),'remove','1'],
                         capture_output = True,
                         text = True)

    checking = json.loads(temp.read_text())
    assert removing.returncode == 0
    assert 'meAgain has been deleted' not in removing.stdout
    assert  checking == []

