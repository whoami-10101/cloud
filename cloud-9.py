import matplotlib.pyplot as plt
import numpy as np

class Processor:
    def __init__(self, name, mips):
        self.name = name
        self.mips = mips
        self.current_time = 0
        self.task_set = []

    def add_task(self, task):
        wait_time = self.current_time
        self.task_set.append(task)
        execution_time = task.inst / self.mips
        self.current_time += execution_time
        return wait_time, execution_time

class Task:
    def __init__(self, name, inst):
        self.name = name
        self.inst = inst
        self.wait_time = 0
        self.execution_time = 0

    def assign_to_processor(self, processor):
        self.wait_time, self.execution_time = processor.add_task(self)

# set of 15 tasks
tasks = [
    Task("t1", 100000), Task("t2", 70000), Task("t3", 5000), Task("t4", 1000), Task("t5", 3000),
    Task("t6", 10000), Task("t7", 90000), Task("t8", 100000), Task("t9", 15000), Task("t10", 1000),
    Task("t11", 2000), Task("t12", 4000), Task("t13", 20000), Task("t14", 25000), Task("t15", 80000)
]

# FCFS
def main_fcfs(tasks):
    processors = [
        Processor("VM1", 500), Processor("VM2", 500), Processor("VM3", 1500),
        Processor("VM4", 1500), Processor("VM5", 2500), Processor("VM6", 2500)
    ]
    total_wait_time = 0
    total_execution_time = 0

    for i, task in enumerate(tasks):
        processor = processors[i % len(processors)]
        task.assign_to_processor(processor)
        
        total_wait_time += task.wait_time
        total_execution_time += task.execution_time

    return total_wait_time, total_execution_time

# SJF
def sort_tasks_sjf(tasks):
    return sorted(tasks, key=lambda t: t.inst)

def main_sjf(tasks):
    processors = [
        Processor("VM1", 500), Processor("VM2", 500), Processor("VM3", 1500),
        Processor("VM4", 1500), Processor("VM5", 2500), Processor("VM6", 2500)
    ]

    sorted_tasks = sort_tasks_sjf(tasks)

    total_wait_time = 0
    total_execution_time = 0

    for task in sorted_tasks:
        processor = min(processors, key=lambda p: p.current_time)
        task.assign_to_processor(processor)
        
        total_wait_time += task.wait_time
        total_execution_time += task.execution_time

    return total_wait_time, total_execution_time

# MAX-MIN
def max_min_scheduling(tasks, processors):
    remaining_tasks = tasks.copy()
    scheduled_tasks = []

    while remaining_tasks:
        max_task = max(remaining_tasks, key=lambda t: t.inst)
        best_processor = min(processors, key=lambda p: p.current_time + (max_task.inst / p.mips))
        max_task.assign_to_processor(best_processor)
        scheduled_tasks.append(max_task)
        remaining_tasks.remove(max_task)

    return scheduled_tasks

def main_max_min(tasks):
    processors = [
        Processor("VM1", 500), Processor("VM2", 500), Processor("VM3", 1500),
        Processor("VM4", 1500), Processor("VM5", 2500), Processor("VM6", 2500)
    ]

    scheduled_tasks = max_min_scheduling(tasks, processors)

    total_wait_time = 0
    total_execution_time = 0

    for task in scheduled_tasks:
        total_wait_time += task.wait_time
        total_execution_time += task.execution_time

    return total_wait_time, total_execution_time

tasks_fcfs = [Task(task.name, task.inst) for task in tasks]
tasks_sjf = [Task(task.name, task.inst) for task in tasks]
tasks_max_min = [Task(task.name, task.inst) for task in tasks]

# Run all algorithms
twt_fcfs, tft_fcfs = main_fcfs(tasks_fcfs)
twt_sjf, tft_sjf = main_sjf(tasks_sjf)
twt_max_min, tft_max_min = main_max_min(tasks_max_min)

# Plotting
algorithms = ['FCFS', 'SJF', 'MAX-MIN']
twt = [twt_fcfs, twt_sjf, twt_max_min]  
tft = [tft_fcfs, tft_sjf, tft_max_min]  

x = np.arange(len(algorithms))
width = 0.35

fig, ax = plt.subplots(figsize=(10, 6))

rects1 = ax.bar(x - width/2, twt, width, label='TWT', color='#4289f5')
rects2 = ax.bar(x + width/2, tft, width, label='TFT', color='#f56242')

ax.set_ylabel('Time')
ax.set_title('Tasks Scheduling Algorithms')
ax.set_xticks(x)
ax.set_xticklabels(algorithms)
ax.legend()

ax.set_ylim(0, max(max(twt), max(tft)) + 100)

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height:.2f}',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

plt.tight_layout()
plt.show()

