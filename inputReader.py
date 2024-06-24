import json

def read_input_file(input_file):
    with open(input_file, 'r') as f:
        data = json.load(f)
    branches = [item for item in data if item['type'] == 'branch']
    customers = [item for item in data if item['type'] == 'customer']
    return len(branches), len(customers)

if __name__ == "__main__":
    branches_count, customers_count = read_input_file('input.json')
    print(f"Total branches: {branches_count}")
    print(f"Total customers: {customers_count}")
