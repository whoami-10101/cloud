import random
import matplotlib.pyplot as plt

num_processors = 5
num_tasks = 5

task_times = [random.randint(1, 10) for _ in range(num_tasks)]
processors = [0] * num_processors

for task_time in task_times:
    min_processor_index = processors.index(min(processors))
    processors[min_processor_index] += task_time

plt.bar(range(num_processors), processors, tick_label=[f'P{i+1}' for i in range(num_processors)])
plt.xlabel('Processor')
plt.ylabel('Total Processing Time')
plt.title('Task Scheduling on Processors')
plt.show()

print("Processor Loads:", processors)
print("Task Times:", task_times)

