import random
import matplotlib.pyplot as plt

# Function to simulate task processing times
def generate_task_times(num_tasks):
    return [random.randint(1, 20) for _ in range(num_tasks)]

# First-Come, First-Served (FFS) scheduling algorithm
def ffs_schedule(task_times):
    return sum(task_times)

# Random scheduling algorithm
def random_schedule(task_times):
    random.shuffle(task_times)
    return sum(task_times)

# Optimal scheduling algorithm (assuming we know the shortest processing time)
def optimal_schedule(task_times):
    return sum(sorted(task_times))

# Function to compare algorithms for given number of tasks
def compare_algorithms(num_tasks):
    task_times = generate_task_times(num_tasks)
    
    ffs_time = ffs_schedule(task_times[:])
    random_time = random_schedule(task_times[:])
    optimal_time = optimal_schedule(task_times[:])
    
    return ffs_time, random_time, optimal_time

# Test cases
tasks = [5, 10, 15, 20, 25, 30]
ffs_times = []
random_times = []
optimal_times = []

for num_tasks in tasks:
    ffs_time, random_time, optimal_time = compare_algorithms(num_tasks)
    ffs_times.append(ffs_time)
    random_times.append(random_time)
    optimal_times.append(optimal_time)

# Plotting the results with different colors for each algorithm
plt.figure(figsize=(10, 6))
plt.plot(tasks, ffs_times, marker='o', color='blue', label='FFS')
plt.plot(tasks, random_times, marker='s', color='red', label='Random')
plt.plot(tasks, optimal_times, marker='^', color='green', label='Optimal')
plt.xlabel('Number of Tasks')
plt.ylabel('Total Processing Time')
plt.title('Comparison of Scheduling Algorithms')
plt.xticks(tasks)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

