from src.setting import settings
from src.service import create, listing, update, delete, get_tid_by_task_name

def run():
    args = settings()

    if args.list:
        listing()
        return

    if args.update:
        update(args)
        return 

    if args.delete:
        delete(args)
        return

    if args.get_tid_by_task_name:
        get_tid_by_task_name(args)
        return

    create(args)


if __name__ == "__main__":
    run()