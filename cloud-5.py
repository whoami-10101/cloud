import random
import matplotlib.pyplot as plt

num_processors = 5
num_tasks = 10

task_times = [random.randint(1, 10) for _ in range(num_tasks)]

def optimal_schedule(tasks, num_processors):
    processors = [0] * num_processors
    schedule = [[] for _ in range(num_processors)]

    for task_time in tasks:
        min_processor_index = processors.index(min(processors))
        processors[min_processor_index] += task_time
        schedule[min_processor_index].append(task_time)

    return processors, schedule

def calculate_waiting_time(schedule):
    waiting_times = []
    completion_times = []
    current_completion_time = 0

    for processor_tasks in schedule:
        wait_time = current_completion_time
        for task_time in processor_tasks:
            waiting_times.append(wait_time)
            current_completion_time += task_time
            completion_times.append(current_completion_time)
            wait_time += task_time  

    return waiting_times, completion_times

def plot_schedule(tasks, waiting_times, burst_times, completion_times):
    num_tasks = len(tasks)
    task_indices = range(1, num_tasks + 1)

    plt.figure(figsize=(12, 8))

    #Burst Time
    plt.subplot(2, 1, 1)
    plt.bar(task_indices, burst_times, label='Burst Time')
    plt.xlabel('Task')
    plt.ylabel('Time')
    plt.title('Burst Time for Each Task')
    plt.xticks(task_indices)
    plt.legend()

    # Completion Time
    plt.subplot(2, 1, 2)
    plt.step(task_indices, completion_times, where='mid', label='Completion Time')
    plt.xlabel('Task')
    plt.ylabel('Time')
    plt.title('Completion Time for Each Task')
    plt.xticks(task_indices)
    plt.legend()
    plt.tight_layout()
    plt.show()

processors, schedule = optimal_schedule(task_times, num_processors)

waiting_times, completion_times = calculate_waiting_time(schedule)
burst_times = task_times

print(f"Task Times: {task_times}")
print(f"Processor Loads for Optimal: {processors}")
print(f"Waiting Times: {waiting_times}")
print(f"Burst Times: {burst_times}")
print(f"Completion Times: {completion_times}")

plot_schedule(task_times, waiting_times, burst_times, completion_times)

