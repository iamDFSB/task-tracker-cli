import json
from pathlib import Path
from argparse import ArgumentParser

file_path = Path(__file__).parent.parent / "data/database.json"

def settings():
    # Prepare the argument parser
    parser = ArgumentParser()
    parser.add_argument("-l", "--list", help="List tasks", action="store_true")
    parser.add_argument("-u", "--update", help="Update tasks by TID", type=str)
    parser.add_argument("-d", "--delete", help="Delete tasks by TID", type=str)
    parser.add_argument("-gt", "--get-tid-by-task-name", help="Get TID by task name", type=str)

    parser.add_argument("-t", "--task", help="Task name", default="")
    parser.add_argument("-desc", "--description", help="Task description", default="")
    parser.add_argument("-s", "--status", help="Task status", choices=["To Do", "In Progress", "Done"])
    args = parser.parse_args()

    # Prepare Database
    if not file_path.exists():
        file_path.parent.mkdir(parents=True, exist_ok=True)
        with open(file_path, "w+") as f:
            details = {
                "length": 0,
                "contents": []
            }
            f.write(json.dumps(details))

    return args