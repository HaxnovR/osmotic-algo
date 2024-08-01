import random


class Task:
    def __init__(self, id, execution_time):
        self.id = id
        self.execution_time = execution_time


class Worker:
    def __init__(self, app_no, status):
        self.application_number = app_no
        self.status = status  

    def getId(self):
        return self.application_number

    def getState(self):
        return self.status

    def setState(self, state):
        self.status = state


class osmoticLayer:
    def __init__(self):
        pass


def shortest_job_first(tasks):
    """
    Shortest Job First scheduling algorithm implementation.
    """
    task_execution_order = [] 

    tasks.sort(key=lambda x: x.execution_time)

    for task in tasks:
        task_execution_order.append((task.id, task.execution_time)) 

    return task_execution_order


def randomProcessGenerator(n):
    print("[+] Generating Tasks")
    tasks = []
    for i in range(0, n):
        task = Task(i, random.randint(1, 5))
        tasks.append(task)

    return tasks


def randomWorkerGenerator(n):
    print("[+] Generating workers:")
    workers = []
    for i in range(1, n + 1):
        worker = Worker(i, False)
        workers.append(worker)
    return workers


def printWorkerInfo(worker):
    print(f"Server no: {worker.getId()} \nServer Status: {worker.getState()}")


def printTask(tasks):
    for task in tasks:
        print(f"ID:{task.id}\tExecution time:{task.execution_time}")


if __name__ == "__main__":

    total_workers = int(input("[+] Enter total servers in the network: "))
    workers = randomWorkerGenerator(total_workers)
    for worker in workers:
        printWorkerInfo(worker)

    total_tasks = int(input("[+]Enter total no. of tasks: "))
    tasks = randomProcessGenerator(total_tasks)
    printTask(tasks)

    layer = osmoticLayer()

    execution_order = shortest_job_first(tasks.copy())

    print("\n[+] Order of Task Execution (Task ID,Execution Time):")
    for task in execution_order:
        print(f"\t{task[0]}\t{task[1]}")
