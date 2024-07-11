import random
import matplotlib.pyplot as plt

def generate_tasks(num_tasks):
    return [random.randint(20, 80) for _ in range(num_tasks)]

def assign_tasks(servers, tasks):
    servers_copy = servers.copy()
    minTime = []
    for task in tasks:
        processing_times = [round(task / server, 2) for server in servers_copy]
        min_index = processing_times.index(min(processing_times))
        minTime.append(min(processing_times))
        servers_copy.pop(min_index)
        if not servers_copy:
            servers_copy = servers.copy()
    return round(sum(minTime), 2)

def high_task_to_high_server(servers, tasks):
    servers_sorted = sorted(servers, reverse=True)
    tasks_sorted = sorted(tasks, reverse=True)
    processing_time = [round(tasks_sorted[i] / servers_sorted[i % len(servers_sorted)], 2) for i in range(len(tasks_sorted))]
    return round(sum(processing_time), 2)

def serial_assignment(servers, tasks):
    processing_time = [round(tasks[i] / servers[i % len(servers)], 2) for i in range(len(tasks))]
    return round(sum(processing_time), 2)

def shortest_job_fastest_processor(servers, tasks):
    servers_sorted = sorted(servers, reverse=True)
    tasks_sorted = sorted(tasks)
    processing_time = [round(tasks_sorted[i] / servers_sorted[i % len(servers_sorted)], 2) for i in range(len(tasks_sorted))]
    return round(sum(processing_time), 2)

# Initial server list
original_servers = [203, 423, 507, 290, 690]

# Number of tasks to test
num_tasks_list = [10, 15, 20, 25, 30, 35,40,45,50,55,60,65,70]

# Store the results
results_random = []
results_efficient = []
results_high_task_high_server = []
results_serial = []
results_sjf = []

for num_tasks in num_tasks_list:
    tasks = generate_tasks(num_tasks)
    
    # Random load distribution
    servers = original_servers.copy()
    random.shuffle(servers)
    random.shuffle(tasks)
    total_processing_time_before = round(sum([task / server for server in servers for task in tasks]), 2)
    results_random.append(total_processing_time_before)
    
    # Efficient load distribution
    total_processing_time_after = assign_tasks(original_servers, tasks)
    results_efficient.append(total_processing_time_after)
    
    # High task to high server
    processing_time_high_task_high_server = high_task_to_high_server(original_servers, tasks)
    results_high_task_high_server.append(processing_time_high_task_high_server)
    
    # Serial assignment
    processing_time_serial = serial_assignment(original_servers, tasks)
    results_serial.append(processing_time_serial)
    
    # Shortest job fastest processor
    processing_time_sjf = shortest_job_fastest_processor(original_servers, tasks)
    results_sjf.append(processing_time_sjf)

# Plotting
plt.figure(figsize=(14, 8))
plt.plot(num_tasks_list, results_random, label='Random Load Distribution', marker='o')
plt.plot(num_tasks_list, results_efficient, label='Efficient Load Distribution', marker='o')
plt.plot(num_tasks_list, results_high_task_high_server, label='High Task to High Server', marker='o')
plt.plot(num_tasks_list, results_serial, label='Serial Assignment', marker='o')
plt.plot(num_tasks_list, results_sjf, label='Shortest Job Fastest Processor', marker='o')

plt.xlabel('Number of Tasks')
plt.ylabel('Total Processing Time')
plt.title('Processing Time vs Number of Tasks')
plt.legend()
plt.grid(True)
plt.show()
