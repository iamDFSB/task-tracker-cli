from datetime import datetime
from tabulate import tabulate
from src.database import get_database_data, save_database_data
from src.setting import file_path

headers = ["TID", "Task", "Description", "Status", "Created At"]


def create(args):
    task = args.task
    description = args.description
    status = args.status

    contents = get_database_data(file_path)

    length = len(contents["contents"]) + 1
    created_at = datetime.now()

    TID = f"{length}_{created_at.timestamp()}"   
    contents["length"] = length
    contents["contents"].append({
        "TID": TID,
        "Task": task,
        "Description": description,
        "Status": status,
        "Created At": created_at.strftime("%Y-%m-%d %H:%M:%S")
    })

    save_database_data(contents, file_path)
    print("Task added successfully!")



def listing():
    contents = get_database_data(file_path)
    list_mapped = list(map(
        lambda row: [   
            row["TID"], row["Task"], row["Description"], row["Status"], row["Created At"]
        ],
        contents["contents"] 
    ))
    print(tabulate(list_mapped, headers=headers))
    return


def update(args):
    contents = get_database_data(file_path)
    for row in contents["contents"]:
        if row["TID"] == args.update:
            row["Status"] = args.status
            save_database_data(contents, file_path)
            print(f"Task {args.update} updated successfully!")
            return


def delete(args):
    contents = get_database_data(file_path)
    for i, row in enumerate(contents["contents"]):
        if row["TID"] == args.delete:
            del contents["contents"][i]
            contents["length"] -= 1
            save_database_data(contents, file_path)
            print(f"Task {args.delete} deleted successfully!")
            return


def get_tid_by_task_name(args):
    contents = get_database_data(file_path)
    for row in contents["contents"]:
        if row["Task"] == args.get_tid_by_task_name:
            print(f"TID for task '{args.get_tid_by_task_name}': {row['TID']}")
            return
    print(f"No task found with name '{args.get_tid_by_task_name}'")
    return