import random
import matplotlib.pyplot as plt

def generate_task_times(num_tasks):
    return [random.randint(1, 20) for _ in range(num_tasks)]

# First-Come, First-Served 
def fcfs_schedule(task_times):
    return sum(task_times)

# Min-Max scheduling 
def min_max_schedule(task_times, num_processors):
    processors = [0] * num_processors
    for task_time in sorted(task_times, reverse=True):
        min_processor_index = processors.index(min(processors))
        processors[min_processor_index] += task_time
    return max(processors)

# Min-Min algorithm
def min_min_schedule(task_times, num_processors):
    processors = [0] * num_processors
    for task_time in sorted(task_times):
        min_processor_index = processors.index(min(processors))
        processors[min_processor_index] += task_time
    return max(processors)

# Max-Min scheduling algorithm
def max_min_schedule(task_times, num_processors):
    processors = [0] * num_processors
    for task_time in sorted(task_times, reverse=True):
        max_processor_index = processors.index(max(processors))
        processors[max_processor_index] += task_time
    return max(processors)

# Shortest Job First (SJF)
def sjf_schedule(task_times, num_processors):
    processors = [0] * num_processors
    for task_time in sorted(task_times):
        min_processor_index = processors.index(min(processors))
        processors[min_processor_index] += task_time
    return max(processors)

def compare_algorithms(num_tasks, num_processors):
    task_times = generate_task_times(num_tasks)    
    fcfs_time = fcfs_schedule(task_times[:])
    min_max_time = min_max_schedule(task_times[:], num_processors)
    min_min_time = min_min_schedule(task_times[:], num_processors)
    max_min_time = max_min_schedule(task_times[:], num_processors)
    sjf_time = sjf_schedule(task_times[:], num_processors)
    return fcfs_time, min_max_time, min_min_time, max_min_time, sjf_time

tasks = [5, 10, 15, 20, 25, 30]
num_processors = 5

fcfs_times = []
min_max_times = []
min_min_times = []
max_min_times = []
sjf_times = []

for num_tasks in tasks:
    fcfs_time, min_max_time, min_min_time, max_min_time, sjf_time = compare_algorithms(num_tasks, num_processors)
    fcfs_times.append(fcfs_time)
    min_max_times.append(min_max_time)
    min_min_times.append(min_min_time)
    max_min_times.append(max_min_time)
    sjf_times.append(sjf_time)

plt.figure(figsize=(12, 8))

plt.plot(tasks, fcfs_times, marker='o', color='blue', label='FCFS')
plt.plot(tasks, min_max_times, marker='s', color='red', label='Min-Max')
plt.plot(tasks, min_min_times, marker='^', color='green', label='Min-Min')
plt.plot(tasks, max_min_times, marker='*', color='purple', label='Max-Min')
plt.plot(tasks, sjf_times, marker='x', color='orange', label='SJF')

plt.xlabel('Number of Tasks')
plt.ylabel('Total Processing Time')
plt.title('Comparison of Scheduling Algorithms')
plt.xticks(tasks)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

