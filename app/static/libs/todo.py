import datetime


class Task:
    todo = []
    counter = 0

    def __init__(self, taskname, description, time_stop=""):
        self.id = Task.counter
        self.taskname = taskname
        self.description = description
        self.time_start = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        self.time_stop = time_stop
        Task.counter += 1

    def add_task(self):
        task = {
            "id": self.id,
            "name": self.taskname,
            "description": self.description,
            "time_start": self.time_start,
            "time_stop": self.time_stop,
        }
        Task.todo.append(task)

    def remove_task(id):
        try:
            Task.todo.pop(int(id))
            Task.counter -= 1
        except:
            Task.todo.pop(0)
            Task.counter -= 1
