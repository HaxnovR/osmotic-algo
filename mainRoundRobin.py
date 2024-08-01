import random


class Task:
    def __init__(self, id, execution_time,x):
        self.id = id
        self.type = x
        self.execution_time = execution_time

class Worker:
    def __init__(self,app_no,status):
        self.application_number=app_no
        self.status=status #can be True or False
    
    def getId(self):
        return self.application_number
        
    def getState(self):
        return self.status
    def setState(self,state):
        self.status=state
    
#osmotic layer

class osmoticLayer:
    def __init__(self):
        pass

    def getProcesses(self,tasks,workers):
        temp = [[] for worker in workers]
        for task in tasks:
            if task.type in range(0,len(workers)):
                temp[task.type].append(task)
                tasks.remove(task)
        return temp
        
        
        
def round_robin(tasks, quantum):
    """
    Round Robin scheduling algorithm implementation.
    """
    task_queue = tasks.copy()  # Copy the list of tasks to avoid modifying the original list
    task_execution_order = []  # List to store the order of task execution

    while task_queue:
        task = task_queue.pop(0)  # Get the first task in the queue
        execution_time = min(quantum, task.execution_time)  # Calculate the actual execution time for the task
        task.execution_time -= execution_time  # Update the remaining execution time for the task

        task_execution_order.append((task.id, execution_time, task.type))  # Append task execution to the order list

        if task.execution_time > 0:
            task_queue.append(task)  # Add the task back to the queue if it's not completed

    return task_execution_order

def shortest_job_next(tasks):
    """
    Shortest Job Next scheduling algorithm implementation.
    """
    task_execution_order = []  # List to store the order of task execution

    # Sort tasks based on their execution time (shortest first)
    tasks.sort(key=lambda x: x.execution_time)

    for task in tasks:
        task_execution_order.append((task.id, task.execution_time))  # Append task execution to the order list

    return task_execution_order

def hybrid_rr_sjn(tasks, quantum):
    """
    Hybrid Round Robin (RR) and Shortest Job Next (SJN) scheduling algorithm implementation.
    """
    remaining_tasks = tasks.copy()  # Copy the list of tasks to avoid modifying the original list
    task_execution_order = []  # List to store the order of task execution

    while remaining_tasks:
        # Use Round Robin for the initial processing
        rr_execution_order = round_robin(remaining_tasks, quantum)
        
        # Extract remaining tasks after Round Robin scheduling
        remaining_tasks = [Task(task_id, remaining_time,server_no) for task_id, 
                           remaining_time, server_no in rr_execution_order 
                           if remaining_time > 0]
        
        # Apply Shortest Job Next scheduling on the remaining tasks
        sjn_execution_order = shortest_job_next(remaining_tasks)
        
        # Append the task execution order from SJN scheduling to the final order list
        task_execution_order.extend(sjn_execution_order)
        
        # Update remaining tasks after SJN scheduling
        remaining_tasks = []

    return task_execution_order



#random process generator
def randomProcessGenerator(n,total_workers):
    print("[+] Generating Tasks")
    tasks = []
    for i in range(0,n):
        task = Task(i,random.randint(1,5),random.randint(0,total_workers))
        tasks.append(task)
    
    return tasks

def randomWorkerGenerator(n):
    print("[+] Generating workers:")
    workers = []
    for i in range(1,n+1):
        worker = Worker(i,False)
        workers.append(worker)
    return workers

def printWorkerInfo(worker):
    print("Server no: {0} \nServer Status: {1}".format(worker.getId(),worker.getState()))
        

#print function for tasks
def printTask(tasks):
    for task in tasks:
        print("ID:{0}\tExecution time:{1}\ttype: {1}".format(task.id,
                                                       task.execution_time,
                                                       task.type))

if __name__ == "__main__":
    
    # Define the quantum for Round Robin scheduling
    quantum = int(input("[+]Enter Time Quantum: "))
    
    #define a list of workers who will process the data
    total_workers = int(input("[+] Enter total servers in the network: "))
    workers = randomWorkerGenerator(total_workers)
    for worker in workers:
        printWorkerInfo(worker)
    
    # Define a list of tasks (Task ID, Execution Time)
    total_tasks = int(input("[+]Enter total no. of tasks: "))
    tasks = randomProcessGenerator(total_tasks,total_workers)
    printTask(tasks)

    # Create an osmotic layer
    layer = osmoticLayer()

    # Run the hybrid RR-SJN scheduling algorithm on the servers
    execution_group = layer.getProcesses(tasks,workers)
    execution_order = [[] for worker  in workers]
    for i in range(total_workers):
        execution_order[i].append(hybrid_rr_sjn(execution_group[i],quantum))
        
        

    # Print the order of task execution
    for worker in range(len(workers)):
        printWorkerInfo(workers[worker])
        print("\n[+] Order of Task Execution (Task ID,Execution Time):-")
        for task in execution_order[worker]:
            print("\n",task)
            # print("\t{0}\t{1}".format(task[0],task[1]))
        