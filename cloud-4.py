import random
import matplotlib.pyplot as plt

num_processors = 5
num_tasks = 5
task_times = [random.randint(1, 10) for _ in range(num_tasks)]

def fcfs_schedule(tasks, num_processors):
    processors = [0] * num_processors
    for i, task_time in enumerate(tasks):
        processors[i % num_processors] += task_time
    return processors

def random_schedule(tasks, num_processors):
    processors = [0] * num_processors
    for task_time in tasks:
        processors[random.randint(0, num_processors - 1)] += task_time
    return processors

def optimal_schedule(tasks, num_processors):
    processors = [0] * num_processors
    for task_time in tasks:
        min_processor_index = processors.index(min(processors))
        processors[min_processor_index] += task_time
    return processors

def plot_processors(processors_fcfs, processors_random, processors_optimal, title):
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 3, 1)
    plt.bar(range(len(processors_fcfs)), processors_fcfs, tick_label=[f'P{i+1}' for i in range(len(processors_fcfs))])
    plt.xlabel('Processor')
    plt.ylabel('Total Processing Time')
    plt.title('FCFS')

    plt.subplot(1, 3, 2)
    plt.bar(range(len(processors_random)), processors_random, tick_label=[f'P{i+1}' for i in range(len(processors_random))])
    plt.xlabel('Processor')
    plt.ylabel('Total Processing Time')
    plt.title('Random')

    plt.subplot(1, 3, 3)
    plt.bar(range(len(processors_optimal)), processors_optimal, tick_label=[f'P{i+1}' for i in range(len(processors_optimal))])
    plt.xlabel('Processor')
    plt.ylabel('Total Processing Time')
    plt.title('Optimal')

    plt.suptitle(title)
    plt.tight_layout()
    plt.show()

processors_fcfs = fcfs_schedule(task_times, num_processors)
processors_random = random_schedule(task_times, num_processors)
processors_optimal = optimal_schedule(task_times, num_processors)

print(f"Task Times: {task_times}")
print(f"Processor Loads for FCFS: {processors_fcfs}, Total Time: {max(processors_fcfs)}")
print(f"Processor Loads for Random: {processors_random}, Total Time: {max(processors_random)}")
print(f"Processor Loads for Optimal: {processors_optimal}, Total Time: {max(processors_optimal)}")

plot_processors(processors_fcfs, processors_random, processors_optimal, 'Task Scheduling Comparison (5 Tasks)')

