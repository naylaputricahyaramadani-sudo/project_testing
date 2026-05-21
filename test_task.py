from task_manager import (
    add_task,
    update_status,
    delete_task,
    search_task
)


def test_add_task_valid():
    tasks = []

    result = add_task(
        tasks,
        "Belajar Testing",
        "high",
        "Rina"
    )

    assert len(result) == 1


def test_add_task_empty():
    tasks = []

    result = add_task(
        tasks,
        "",
        "high",
        "Rina"
    )

    assert result == "Error: Title wajib diisi"


def test_invalid_priority():
    tasks = []

    result = add_task(
        tasks,
        "Task Baru",
        "urgent",
        "Rina"
    )

    assert result == "Error: Priority tidak valid"


def test_update_status_valid():
    tasks = [
        {
            "id": 1,
            "status": "todo"
        }
    ]

    result = update_status(
        tasks,
        1,
        "done"
    )

    assert result[0]["status"] == "done"


def test_update_status_invalid():
    tasks = [
        {
            "id": 1,
            "status": "todo"
        }
    ]

    result = update_status(
        tasks,
        1,
        "finish"
    )

    assert result == "Error: Status tidak valid"