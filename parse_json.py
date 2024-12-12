import sys
import json

# Check if the response file exists and is not empty
try:
    with open(sys.argv[1], 'r') as file:
        data = json.load(file)
except FileNotFoundError:
    print("Error: The response file was not found.")
    sys.exit(1)
except json.JSONDecodeError:
    print("Error: Failed to decode JSON. The response might be empty or malformed.")
    sys.exit(1)

# Initialize dictionaries to group stubs by their states
stopped_stubs = {}
running_stubs = {}
starting_stubs = {}
broken_stubs = {}

# Parse the JSON and group the names and their recent throughput rates by state
for item in data:
    name = item.get('name')
    state = item.get('state')
    hits = item.get('activity', {}).get('hits', [])
    recent_throughput_rate = (hits[-1] / 30) if hits else 0
    
    if state == 'stopped':
        stopped_stubs[name] = recent_throughput_rate
    elif state == 'running':
        running_stubs[name] = recent_throughput_rate
    elif state == 'starting':
        starting_stubs[name] = recent_throughput_rate
    elif state == 'broken':
        broken_stubs[name] = recent_throughput_rate

# Print the grouped output
print("Stopped Stubs:")
for name, rate in stopped_stubs.items():
    print(f'Name: {name}, Recent Throughput Rate: {rate:.2f} transactions per second')

print("\nRunning Stubs:")
for name, rate in running_stubs.items():
    print(f'Name: {name}, Recent Throughput Rate: {rate:.2f} transactions per second')

print("\nStarting Stubs:")
for name, rate in starting_stubs.items():
    print(f'Name: {name}, Recent Throughput Rate: {rate:.2f} transactions per second')

print("\nBroken Stubs:")
for name, rate in broken_stubs.items():
    print(f'Name: {name}, Recent Throughput Rate: {rate:.2f} transactions per second')