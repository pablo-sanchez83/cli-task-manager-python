import sys
import csv
import datetime

taskfile = "tasks.csv"

order = sys.argv[1]

def get_last_id():
    with open(taskfile, "r") as f:
        reader = csv.reader(f)
        rows = list(reader)
        if rows:
            return rows[-1][0]
        else:
            return 0

if order == "add":
    task = sys.argv[2]
    row = [get_last_id() + 1, task, "todo", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
    with open(taskfile, "a") as f:
        writer = csv.writer(f)
        writer.writerow(row)
elif order == "list":
    if len(sys.argv) > 2:
        filter = sys.argv[2]
        with open(taskfile, "r") as f:
            reader = csv.reader(f)
            rows = list(reader)
            for row in rows:
                if len(row) > 0:
                    if filter == "todo":
                        if row[2] == "todo":
                            print(row)
                    elif filter == "in-progress":
                        if row[2] == "in-progress":
                            print(row)
                    elif filter == "done":
                        if row[2] == "done":
                            print(row)
    else:
        with open(taskfile, "r") as f:
            reader = csv.reader(f)
            rows = list(reader)
            for row in rows:
                if len(row) > 0:
                    print(row)
elif order == "update":
    id = sys.argv[2]
    update = sys.argv[3]
    with open(taskfile, "r") as f:
        reader = csv.reader(f)
        rows = list(reader)
        for row in rows:
            if row[0] == id:
                row[1] = update
                row[4] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                break
    with open(taskfile, "w") as f:
        writer = csv.writer(f)
        writer.writerows(rows)
elif order == "delete":
    id = sys.argv[2]
    with open(taskfile, "r") as f:
        reader = csv.reader(f)
        rows = list(reader)
        for row in rows:
            if row[0] == id:
                rows.remove(row)
                break
    with open(taskfile, "w") as f:
        writer = csv.writer(f)
        writer.writerows(rows)
elif order == "mark-in-progress":
    id = sys.argv[2]
    with open(taskfile, "r") as f:
        reader = csv.reader(f)
        rows = list(reader)
        for row in rows:
            if row[0] == id:
                row[2] = "in-progress"
                row[4] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                break
    with open(taskfile, "w") as f:
        writer = csv.writer(f)
        writer.writerows(rows)
elif order == "mark-done":
    id = sys.argv[2]
    with open(taskfile, "r") as f:
        reader = csv.reader(f)
        rows = list(reader)
        for row in rows:
            if row[0] == id:
                row[2] = "done"
                row[4] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                break
    with open(taskfile, "w") as f:
        writer = csv.writer(f)
        writer.writerows(rows)

        

        
