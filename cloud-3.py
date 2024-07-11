import random
import matplotlib.pyplot as plt

def fcfs_schedule(tasks, num_processors):
    processors = [0] * num_processors
    for i, task_time in enumerate(tasks):
        processors[i % num_processors] += task_time
    return processors

def plot_processors(processors, title):
    plt.bar(range(len(processors)), processors, tick_label=[f'P{i+1}' for i in range(len(processors))])
    plt.xlabel('Processor')
    plt.ylabel('Total Processing Time')
    plt.title(title)
    plt.show()

num_processors = 5

tasks_10 = [random.randint(1, 10) for _ in range(10)]
processors_10 = fcfs_schedule(tasks_10, num_processors)

print(f"Task Times for 10 tasks: {tasks_10}")
print(f"Processor Loads for 10 tasks using FCFS: {processors_10}")

plot_processors(processors_10, 'Task Scheduling on 5 Processors (10 Tasks) using FCFS')

