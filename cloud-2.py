import random
import matplotlib.pyplot as plt

def schedule_tasks(tasks, num_processors):
    processors = [0] * num_processors
    
    for task_time in tasks:
        min_processor_index = processors.index(min(processors))
        processors[min_processor_index] += task_time
    
    return processors

def plot_processors(processors, title):
    plt.bar(range(len(processors)), processors, tick_label=[f'P{i+1}' for i in range(len(processors))])
    plt.xlabel('Processor')
    plt.ylabel('Total Processing Time')
    plt.title(title)
    plt.show()

num_processors = 5

tasks_5 = [random.randint(1, 10) for _ in range(5)]
processors_5 = schedule_tasks(tasks_5, num_processors)
print(f"Task Times for 5 tasks: {tasks_5}")
print(f"Processor Loads for 5 tasks: {processors_5}")
plot_processors(processors_5, 'Optimal Task Scheduling on 5 Processors (5 Tasks)')


