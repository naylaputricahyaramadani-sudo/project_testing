# task_manager.py

def add_task(tasks, title, priority, assignee):
    if not isinstance(title, str):
        return "Error: Title harus string"

    if title.strip() == "":
        return "Error: Title wajib diisi"

    if priority not in ["low", "medium", "high"]:
        return "Error: Priority tidak valid"

    new_task = {
        "id": len(tasks) + 1,
        "title": title,
        "priority": priority,
        "assignee": assignee,
        "status": "todo"
    }

    tasks.append(new_task)
    return tasks


def update_status(tasks, task_id, status):
    if status not in ["todo", "in_progress", "done"]:
        return "Error: Status tidak valid"

    for task in tasks:
        if task["id"] == task_id:
            task["status"] = status
            return tasks

    return "Task tidak ditemukan"


def delete_task(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return tasks

    return "Task tidak ditemukan"


def search_task(tasks, assignee):
    result = []

    for task in tasks:
        if task["assignee"] == assignee:
            result.append(task)

    return result